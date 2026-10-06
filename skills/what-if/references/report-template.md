# What-if output

Interview question:

```text
What if <scenario>?
Right now: <behavior, file:line; or unknown>
Coverage: <test and whether run; or None>
What should happen?
```

Progress and final report:

```markdown
# What if: <feature>
<Case counts by status>

| # | Scenario | Expected, source | Current behavior, evidence | Status |
| --- | --- | --- | --- | --- |
| <id> | <case> | <user/docs/test/assumed> | <file:line or unknown> | <status> |

Bugs: <case IDs, mismatch>
Tests to write: <file/suite, case IDs, scenario and expected result>
Manual checks: <case IDs, steps, pass condition>
Open questions: <missing requirement/evidence>
```

Empty sections say `None.`. Include Bug and Untested cases in proposed tests. Preserve uncertainty; quick mode starts with "Check assumed expectations and Open cases first."
