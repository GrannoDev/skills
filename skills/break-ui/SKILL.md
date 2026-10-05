---
name: break-ui
description: Exercise UI inputs, timing, navigation, layout, failures, and keyboard use; report reproduced bugs by severity. Run only when invoked by name.
argument-hint: "[url or app] [flow]"
disable-model-invocation: true
---

# Break UI

Hunt and report; fix code only when requested.

1. Identify URL/build, flows, test accounts, and restrictions from the request/setup. Default to the whole app. Use local/dev/staging and test payment data; production testing requires explicit authorization. Start through documented setup and capture a baseline screenshot.
2. Use supported browser/simulator/emulator tools. Fall back to other automation only when unavailable. If interaction and observation are impossible, report the missing capability and stop.
3. Map screens, forms, modals, navigation, and destructive controls. Include existing defects. Select requested or applicable [attack angles](references/attack-angles.md); state exclusions. Default budget is 40 UI actions per angle, unless specified otherwise.
4. Exercise angles yourself or delegate when agents are available. Supply target/scope, angle, map, account references, restrictions, budget, and evidence directory. Parallel work requires isolated UI sessions and separate test records where needed; shared tabs/devices run sequentially. Reset only authorized disposable data.
5. Retest from known state, merge duplicates, and record successes/attempts for intermittent failures. Put unconfirmed issues under Not reproduced; do not count them as bugs. Rank by the highest applicable concrete impact:

| Severity | Impact |
| --- | --- |
| Critical | Data loss/corruption, security breach, app-wide crash, core flow blocked without workaround |
| High | Incorrect data, reload-required stuck state, core flow broken with workaround |
| Medium | Broken secondary feature, lost input, missing/misleading error |
| Low | Observable layout/wording defect without functional blockage |

Use [the report](references/report-template.md), including coverage and blockers even with zero findings. Link captured evidence without secrets; do not report style preferences as bugs. Offer fixes only if not already requested.
