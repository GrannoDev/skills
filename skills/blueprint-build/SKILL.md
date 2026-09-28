---
name: blueprint-build
description: Build an approved blueprint from .blueprints/ step by step, tests first, then summarize how the feature works, why, and which files changed. Run only when the user invokes it by name.
argument-hint: "[slug or path]"
disable-model-invocation: true
---

# Blueprint Build

Implement an approved blueprint step by step. Write the tests for each step before its code, record every change from the plan, and end with a summary of what was built. The blueprint file is the source of truth. Don't rely on the conversation that produced it.

## 1. Load the blueprint

Take the slug or path from the user's message and read `.blueprints/<slug>.md`. If they didn't give one, list the blueprints in `.blueprints/` with status `approved` or `building`. Use the only match, or ask which one if there are several. If there are none, say so and suggest `/blueprint`.

Check the frontmatter `status`:

- **`draft`:** stop. Tell the user to finish it with `/blueprint <slug>`.
- **`approved`:** start from step 1.
- **`building`:** resume from the first unchecked step. Tell the user which step that is.
- **`done`:** ask whether they want to build it again.

If **Open questions** isn't empty, stop and list the questions, whatever the status says.

## 2. Preflight

- Run `git status --short`. If there are uncommitted changes the blueprint doesn't explain, list them and ask whether to continue.
- If the current branch is `base_branch`, offer to create `feat/<slug>`. Use a question tool if you have one.
- On a fresh start, add `base_sha: <git rev-parse HEAD>` to the frontmatter so the summary can diff against it later. Keep the existing value when resuming.
- Set `status: building`.
- Read every file listed in **Context**. If the code has moved on since planning, such as a renamed function or a changed model, list the differences. Ask before building on top of them if they affect a model, an API or a decision.

## 3. Build each step

For each unchecked step in **Implementation steps**, in order:

1. **Tests first.** Write the cases from **Logic to test** that this step covers. Run them and confirm they fail because the behavior is missing, not because of a typo or a broken fixture. If a failing test would be impractical, say why and name the check you'll use instead.
2. **Implement.** Make the smallest change that does what the step says. Follow the conventions in Context.
3. **Verify.** Run the step's tests and its verify check. Fix the code until they pass. Don't weaken a test to make it pass.
4. **Tick it.** Change `- [ ]` to `- [x]` in the blueprint and save it right away, so an interrupted build can resume.

When reality doesn't match the plan, add an entry under `## Deviations` at the end of the blueprint: which step, what changed, and why.

- **Small deviations**, such as a renamed helper, an extra parameter or a split step: record them and keep going.
- **Contract changes**, meaning anything that changes a domain model, an API, a decision or an invariant: stop and ask the user first. Record the answer.

Never skip a step or a test case without recording it as a deviation.

## 4. Verify the whole feature

- Run the full test suite, plus the type checker, linter and build if the project has them. Fix failures your changes caused. If a failure is unrelated, show it and leave it alone.
- Compare the diff against the blueprint. If your harness can start subagents, give a fresh agent the blueprint and `git diff <base_sha>` with this brief. Otherwise, do it yourself.

  ```
  Compare this diff against the blueprint. Report:
  - Models, APIs, test cases or steps in the blueprint that the diff doesn't implement.
  - Changes in the diff the blueprint doesn't call for and Deviations doesn't explain.
  - Invariants from the blueprint the code doesn't enforce.
  Don't report style issues.
  ```

- Fix real gaps, or record them as deviations with the reason.

## 5. Summarize

Get the changed files, including new ones:

```bash
git diff --stat <base_sha>
git ls-files --others --exclude-standard
```

Write the summary in this format:

```
## Summary: <title>

### How it works
<Walk the main data flow through the real code, one numbered step per hop,
with file:line references. Someone new to the feature should be able to
follow a request from start to finish.>

### Why it works this way
- <Decision>: <reason>, and what it rules out.
- <Invariant>: where it's enforced (file:line) and which test proves it.

### Files
New:
- `path`: what it holds
Changed:
- `path`: what changed
Tests:
- `path`: <n> tests, what they cover

### Deviations
<One line each, or "None.">

### Follow-ups
<Things left out, known limits, TODOs you added. Or "None.">
```

Append the summary to the blueprint, set `status: done`, and show it to the user.

Then suggest `/what-if` on the new feature to look for edge cases the plan missed, and `/commit` to commit the work. Don't commit, push or open a PR unless the user asks.
