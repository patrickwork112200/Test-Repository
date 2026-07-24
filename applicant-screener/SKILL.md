---
name: applicant-screener
description: Screen job applicants against a job description (JD), salary budget, and any other stated requirements, producing an evidence-based scorecard and a mandatory verdict — Endorse / Endorse with Conditions / Do Not Endorse / Insufficient Information. Use whenever the user shares a resume, CV, LinkedIn profile, or candidate write-up together with a JD, requisition, role requirements, or budget and wants screening, evaluation, vetting, shortlisting, fit assessment, comparison, or ranking — including phrasings like "screen this candidate", "is this profile a fit", "should I endorse/submit/proceed", "check against the JD/budget", or when they simply paste a CV plus a JD with no explicit instruction. Also use for batch screening of multiple candidates against one role.
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
   civil/marital status, religion, ethnicity, nationality (except work
   authorization as a legal requirement), disability, pregnancy, photos, or
   appearance — even when the CV volunteers them, as CVs in many regions do.
   They must not appear in scores, rationale, or the report. This keeps the
   screen lawful (Title VII/EEOC and equivalents), and it also keeps it
   accurate: none of these predict job performance.
6. **This is decision support, not the decision.** The verdict is a
   recommendation to a human. Say so in the report footer. The evidence-cited
   scorecard doubles as the audit trail that AI-in-hiring rules (NYC Local Law
   144, EU AI Act) increasingly expect.

## Step 0 — Intake

Collect what you have and name what you don't. Required inputs:

- **JD / requisition**: role title, responsibilities, required and preferred
  skills, experience level, education/certifications, location and work setup
  (onsite/hybrid/remote), shift/schedule if any.
- **Budget**: salary or rate range, currency, and whether it's basic pay or a
  total package. If the user gave a single number, treat it as the ceiling.
- **Candidate materials**: CV/resume at minimum; plus anything else offered —
  screening-call notes, portfolio, LinkedIn, assessment results, expected and
  current compensation, notice period / availability.
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
scoring worth doing. Standard gates (apply the ones the inputs support):

- Work authorization / right to work in the role's location
- Location and work-setup compatibility (including relocation willingness if
  stated)
- Mandatory licenses or certifications
- Minimum experience bar explicitly set by the user or client
- Budget: expected compensation vs. ceiling (see Step 4 for how much stretch
  is tolerable before this gates)
- Availability vs. hard start-date deadline
- Confirmed integrity issues (fabricated credentials, misrepresented dates)

A failed gate means **Do Not Endorse** regardless of scores — but verify the
failure is real before pulling the trigger: an ambiguous CV line is a probe
question, not a gate failure. Distinguish *failed* (evidence of
incompatibility) from *unverified* (no evidence either way).

## Step 3 — Score the candidate

Read `references/scoring-rubric.md` and score every criterion in the matrix
0–5 against its anchors, citing evidence with its demonstrated/claimed/inferred
tag. Key habits, argued fully in the reference:

- Score what the CV *shows*, not what the job titles imply.
- Recency matters: a skill last used seven years ago is not today's skill.
- Use the full scale. A screen where everything lands on 3–4 has measured
  nothing; force yourself to identify the candidate's genuinely weakest and
  strongest areas.
- Weighted total = Σ(weight × score) / 5, expressed as a percentage.

## Step 4 — Compensation & budget analysis

Read `references/compensation.md` and work the numbers: current vs. expected
compensation, expected vs. budget ceiling, the increase the candidate is
asking for, basic-vs-total-package traps, currency and rate-type
normalization, and notice-period economics. Classify the result as **Within
budget / Stretch (≤10% over, negotiable) / Breach (>10% over or firm above
ceiling)**. Breach gates the verdict; Stretch conditions it.

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
| **ENDORSE** | All gates pass · weighted score ≥ 75% · every must-have scored ≥ 3 on real evidence · comp Within budget · no unresolved critical flags |
| **ENDORSE WITH CONDITIONS** | All gates pass · weighted score ≥ 60% · comp at worst Stretch · remaining concerns are specific, probeable, and plausibly resolvable — and you list each condition explicitly |
| **DO NOT ENDORSE** | Any gate failed, or weighted score < 60%, or a must-have scored ≤ 1 with no path to resolve, or comp Breach with no flexibility signal, or a critical flag stands |
| **INSUFFICIENT INFORMATION** | A must-have or the budget picture is unknowable from the materials and the verdict would flip depending on the answer — list exactly what to collect, then re-screen |

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
comp fit as the tiebreaker. It is a legitimate outcome for a batch to produce
zero endorsements — say so plainly rather than endorsing the least-bad option.

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
