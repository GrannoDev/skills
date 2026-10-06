---
name: evidence-based-verification
description: Verify features and bugfixes with focused behavioral checks and before-and-after videos or images when useful. Save only visual evidence and summarize results in chat. Use when implementing changes or verifying completed work.
---

# Evidence-based verification

Prove the requested behavior with the smallest reproducible scenario. For fixes, capture the failure before editing and repeat the same check afterward. Keep inputs and state comparable. If a baseline is unavailable, explain why; never invent it.

Scale verification to the change. Stop when the focused check proves the behavior and required project checks pass. Do not add unrelated scenarios, tools, or tests just to produce more evidence.

## Save only videos and images

Use `<project-root>/evidence/<local-date>-<task>/`, unless the project or user specifies another destination. Create the folder only when there is visual evidence to save. Store media directly in it, with descriptive names such as `before.mp4` and `after.mp4`. Copy recordings out of temporary recorder storage before cleanup; avoid overwriting another run.

Evidence files must be videos or images. Do not save reports, logs, command output, warnings, JSON, traces, metadata sidecars, patch/diff snapshots (`.patch`, `.diff`), or text dumps (`.txt`) as verification artifacts. This applies outside the evidence folder too. Read diagnostic output in the terminal and summarize relevant results in chat. Do not redirect or tee verification commands into evidence files. Leave existing project logging alone.

If a tool requires intermediate files, use the operating system's temporary directory and remove this task's non-media scratch files before delivery. The media review retention rule below does not apply to scratch files. Preserve source changes, regression tests, required application outputs, and unrelated files.

## Capture and check

- UI: Use a short recording for interactions or motion, and screenshots for static visual changes. Capture the actual application with comparable viewport, state, and framing before and after. Keep only the media needed to demonstrate the result.
- Inspect the final media for readability and the claimed behavior. Keep native capture quality; never upscale or duplicate frames to imply better quality. Screenshots cannot prove timing or motion. If capture is unavailable, state the gap in chat.
- Non-UI: Run the smallest reproducible check that exercises the changed behavior. Prefer existing project tools and tests. Report the command or steps, relevant inputs, observed result, and exit code in chat. A build or unrelated passing suite is insufficient. Do not manufacture media by screenshotting terminal output or text reports.

## Summarize in chat and retain media

Use [references/report-template.md](references/report-template.md) as a short chat summary, never as a saved report. Link or embed the videos and images with observations and useful timestamps. State missing evidence and unverified claims. Keep secrets out of captures; upload or commit artifacts only when authorized.

Retain temporary media until the user explicitly confirms review in response to a cleanup request. Ask for that confirmation when delivering temporary media. Then remove only this task's temporary media. Keep PR-attached media and the files supporting its links.
