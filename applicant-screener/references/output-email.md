# Default Deliverable: Decision Summary + Action Email

The full report in `references/report-template.md` is the *internal working
artifact* — build it, keep it ready to defend any line, but do not hand it
over unprompted. What the user actually sends and acts on is two things:

1. a **decision summary** they can absorb in fifteen seconds, and
2. an **action email** in their own voice they can send with light edits.

Produce the full scorecard only when asked ("show the scorecard / full
report") or when the user is clearly reviewing the methodology itself.

## The decision summary

Five to eight lines, prose and bold — no tables, no percentages-first. In
order:

- **The verdict, in plain words**, with its practical meaning attached:
  "Endorse — send today", "Cannot endorse yet — fixable, four things to
  close", "Do not endorse — wrong role; fits X", "Can't call it yet — two
  answers needed".
- **Why, in 2–3 sentences**: the decisive evidence for and the decisive
  gap against — the two facts the user would quote to their delivery
  manager. Name panel-feedback provenance when it drove the call.
- **Money, one line**: comp fit in words plus the required bill at target
  ("asking 130 vs 120 ceiling — closable; we'd need to bill ~₱X/hr at
  target margin").
- **Confidence, one line, in words**: what would flip this verdict and how
  close it is ("even scoring him generously he lands under the bar" / "one
  good answer on Snowflake flips this").
- Close with: *"Full scorecard behind this if you want it."*

The numbers still exist — every sentence above must be backed by the
internal scorecard, and must survive being challenged. Summarizing is
compression, never substitution: if a claim can't be traced to the
scorecard, it doesn't go in the summary.

## The action email

Write it ready-to-send in the user's voice, chosen by verdict tier:

| Verdict / situation | Email | To |
|---|---|---|
| Endorse | Endorsement note — who, role, the 2–3 selling points, comp/availability line, next step | Delivery / account team |
| Close, but the evidence isn't *shown* | **CV-rework request** (pattern A below) | Sourcing / delivery team |
| Gaps on *core requirements* — fit itself in doubt | **Requirement-checklist, confirm-or-replace** (pattern B below) | Sourcing / delivery team |
| Do Not Endorse (final) | Short pass note + redirect: the role profile the candidate does fit | Whoever owns the pipeline |
| Insufficient Information | The exact questions, phrased to forward to whoever can answer | Recruiter / candidate |

Choosing between A and B: pattern A when the screen suggests the experience
probably exists but isn't evidenced (summary claims with no role backing,
panel feedback saying "show it"); pattern B when the CV affirmatively shows
*different* experience than the requirement (React Native when the req is
React web; MySQL/Mongo when the req is Postgres/Vector DB). A asks the team
to surface what's there; B asks them to confirm it exists at all — or
replace the candidate.

### Voice and persona

Learned from the user's own sends — keep it, don't flatten it into
AI-speak:

- "Hi Team," opening; "Warm regards," close. First person singular.
- Plain declarative sentences. States the finding, then the why, briefly,
  with client context ("UL runs Snowflake, and it is part of why Benjie
  did not move forward").
- Quotes the CV precisely when making a charge ("the only 'Snowflake' on
  the CV is the schema type").
- Direct but never harsh; the team is being enlisted, not blamed ("I need
  your assistance here team").
- Ends with the personal ask and the real stakes, one or two sentences.
- No corporate filler, no hedging, no exclamation marks, no bullet soup.

### Pattern B — the requirement-checklist email (confirm-or-replace)

For core-requirement gaps. The email is the must-have matrix rendered in
plain words — every line traces to the internal scorecard:

1. **Opening = thanks + verdict**, two lines: "Thanks for sending
   [Candidate]'s profile. On review I won't be able to endorse him for
   this requirement yet — the gaps are on the core requirements."
2. **THE ROLE** — the requirement distilled to one or two lines, close to
   the req's own wording. (ALL-CAPS section headers are part of the voice
   here — they make the email scannable on a phone.)
3. **HOW THE CV CHECKS OUT** — one line per core requirement:
   **Yes / Partial / No**, with the evidence in the same breath ("React
   UI — Partial. His work is React Native; all three projects on the CV
   are mobile apps"). A "No" means checked-and-absent, not unchecked —
   the exhaustive-enumeration rule from the scoring rubric is what lets
   you say it flatly.
4. **IF HE HAS MORE THAN THE CV SHOWS** — the verify-vs-add guardrail as
   an ask: for each gap, an updated CV naming the project, what he built,
   and roughly when. Never "add these keywords."
5. **Additional requests** — the screen's flags as neutral asks:
   unexplained recent gaps ("please clarify why there's nothing shown
   from [month] to present"), summary-vs-role contradictions ("the
   summary says he built backends with Node; the role bullet says he
   collaborated with backend developers — please align it to whichever
   is more accurate"). Neutral phrasing; the team resolves it, nobody
   gets accused.
6. **Close = the fork**, so the pipeline moves either way: "If he fits,
   re-endorse with the updated CV. If not, I need [the replacement
   profile as a one-line JD: stack + seniority + differentiator]" —
   e.g. "a Python/Flask + React web full-stack engineer, preferably with
   AI application experience." The sourcing spec comes straight from the
   requirement matrix's unmet must-haves.

### Pattern A — the CV-rework email

1. **Subject line** that carries the verdict and the stakes: who, what's
   needed, why now.
2. **Opening paragraph = the verdict**: reviewed X's CV against the JD and
   [prior-candidate panel feedback]; cannot endorse yet; the CV as it
   stands fails on [the same points that sank the prior candidate / the
   named gaps]; fixable if the experience is real.
3. **The guardrail, before the items** — verbatim in spirit: *verify each
   item with the candidate first. If they did it, evidence it in the role
   where they did it — project, what they personally built, when. If they
   didn't, say so and we position them differently. We do not add keywords
   the candidate can't defend in panel; that fails harder than a thin CV.*
4. **Provenance headers**, panel feedback first: "Items 1–N come straight
   from [client]'s panel feedback; the rest are our own bar from the JD."
   Presentation items (template, proofread) last.
5. **Numbered items**, each in three beats: what the CV shows now (quoted)
   → why it matters (whose requirement) → exactly what to change and
   where ("under the role where he used it, with the project and what he
   personally did"). One item, one fix.
6. **Closing**: the stakes in one sentence ("this has to be right the
   first time — there is no second submission on this one"), the ask, and
   a concrete offer that removes friction (e.g. "put me on a 30-minute
   call with the candidate; items 1–5 we can pull out of him directly").

### Condensed exemplar — pattern A (genericized)

> **Subject: [Candidate] — CV rework needed before [Client] endorsement
> (same gaps that cost us [prior candidate])**
>
> Hi Team,
>
> I reviewed [Candidate]'s CV against the [Client] JD and the panel
> feedback from [prior candidate]'s rejection. My call: we cannot endorse
> yet — as the CV stands the panel would reject him on the exact points
> that took [prior candidate] out, and this client will not give the same
> profile a second look. All of it is fixable, if the experience is real.
>
> One rule before the items: verify each point with [Candidate] first. If
> he did it, we show it in the role where he did it — project, what he
> personally built, when. If he didn't, tell me and we position him
> differently. We do not add keywords he can't defend in panel.
>
> Items 1–2 are straight from [Client]'s panel feedback; 3–4 are our own
> bar from the JD; 5–6 are presentation.
>
> 1. **[Tool] — the platform, not the [near-miss the CV actually
>    shows].** [What the CV says now.] [Client] runs [Tool] and it is one
>    of the reasons [prior candidate] was rejected. If the experience is
>    real: which role, which project, what he built, when.
> 2. …
>
> I know this is a lot, but this endorsement has to be right the first
> time. If it helps, put me on a 30-minute call with [Candidate] — the
> first few items we can pull out of him directly.
>
> Warm regards,

Numbers, client names, and candidate names come from the live screen; the
pattern and voice come from here.
