# Evidence report

Use relative artifact links. Include only applicable fields and files that exist.

```markdown
# Evidence: <task>

Changed: <resulting behavior>
Why: <user impact>
How: <key implementation change>
Context: <before/after revisions and relevant uncommitted state; environment, fixtures, capture settings>

| Scenario | Expected | Before observed | After observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| S01: <trigger> | <requirement and source> | <actual result> | <actual result> | <PASS / FAIL / BLOCKED / NOT RUN> | <links and timestamps> |

Reproduce: <working directory, exact commands or steps, inputs, assertions, reset procedure>
Checks: <commands, exit codes, observed results, saved output links>
Visual quality: <what was inspected and whether it is readable; omit for non-UI>
Limitations: <missing baseline, capture gaps, blocked or untested behavior; None if fully verified>
```

Repeat scenario-specific reproduction details when needed. `PASS` requires an observed expected result; supporting checks may pass both before and after. Mark verification incomplete when a required claim lacks evidence.
