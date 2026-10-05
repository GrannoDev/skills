---
name: evidence-based-verification
description: Verify features and bugfixes with readable before-and-after evidence saved in an evidence folder. Use when implementing changes or verifying completed work.
---

# Evidence-based verification

Prove the requested behavior with the smallest reproducible scenario. For fixes, capture the failure before editing and repeat the same check afterward. Keep inputs and state comparable. If a baseline is unavailable, explain why; never invent it.

## Save evidence

Use `<project-root>/evidence/<local-date>-<task>/`, unless the user specifies another destination. Save `report.md` and the needed `videos/`, `screenshots/`, and `logs/` subfolders. Name artifacts by scenario and phase, such as `S01-before.mp4` and `S01-after.mp4`. Copy recordings out of temporary recorder storage before cleanup; avoid overwriting another run.

## Capture and check

- UI: Record the actual workflow before and after. Prefer native 1080p+, 30 fps for interactions, and 60 fps for motion. Match viewport and framing; preserve the device being tested. Never upscale or duplicate frames to imply better quality.
- Inspect a saved sample before the full recording. Important text and results must be readable. Fix poor capture settings or use readable screenshots and disclose the video limitation. Screenshots cannot prove timing or motion.
- When FFmpeg tools are available, run [scripts/check_video.py](scripts/check_video.py) on each final video and save its JSON in `logs/`. Use `--help` for thresholds. A technical pass still requires visual inspection; inspect playback for motion claims.
- Non-UI: Save exact commands or steps, inputs, outputs, exit codes, and relevant resulting state. Exercise the changed behavior; a build or unrelated passing suite is insufficient.

## Report and retain

Use [references/report-template.md](references/report-template.md). Link full-quality artifacts with observations and useful timestamps. In chat, give a short Changed / Why / How summary and link the report. State missing evidence and unverified claims. Keep secrets out of evidence; upload or commit artifacts only when authorized.

Retain temporary evidence until the user explicitly confirms review in response to a cleanup request. Ask for that confirmation when delivering it. Then remove only this task's temporary evidence. Keep PR-attached evidence and the files supporting its links.
