# Build summary

Use this body under the blueprint's `## Summary` heading and in the final response. Keep file references specific; report actual check results rather than claiming “tested”. Empty Deviations and Follow-ups sections say `None.`.

```markdown
### How it works
1. <Main flow through the real code, with file:line references.>

### Why it works this way
- <Decision and reason.>
- <Invariant: enforcement location and test that proves it.>

### Files
- New: `<path>` — <purpose>
- Changed: `<path>` — <behavior changed>
- Tests: `<path>` — <scenarios covered>

### Verification
- `<command>` — <passed / failed / not run, with reason>
- Failing-before evidence: <regression test and failure, or why unavailable>

### Deviations
- Step <n>: <departure and reason>

### Follow-ups
- <Remaining work, limitation, or blocker.>
```
