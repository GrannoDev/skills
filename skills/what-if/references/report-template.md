# What-if output

Use this question during the interview:

```text
What if <concrete scenario>?
Right now: <behavior, file:line; or Cannot determine.>
Test coverage: <test name and whether run, or None.>
What should happen?
```

Use this ledger for progress and the final report. Count each case once. Preserve assumptions in Expected and uncertainty in Now; do not present them as confirmed defects.

```markdown
## What if: <feature>

<n> cases: <n> ✅, <n> 🟡, <n> 🔴, <n> 🔵, <n> ⚪, <n> ❓

| # | What if… | Expected (source) | Now (evidence) | Status |
| --- | --- | --- | --- | --- |
| <id> | <scenario> | <behavior; user/docs/test/assumed> | <behavior; file:line or unknown> | <status> |

### Bugs
- #<id>: <mismatch and required behavior; suggest /use-tdd>

### Tests to write
**<file or suite>**
- #<id>: <scenario → expected behavior>

### Manual checks
- #<id>: <steps and observable pass condition>

### Open questions
- #<id>: <missing requirement or evidence needed>
```

Empty sections say `None.`. In quick mode, begin with “Check assumed expectations and Open cases first.” Include known bugs needing regression coverage in Tests to write alongside Untested cases.
