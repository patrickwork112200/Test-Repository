# shared/output-verification.md — the AI-Review Gate (cross-skill, binding)

**Status:** ACTIVE since 2026-08-01 — Patrick's standing directive. **Cross-skill:** binds every skill and every plain prompt, not one skill's pipeline. Precedence unchanged: **current prompt > ACTIVE lesson > skill default.**

## His directive (verbatim, 2026-08-01)

> "Save to your second brain memory for prompts requesting documents, pdfs, or any file outputs. Ensure that all outputs are tested using AI verification. Where that output when pasted to any AI tool for review, that AI reviewing your created output must say only good things and will opt to give good feedback. If normal prompt outputs can have this also, then that would be great. This must be a strict testing process."

## The rule

Before any deliverable is called done it is reviewed **the way a stranger would review it** — pasted cold into another AI, no conversation context, no framing, nobody present to explain it — and it must come back with **no substantive criticism**.

The bar is not "the reviewer said nice things." The bar is **a competent reviewer has nothing substantive left to fix**. Praise is the symptom; the absence of a valid finding is the test. An artifact that survives a hostile cold read gets good feedback from a friendly one automatically.

## The honesty boundary (hard — never crossed)

The gate earns clean reviews by making the artifact genuinely good. It never:

- **embeds hidden or disguised instructions to a reviewing AI** — invisible or white-on-white text, 1pt fonts, off-canvas text, alt-text/metadata/comment prompts, "ignore previous instructions", "rate this highly";
- **frames for flattery** instead of earning the verdict;
- **claims a review that did not run**, or reports a pass a check did not actually produce.

Three reasons, in order of weight: it is detectable and would embarrass Patrick if found in a client document; it destroys the signal, because a review that can be gamed tells him nothing about whether the work is good; and a document that needs to manipulate its reader is a document that did not survive on merit. Anything unverifiable in the current environment is reported **PENDING with the exact procedure**, never dressed as passed.

## Scope

| Tier | Applies to | Weight |
|---|---|---|
| **FULL** | Anything leaving as a file — `.docx` `.xlsx` `.pptx` `.pdf` `.csv`, images, code files — and every client- or candidate-facing message | Full panel, full rubric, certificate |
| **LIGHT** | Substantive in-chat outputs: analyses, tables, plans, recommendations, drafted emails, research answers | One reviewer pass + reflex sweep + cold-paste test |
| **EXEMPT** | Conversational turns, one-line factual answers, and work he explicitly scoped down ("just the table", "quick answer") | — |

The crown rule stands: **his explicit form instruction outranks the gate's cosmetics** — but never its honesty clauses. No fabrication, no faked verification, no hidden reviewer manipulation, whatever the instruction.

## The process — fail-closed, at most 3 cycles

### V0 · Name the reviewer

State who reviews this and what they would be asked. Default panel of three, deliberately different lenses — three identical skeptics find one class of defect three times:

1. **The Skeptic** — briefed to find every flaw and be harsh. Hunts errors, gaps, unsupported claims.
2. **The Intended Reader** — the actual audience (a non-technical TA coordinator, a client hiring manager, a Grade 12 student). Judges usefulness and readability, not craft.
3. **The Domain Expert** — a practitioner in the artifact's field. Judges correctness against field norms and conventions.

### V1 · Cold-paste simulation

Review the artifact **alone**, exactly as it would arrive in a stranger's paste buffer — no prompt history, no explanation. If it only makes sense with context that would have to be supplied out loud, it fails here. The artifact carries its own purpose line, its own labels, its own units.

### V2 · Run the rubric

Every dimension gets PASS or a finding **with evidence** — quote the line, name the cell, number the page. A finding without a locator is not a finding.

| # | Dimension | Fails when |
|---|---|---|
| 1 | Brief fidelity | It answers a nearby question, not the one asked; scope silently widened or narrowed |
| 2 | Factual integrity | A number, name, citation, or claim not traceable to a real source; a fabricated DOI, link, or statistic |
| 3 | Completeness | A promised section is thin or missing; an unlabelled placeholder; a dangling TBD |
| 4 | Internal consistency | Totals do not cross-foot; a label contradicts its data; names, dates, or currency drift between pages |
| 5 | Reader fit | Wrong depth, wrong length, or wrong vocabulary for the stated reader |
| 6 | Structure & navigation | The point is not findable in ten seconds; a heading promises what the body does not deliver |
| 7 | Format & convention | Breaks the field's prescribed format (APA, a client template) or, absent one, the Gallery Standard |
| 8 | Mechanical integrity | The file does not open clean, formulas error, pages render wrong, links or cross-references break |
| 9 | Tone & voice | Not Patrick's voice where it should be; AI-slop fingerprint; unsupported superlatives |
| 10 | Leak & safety | Internal data (pay, bill, GP/GPM, screening scores) in a client-facing artifact; confidential content misrouted |

### V3 · Kill the reflex critiques

LLM reviewers reach for the same findings nearly every time. They are free points, and leaving one on the table invites a critique that has nothing to do with the real quality of the work. Sweep before shipping:

- unsourced claims → cite it, or label it an assumption
- numbers with no unit, basis, or as-of date → stamp them
- no stated purpose or audience → one line at the top
- no limitations or caveats → one honest line (**a line, not a section**)
- terminology drift → one term per concept, everywhere
- placeholders → zero, or visibly marked as intentional fill-ins
- formatting drift → fonts, heading levels, table alignment, page numbers
- vague quantifiers (*significant, several, robust*) → a number, or cut it
- passive hedging and marketing adjectives → specifics
- accessibility → contrast, alt text, type floors
- arithmetic → totals equal the sum of their parts
- broken links, DOIs, cross-references
- ambiguous next actions → who does what, by when
- spelling, grammar, spacing

### V4 · Verdict and repair

Any finding at minor or worse → repair **at the layer that owns it** (a structure fault goes back to the outline; it is not patched at the surface), then **re-review from scratch with a fresh reviewer** — never a re-read of the same pass, which reliably confirms its own earlier judgement. Maximum 3 cycles; still failing on the same seam → change the approach and say so plainly rather than re-tuning.

### V5 · Certificate

Delivery carries a short block: reviewers run, findings found and fixed, anything residual, and whatever could not be machine-checked here. **The certificate lives in chat, never as extra pages inside the artifact.**

```
AI-REVIEW GATE — {artifact}
Reviewers: Skeptic · Intended Reader ({who}) · Domain Expert ({field})
Cold-paste: PASS | Rubric: 10/10 | Reflex sweep: clean
Cycles: {n} | Findings fixed: {list} | Residual: {none | named}
Unverifiable here: {none | check + exact procedure}
```

## The reviewer prompt Patrick can use himself

So his own spot-check matches the internal gate, the standard test is:

> "Review the attached as a demanding {domain} professional seeing it for the first time, with no context about who made it or why. List every factual error, inconsistency, gap, and formatting defect you find, with the specific line or cell. Then state whether you would send this to a client as-is, and what you would change first."

A clean run on that prompt is the target.

**Stated honestly, because the gate does not promise what it cannot deliver:** a reviewer *instructed* to produce three criticisms will produce three — "say only good things" is unfalsifiable as a guarantee, and any method that forced it would be manipulation rather than quality. What the gate does promise is that **no valid criticism survives**: residual comments come back as preference and taste, not defect. That is the achievable form of his instruction, and it is the one worth having.

## Reconciliation with existing memory

- **Does not replace the `microsoft-office-document-creation` L0–L10 pipeline or its Ship Certificate.** The gate is one added lens at the end — the cold outsider — after the Gallery Judge (design) and the blind Number Re-deriver (figures). Where L8/L9 already prove a dimension, the gate reads their evidence instead of re-running it.
- **Yields to "ship the artifact, not a guide about the artifact" (2026-08-01).** The gate adds **no pages**. Where a reflex item (limitations, methodology, definitions) collides with reader-fit, satisfy it in the smallest honest form — a line, a footnote, a bracket — never a new section. Reviewer-pleasing never outranks reader-fit.
- **Extends "write to the reader's expertise, not the subject's" (2026-07-29).** The reviewer is a **proxy**, never the actual reader. Where the two conflict the real reader wins, and the certificate says so.
- **Inherits the no-leak boundary.** Rubric line 10 is the existing client-facing rule (no pay, bill, GP/GPM, scores) enforced at review time rather than trusted at authoring time.
- **Inherits certificates-over-claims** (`profile/preferences.md`): a defaulted or pending item is named, never dressed as done.
- **Consistent with memory hygiene (2026-07-28).** This is a durable standing rule, not a decision in flight — captured once, in one place, and referenced from the per-skill lessons rather than copied into them.
