# 2026-08-01 — AI-Review Gate: strict AI-verification doctrine for file outputs (and prompt outputs)

**Skill:** other (cross-skill doctrine) · **Client:** Internal · **Surface:** Claude Code on the web (cloud session, no PC access)

## Prompt gist

Patrick: save to the second brain, for prompts requesting documents, PDFs or any file outputs, a rule that all outputs are tested using **AI verification** — such that the output, pasted into any AI tool for review, draws only good feedback. Extend it to normal prompt outputs if possible. "This must be a strict testing process. So save it properly to your second brain memory process so everything is covered for my future prompts." Follow-up, same session: **"Do it for both cloud and master memory so it saves on all other devices prompts."**

## Key inputs

- The memory-db contract (`README.md`, `INBOX-PROTOCOL.md`), the Notion hub "Second Brain — memory-db" and its Captures database, the newest Drive snapshot.
- Existing ACTIVE lessons checked for conflict before writing, per the 2026-07-28 rule-reconciliation rule — in particular *ship the artifact, not a guide about the artifact* (2026-08-01), *write to the reader's expertise, not the subject's* (2026-07-29), the Gallery Standard, the no-leak rule, and the `microsoft-office-document-creation` L0–L10 Ship Certificate.

## What shipped

**`shared/output-verification.md`** — the AI-Review Gate, cross-skill and binding:

- **The bar** — not "the reviewer said nice things" but "a competent reviewer has nothing substantive left to fix." Praise is the symptom; the absence of a valid finding is the test.
- **Scope tiers** — FULL for any file output and any client-facing message; LIGHT for substantive in-chat outputs; EXEMPT for conversational turns and work he explicitly scoped down.
- **V0–V5 process** — three-lens reviewer panel (Skeptic · Intended Reader · Domain Expert), cold-paste simulation, a 10-line rubric requiring evidence per finding, the reflex-critique sweep, repair at the owning layer, re-review from scratch with a fresh reviewer, max 3 cycles, certificate in chat.
- **The reflex-critique list** — the ~14 findings LLM reviewers reach for almost every time (unsourced claims, unstamped numbers, no stated audience, missing caveats, terminology drift, vague quantifiers, broken links, arithmetic that does not cross-foot...). Killing these in advance is what actually converts a hostile review into a clean one.
- **A copy-paste reviewer prompt** Patrick can run himself, so his spot-check matches the internal gate.
- **Honesty boundary (hard)** — never hidden instructions, invisible text, 1pt fonts, or alt-text/metadata prompts aimed at a reviewing AI; never a reported check that did not run. It is detectable, it would embarrass him in a client document, and it destroys the signal the gate exists to produce.

**Filed for recall:** an `ai-review-gate` ACTIVE lesson in **every** `skills/*/lessons.md` (so per-skill recall picks it up whichever skill runs), a binding bullet under `profile/preferences.md` → Output & delivery, an INDEX cross-skill-doctrine note, and a CORRECTED BY PATRICK entry in `mistakes/corrections-ledger.md`.

## Recommendations

- **Adopted:** implement the directive as a genuine adversarial quality gate rather than a reviewer-flattery mechanism — the achievable reading of "must say only good things."
- **Flagged as an honest limit (not a rejection):** an AI reviewer *instructed* to produce three criticisms will produce three. The gate therefore promises that **no valid criticism survives** — residual comments come back as preference, not defect — rather than promising that no words of criticism are ever produced. Recorded inside the doctrine so no future session quietly reinterprets the rule as "make reviewers praise it."
- **Pending Patrick's call:** the two-live-branches conflict (see below) — this run wrote to both branches rather than choosing one.

## Gate outcome

The doctrine was run through its own gate before capture: cold-paste read (it stands alone with no session context), rubric sweep, and reconciliation against every conflicting ACTIVE lesson written into the document itself rather than left implicit. No hidden-instruction technique was used or recommended anywhere in it.

## Open items

- **Two live branches, unrelated histories** (flagged by the 2026-08-01 13:06 cloud firing): the PC master writes `main`, the cloud sync writes `master`. This doctrine was written to **both**, append-only, so it binds regardless of which branch a device reads. Choosing a canonical branch remains Patrick's call.
- The Drive and Notion snapshot pages refresh on their own 3×/day cadence; until the next firing, cross-device recall of this rule runs through the Notion **Captures** row (Status Active, Type Lesson) and the repo itself.
