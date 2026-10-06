---
name: what-if
description: Review a feature's edge cases one question at a time and produce an evidence-backed test plan. Run only when invoked by name.
argument-hint: "[-q] [feature or path]"
disable-model-invocation: true
---

# What if

Review only; write code/tests when requested.

Default: confirm the feature contract, ask one "What if?" at a time, and update the case ledger after each answer. Show it every 5 questions; offer another round after 15. Stop on request or when cases run out. `-q`: skip questions, derive expectations from docs/tests/contract, mark assumptions, and leave unresolved product decisions Open.

1. Select the requested feature/path or infer from branch/diff, confirming it in default mode. Ask if ambiguous.
2. Read implementation/tests; summarize inputs, outputs, state, dependencies, and invariants. Confirm the contract in default mode.
3. Choose relevant [checklist scenarios](references/checklist.md), using real fields/states. Deduplicate; prioritize likely loss of data, money, or access.
4. Record current behavior with file:line and test names, including whether tests ran. Unknown behavior stays unknown; absent tests do not prove bugs.
5. Ask using [the question/report template](references/report-template.md). Record answers, update the contract/cases, and resolve conflicting answers once. Propose behavioral tests grouped by existing file/suite and fixtures.

| Status | Meaning |
| --- | --- |
| Tested | Established expectation matches code and an existing assertion; state whether run |
| Untested | Expectation appears satisfied, automatable, but uncovered |
| Bug | Demonstrated contradiction of a confirmed/documented expectation; cite both |
| Out of scope | User excluded it |
| Open | Requirement/behavior unresolved, including assumption-only suspicions |
| Manual | Established expectation needs manual checking; no known contradiction |

Assign each case once. Incorrect behavior is Bug even when checked manually. Never claim unrun tests passed. End with the plan; offer implementation only if not already requested.
