---
name: use-tdd
description: Fix a bug with a focused regression check that fails before the fix and passes after. Run only when invoked by name.
argument-hint: "[bug]"
disable-model-invocation: true
---

# TDD Bug Fix

Make the bug executable before changing production code when an existing, practical test path is available.

## Workflow

1. Identify the expected behavior, current behavior, and smallest reproduction. Resolve missing requirements before asserting an expectation.
2. Choose the closest existing unit, component, or integration test path. Write a focused regression test of observable behavior, reusing fixtures and conventions.
3. Run it before the fix. Confirm failure comes from the bug, not setup, syntax, or a broken fixture. If it passes, correct the reproduction/test before editing production code.
4. Make the smallest fix that preserves nearby contracts. Do not weaken assertions to fit incorrect behavior.
5. Rerun the regression test and relevant nearby/required checks. For flaky bugs, control timing, randomness, or other external state where practical.

If the test would need broad harness setup, brittle mocks, slow infrastructure, inaccessible production state, or unrelated fixture churn, use the closest useful executable or manual reproduction instead. Record why; do not build a new framework just to satisfy TDD.

## Output

```markdown
Fixed: <bug and resulting behavior>
Before: <test/check, command, and observed failure>
After: <same check and result; nearby/required checks and results>
Limitations: <missing failing-before evidence or incomplete verification, with reason; or None.>
```

Report observed evidence. Never claim a failing-before or passing-after result you did not demonstrate.
