# AI General III Pancake – WH3 maintenance fork kickoff

This repository now contains a **starter tactical controller** to begin replacing static behavior with strategic target scoring while preserving AI General III architecture.

## Added files

- `script/pancake_lib/aigeneral_tactical_controller.lua`
  - battle-state evaluation (`friendly/enemy ratio`)
  - dynamic mode switching (`defensive`, `balanced`, `aggressive`)
  - per-unit target scoring favoring artillery and missile threats
  - safe unitcontroller attack issue wrapper

- `script/battle/mod/aigeneral_iii_main.patch_notes.lua`
  - concrete integration steps for wiring the module into `aigeneral_iii_main.lua`

## Next steps in your extracted pack project

1. Add `"aigeneral_tactical_controller"` to `require_pancake_libs(...)` in `aigeneral_iii_main.lua`.
2. Build a repeat callback during live battle phases that calls tactical tick every ~1.2s.
3. Gate tactical overrides behind MCT settings and current AI General exclusion logic.
4. Extend `score_target_for_unit` with lord/hero focus, anti-large matching, and local distance threat.
5. Add reserve policy (10–20%) and anti-overchase leash distance.
