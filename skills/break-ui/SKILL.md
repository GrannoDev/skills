---
name: break-ui
description: Exercise a UI across failure angles and report reproduced bugs ranked by severity. Run only when invoked by name.
argument-hint: "[url or app] [flow]"
disable-model-invocation: true
---

# Break UI

Explore a UI, reproduce failures, and report evidence. Do not fix code unless requested.

## 1. Establish the target

Use the request and project setup to identify the URL/build, scoped screens/flows, test accounts, and off-limits actions. Default to the whole app when no narrower scope is given. Use local/dev/staging; obtain explicit authorization before testing production. Use test credentials and test payment data only.

Prefer the harness's supported browser/simulator/emulator tools and follow their usage instructions. Other automation is a fallback when supported tools are unavailable. If you cannot both interact and observe results, report the missing capability and stop. Start the app through its documented setup if needed; confirm it loads and capture a screenshot.

## 2. Map and select angles

Map in-scope screens, navigation, inputs, forms, modals, and destructive controls. Capture baseline screenshots and note existing defects without excluding them from the final report.

Read [references/attack-angles.md](references/attack-angles.md). Use the requested angles, or all applicable angles: Input, Timing and repetition, Navigation and state, Layout and viewport, Failure paths, Keyboard and accessibility. Report exclusions with reasons.

## 3. Exercise

Use the brief below yourself or delegate one angle per subagent when available. Default budget: 40 UI actions per angle; honor a user-specified budget.

```text
Target and scope: <URL/build, allowed host/app, screens/flows>
Angle and attacks: <selected attack-angles.md section>
Map and baseline defects: <short map>
Accounts and off-limits actions: <test account references; restrictions>
Budget: <actions>
Evidence directory: <scratch or gitignored path>/<angle>/

Stay within the target and scope. Do not edit code or use real payment data.
Report observable failures: title, location, exact reproduction steps,
expected behavior and its source, actual result, screenshots/logs.
If no failures, report what was attempted and blocked.
```

Parallel agents need isolated UI sessions. Use distinct accounts/test records for shared backend state when practical. On a shared tab/device, run sequentially. Reset only disposable, authorized test state; never clear unrelated user data. Keep evidence outside tracked source files and credentials out of reports.

## 4. Reproduce and rank

Retest findings from a known state, merge duplicates, and retain clear steps. Record intermittent findings with attempts/successes. Move unconfirmed findings to Not reproduced; do not count them as bugs.

| Severity | Criterion |
| --- | --- |
| Critical | Data loss/corruption, security breach, app-wide crash, or core flow blocked without a workaround. |
| High | Incorrect data, stuck state requiring reload, or core flow broken with a workaround. |
| Medium | Broken secondary feature, lost input, or missing/misleading error. |
| Low | Layout, visual, or wording defect without functional blockage. |

Use the highest applicable severity and explain its concrete impact. Do not report style preferences as defects.

## 5. Report

Use [references/report-template.md](references/report-template.md). Include coverage and blocked checks even if no bugs were found. End with the report; offer fixes if the user has not already requested them.
