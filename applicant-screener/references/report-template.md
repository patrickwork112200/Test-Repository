# Screening Report Template (internal working artifact)

This full report is the audit trail behind the screen — build it so every
line of the user-facing summary can be defended, but **the default
deliverable is the decision summary + action email in
`references/output-email.md`**; produce this full report only when the user
asks for the scorecard or is reviewing the methodology itself.

When producing it, use this structure exactly. The verdict leads — a reader
in a hurry gets the answer, the confidence, and the one thing that matters
most within the first three lines. Never delete a section: when one is
empty, write "none found" in it, so absence reads as checked-and-clear
instead of unchecked.

**The report is an internal document.** Comp figures, red flags, competing
processes, and the verdict rationale are for the user and their team — not
for the candidate, and not for the client as-is. Only the "Strengths"
section is written to be liftable outward, and only for endorsed candidates.

---

## Single-candidate report

```markdown
# Screening Report: [Candidate Name] — [Role Title]

## Verdict: [ENDORSE / ENDORSE WITH CONDITIONS / DO NOT ENDORSE / INSUFFICIENT INFORMATION]

**Weighted score:** X% [· sensitivity: Y% if unknowns score 2] · **Comp fit:** Within/Stretch/Breach/Unassessed · **Gates:** [all verified · / · all passed (N provisional — see probes) · / · none failed, N unverified — see conditions · / · failed: [gate]]
**Bill:** required ₱X/hr (₱Y/day · ₱Z/mo) at 40% target GPM — [engagement shape; workbook/snapshot; AS OF date; full detail in the rate block below]
**Bottom line:** [2–3 sentences: the single strongest reason for this verdict,
the biggest risk, and — if borderline — the one piece of information that
would most change the call.]
**Robustness:** [how many criteria would have to move up a full point to
change the verdict tier — e.g. "raising the two weakest criteria a point
each still lands at 57%, below the 60% threshold"; if one point flips it,
label the call borderline.]

[If ENDORSE WITH CONDITIONS — list each condition: what must be resolved, by
whom, before what stage. If a condition asks a sourcing team to revise the
CV, split it explicitly into "verify with the candidate and evidence it
(project names, dates, scale)" vs. "add it" — unverified additions fail the
panel rather than pass the screen, so a keyword-padded CV is a worse
deliverable than the current one.]
[If DO NOT ENDORSE on role fit (not gates/integrity) — name the role profile
the evidence does support and recommend screening against it: "Do not
endorse for this requisition; profile fits [role] — screen against that
req if one is open."]
[If INSUFFICIENT INFORMATION — list exactly what to collect, then re-screen.]

[If the user waived a constraint (budget, deadline, a dealbreaker), state the
waiver here so the relaxed standard is visible.]

## Gate check

Statuses per SKILL.md Step 2: ✅ verified · ✅ provisional (claimed/inferred,
confirmation routine — never print "passed" without the qualifier) · ❓
unverified · ❌ failed.

| Gate | Result | Evidence |
|---|---|---|
| Work authorization | ✅ verified / ✅ provisional / ❓ / ❌ | |
| Location & work setup | | |
| [Legally required cert / start date / budget ceiling / user-named dealbreaker …] | | |

## Scorecard

Weights defined from the JD before scoring; challenge them if they look wrong.

| Criterion | Weight | Score /5 | Evidence [demonstrated/claimed/inferred] |
|---|---|---|---|
| [Must-have ▸ criterion] | | | |
| [Nice-to-have ▸ criterion] | | | |
| **Weighted total** | 100 | **X%** | scored on Z of 100 weight; U-criteria excluded |

## Compensation & availability

[Comp table from references/compensation.md — expected vs. ceiling first,
current only where lawfully known, classification with one-line
justification, notice period vs. deadline. Internal only.]

## Rate & bill analysis — [Staff Aug / seat in Managed deal] · [internal / vendor] · AS OF [date]

[Per the "Pay rate & bill rate analysis" section of
references/compensation.md. Internal only. Keep it tabular and tight — the
verdict above must not be pushed down the page.]

| Market monthly basic ([role], [location]) | P25 | P50 | P75 |
|---|---|---|---|
| Band (ESTIMATE — VERIFY) | | | |

Candidate sits [where] in the band because [one line]. [If expectation known
and well above band: negotiation datapoint — gap ₱X / Y%; if last role sits
a band above the req: expectation risk is structural; likely landing ₱Z.]

| | At P50 | At candidate expectation |
|---|---|---|
| Monthly employer cost | | [if known] |
| Required bill @ 40% target GPM | ₱/mo · ₱/day · ₱/hr | |
| Required bill @ 30% floor | | |
| Indicative TCV ([client] default [N] months) | | |

**Priceability:** [workbook ladder verdict: FEASIBLE / BELOW target, above
floor / BELOW floor — restructure / LOSS at this ceiling — vs. any ceiling
given; if not FEASIBLE, levers with monthly ₱ freed, lever-board order.]
Sources: [each named with publication date; note what was rejected and why;
band disagreement >~20% shown as a range]. Cost model: [live workbook /
snapshot 2026-07]. What would firm this up: [own recent offers / client's
prior accepted rates / live recruiter check].

## Risks & red flags

| Flag | Severity | Probe question |
|---|---|---|
| [—] | [Concern/Critical] | [—] |

[Or: "None found — tenure pattern, dates, and credentials all check out."
Include acceptance/pipeline risk here when known — competing processes,
counteroffer exposure, push-only motivation — with the recommended response
(expedite, pre-close comp, address the stated dealbreaker). Internal only.]

## Strengths

[2–4 bullets — the case *for* the candidate. Every screen that reaches a
scorecard gets this section, including Do Not Endorse — it keeps the screen
honest about what the candidate does bring. For ENDORSE-tier verdicts,
phrase the bullets so the user can lift them straight into a client
submittal or hiring-manager pitch; for DO NOT ENDORSE, write them as an
internal fairness check, not as submittal copy — selling language on a
rejected candidate invites accidental reuse.]

## Probe questions for the next conversation

[6–10 questions, ordered: knockouts → comp → motivation → skill depth →
flags → behavioral. Pull phrasings from references/screening-questions.md.
Each traces to a U-score, a ❓/provisional gate, a Stretch, or a flag above —
no generic filler. If the user permits disclosing budget, the comp probe
should disclose it; if unknown, ask expectations only.]

---
*Screening assessment produced by AI as decision support against the stated
JD, budget, and requirements. Scores reflect evidence available in the
materials provided as of [date]. Final hiring judgment rests with the
recruiter/hiring team. Protected characteristics were excluded from
evaluation.*
```

## Batch report (multiple candidates, one role)

Lead with the ranking, then per-candidate detail sized per SKILL.md batch
mode (full reports up to ~5 candidates; short-form blocks beyond that, full
reports only for those recommended to advance). Ranking table:

```markdown
# Screening Summary: [Role Title] — N candidates

| # | Candidate | Verdict | Score (coverage) | Comp fit | Band position | Gates | Differentiator |
|---|---|---|---|---|---|---|---|
| 1 | | ENDORSE | 82% (100/100) | Within | ~P50 | ✅ | [one line — what separates them from #2] |
| 2 | | ENDORSE W/ CONDITIONS | 74% (85/100) | Stretch | P75+ | ✅ 1 provisional | |
| 3 | | DO NOT ENDORSE | 51% (100/100) | Breach | unknown | ❌ budget | |

**Recommendation:** [Who to submit/advance, in what order, and why — or state
plainly that no candidate clears the bar and what profile to source instead.]

[One rate block for the role — not one per candidate; the Band position
column above is each candidate's only per-candidate rate line.]
```

Ranking order: verdict tier first, weighted score second, comp fit third.
Never promote a candidate a tier because the pool above them is thin, and
when coverage differs, note that scores on materially different coverage
(e.g. 85 vs. 100 of 100 weight) are not directly comparable — verdict tier,
which already accounts for unknowns, is the safer ordering.

## Style rules

- State numbers plainly; never bury the verdict under hedging. "Endorse with
  conditions" + a firm condition list beats a mushy "strong candidate but…".
- Every evidence cell cites something the user can check (CV line, note,
  stated figure) with its demonstrated/claimed/inferred tag.
- Keep the whole single-candidate report readable in ~2 minutes; depth lives
  in the tables, not in prose paragraphs.
- If the user asked for a specific output format (their own template, a
  submittal email, a one-liner), honor it — but the verdict line and the
  conditions list survive into any format; they are the non-negotiable core
  of the skill's output.
