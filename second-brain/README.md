# AI-Review Gate — where it is saved

Portable copy of the doctrine captured to Patrick's second brain on **2026-08-01**. The
canonical home is the `claude-memory-db` repo; this folder exists so the spec is readable
without cloning that private repo.

## Files here

| File | What it is |
|---|---|
| `output-verification.md` | The doctrine itself — the copy written to `shared/output-verification.md` in memory-db |
| `20260801-ai-review-gate-run-record.md` | The run record — what shipped, recommendations, open items |

## Where it actually lives (all five write targets)

| Target | Path / ID | Reached by |
|---|---|---|
| memory-db `main` | commit `f509a7a` | The **PC master** — `sync.ps1` pulls this branch |
| memory-db `master` | commit `9b796df` | The **cloud "Second-Brain Sync" Routine**, 3×/day |
| Notion Captures | page `3afe53e3-ddd0-812c-925e-c8184890488d` | Any Claude surface with the Notion connector — read immediately as a binding rule |
| Google Drive inbox | file `1v_q1J0L05YZBTrpNHlPhT1z5GqtY6XY2` | The INBOX PROTOCOL write-path from non-master devices |
| This repo | branch `claude/second-brain-file-outputs-y6xma5` | Human-readable copy |

Both memory-db branches were written because the remote carries **two live branches with
unrelated histories** (flagged by the 2026-08-01 13:06 cloud sync): the PC master writes
`main`, the cloud Routine writes `master`, and neither descends from the other. Writing to
one only would have left half the devices unaware of the rule. Choosing a canonical branch
is still Patrick's call.

## What was written into memory-db

- `shared/output-verification.md` — the full gate spec.
- An `ai-review-gate` **ACTIVE lesson in every `skills/*/lessons.md`** — this is the part that
  makes it fire on future prompts, since each skill's recall step reads its own `lessons.md`.
- `profile/preferences.md` → Output & delivery — the binding one-paragraph form.
- `INDEX.md` — cross-skill doctrine note plus the per-skill lesson counts.
- `mistakes/corrections-ledger.md` — a CORRECTED BY PATRICK entry.
- `ledger/runs.jsonl` + `skills/other/runs/20260801-ai-review-gate-doctrine.md` — the run record.
- `ledger/ingested.md` — the Drive twin's ID, so the sync never folds it a second time.

## The one thing to know about the rule

It earns clean reviews by making the artifact genuinely good — never by hidden instructions,
invisible text, or metadata aimed at a reviewing AI. The promise is that **no valid criticism
survives**, not that no words of criticism are ever produced: a reviewer instructed to find
three faults will find three, and any method that forced praise would be manipulation rather
than quality.
