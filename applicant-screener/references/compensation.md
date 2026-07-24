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
  table: monthly ↔ hourly via ~22 working days × 8 hours (≈176 hrs/month)
  unless the contract says otherwise; contractor all-in rates price in
  benefits, leave, and statutory items an FTE package carries separately —
  a rough 1.2–1.4× loading on FTE basic is the comparison heuristic, labeled
  as such. When the classification lands within ~3 percentage points of the
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
