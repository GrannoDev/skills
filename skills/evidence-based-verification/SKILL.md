---
name: evidence-based-verification
description: Verify a feature or bugfix with observable before-and-after evidence and a concise Why / How report. Use when implementing changes or verifying completed work, with videos for UI changes and reproducible behavioral checks for non-UI changes.
---

# Evidence-based verification

Show what changed with evidence the user can inspect. Explain why the change was needed and how it achieves the result.

## Choose the evidence before editing

Identify the behavior being changed and the smallest scenario that demonstrates it. Define the expected outcome from the task requirements. Capture the baseline before modifying the implementation whenever possible.

For a bugfix, demonstrate the reported failure and rerun the same scenario after the fix. For a feature, show the existing workflow or missing capability, then demonstrate the new behavior against its acceptance criteria. A new feature does not need an artificial failing baseline.

Keep inputs, environment, and relevant state comparable between runs. Record the revision or working-tree state used, the reproduction steps or command, and enough setup information to repeat the check. Reset mutable test data between runs where needed.

If work is already complete, recover the baseline from a known earlier revision in an isolated checkout when practical. Preserve current changes. If no usable baseline exists, provide after evidence and state that the before evidence is missing and why. Never recreate a supposed baseline by guessing at the old behavior.

## UI changes

Provide before and after videos of the affected workflow. Keep each recording focused on the trigger and visible result, with enough context to understand the interaction.

If video capture is unavailable, provide before and after screenshots and briefly explain the fallback. Use matching viewport sizes, application states, and framing. For an interaction, capture the relevant sequence of states rather than only the final screen.

Use actual captures of the running application. Inspect the recordings or screenshots before presenting them to confirm they show the claimed behavior and are readable. Label artifacts Before and After and give them distinct filenames.

Screenshots alone cannot establish timing, animation quality, or an entire interaction. Supplement them with an observed interaction check or relevant automated result when needed, and state any remaining gap. If neither recording nor screenshots are available, provide the strongest available behavioral check and explicitly mark visual verification as incomplete.

## Non-UI changes

Choose the smallest reproducible check that exercises the changed behavior through an appropriate interface. Prefer existing project tools and tests. Examples include:

| Change | Useful evidence |
| --- | --- |
| API behavior | The request, response status and relevant body, plus any expected side effect. |
| CLI behavior | The invocation, representative input, stdout or stderr, exit code, and resulting files when relevant. |
| Business logic | A focused regression or acceptance check with the input, expected result, and actual result. |
| Data processing | A controlled fixture and the resulting records, output diff, or invariant checks. |
| Performance | Comparable workloads and conditions, repeated measurements, and the observed variation. |

For a bugfix, confirm that the baseline fails because of the reported bug, not a setup error, and that the same check passes after the fix. For a feature, verify its intended behavior and relevant boundary or failure cases. Add a focused test when useful; a reproducible command or manual check can be sufficient without building a new test framework.

Save the relevant output and exact commands or steps. A code diff, successful build, or passing unrelated suite does not by itself prove the requested behavior. Run applicable project checks as supporting evidence. For changes spanning UI and backend behavior, provide both kinds of evidence where each is needed to support the claims.

## Deliver the evidence

Keep artifacts in the project's established location, or a clearly named task output directory. Use safe fixtures and omit credentials and private data from captures and logs. Keep evidence accessible to the user after temporary environments are removed. Do not publish or upload it externally unless authorized.

End with a short report using the shape below. Keep Why and How to one or two sentences each. Group related changes; separate unrelated outcomes only when necessary. Embed viewable media when supported and link to all evidence using accessible artifact links or absolute local paths. Include concise observations so the user knows what each artifact proves.

```text
Changed: <problem fixed or feature created, and resulting behavior>
Why: <user impact or need>
How: <key change and how it produces the result>
Evidence:
- Before: <linked artifact or saved check output, with observed behavior>
- After: <linked artifact or saved check output, with observed behavior>
- Checks: <relevant commands or steps and actual results>
Limitations: <missing evidence, failed checks, or unverified behavior and reason; omit if none>
```

Distinguish observed results from expectations. Report incomplete verification directly; never claim a capture, test run, or successful outcome that did not occur.
