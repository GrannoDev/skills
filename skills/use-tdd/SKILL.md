---
name: use-tdd
description: Fix a bug with a focused regression check that fails before the fix and passes after. Run only when invoked by name.
argument-hint: "[bug]"
disable-model-invocation: true
---

# TDD bug fix

1. Identify expected behavior, actual behavior, and the smallest reproduction. Resolve unclear requirements before asserting them.
2. Add a focused behavioral regression test through the closest existing unit/component/integration path. Reuse fixtures and conventions.
3. Run it before changing production code. Failure must come from the bug, not setup or syntax. If it passes, correct the reproduction first.
4. Make the smallest fix preserving nearby contracts; never weaken assertions to accommodate incorrect behavior.
5. Rerun the regression and relevant required checks. Control timing/randomness for flaky failures when practical.

If a test needs broad infrastructure, brittle mocks, or unrelated fixture churn, use a practical executable/manual reproduction and explain why. Do not create a framework merely to satisfy TDD.

Report `Fixed`, `Before` with command and observed failure, `After` with the same check and required results, and `Limitations`. Claim only checks actually performed.
