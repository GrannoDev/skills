# Bug hunt report

Start with the target, revision or working state, tested scope, and counts of reproduced findings and verified fixes. List findings in impact order. Keep Why and How to one or two sentences each; link detailed output rather than pasting full logs.

For each finding:

```text
<ID> <severity> <short title>
Status: <Reproduced | Suspected | Fixed and verified | Fix not verified>
Why: <concrete user or security impact and relevant prerequisites>
How: <observed trigger and supported cause; describe the fix if made>
Reproduce: <actor, ownership, starting state, input, and exact steps or command>
Expected: <required behavior and its source>
Actual: <observed response and resulting persistent or external effects>
Evidence before: <capture or check-output links and observation>
Evidence after: <comparable links and observation, or not applicable / unavailable with reason>
Checks: <original reproduction and relevant regression results; frequency if intermittent>
```

Do not invent a root cause for How. State when the cause is unknown and explain the demonstrated trigger instead. Separate suspected issues from confirmed findings and identify what would confirm or dismiss them.

End with a compact coverage table:

| Flow or invariant | Actors and layers exercised | Result or evidence | Gap |
| --- | --- | --- | --- |

Include blocked, skipped, or incomplete checks and why. If there are no confirmed findings, say "No bugs reproduced in the tested scope" and retain the coverage table. Omit an empty suspicions section. For multiple fixes, provide a short overall Changed / Why / How summary following evidence-based-verification without duplicating each finding.
