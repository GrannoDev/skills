# Bug hunt report

Start with target, revision, scope, and reproduced/verified counts. Rank confirmed findings, then suspicions. Keep Why/How short and supported by evidence.

```text
<ID> <severity> <failure>
Status: <Reproduced | Suspected | Fixed and verified | Fix not verified>
Why: <impact and prerequisites>
How: <observed trigger/cause; fix if made; unknown if unsupported>
Reproduce: <actor, ownership, starting state, input, exact steps/request>
Expected: <contract and source>
Actual: <response, durable state, external effects>
Before: <artifact links and observations>
After: <comparable links, or unavailable/not applicable with reason>
Checks: <commands/results; intermittent successes/attempts>
```

End with `Flow/invariant | Actors/layers | Result/evidence | Gap` coverage. Include blocked/skipped checks. With zero findings, say "No bugs reproduced in the tested scope." Omit empty suspicions; link the evidence package rather than duplicating it.
