---
name: blueprint-build
description: Implement an approved .blueprints/ plan step by step, tests first, and record verification and deviations. Run only when invoked by name.
argument-hint: "[slug or path]"
disable-model-invocation: true
---

# Blueprint Build

Use the blueprint as the feature contract; inspect current repo instructions and code for implementation details. Do not depend on the planning conversation.

## Load and prepare

1. Read the requested path or `.blueprints/<slug>/PLAN.md` (fall back to a legacy `.blueprints/<slug>.md`). Without an argument, use the only `approved` or `building` blueprint; ask if several match. If none match, suggest `/blueprint`.
2. Reject `draft`, unknown status, or unresolved Open questions. For `done`, ask what should be rebuilt. Start `approved` at step 1; resume `building` at the first unchecked step, verifying that checked steps still exist and pass.
3. Inspect `git status --short`. Preserve existing work; ask only if unrelated changes overlap the implementation or make its scope unclear. If on `base_branch`, offer `feat/<slug>` unless the user already chose a branch.
4. Read Context files and applicable repo instructions. Ask about drift that changes a model, API, decision, or invariant. Routine renames can be recorded as deviations.
5. On the first build, record `base_sha` from `git rev-parse HEAD`; preserve it on resume. Set `status: building` after preflight succeeds. Track this build's files separately from pre-existing changes.

## Implement each unchecked step

1. Write the step's practical regression tests from Logic to test before production code. Run them and confirm they fail because the behavior is missing. If that is impractical, record why and the replacement check.
2. Implement the step using the repo's conventions. Do not weaken assertions to fit incorrect behavior.
3. Run its tests and specified verification. Tick and save the checkbox only after they pass.

Record each departure under `## Deviations`: step, change, and reason. Continue through mechanical adjustments. Ask before changing a planned model, API, decision, or invariant, unless that change is already authorized. Record omitted steps or tests; an unresolved required step remains unchecked.

## Verify and finish

- Run the blueprint's required checks and applicable repo checks, including the full suite, type check, lint, and build where required. Fix failures caused by this work; report unrelated failures with evidence.
- Compare the implementation against all planned models, APIs, tests, steps, and invariants. Check that Deviations explains extra work. Review yourself or use a fresh read-only agent when available.
- Write `## Summary` using [references/summary-template.md](references/summary-template.md). Use the diff from `base_sha` plus untracked files as evidence, but attribute only this build's changes.
- Set `status: done` only when every required step and check is complete. Otherwise keep `building` and report the remaining work or blocker. Append the summary and show it to the user.

End with the blueprint path and relevant next commands (`/what-if`, `/commit`). Commit, push, or open a PR only when requested.
