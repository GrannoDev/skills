---
name: break-ui
description: Send agents to break a UI in a browser, iOS Simulator or Android emulator, one per attack angle, and return a ranked, reproduced bug report. Run only when the user invokes it by name.
argument-hint: "[url or app] [flow]"
disable-model-invocation: true
---

# Break UI

Map the app, send one agent per attack angle to try to break it, reproduce what they find, and report the bugs ranked by severity. Don't fix anything unless the user asks.

## 1. Set the target

Get these from the user's message, the project, or by asking. Use a question tool if you have one.

- **App:** a URL, a dev server to start, or an iOS/Android build to install.
- **Scope:** the screens or flows to attack. Default to the whole app if the user doesn't say.
- **Accounts:** test accounts or seed data the agents can use. Never use the user's real credentials.
- **Off-limits:** anything the agents must not touch, such as account deletion or real payments.

Only attack local, dev or staging environments. If the target looks like production (a public domain with real users, live payment keys), stop and ask before going further.

## 2. Find the tools

Work out what this harness can drive. Look for, in order:

- **Browser:** a browser automation tool (a built-in browser, a browser MCP server such as Playwright or Chrome DevTools, or a browser extension). If there's none but Node is installed, you can write and run Playwright scripts.
- **iOS:** a simulator tool, or `xcrun simctl` for install, launch, screenshots, deep links and app state, plus `idb` or a UI test runner for taps if one is installed.
- **Android:** an emulator tool, or `adb` (`adb shell input tap/text/swipe`, `adb exec-out screencap -p`, `adb shell am start -d <deeplink>`).

If you can't find a way to both act on the UI and see it, tell the user what's missing and stop.

Start the app if it isn't running, and confirm you can load the first screen and take a screenshot.

## 3. Map the app

Do one quick pass yourself before sending anyone:

- List the screens and flows in scope, and how to reach each one (URL, deep link, or taps from launch).
- Note every input, form, destructive button, modal and list.
- Save a baseline screenshot of each screen.
- Note anything that's already broken, so agents don't report it as new.

Keep the map short. It's the brief every agent gets.

## 4. Pick the angles

Read [references/attack-angles.md](references/attack-angles.md). By default send one agent for each angle:

1. Input
2. Timing and repetition
3. Navigation and state
4. Layout and viewport
5. Failure paths
6. Keyboard and accessibility

Drop angles that don't apply (a read-only dashboard has little to fuzz), and say which you dropped and why. If the user names angles, send only those.

## 5. Send the agents

Give each agent this brief, filled in:

```
You're trying to break <app> at <url or build>. Your angle: <angle>.

App map:
<map from step 3>

Attacks to try:
<the angle's section from attack-angles.md>

Rules:
- Only act on <target host or app>. Don't follow links off it.
- Use only these test accounts: <accounts>. Never enter real credentials or payment details.
- Don't touch: <off-limits>.
- Don't edit the code.
- Save screenshots to <evidence dir>/<angle>/.
- Stop after about <budget> actions, or when you run out of ideas for this angle.

For each bug, report: title, where, steps to reproduce, expected, actual,
evidence (screenshot paths, console or log errors). Report only real
misbehavior, not style opinions. If you found nothing, say what you tried.
```

Use a scratch directory outside the repo for evidence, or one that's gitignored. Set the budget to about 40 actions unless the user asks for a longer or shorter run.

**Running them:**

- If your harness can start subagents, run the agents in parallel. Otherwise, work through the angles one at a time yourself, following the same brief.
- **Browser:** give each agent its own tab, window or browser context so they don't navigate each other away. If they share a backend, give each its own test account where you can.
- **iOS and Android:** agents can't share one device. Run them one after another, or give each its own simulator (`xcrun simctl clone`) or emulator.
- Reset the app between agents on a shared device (reinstall, or clear its data) so one agent's damage doesn't show up in the next agent's report.

## 6. Reproduce the findings

Before reporting, try each finding again from a fresh state, following its steps exactly.

- **Reproduced:** keep it.
- **Only sometimes:** keep it and mark it flaky, with how many tries it took.
- **Not reproduced:** drop it, but list it at the end so the user can check.

Merge duplicates. Two agents often hit the same bug from different angles; keep the clearest steps and note both angles.

## 7. Report

Rank the bugs by severity:

- **Critical:** crash, data loss or corruption, security hole, or a core flow that can't be finished.
- **High:** wrong data shown or saved, a stuck state that needs a reload, or a core flow broken with a workaround.
- **Medium:** a broken secondary feature, a missing or misleading error, or lost input.
- **Low:** layout, visual or wording problems that don't block anything.

Use this format:

```
## Break UI: <app>

<n> bugs: <n> critical, <n> high, <n> medium, <n> low
Angles: input, timing, navigation, layout, failure paths, keyboard

### 1. [Critical] Checkout submits twice on double-click
Where: /checkout, Pay button
Angle: timing
Steps:
1. Add any item to the cart and go to /checkout
2. Double-click Pay
Expected: one order
Actual: two orders created, card charged twice (test mode)
Evidence: evidence/timing/checkout-double.png, POST /orders x2 in network log
```

End with:

- **Not reproduced:** findings you dropped, one line each.
- **Not covered:** angles or screens nobody reached, and why.

Then ask whether the user wants you to fix any of them. Don't start fixing on your own.
