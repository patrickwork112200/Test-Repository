# Scoring Rubric

Score every criterion in the requirement matrix on the 0–5 scale below. The
anchors exist so that two screens of the same candidate land on the same
numbers — if you find yourself scoring on gut feel, re-read the anchor and find
the evidence line that justifies the number.

## The 0–5 scale

| Score | Anchor | Evidence standard |
|---|---|---|
| **5** | Exceeds the requirement with depth to spare — has done this at larger scale, higher complexity, or taught/led others in it | Demonstrated, recent, quantified |
| **4** | Fully meets the requirement — clear hands-on evidence at the required level | Demonstrated, recent |
| **3** | Meets the core of the requirement with minor stretch — evidence is real but thinner, older, or at smaller scale than ideal | Demonstrated or strongly claimed with corroboration |
| **2** | Partial — adjacent or transferable experience; would need ramp-up or supervision | Claimed, or demonstrated in a neighboring skill |
| **1** | Trace evidence only — the skill appears in a list or a one-line mention with nothing behind it | Claimed, uncorroborated |
| **0** | No evidence at all, or evidence of the opposite | — |

**Unknown ≠ 0.** Score 0 only when the materials affirmatively show absence.
When the materials are simply silent, mark the criterion **U (unknown)**,
exclude it from the weighted total, report the total both ways ("72% scored /
64% if unknowns score 2"), and add a probe question. This stops silence from
being punished like failure — but also stops it from being invisibly forgiven:
an unknown on a **must-have** caps the verdict at Endorse with Conditions no
matter the total, and two or more must-have unknowns force Insufficient
Information.

## Scoring by criterion type

**Technical / functional skills.** Look for the skill *in use*: named projects,
what the candidate built/fixed/ran with it, scale indicators (users, data
volume, team size, uptime). A skills-section keyword with no appearance in any
role description is a 1, not a 3. When assessment or test results are among
the materials (coding tests, work samples, certifications with exam scores),
they are the strongest evidence class available — work samples are the best
single predictor of job performance — and they override thinner CV signals in
either direction. Version/stack specifics ("Spring Boot 3,
Kafka, k8s on EKS") are a mild positive signal of real use; long undifferentiated
tool lists are a mild negative one.

**Recency discount.** A required skill last evidenced 3–5 years ago: cap at 3.
More than 5 years ago: cap at 2. Note the discount in the evidence column so
the user sees why. Exception: skills that don't rot (domain knowledge,
regulatory expertise) — use judgment and say when you're not discounting.

**Domain / industry experience.** Weight actual immersion (years inside the
domain, regulated-environment exposure, domain-specific systems) over incidental
contact ("a client in insurance" is not insurance-domain experience).

**Seniority & scope.** Compare scope, not titles — titles inflate and deflate
across companies and countries. Indicators of real scope: team size led,
budget owned, systems owned end-to-end, who they reported to, decisions they
describe making. A "Senior Manager" who describes individual-contributor work
scores as an IC.

**Education & certifications.** Score against what the JD actually requires.
Verify plausibility: certification names and issuers should be real and
current (an expired cert is a probe question). Where the JD says "or
equivalent experience", treat strong experience as fully equivalent — don't
double-penalize a non-degree candidate whose experience already scored.

**Communication & collaboration.** Resumes are weak evidence here; screening
notes, the quality of the CV's own writing (for roles where writing matters),
and portfolio/publication artifacts are better. Score U rather than
fabricating a soft-skill score from nothing — this criterion is the most
common victim of halo effect.

**Stability / logistics.** Tenure pattern (see red-flags reference for what
counts as a flag vs. market-normal), availability, notice period, location
logistics. This criterion scores the *pattern*, not any single event.

## Calibration traps

- **Central tendency** — everything 3–4. If your six criteria span less than
  two points, you haven't found the candidate's real strengths and weaknesses;
  go back to the evidence.
- **Halo / horns** — one vivid strength (brand-name employer, elite school) or
  weakness bleeding into unrelated criteria. Score each criterion only on its
  own evidence; employer prestige is not itself evidence of skill.
- **Experience-quantity anchoring** — "12 years" is not a score. Two years of
  intense, relevant, recent work regularly outperforms ten years of the same
  year repeated ten times. Score the evidence of capability, not the calendar.
- **JD literalism** — the JD asks for "8+ years of Java"; a 7-year candidate
  with a 5-anchor evidence profile is a 4, not a gate failure, unless the user
  flagged the years as a hard client requirement.
- **Same-rubric discipline (batch mode)** — never adjust an anchor because of
  who else is in the pool. The pool changes; the standard doesn't.

## Computing the total

- Weighted total = Σ(weight × score) ÷ 5, as a percentage of the scored
  weight. Exclude U-criteria from both numerator and denominator, and show the
  sensitivity line ("if unknowns score 2 → X%").
- Report the per-criterion table in full (criterion, weight, score, evidence
  with demonstrated/claimed/inferred tag). The table *is* the audit trail.
- Round to whole percentages. False precision ("73.4%") implies a measurement
  quality this instrument doesn't have.
