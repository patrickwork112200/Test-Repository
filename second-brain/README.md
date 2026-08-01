# AI-Review Gate — and the second-brain repairs shipped alongside it

Portable copy of the doctrine captured to Patrick's second brain on **2026-08-01**, plus a record
of the infrastructure faults fixed in the same session. The canonical home is the private
`claude-memory-db` repo; this folder exists so the spec is readable without cloning it.

## Files here

| File | What it is |
|---|---|
| `output-verification.md` | The doctrine — the copy written to `shared/output-verification.md` in memory-db |
| `20260801-ai-review-gate-run-record.md` | The run record — what shipped, recommendations, open items |

## The rule in one paragraph

Before any file output or client-facing message is called done, it is reviewed **the way a stranger
would review it** — pasted cold into another AI with no conversation context, nobody present to
explain it — and it ships only when **no substantive criticism survives**. Three-lens reviewer panel,
cold-paste simulation, a 10-line rubric where every finding needs a locator, the reflex-critique
sweep, repair at the layer that owns the fault, re-review from scratch, max 3 cycles, certificate in
chat. Substantive in-chat outputs get a LIGHT version. It earns clean reviews by making the artifact
genuinely good — **never** by hidden instructions, invisible text, or metadata aimed at a reviewing
AI. The promise is that no *valid* criticism survives, not that no critical words are ever produced.

## Where the doctrine lives

| Target | Reference | Reached by |
|---|---|---|
| memory-db `main` + `master` | commit `8c8ccd1` (both refs) | PC master (`sync.ps1`) and the cloud Routine |
| Notion Captures | page `3afe53e3-ddd0-812c-925e-c8184890488d` | Any Notion-connected surface — binding immediately |
| Notion snapshot page | status block prepended | Full regeneration at the next Routine firing |
| Google Drive | `memory-db-snapshot.md` id `1r7lRF4C7jvWgOgjYj6nV3c3Way7h4ip5` | Drive-only surfaces |
| Drive inbox | `capture-20260801-1330-other-ai-review-gate.md` | The INBOX PROTOCOL write path |
| This repo | branch `claude/second-brain-file-outputs-y6xma5` | Human-readable copy |

The rule fires on future prompts because an `ai-review-gate` ACTIVE lesson is filed in **every**
`skills/*/lessons.md` — each skill's recall step reads its own lessons file — and the rule is also in
`profile/preferences.md`, `INDEX.md`, and the corrections ledger.

## Faults found and fixed in the same session

**1. Two live branches with unrelated histories.** `main` (PC master) and `master` (cloud sync) were
both being written 3×/day and neither was a superset of the other — `main` held the harvest layers
and the newer `README`/bootstrap/`sync.ps1`, `master` held every capture fold from 2026-07-29 on and
the much larger `client-facts.md` and `voice-corrections.md`. Merged with
`--allow-unrelated-histories` into one commit that is a superset of both (143 files = the exact union,
zero lost); both refs now point at it and share ancestry, so any future fork is an ordinary mergeable
one. `tools/sync.ps1` and the cloud spec now both push **both** refs — the PC side with a
fast-forward-only mirror push that can never discard work — so they cannot silently fork again.

**2. `make-snapshot.ps1` was silently dropping two skills.** Its skills loop iterated a **hardcoded
seven-skill list**, so `legal-philippines` and `other` never appeared in any snapshot — a lessons file
in either was invisible to every cloud recall surface. Its unguarded `Get-Content` would also throw on
a skill folder without a `lessons.md`. Now enumerates `skills/` from disk with `Test-Path` guards and
inlines `shared/output-verification.md`. Snapshot went 42 → 47 sections.

**3. The Drive snapshot had been structurally broken since 2026-07-30.** The Drive connector must
carry a whole file in one call and truncates near 64 KB; the full snapshot is ~286 KB. The newest
Drive copy this morning was built from the old `main` and carried only **25 of 47** sections — missing
every 2026-07-29 to 07-31 screening run. Drive now receives a **curated binding-layer core** (~49 KB):
preferences and the AI-Review Gate in full, plus every skill's ACTIVE lessons condensed to their
standing rules, with an honest scope paragraph naming what is not in it and where it is. Notion keeps
the full copy via chunked writes.

**4. Two unsynced Notion captures folded.** The Practical Research 2 run record (with its seven
verified-sources build rules) and the `ship-the-artifact-not-a-guide` CORRECTION, now an ACTIVE lesson.
Zero captures remain unsynced.

## Left for Patrick — two things I could not do

- **The Routine's stored prompt could not be edited.** `update_trigger` refuses prompt edits for a
  routine bound to another session, and the "Second-Brain Sync" Routine is bound to
  `session_01QvrAY2UJ5eU2MpMVzyy5WD`. Its inline summary still says pull/push `master` only and upload
  a full snapshot to Drive. Because the prompt tells each firing to follow `tools/cloud-sync-routine.md`
  exactly, the correction was written into that spec behind a loud **READ THIS FIRST** banner at the
  top. To fix the prompt itself, edit it in the claude.ai UI or re-create the Routine from a session
  holding the Notion and Drive connectors.
- **A truncated Drive file cannot be deleted.** `memory-db-snapshot.md` id
  `1PVL25NazWZTmwTsnzZkFONKp64rma3Ry` (67,770 bytes, cut off mid-file on 2026-07-30) is still in the
  folder — the connector has no delete capability. It is older than the current copy so newest-wins
  already ignores it; deleting it by hand just removes the confusion.
