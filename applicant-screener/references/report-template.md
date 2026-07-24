# Screening Report Template

Use this structure exactly. The verdict leads — a reader in a hurry gets the
answer, the confidence, and the one thing that matters most within the first
three lines. Omit a section only when it's genuinely empty (e.g. no flags),
and say "none found" rather than deleting it, so absence reads as checked-
and-clear instead of unchecked.

---

## Single-candidate report

```markdown
# Screening Report: [Candidate Name] — [Role Title]

## Verdict: [ENDORSE / ENDORSE WITH CONDITIONS / DO NOT ENDORSE / INSUFFICIENT INFORMATION]

**Weighted score:** X% [· sensitivity: Y% if unknowns score 2] · **Comp fit:** Within/Stretch/Breach/Unassessed · **Gates:** all passed / failed: [gate]
**Bottom line:** [2–3 sentences: the single strongest reason for this verdict,
the biggest risk, and — if borderline — the one piece of information that
would most change the call.]

[If ENDORSE WITH CONDITIONS — list each condition: what must be resolved, by
whom, before what stage.]
[If INSUFFICIENT INFORMATION — list exactly what to collect, then re-screen.]

## Gate check

| Gate | Result | Evidence |
|---|---|---|
| Work authorization | ✅ / ❌ / ❓ | |
| Location & work setup | | |
| [Mandatory cert / min experience / start date / budget ceiling …] | | |

## Scorecard

Weights defined from the JD before scoring; challenge them if they look wrong.

| Criterion | Weight | Score /5 | Evidence [demonstrated/claimed/inferred] |
|---|---|---|---|
| [Must-have ▸ criterion] | | | |
| [Nice-to-have ▸ criterion] | | | |
| **Weighted total** | 100 | **X%** | scored on Z of 100 weight; U-criteria excluded |

## Compensation & availability

[Comp table from references/compensation.md — current, expected, budget,
increase ask, classification with one-line justification, notice period vs.
deadline.]

## Risks & red flags

| Flag | Severity | Probe question |
|---|---|---|
| [—] | [Concern/Critical] | [—] |

[Or: "None found — tenure pattern, dates, and credentials all check out."]

## Strengths worth selling

[2–4 bullets — the case *for* the candidate, phrased so the user can lift
them straight into a client submittal or hiring-manager pitch. Every screen
that reaches a scorecard gets this section, including Do Not Endorse — it
keeps the screen honest about what the candidate does bring.]

## Probe questions for the next conversation

[6–10 questions, ordered: knockouts → comp → skill depth → flags →
behavioral. Pull phrasings from references/screening-questions.md. Each
traces to a U-score, a Stretch, or a flag above — no generic filler.]

---
*Screening assessment produced by AI as decision support against the stated
JD, budget, and requirements. Scores reflect evidence available in the
materials provided as of [date]. Final hiring judgment rests with the
recruiter/hiring team. Protected characteristics were excluded from
evaluation.*
```

## Batch report (multiple candidates, one role)

Lead with the ranking, then one full single-candidate report per candidate
(collapsible/sectioned). Ranking table:

```markdown
# Screening Summary: [Role Title] — N candidates

| # | Candidate | Verdict | Score | Comp fit | Gates | Differentiator |
|---|---|---|---|---|---|---|
| 1 | | ENDORSE | 82% | Within | ✅ | [one line — what separates them from #2] |
| 2 | | ENDORSE W/ CONDITIONS | 74% | Stretch | ✅ | |
| 3 | | DO NOT ENDORSE | 51% | Breach | ❌ budget | |

**Recommendation:** [Who to submit/advance, in what order, and why — or state
plainly that no candidate clears the bar and what profile to source instead.]
```

Ranking order: verdict tier first, weighted score second, comp fit third.
Never promote a candidate a tier because the pool above them is thin.

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
