---
name: what-if
description: Review one feature's edge cases with the user and produce an evidence-backed test plan. Run only when invoked by name.
argument-hint: "[-q] [feature or path]"
disable-model-invocation: true
---

# What If

Review one feature, keep a case ledger in chat, and end with a test plan. Do not write code or tests unless requested.

## Modes

- **Default:** confirm the contract, then ask one “What if…?” at a time. Update the ledger after each answer; show it every 5 questions. Offer another round after 15 questions. Stop when the user asks or cases run out.
- **`-q`:** skip the interview. Derive expectations from docs, tests, and the stated contract. Mark unsupported expectations *(assumed)*; unresolved product decisions remain Open. An assumption alone cannot establish a Bug.

## Workflow

1. **Identify the feature.** Use the requested feature/path, or infer from the branch/diff and confirm it in default mode. Ask if still ambiguous.
2. **State the contract.** Read implementation and tests. Summarize inputs, outputs, state, dependencies, and invariants. Confirm or correct it in default mode.
3. **Find cases.** Use [references/lenses.md](references/lenses.md) for general risks and only relevant sections of [references/checklist.md](references/checklist.md) for platform specifics. Deduplicate overlapping cases. Prioritize likely failures with high impact, especially loss of data, money, or access.
4. **Inspect evidence.** For each case, identify current behavior with file:line, relevant test names, and where the expected behavior comes from. Say when behavior cannot be determined; absence of a test does not prove a bug.
5. **Resolve expectations.** In default mode, ask using [references/report-template.md](references/report-template.md). Record the user's answer, update the contract if needed, and add related cases. If answers conflict, explain the conflict once and ask which takes precedence.
6. **Report.** Use the same reference for the ledger and final report. Propose scenario-named tests grouped by existing file/suite, focused on observable behavior. Use tables for similar input cases and existing fixtures; do not prescribe a new test framework.

## Case statuses

| Status | Meaning |
| --- | --- |
| ✅ Tested | Code agrees with an established expectation, and an existing test asserts it. Say whether that test was run. |
| 🟡 Untested | Established expectation appears satisfied and can be automated, but no test covers it. |
| 🔴 Bug | Code demonstrably contradicts a user-confirmed or documented expectation; cite both. |
| ⚪ Out of scope | The user excluded this case. |
| ❓ Open | Requirement or current behavior is unresolved; includes suspected bugs based only on assumptions. |
| 🔵 Manual | Established expectation has no practical automated check and needs manual verification; no known contradiction. |

Keep these categories mutually exclusive. Known incorrect behavior is Bug even if checked manually. Do not call a test passing without running it.

End with the plan and relevant `/use-tdd` suggestions. Offer implementation only if it has not already been requested.
