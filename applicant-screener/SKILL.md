---
name: applicant-screener
description: Screen job applicants against a job description (JD), salary budget, and any other stated requirements, producing an evidence-based scorecard and a mandatory verdict — Endorse / Endorse with Conditions / Do Not Endorse / Insufficient Information. Use whenever the user shares a resume, CV, LinkedIn profile, or candidate write-up and wants screening, evaluation, vetting, shortlisting, fit assessment, comparison, or ranking — including phrasings like "screen this candidate", "is this profile a fit", "should I endorse/submit/proceed", "check against the JD/budget", or when they simply paste a CV plus a JD with no explicit instruction. Applies even when only a CV is provided with no JD yet (the skill gathers the requirements first), and for batch screening of multiple candidates against one role.
---

# Applicant Screener

Screen candidates the way the best-evidenced hiring research says to: against a
defined standard, not an impression. Structured, criterion-anchored evaluation
is dramatically more predictive and more consistent than holistic resume
reading — and it produces a decision the user can defend to a hiring manager or
client. Every screen ends in a verdict; never leave the user with a summary and
no recommendation.

The workflow below is the spine. Reference files carry the depth — read each
one at the step that calls for it rather than all upfront.

## Operating principles

These govern every step:

1. **Evidence over impression.** Every score and every claim in the report must
   trace to something concrete: a line in the CV, a screening note, a stated
   number. Tag evidence as **demonstrated** (verifiable output: shipped
   projects, quantified results, certifications), **claimed** (asserted but
   unverified: skill lists, self-ratings), or **inferred** (your deduction:
   "likely has X because of role Y"). Never let an inferred point outweigh a
   demonstrated one.
2. **The rubric is fixed before scoring begins.** Build the requirement matrix
   from the JD first, then score against it. Never reverse-engineer criteria to
   fit a candidate you like — that is how halo effect gets laundered into a
   scorecard. When screening multiple candidates for one role, the same matrix
   applies to all of them, unchanged.
3. **Gaps in information are findings, not guesses.** When the CV doesn't say,
   the answer is "unknown — probe in the screen", never a silently assumed
   score. Unknowns on must-haves cap the verdict (see Verdict rules).
4. **Red flags are questions, not rejections.** An employment gap or short
   tenure is something to probe, not grounds to fail someone. Only hard gate
   failures and confirmed integrity issues justify rejection on their own.
5. **Never evaluate protected characteristics.** Age, date of birth, gender,
   gender identity, sexual orientation, civil/marital status, pregnancy or
   family plans, caregiving status, religion, ethnicity, caste, national
   origin (work authorization is assessed as a legal requirement, never
   inferred from origin signals), disability or health conditions, union
   membership, political views, veteran status, photos, accent, or
   appearance — even when the CV volunteers them, as CVs in many regions do.
   They must not appear in scores, rationale, or the report, and criminal or
   credit history is out of scope for this screen entirely (it is regulated
   separately — leave it to the user's formal background-check process). If a
   candidate's answer to a probe discloses protected information, exclude it
   from the evaluation and do not record it. This keeps the screen lawful
   (Title VII/EEOC and equivalents), and it also keeps it accurate: none of
   these predict job performance.
6. **This is decision support, not the decision.** The verdict is a
   recommendation to a human; say so in the report footer, and never present
   the screen as final. Be aware that using an AI screen at all may bring the
   user's process under AI-in-hiring rules (NYC Local Law 144's bias-audit and
   notice duties, the EU AI Act's high-risk obligations, and similar) — the
   evidence-cited scorecard supports the auditability those rules expect, but
   it does not by itself make the user compliant; that is their counsel's
   call, and worth a one-line reminder if the user seems to be automating
   decisions end-to-end.

## Step 0 — Intake

Collect what you have and name what you don't. Required inputs:

- **JD / requisition**: role title, responsibilities, required and preferred
  skills, experience level, education/certifications, location and work setup
  (onsite/hybrid/remote), shift/schedule if any.
- **Budget**: salary or rate range, currency, and whether it's basic pay or a
  total package. If the user gave a single number, treat it as the ceiling.
- **Candidate materials**: CV/resume at minimum; plus anything else offered —
  screening-call notes, portfolio, LinkedIn, assessment results, expected
  compensation (and current, where lawfully known), notice period /
  availability, and motivation signals: reason for leaving, why this role,
  competing processes or offers in flight. Motivation data rarely arrives
  unasked — when absent, it becomes probe questions, because offer-acceptance
  risk is part of what the user is deciding.
- **Other requirements**: anything the user stated beyond the JD — client
  preferences, start-date deadline, work authorization, background-check
  needs, specific tools or clearances.

If something material is missing, do not stall the whole screen: run every
step the inputs support, then let the Verdict step decide whether the holes are
disqualifying to a conclusion (they often force *Insufficient Information* —
that is a legitimate verdict, not a failure). List every missing item and the
exact question that would resolve it. If there is no budget, screen everything
else and mark compensation fit as unassessed. If there is no JD at all, ask for
one — a screen without a standard is exactly the impression-based evaluation
this skill exists to prevent.

## Step 1 — Build the requirement matrix

Parse the JD and any extra requirements into a scoring matrix **before looking
closely at the candidate**:

1. **Split must-haves from nice-to-haves.** Must-haves are requirements whose
   absence makes the hire fail: legally required credentials, core technical
   skills the role cannot function without, minimum experience the client
   insists on, location/setup/shift constraints, work authorization. Everything
   else — preferred skills, bonus domains, "a plus" items — is nice-to-have.
   JDs routinely inflate wants into needs; use judgment about which "required"
   items are truly load-bearing, and say so when you downgrade one.
2. **Weight the criteria** so weights sum to 100. Default allocation (adjust
   to the role and state your weights): core technical/functional skills 40,
   relevant domain/industry experience 20, seniority & scope match 15,
   nice-to-have skills 10, communication & collaboration evidence 10,
   stability/logistics 5. Compensation fit and hard gates are handled
   separately — they gate, they don't average.
3. **Define what "strong" looks like per criterion** — one line each — so the
   scoring anchors in `references/scoring-rubric.md` have something concrete
   to bite on.

Show the matrix in the report so the user can challenge the weights.

## Step 2 — Knockout gates

Check hard gates first; a clean gate check is what makes the rest of the
scoring worth doing. Gates are a **closed list** of legal/logistical items,
plus anything the user *explicitly names* as a knockout:

- Work authorization / right to work in the role's location
- Location and work-setup compatibility (including relocation willingness if
  stated)
- Licenses or certifications that are legally required for the role
- Budget: expected compensation vs. ceiling (classification per Step 4;
  Breach gates, Stretch conditions)
- Availability vs. hard start-date deadline
- Confirmed integrity issues (fabricated credentials, misrepresented dates)
- Any requirement the user or client has explicitly called a dealbreaker

Everything else the JD labels "required" — years of experience, skills,
domain — is a **scored must-have**, not a gate: it fails a candidate through
the must-have score floor in Step 6, which tolerates near-misses the way real
hiring does (a 7-year candidate against "8+ years" is a scoring question, not
an auto-reject). A requirement never appears in both the gate table and the
scorecard — decide which it is, once, and say so.

Every gate gets one of four statuses, and the distinction is load-bearing for
the verdict:

- **✅ Verified** — affirmative evidence (document seen, candidate stated it
  directly, user confirmed).
- **✅ Provisional** — supported by claimed or reasonably inferred evidence
  with nothing contrary, where confirmation is routine (sourcer notes say
  "amenable to hybrid"; a candidate working in-country for local employers,
  pending the standard document check). Never infer work authorization from
  name, education, or origin signals — provisional status for it comes only
  from an actual statement or an existing local employment pattern.
- **❓ Unverified** — no evidence either way.
- **❌ Failed** — evidence of incompatibility.

A ❌ gate means **Do Not Endorse** regardless of scores — but verify the
failure is real before pulling the trigger: an ambiguous CV line is ❓, not ❌.
Provisional and unverified gates flow into the verdict rules in Step 6; every
one of them must reappear as a named probe or condition.

## Step 3 — Score the candidate

Read `references/scoring-rubric.md` and score every criterion in the matrix
0–5 against its anchors, citing evidence with its demonstrated/claimed/inferred
tag. Key habits, argued fully in the reference:

- Score what the CV *shows*, not what the job titles imply.
- Recency matters: a skill last used seven years ago is not today's skill.
- Use the full scale. A screen where everything lands on 3–4 has measured
  nothing; force yourself to identify the candidate's genuinely weakest and
  strongest areas.
- Compute the weighted total by the rubric's formula (unknowns excluded from
  both sides of the fraction, with a sensitivity line showing the total if
  unknowns scored 2).

## Step 4 — Compensation & budget analysis

Read `references/compensation.md` and work the numbers: expected compensation
vs. budget ceiling on a like-for-like basis (current comp only where lawfully
known — the reference covers salary-history-ban jurisdictions),
basic-vs-total-package traps, currency and rate-type normalization, and
notice-period economics. The reference is the single source of truth for the
classification thresholds; the outcome is one of **Within / Stretch / Breach /
Unassessed**. Breach gates the verdict, Stretch conditions it, Unassessed
caps it at Endorse with Conditions.

## Step 5 — Risk & red-flag review

Read `references/red-flags.md` and sweep the materials for tenure patterns,
gaps, date inconsistencies, title inflation, credential concerns, and
fraud/authenticity signals (an increasingly real problem — treat it
seriously). For each flag found, record: the flag, severity
(note / concern / critical), and the probe question that would resolve it.
Flags become interview probes in the report; only *critical, evidence-backed*
flags (confirmed fabrication, impostor signals) escalate to a gate failure.

## Step 6 — Verdict

Mandatory. Exactly one of four:

| Verdict | Conditions |
|---|---|
| **ENDORSE** | Every gate ✅ (verified or provisional — no ❓/❌) · weighted score ≥ 75% · every must-have scored ≥ 3 on real evidence · comp Within budget · no unresolved critical flags. Provisional gates are compatible with Endorse only when each outstanding confirmation is named in the probe list |
| **ENDORSE WITH CONDITIONS** | No gate ❌ · weighted score ≥ 60% · comp at worst Stretch or Unassessed · remaining concerns are specific, probeable, and plausibly resolvable — and you list each condition explicitly. Any ❓ gate lands here at best, with that gate as a named condition; Unassessed comp lands here at best, with "confirm expected comp ≤ ceiling" as a condition |
| **DO NOT ENDORSE** | Any gate ❌, or weighted score < 60%, or a must-have scored ≤ 1 with no path to resolve, or comp Breach (absent an explicit user waiver of the budget), or a critical flag stands |
| **INSUFFICIENT INFORMATION** | Two or more *material* unknowns (must-have U-scores, ❓ gates, or Unassessed comp) and the verdict would flip depending on the answers — list exactly what to collect, then re-screen. A single material unknown is a condition, not an information failure |

Rules of application:

- Gates and critical flags override scores in both directions — a 90% scorer
  who fails work authorization is still Do Not Endorse.
- The score bands are defaults, not physics. If you deviate (e.g. a 58% scorer
  whose two weak criteria are trainable nice-to-haves), say so and justify it —
  the band you *didn't* follow must appear in the rationale.
- "Endorse with Conditions" without listed conditions is not a verdict; each
  condition must name who resolves it and how (e.g. "confirm amenability to
  ₱X basic — recruiter, before submittal").
- Borderline calls get a confidence note: what single piece of information
  would most change this verdict?
- **User overrides.** The constraints belong to the user: if they waive their
  own budget, deadline, or a stated dealbreaker ("ignore the budget for this
  one"), re-screen with the waiver applied and record it in the report so the
  relaxed standard is visible. The *assessment* is not theirs to waive: if
  asked to output an endorsement the evidence doesn't support ("just endorse
  him"), give the honest verdict with reasons — the user can submit whomever
  they choose, but a screen that flatters on request protects no one,
  including them.

## Step 7 — Report

Produce the report using the exact template in
`references/report-template.md`. The template leads with the verdict — the
user should get the answer in the first three lines, then the evidence. Where
the screen surfaced unknowns, the report's **Probe questions** section turns
them into a ready-to-use screening-call script; pull question phrasings from
`references/screening-questions.md` when useful.

## Batch mode — multiple candidates, one role

Build the matrix once (Step 1), then run Steps 2–6 per candidate
independently — never score candidate B relative to candidate A; relative
scoring re-introduces the impression-based comparison this skill replaces.
Then add a ranking table: candidate, weighted score, comp fit, gates, verdict,
one-line differentiator. Rank by verdict tier first, weighted score second,
comp fit as the tiebreaker. Two honesty rules for the table: when candidates
have different scored-weight coverage (unknowns excluded for one but not
another), show the coverage next to each score — an 80% scored on 70 of 100
weight is not the same measurement as an 80% on full weight; and it is a
legitimate outcome for a batch to produce zero endorsements — say so plainly
rather than endorsing the least-bad option.

Scale the write-up to the batch, not the other way around. Up to ~5
candidates: full report each. Beyond that: ranking table plus a short-form
block per candidate (verdict, score with coverage, gate exceptions, top two
strengths, top two concerns, the 2–3 probes that matter) — full reports only
for the candidates you're recommending advance, or on request. The scoring
rigor never shrinks with the batch; only the prose does.

The reverse case — one candidate against several roles — works the same way
mirrored: one matrix per role, full screen per role, then a table of verdicts
recommending which role (if any) to put the candidate forward for.

## Reference files

| File | Read at | Contents |
|---|---|---|
| `references/scoring-rubric.md` | Step 3 | 0–5 anchors, per-criterion-type guidance, calibration traps |
| `references/compensation.md` | Step 4 | Budget math, package normalization, notice-period economics, Philippines annex |
| `references/red-flags.md` | Step 5 | Flag catalog with severities, fraud/authenticity signals, probe conversions |
| `references/screening-questions.md` | Step 7 | Question bank: comp/logistics, skill-depth, tenure/gap, authenticity, behavioral |
| `references/report-template.md` | Step 7 | The exact output template, single and batch |
