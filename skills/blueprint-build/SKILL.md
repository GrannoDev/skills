---
name: blueprint-build
description: Implement an approved .blueprints/ plan tests-first, saving step progress, verification, and deviations. Run only when invoked by name.
argument-hint: "[slug or path]"
disable-model-invocation: true
---

# Blueprint build

Treat the saved plan as the contract; use current repository instructions for implementation.

## Preflight

1. Read the requested plan or `.blueprints/<slug>/PLAN.md`, with legacy `.blueprints/<slug>.md` fallback. Without an argument, select the only `approved`/`building` plan; ask if several match. If none exist, suggest `/blueprint`.
2. Reject draft/unknown statuses or unresolved Open questions. Ask what to rebuild for `done`. Start `approved` plans at step 1. Resume `building` at the first unchecked step after checking that completed steps still exist and pass.
3. Inspect `git status --short` and Context files. Preserve unrelated work; clarify overlapping changes or drift affecting a model, API, decision, or invariant. Record routine renames as deviations. On `base_branch`, offer `feat/<slug>` unless a branch was already chosen.
4. Record `base_sha` once from HEAD; preserve it on resume. Track this build's changes separately. Set `building` after preflight succeeds.

## Build and finish

For each unchecked step, write practical regression tests first and demonstrate failure from missing behavior. Record a replacement check when tests are impractical. Implement without weakening assertions. Run the step's tests and verification, then tick and save its checkbox.

Record departures under `## Deviations`. Ask before changing planned models, APIs, decisions, or invariants unless already authorized. Unresolved required steps stay unchecked.

Run required plan/repository checks. Fix failures caused by this work; report unrelated failures. Compare implemented contracts, invariants, and tests with the plan. Add [the summary](references/summary-template.md), using the `base_sha` diff and untracked files while attributing only this build's work.

Set `done` only when all required steps/checks pass; otherwise retain `building` and report remaining work. Show the summary and plan path. Suggest `/what-if` or `/commit` when relevant; commit, push, or open a PR only when requested.
