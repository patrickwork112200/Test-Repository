# Compensation & Budget Analysis

Budget misalignment is the most common late-stage deal-killer, and the most
preventable — surface it at screening, in numbers, every time. The output of
this step is a comp table plus a classification: **Within / Stretch / Breach /
Unassessed**.

## Anchor on expected comp, not salary history

The classification runs on **expected compensation vs. ceiling** — always
lawful to ask, and the number the deal actually closes on. Current
compensation is context, not the anchor: many jurisdictions (a growing list
of US states and localities, and others) ban asking about salary history, and
even where legal it imports pay inequities the ban laws exist to break.
Rules:

- Use current comp only when lawfully obtained — volunteered, in the
  materials, or asked where permitted. Never make it a required input.
- The increase-ask figure is an optional negotiation diagnostic computed only
  when current comp is lawfully known; its absence never blocks the
  classification.
- Where salary history can't be asked, the equivalent probe is forward-only:
  "what are you expecting?" plus, if useful, disclosing the budget.

## The numbers to establish

| Figure | Notes |
|---|---|
| Expected compensation | The anchor. As stated; note whether framed as firm or negotiable |
| Budget range / ceiling | From the user. A single number = ceiling. Confirm basic vs. package basis |
| Current compensation | Only where lawfully known. Basic vs. package — never mix the two in a comparison |
| Increase ask | (Expected − Current) ÷ Current, as % — optional, only when current is known |
| Market context | Only if you know the market for the role and location; label it as your estimate, not data |

If expected comp is missing, that's a probe question, not a guess — the
classification is **Unassessed**, which caps the verdict at Endorse with
Conditions with "confirm expected comp ≤ ceiling" as the condition (per the
SKILL.md verdict rules; it escalates to Insufficient Information only when it
is one of two or more material unknowns).

## Classification

Classify on the number first; firmness modifies:

- **Within budget** — expected ≤ ceiling on a like-for-like basis.
- **Stretch** — expected exceeds ceiling by ≤10%. Default classification for
  this zone even when negotiability is unstated — willingness to move is the
  probe, not a precondition ("negotiate to ≤ ceiling; candidate asking +8%
  over; flexibility unconfirmed"). Exception: an expectation *stated as firm*
  above the ceiling is Breach at any overage. Stretch never blocks
  endorsement by itself; it becomes an explicit condition.
- **Breach** — expected exceeds ceiling by >10%, or exceeds it at all with a
  stated-firm expectation. Breach gates the verdict at Do Not Endorse *unless*
  the user explicitly waives or softens the budget — then re-screen with the
  waiver recorded and present the exact overage as their call.

The 10% line is a default; if the user or client has stated their own
tolerance, that wins.

## Like-for-like traps

- **Basic vs. package.** A ₱90k-basic budget against a "₱95k" expectation that
  includes allowances may actually be Within. Decompose both sides before
  classifying: basic, guaranteed allowances, variable pay, benefits with cash
  value.
- **Rate types.** Contractor day/hourly rates vs. FTE salary are not
  comparable without conversion. Pin the conventions and state them in the
  table: monthly ↔ daily via 21.75 workdays, monthly ↔ hourly via 174 hrs
  (8-hr day) or 195.75 hrs (9-hr day) — the same conventions the rate
  analysis below uses — unless the contract says otherwise; contractor
  all-in rates price in benefits, leave, and statutory items an FTE package
  carries separately — a rough 1.2–1.4× loading on FTE basic is the
  comparison heuristic, labeled as such. When the classification lands within ~3 percentage points of the
  10% Stretch/Breach line *because of* a conversion convention, say so and
  show the classification under both conventions rather than letting an
  assumption silently pick the verdict.
- **Currency.** Normalize to the budget's currency at an approximate current
  rate and say which rate you assumed.
- **Annualized vs. monthly.** Some markets quote monthly (often ×13 or ×14 to
  annualize — e.g. 13th month pay), others annual. Mismatched annualization
  is a silent 8% error.
- **Increase-ask realism.** Asks of 15–30% over current are market-normal for
  a move in most hiring markets; an ask *below* +10% can signal urgency (probe
  gently — urgency isn't disqualifying but explains negotiation dynamics); an
  ask above +50% needs a reason (undermarket current pay, added scope) —
  probe for it rather than assuming either greed or error.

## Notice period & availability economics

Availability is part of the budget conversation: a hard start deadline plus a
long notice period can cost more than a salary gap.

- Establish: notice period per current contract, whether it's buyout-able, and
  earliest realistic start date (assume notice starts after offer acceptance,
  not after your screen).
- 30 days is standard in many markets; 60–90 days is common at senior levels
  in some (e.g. India, parts of Europe). "Immediate joiner" is a plus worth
  naming — and worth one probe about why (often benign: contract just ended).
- If the client deadline minus today is shorter than the notice period, that's
  a gate-level conflict unless buyout or negotiation is on the table — cost it
  as a condition.

## Philippines annex

Apply when the role or candidate is Philippines-based; these specifics change
the like-for-like math:

- **13th month pay** is legally mandatory (1/12 of annual basic) — it is *not*
  a differentiator, so a package "including 13th month" is padding the number.
  Annualize monthly basic ×13 on both sides consistently.
- **Allowances** (de minimis, transport, meal, communication) are commonly
  quoted inside "monthly package"; decompose to basic before comparing —
  taxation and 13th-month both compute on basic.
- **HMO with dependents, group life, leave conversion** carry real cash value
  in candidate decisions; note when the client's benefits offset a small basic
  gap.
- **Night differential** (statutory minimum +10% for 10pm–6am work) matters
  for shift roles supporting AU/EU/US hours — confirm whether quoted comp
  already includes the shift premium.
- **Notice**: 30 days' written notice is the statutory resignation standard;
  many employers hold candidates to the full 30 even when asked to waive.
- Quote in ₱ (PHP); "k" conventions are monthly ("₱90k" = ₱90,000/month
  basic unless stated otherwise).

## Comp table (goes in the report)

| Item | Candidate | Budget/Target | Basis |
|---|---|---|---|
| Expected comp | | ceiling | like-for-like basis after normalization; conversion conventions stated |
| Current comp | where lawfully known, else "not collected" | — | basic/package, currency, monthly/annual |
| Increase ask | X% (only when current known) | — | |
| Classification | **Within / Stretch / Breach / Unassessed** | | one-line justification; note if conversion-sensitive near the 10% line |
| Notice / availability | | deadline if any | conflict yes/no |

---

# Pay rate & bill rate analysis

Every single-candidate screen produces this block, budget supplied or not —
it answers "what should this role cost, and what do we need to bill," which
the ceiling comparison above cannot. It is planning context alongside the
classification, never a replacement for it: **the existing Within / Stretch /
Breach / Unassessed classification and its verdict effects are unchanged by
anything in this section.**

## Establish engagement shape first — do not skip

Two facts move this math more than the market band's own error bars. Resolve
both before pricing; ask the user when the materials don't say:

1. **Which calculator applies.** Staff Aug is the default for a
   single-candidate screen. If the requisition is a seat in a pod or an
   outcome deal (Managed Capacity / Managed Services), still price the seat
   with the Staff Aug model but state that deal-level margin is set
   elsewhere and this seat price is an input to it, not the answer.
2. **Internal employee vs. vendor/contractor.** Converting a ₱125k-basic
   internal seat to vendor strips roughly ₱29,000/month of statutory,
   insurance, and HMO cost (per the workbook lever board) — a rate analysis
   that ignores engagement type is wrong by more than the band's error bars.
   In vendor mode the cost stack is the vendor's rate plus only what
   Ascendion still carries (typically BGV/laptop if provided).

## Cost model — the user's calculator, not an invented one

**Precedence:** when the user's live Ascendion sales calculator workbook is
available in the session, read it and take every convention from it — the
user updates it, and the workbook always outranks what follows. The model
below is a **snapshot (taken 2026-07 from "Patrick Version 2026 Updated")**
for when the workbook isn't attached; label any snapshot-based run "cost
model: snapshot 2026-07 — verify against current workbook".

Workbook orientation (as of the snapshot): sheets `TOD - Staff Aug`,
`Managed Capacity`, `Managed Services`, plus a hidden `SSS` statutory tab.
The Staff Aug sheet prices three scenarios — (1) known bill rate → GP/GPM,
(2) target GPM + utilisation → required rate (the "Reverse Solver"), (3)
bill-rate ceiling → margin fit + levers. The rate analysis here runs
scenarios 2 and 3; when the user supplies a candidate's or client's actual
bill rate, run scenario 1 too.

Staff Aug monthly employer cost =

    Basic
  + SSS ER + SSS MPF ER + EC ER      (all three looked up on Basic +
                                      non-taxable allowance against the SSS
                                      schedule)
  + PHIC ER                          (2.5% of basic, capped ₱2,500 at
                                      basic ≥ ₱100,000)
  + HDMF ER ₱200
  + 13th month accrual               (Basic ÷ 12)
  + severance accrual                (Basic ÷ 12, when costed — default: costed)
  + life & accident insurance
  + HMO incl. dependents
  + BGV amortisation
  + laptop amortisation
  + taxable & non-taxable allowances

Bill-rate math:

    Effective bill (monthly) = bill normalised to monthly
                               (daily × 21.75; hourly × 174 @ 8 hrs/day
                                or × 195.75 @ 9 hrs/day)
                               − unbilled leaves − unbilled holidays
    GP  = effective bill − total cost        GPM = GP ÷ effective bill
    U   = 1 − (non-billable leaves + non-billable holidays) ÷ (21.75 × 12)
    Required bill = total cost ÷ (U × (1 − target GPM))

The unbilled-leave/holiday deduction is (monthly bill ÷ 21.75) × (days ÷ 12)
per category; utilisation can also be set manually (workbook supports both —
auto from leave/holiday flags is the default).

Defaults unless the user says otherwise: 21.75 workdays/month, 12 leaves/yr,
20 holidays/yr, leaves **not** billable, holidays billable, severance
costed, **40% target GPM**, **30% floor GPM**, FX ₱56/USD, 12% VAT excluded
from GPM. (The workbook's target-GPM cell is a deal input — read the live
value when the workbook is attached.) `scripts/rate_math.py` implements
exactly this arithmetic — use it rather than freehand math; statutory
lookups (the SSS trio) are inputs to it, not hardcoded in it.

**Re-verify the statutory tables, not just salary data.** The workbook's SSS
tab is labelled 2025 (snapshot: SS ER caps at ₱2,000 on a ₱20,000 MSC, MPF
ER at ₱1,500 on the ₱15,000 MPF band, EC ₱30; lookup is approximate-match on
basic + non-taxable allowance). 2025 was the final scheduled step of the RA
11199 contribution ladder, so the table may well still be current — but
check the current SSS schedule (and the PhilHealth premium rate/cap and HDMF
rate) on every run, and flag drift rather than silently using a stale table.

## Market band — sourcing discipline (this is the part that has to be right)

- **Search live every run.** Never answer the band from training data; PH IT
  salary data moves, and a stale band silently mis-prices a deal.
- Scope the band to role title, seniority, tech stack, and Metro Manila (or
  the stated work location). Report **P25 / P50 / P75 monthly basic**, and
  place the candidate in the band with a one-line why.
- **Cite each source with its publication date** and stamp the whole band
  **AS OF the run date**.
- Prefer PH-specific sources with disclosed methodology and sample size over
  global aggregators extrapolating from thin PH data. Name what you used
  *and what you rejected*.
- Where credible sources disagree by more than ~20%, show the range and the
  disagreement — never average into false precision.
- Mark the band **ESTIMATE — VERIFY**, and say what would firm it up: the
  team's own recent offers for the role, the client's prior accepted rates,
  or a live recruiter check.

## What the rate block reports

In this order (template in `references/report-template.md`):

1. **Market pay band** — P25/P50/P75 monthly basic, scoped and sourced as
   above; candidate's position in the band.
2. **Monthly employer cost** — at P50, and at the candidate's expectation
   where known, via the cost model.
3. **Required bill rate** — at the 40% target GPM and the 30% floor —
   monthly, daily, and hourly.
4. **Indicative TCV** — required monthly bill × engagement duration, using
   the per-client duration defaults in `references/client-profiles.md` (AXA
   3 months, UL 6, Manulife 6, Macquarie 12) unless the requisition states
   its own. Always labelled *indicative*.
5. **Priceability verdict** — whether the role is priceable at market pay
   against any ceiling the user gave, using the workbook's ceiling-fit
   ladder verbatim: **FEASIBLE — hits target within ceiling** (cost headroom
   ≥ 0 at target GPM) · **BELOW target, above floor** · **BELOW floor —
   restructure** · **LOSS at this ceiling**. Cost room at a ceiling =
   ceiling × U × (1 − target GPM); headroom = room − total cost. When not
   FEASIBLE, list the levers that close the gap with the monthly ₱ each
   frees, computed from the cost model (never recited from memory), in the
   lever board's order — which ranks by monthly ₱ freed:
   1. Convert to vendor engagement — frees the statutory subtotal + life &
      accident + HMO incl. dependents (≈₱29k/month on a ₱125k basic).
   2. Move basic toward the max affordable basic — solve
      (cost room − SSS trio − HDMF − other costs) ÷ (1 + 0.025 + 2/12),
      the divisor covering PHIC, 13th month, and severance that scale with
      basic.
   3. Trim non-taxable allowance (frees its full amount, and can drop the
      SSS bracket).
   4. Trim HMO plan/dependents.
   5. Laptop provided by client (frees the amortisation).
   Pricing at the 30% floor instead of the 40% target and extending the
   engagement duration are pricing-side levers — present them separately
   from the cost-side board, since they change the required rate, not the
   cost.

## Guardrails

- An estimated market band **never** drives a Breach classification or a Do
  Not Endorse on its own. Only the candidate's actual stated expectation
  against a user-supplied ceiling can. Band-only comp picture → fit stays
  **Unassessed**; the band is planning context, labelled as such.
- A known expectation well above the band is a **negotiation datapoint** —
  report the gap in pesos and percent — not a fit judgment.
- **Level mismatch is structural.** If the candidate's last role sits a band
  above the requisition, say the expectation risk is structural and name the
  likely landing number (their current band's floor, not the req's midpoint).
- One line of the report's opening block carries the required bill at
  target; the full table lives in the rate block. The rate work must never
  push the verdict down the page.
