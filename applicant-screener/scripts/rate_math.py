#!/usr/bin/env python3
"""Ascendion Staff Aug rate math — mirrors the sales calculator workbook.

Conventions snapshot 2026-07 ("Patrick Version 2026 Updated", sheet
"TOD - Staff Aug"). When the live workbook is attached to the session, its
cell values and conventions win over these defaults.

The SSS employer trio (SS ER, MPF ER, EC ER) is a bracket lookup on
basic + non-taxable allowance against the current SSS schedule — pass the
looked-up values in; this script deliberately does not embed the table so a
stale schedule can never hide inside it.

Usage examples:
  # Scenario 2 (reverse solver) + scenario 3 (ceiling fit):
  python3 rate_math.py --basic 125000 --nontax-allowance 5000 \
      --sss-er 2000 --mpf-er 1500 --ec-er 30 --life 100 --hmo 1800 \
      --laptop 1000 --ceiling 150000

  # Vendor engagement (statutory/insurance/HMO stripped):
  python3 rate_math.py --engagement vendor --vendor-rate 110000 --laptop 1000

Outputs JSON so the caller can drop numbers straight into the report.
"""

import argparse
import json

WORKDAYS = 21.75
HOURS_8 = 174.0     # 21.75 x 8
HOURS_9 = 195.75    # 21.75 x 9


def monthly_cost(a):
    """Monthly employer cost, per the workbook's cost build-up."""
    if a.engagement == "vendor":
        # Vendor rate replaces salary + statutory + insurance + HMO.
        items = {
            "vendor_rate": a.vendor_rate,
            "bgv": a.bgv,
            "laptop": a.laptop,
        }
        return sum(items.values()), items
    phic = 2500.0 if a.basic >= 100000 else a.basic * 0.025
    items = {
        "basic": a.basic,
        "sss_er": a.sss_er,
        "mpf_er": a.mpf_er,
        "ec_er": a.ec_er,
        "phic_er": round(phic, 2),
        "hdmf_er": 200.0,
        "thirteenth_month": round(a.basic / 12, 2),
        "severance_accrual": round(a.basic / 12, 2) if a.severance else 0.0,
        "life_accident": a.life,
        "hmo_incl_dependents": a.hmo + a.hmo_dep1 + a.hmo_dep2,
        "bgv": a.bgv,
        "laptop": a.laptop,
        "taxable_allowance": a.tax_allowance,
        "nontax_allowance": a.nontax_allowance,
    }
    return sum(items.values()), items


def utilisation(a):
    if a.manual_utilisation is not None:
        return a.manual_utilisation
    unbilled = (0 if a.leaves_billable else a.leaves) + (
        0 if a.holidays_billable else a.holidays
    )
    return 1 - unbilled / (WORKDAYS * 12)


def effective_bill(monthly_bill, a):
    """Monthly bill less unbilled leave/holiday deductions."""
    daily = monthly_bill / WORKDAYS
    ded = 0.0
    if not a.leaves_billable:
        ded += daily * (a.leaves / 12)
    if not a.holidays_billable:
        ded += daily * (a.holidays / 12)
    return monthly_bill - ded


def to_monthly(rate, rate_type):
    factor = {"monthly": 1, "daily": WORKDAYS, "hourly8": HOURS_8, "hourly9": HOURS_9}
    return rate * factor[rate_type]


def rates_block(monthly):
    return {
        "monthly": round(monthly, 2),
        "daily": round(monthly / WORKDAYS, 2),
        "hourly_8h": round(monthly / HOURS_8, 2),
        "hourly_9h": round(monthly / HOURS_9, 2),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--engagement", choices=["internal", "vendor"], default="internal")
    p.add_argument("--basic", type=float, default=0.0)
    p.add_argument("--vendor-rate", type=float, default=0.0, help="vendor monthly all-in rate")
    p.add_argument("--sss-er", type=float, default=0.0, help="from current SSS schedule, on basic + non-tax allowance")
    p.add_argument("--mpf-er", type=float, default=0.0)
    p.add_argument("--ec-er", type=float, default=0.0)
    p.add_argument("--life", type=float, default=0.0)
    p.add_argument("--hmo", type=float, default=0.0)
    p.add_argument("--hmo-dep1", type=float, default=0.0)
    p.add_argument("--hmo-dep2", type=float, default=0.0)
    p.add_argument("--bgv", type=float, default=0.0)
    p.add_argument("--laptop", type=float, default=0.0)
    p.add_argument("--tax-allowance", type=float, default=0.0)
    p.add_argument("--nontax-allowance", type=float, default=0.0)
    p.add_argument("--no-severance", dest="severance", action="store_false")
    p.add_argument("--leaves", type=float, default=12)
    p.add_argument("--holidays", type=float, default=20)
    p.add_argument("--leaves-billable", action="store_true")
    p.add_argument("--holidays-not-billable", dest="holidays_billable", action="store_false")
    p.add_argument("--manual-utilisation", type=float, default=None)
    p.add_argument("--target-gpm", type=float, default=0.40)
    p.add_argument("--floor-gpm", type=float, default=0.30)
    p.add_argument("--bill", type=float, default=None, help="known bill rate (scenario 1)")
    p.add_argument("--bill-type", choices=["monthly", "daily", "hourly8", "hourly9"], default="monthly")
    p.add_argument("--ceiling", type=float, default=None, help="monthly bill-rate ceiling (scenario 3)")
    p.add_argument("--duration-months", type=float, default=None, help="for indicative TCV")
    a = p.parse_args()

    cost, items = monthly_cost(a)
    u = utilisation(a)
    out = {
        "engagement": a.engagement,
        "monthly_cost": round(cost, 2),
        "cost_items": items,
        "utilisation": round(u, 4),
        "conventions": "21.75 workdays; hourly x174 (8h) / x195.75 (9h); snapshot 2026-07 — live workbook wins",
    }

    # Scenario 2 — reverse solver at target and floor.
    for label, gpm in (("target", a.target_gpm), ("floor", a.floor_gpm)):
        req = cost / (u * (1 - gpm)) if u > 0 and gpm < 1 else None
        out[f"required_bill_at_{label}"] = {"gpm": gpm, **rates_block(req)} if req else None
    if a.duration_months and out["required_bill_at_target"]:
        out["indicative_tcv_at_target"] = {
            "months": a.duration_months,
            "tcv": round(out["required_bill_at_target"]["monthly"] * a.duration_months, 2),
            "label": "indicative — required monthly bill at target GPM x duration",
        }

    # Scenario 1 — known bill rate.
    if a.bill is not None:
        mb = to_monthly(a.bill, a.bill_type)
        eff = effective_bill(mb, a)
        gp = eff - cost
        out["at_given_bill"] = {
            "monthly_bill": round(mb, 2),
            "effective_bill": round(eff, 2),
            "gp": round(gp, 2),
            "gpm": round(gp / eff, 4) if eff else None,
        }

    # Scenario 3 — ceiling fit, workbook verdict ladder + cost-side levers.
    if a.ceiling is not None:
        eff_rev = a.ceiling * u
        gp = eff_rev - cost
        gpm = gp / eff_rev if eff_rev else 0
        room = a.ceiling * u * (1 - a.target_gpm)
        headroom = room - cost
        if headroom >= 0:
            verdict = "FEASIBLE - hits target within ceiling"
        elif gpm >= a.floor_gpm:
            verdict = "BELOW target, above floor"
        elif gpm >= 0:
            verdict = "BELOW floor - restructure"
        else:
            verdict = "LOSS at this ceiling"
        fit = {
            "ceiling": a.ceiling,
            "effective_revenue": round(eff_rev, 2),
            "gp_at_ceiling": round(gp, 2),
            "gpm_at_ceiling": round(gpm, 4),
            "cost_room_at_target": round(room, 2),
            "cost_headroom": round(headroom, 2),
            "verdict": verdict,
        }
        if a.engagement == "internal" and headroom < 0:
            statutory = (
                a.sss_er + a.mpf_er + a.ec_er
                + (2500.0 if a.basic >= 100000 else a.basic * 0.025)
                + 200.0 + round(a.basic / 12, 2)
                + (round(a.basic / 12, 2) if a.severance else 0.0)
            )
            other = (
                a.life + a.hmo + a.hmo_dep1 + a.hmo_dep2 + a.bgv + a.laptop
                + a.tax_allowance + a.nontax_allowance
            )
            fit["levers"] = {
                "1_convert_to_vendor_frees": round(
                    statutory + a.life + a.hmo + a.hmo_dep1 + a.hmo_dep2, 2
                ),
                "2_max_affordable_basic_approx": round(
                    (room - (a.sss_er + a.mpf_er + a.ec_er + 200) - other)
                    / (1 + 0.025 + 2 / 12),
                    2,
                ),
                "3_trim_nontax_allowance_frees": a.nontax_allowance,
                "4_trim_hmo_dependents_frees": a.hmo + a.hmo_dep1 + a.hmo_dep2,
                "5_laptop_by_client_frees": a.laptop,
                "note": "workbook lever-board order (ranked by monthly PHP freed); pricing-side levers (floor GPM, duration) are separate",
            }
        out["ceiling_fit"] = fit

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
