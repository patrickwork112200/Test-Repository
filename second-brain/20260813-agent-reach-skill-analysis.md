# 2026-08-13 — Agent Reach (Panniantong): full analysis and lessons for the second brain

**Skill:** other (cross-skill capability lesson) · **Client:** None · **Surface:** Claude Code on the web (cloud session)
**Source:** [github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — public repo, MIT license, v1.5.0, ~68k stars, cloned and read in full this session (README, CLAUDE.md, SKILL.md / SKILL_en.md, all 7 reference files, docs/install.md, and the source: `base.py`, `doctor.py`, `probe.py`, `core.py`).
**Canonical capture:** Notion Captures row `3bbe53e3-ddd0-813d-b8d3-fc44a9b638ac` (Type: Lesson, Date 2026-08-13). This file is the human-readable copy; folding into memory-db lessons is the sync's job, and binding is Patrick's.

---

## What Agent Reach is

"Give your AI agent eyes to see the entire internet." A Python CLI + library that gives AI agents **read/search access to 15 internet platforms with zero API fees**. Its own positioning, stated in CLAUDE.md and enforced in the code:

> Installer + doctor + config tool. **NOT a wrapper** — after install, agents call upstream tools directly.

It is a **capability layer**: it does *selection, installation, health-checking, and routing*. The actual reading is done by best-in-class upstream open-source tools the agent calls directly. Distribution is a single pasted sentence — the install doc at `docs/install.md` is written **for the AI agent to execute**, with the human only pasting one line and supplying credentials when asked.

### Platform coverage

| Tier | Platforms | How |
|---|---|---|
| **Zero-config (6+)** | Web pages (Jina Reader `r.jina.ai`), YouTube (yt-dlp), GitHub (gh CLI), RSS (feedparser), Exa semantic web search (via mcporter MCP, free, no key), V2EX (public API), Bilibili basic (bili-cli) | Work immediately after install |
| **Login-backed** | Twitter/X (twitter-cli ▸ OpenCLI), Reddit (OpenCLI ▸ rdt-cli — *no* zero-config path, anonymous endpoints blocked), XiaoHongShu (OpenCLI ▸ xiaohongshu-mcp ▸ xhs-cli), Facebook + Instagram (OpenCLI browser session), Xueqiu stocks, LinkedIn (mcp-server-linkedin ▸ Jina Reader) | Cookies via manual Cookie-Editor export, or an existing Chrome session the user already controls |
| **Transcription** | Xiaoyuzhou podcasts, no-subtitle YouTube/Bilibili audio | Whisper via free Groq key (`agent-reach transcribe`) |

---

## The ten design lessons worth keeping

1. **Ordered multi-backend routing.** Every platform = an ordered candidate list (preferred + fallbacks) in one file per channel. Swapping a dead provider = reordering a list, not rewriting code. Real case: Bilibili risk-control blocked yt-dlp outright (HTTP 412, 2026-06) → routed to bili-cli; users felt nothing. Users can force a backend via config/env override, and an unknown override is *ignored* so a stale override can never hide working backends.

2. **The doctor pattern.** `agent-reach doctor --json` reports per-channel status plus the load-bearing field `active_backend` — which backend is *actually serving* the platform right now. Probes **really execute** a lightweight command; `shutil.which()` is explicitly documented as not proof of health (a stale venv shim passes `which()` but cannot exec). The probe classifies `missing / broken / timeout / error` and prescribes the exact fix (`pipx reinstall X`). One misbehaving channel can never take down the whole report — per-channel exceptions degrade to `status: error`. Doctor also scrubs credentials from any echoed URL before rendering, because it is the final output boundary.

3. **Progressive-disclosure skill files.** A compact SKILL.md (~140 lines) carries standing rules, a routing table, and quick commands; seven per-category reference files (search / social / career / dev / web / video / finance) hold the per-backend command groups, caveats, and retry chains. The agent reads the reference only when it needs that platform.

4. **Trigger-engineered description.** The skill description opens "MUST USE when user wants to research/search/look up/find anything on the internet" plus every platform name and URL shape — and closes with an explicit **NOT-for list** (not for writing reports, not for posting/write operations, defer to a dedicated platform skill if installed). Both halves matter: the trigger half fires the skill; the NOT-for half stops scope creep.

5. **Standing rules for the session.** (a) Health-check before acting on multi-backend/login-backed platforms; (b) *announce* "using agent-reach, platform X via backend Y" before starting; (c) on failure, follow the reference's retry chain — never guess commands; (d) broad research = combine platforms in parallel (Exa web search + Twitter/Reddit discussions + XiaoHongShu/Bilibili for Chinese perspectives), then synthesize; (e) version-watch for the user after substantial tasks, but never interrupt the current task to update and never nag twice about the same version.

6. **Success = non-empty verified content, never exit code 0.** Written into multiple references: HTTP 400 from Xueqiu is a session/cookie problem, *not* "the stock doesn't exist"; an empty caption-URL response from Bilibili is a transient, retry up to 3× — *not* "the video has no subtitles"; `whoami` succeeding while `stock` fails is an adapter problem, not a login problem. Misdiagnosis text is pre-written into the docs so the agent can't reach the lazy wrong conclusion.

7. **Explicit ordered retry chains, stop on first success.** YouTube subtitles: yt-dlp → `opencli youtube transcript` (3 retries on empty response) → `agent-reach transcribe` (Whisper). Twitter search: retry once → `pipx upgrade` and retry → OpenCLI fallback → route around via the stable commands (`feed`, `user-posts`). The chain is data in the skill file, not improvisation at run time.

8. **Safe-by-default install with hard boundaries.** The default `agent-reach install` is a **read-only check**; `--system` is required for any host modification; `--dry-run` previews. The install doc gives the executing agent explicit boundaries: no sudo without approval, nothing outside `~/.agent-reach/`, never create files in the agent workspace (config → `~/.agent-reach/` with 600 perms; temp → `/tmp/`). Optional channels are opt-in via a menu the agent shows the user — nothing login-backed installs unnamed.

9. **Hard authentication boundaries.** Never automate logins; never read browser cookies. Cookies arrive only via the user's own manual Cookie-Editor export. OpenCLI may only reuse an existing Chrome session the user already controls. Saved Twitter cookies are used *only* by doctor's config check — live calls require `TWITTER_AUTH_TOKEN`/`TWITTER_CT0` explicitly set in the child process env, without logging values. Transcription will not silently fail over from Groq to OpenAI — `--allow-provider-fallback` must be passed explicitly, because failover changes *who receives the audio*.

10. **Maintenance as the value proposition.** "Access methods go stale" is treated as a law of nature: 2026-03 a batch of single-platform CLIs went unmaintained; 2026-06 Bilibili killed yt-dlp. The project's promise is that the maintainer re-verifies routes on real machines and reorders backends — plus `agent-reach check-update` and a daily `agent-reach watch` cron pattern that notifies only on problems or new versions, staying silent when all is well.

### Security posture (their guidance, worth adopting anywhere)

- Cookie/browser-session platforms carry **ban risk** (platforms detect non-browser API calls) → use a **dedicated secondary account**, never the main one; this also limits blast radius if a cookie leaks.
- Credentials live only in local `~/.agent-reach/config.yaml`, permission 600, never uploaded.
- Don't hammer from VPS/datacenter IPs (especially Twitter followers/following); residential proxy ~$1/mo if server-deployed. Rate-limit XiaoHongShu operations 2–3 s apart or captchas fire.

---

## Applicability to Patrick's setup (assessment, not from the repo)

- **Cloud sessions (Claude Code on the web / Cowork):** the zero-config channels are usable per-session via `pipx install https://github.com/Panniantong/agent-reach/archive/main.zip` — web reading, YouTube subtitles, GitHub, RSS, Exa search, V2EX. Anything needing OpenCLI/Chrome login state (Reddit, XiaoHongShu, Facebook, Instagram, Bilibili subtitles, Twitter fallback) is **desktop-only** — it must run on the PC where the Chrome session lives. Cloud containers also route HTTPS through an agent proxy, which may interfere with some upstream tools.
- **Recruitment relevance:** the LinkedIn channel (mcp-server-linkedin: `search_people`, `search_jobs`, `get_person_profile`, `get_company_profile`) could aid candidate sourcing/verification — but it automates a personal LinkedIn session, which risks account restriction under LinkedIn's ToS. If ever used: dedicated account, Patrick's explicit prior OK, never his main profile.
- **Skill-building reuse:** the design patterns (ordered-backend routing, doctor with real probes, retry chains with non-empty-content success criteria, safe-by-default execution, progressive-disclosure SKILL.md, trigger-engineered descriptions with NOT-for lists) are directly reusable in Patrick's own skills regardless of whether the tool itself is ever installed.

## PROPOSED rules — unconfirmed until Patrick binds them

1. **Internet-reach routing:** when a request needs live internet content beyond built-in web search — social-platform opinions (Twitter/X, Reddit), video content (YouTube/Bilibili), podcast transcripts, LinkedIn profiles/jobs, Chinese-platform perspectives (XiaoHongShu, V2EX, Xueqiu) — consider the Agent Reach pattern: install (read-only check first), `agent-reach doctor --json`, use zero-config channels immediately, ask Patrick before configuring any login-backed channel. Never automate logins; cookies only via his own Cookie-Editor export; dedicated secondary accounts only.
2. **Research method:** for broad research, adopt the multi-platform standing rule even without the tool — semantic web search + platform-native discussion sources in parallel, then synthesize; treat "exit 0 but empty content" as failure; follow an explicit ordered retry chain instead of guessing commands.
3. **Skill authoring:** reuse the design patterns above when building or improving Patrick's skills.

## Verification run — 2026-08-13, this cloud session

The analysis was verified by actually installing and exercising the tool (not just reading it):

- `pip install` from the cloned source succeeded (the GitHub archive-zip route is blocked by the cloud proxy — **in cloud sessions, clone the repo and install from the local path**). `agent-reach --version` → v1.5.0.
- `agent-reach doctor --json` ran clean and reported per-channel status + `active_backend` exactly as documented. In this container: **web (Jina Reader), V2EX, RSS, and Bilibili search API came up OK with zero config**; YouTube/GitHub/Xueqiu showed `warn` (missing system deps — gh CLI, JS runtime — which the safe-by-default install correctly refuses to add without `--system`); Exa showed `off` (mcporter not installed); all login-backed channels `off`, as expected with no Chrome session.
- Real-content checks per the skill's own success criterion (non-empty content, not exit code): Jina Reader returned clean markdown for a live page; the V2EX hot-topics API returned 10 real topics.

Conclusion: the cloud-session claim in this document is **confirmed** — zero-config reading works per-session; login-backed channels remain desktop-only.

## Decisions — made 2026-08-13 under Patrick's explicit delegation ("Decide for me end-to-end")

1. **Adopted as working practice:** the internet-reach routing rule (PROPOSED #1 above) and the research-method rule (PROPOSED #2) are adopted as the working default going forward. Formal binding still happens through the normal sync/PC-master path; this records the decision and its provenance (Patrick's delegation, user turn, 2026-08-13).
2. **LinkedIn channel: NO.** Not enabled, not to be enabled by default. It automates a personal LinkedIn session, and Patrick's LinkedIn account is a core professional asset in his recruitment work — account-restriction risk outweighs sourcing convenience. Revisit only if Patrick explicitly asks, and then only with a dedicated account.
3. **PC install: optional, left to Patrick.** Not executable from a cloud session. When he wants the login-backed channels (Twitter, Reddit, XHS, Facebook, Instagram), the one-liner to paste to any agent on his PC is: `帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md` — safe-by-default; approve `--system` only when asked.
4. **Cloud sessions:** install per-session from a local clone when a task needs it (verified working this session).

## Open items

- Unabyss mirror of this lesson: attempted repeatedly during the known Unabyss outage window (trial/quota issue captured 2026-08-12); the Notion capture rows are the canonical record until Unabyss recovers.
