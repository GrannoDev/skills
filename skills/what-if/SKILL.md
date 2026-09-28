---
name: what-if
description: Start a what-if session that walks through the edge cases of one feature, one question at a time, and ends with a test plan. Run only when the user invokes it by name.
argument-hint: "[-q] [feature or path]"
disable-model-invocation: true
---

# What If

Work through the edge cases of one feature with the user, one "What if…?" at a time. Keep a ledger of every case and end with a list of tests to write. Don't write code or tests unless the user asks.

## Quick mode with `-q`

If the user passes `-q` (`/what-if -q <feature>`, or "what-if -q"), skip the interview:

- **Contract:** state it and continue without waiting for confirmation.
- **Questions:** don't ask any. For each case, decide the expected behavior yourself from the contract, the existing tests, docs and comments, and common sense.
- **Assumptions:** mark every expected behavior you decided with *(assumed)*. A 🔴 in quick mode means "looks wrong to me", not a confirmed bug.
- **Open cases:** when there's no reasonable default, such as a business rule or a product decision, mark the case ❓ instead of guessing.
- **Report:** go straight to the report in step 5, covering every case you found. Start it with one line saying the expected behaviors are assumed and the user should check the 🔴 and ❓ cases first.

Everything else in this skill still applies.

## 1. Pin the feature

Get the feature from the user's message. If they didn't name one, use the current branch or uncommitted diff and confirm it with them. If it's still unclear, ask. Use a question tool if you have one.

Read the feature's code and its existing tests. Then state its contract in a few lines:

- **Inputs:** what it takes, and from where.
- **Outputs:** what it returns, renders or writes.
- **State:** what it reads or changes (database, cache, files, session).
- **Dependencies:** services, the clock, randomness, other modules it calls.
- **Invariants:** what must always be true ("a cart total is never negative").

Ask the user to confirm or correct the contract before going further. Every question after this is measured against it.

## 2. Find the cases

Read [references/lenses.md](references/lenses.md). Run the feature through each lens and write down every case that could plausibly happen. Skip lenses that don't apply.

For each case, work out from the code what happens now and whether a test covers it. Rank the cases by likelihood × impact: cases that are likely and would lose data, money or access come first.

Keep this list to yourself. The user sees it one question at a time.

## 3. Ask, one at a time

Ask each question in this form:

```
What if <scenario>?

Right now: <what the code does, with file:line>, or "I can't tell from the code".
Tested: <test name>, or no.

What should happen?
```

The user answers with the expected behavior, "don't care" or "not sure". Then:

- Add the case to the ledger with a status.
- If the answer changes the contract, say so and update it.
- If the answer suggests a related case, add it to your list.

Don't argue with the answer. If it contradicts something the user said earlier, point out the conflict once and let them pick.

Stop after about 15–20 questions and offer another round. Also stop when the user says so or you run out of cases.

## 4. Keep the ledger

Give every case one status:

- ✅ **Tested:** the code does the expected thing and a test proves it.
- 🟡 **Untested:** the code seems to do the expected thing, but no test covers it.
- 🔴 **Bug:** the code does something other than what the user expects.
- ⚪ **Out of scope:** the user decided it doesn't matter.
- ❓ **Open:** the user isn't sure. This is usually a missing requirement, not a missing test.

Show the ledger every 5 questions or so, and whenever the user asks. Keep it in the chat; don't write it to a file.

## 5. Report

Use this format:

```
## What if: <feature>

<n> cases: <n> ✅, <n> 🟡, <n> 🔴, <n> ⚪, <n> ❓

| # | What if… | Expected | Now | Status |
|---|----------|----------|-----|--------|
| 1 | the code is applied twice | rejected with "already applied" | stacks the discount (cart.ts:42) | 🔴 |
| 2 | the code expires during checkout | honored until payment | honored | 🟡 |
```

Then list:

- **Bugs:** the 🔴 cases, one line each with the behavior the user expects. Suggest running `/use-tdd` on each one so it gets a failing test before the fix.
- **Tests to write:** the 🟡 cases as test names, grouped by test file or suite. Name each test after its scenario ("honors a code that expires mid-checkout").
- **Open questions:** the ❓ cases, worded so the user can take them to whoever owns the requirement.

Ask whether the user wants you to write the tests. Don't start on your own.

## Testing best practices

Use these to pick cases and to shape the tests you propose.

- **Test the contract, not the implementation.** A test should survive a refactor that doesn't change behavior.
- **Partition, then hit the edges.** Split inputs into groups that should behave the same, test one from each group, then test the boundaries between groups.
- **Many small variations → one table-driven test.** A table of inputs and expected outputs beats ten near-identical tests.
- **Invariants → a property-based test.** When a rule holds for every input ("the total is never negative"), generate inputs instead of listing them.
- **One behavior per test**, named after the scenario it covers.
- **Validate at the edge, trust the inside.** Test what can arrive from users, the network and storage. Don't test states that internal code can't produce.
- **Mock only real boundaries:** the network, the clock, randomness, the filesystem. Inject the clock so time cases are testable.
- **Every bug gets a regression test** that fails before the fix.
