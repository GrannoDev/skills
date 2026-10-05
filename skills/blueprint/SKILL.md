---
name: blueprint
description: Plan one feature with the user and save an approved .blueprints/ plan for /blueprint-build. Run only when invoked by name.
argument-hint: "[-q] [feature]"
disable-model-invocation: true
---

# Blueprint

Plan only. Save `.blueprints/<slug>/PLAN.md` using [the template](references/blueprint-template.md).

## Review modes

Default: show and confirm scope, Context, and each design section before continuing; save confirmations immediately. `-q`: draft everything, mark unsupported choices *(assumed)*, critique, then request approval once. Reuse answers already supplied.

For full-draft reviews, use `plannotator annotate .blueprints/<slug>/PLAN.md --gate --json` when available. `approved` grants approval; incorporate notes. For `annotated`, revise and reopen. For `dismissed`, errors, or unavailable Plannotator, review in chat.

## Workflow

1. Infer the feature or ask. Choose a kebab-case slug. Resume drafts from their first unconfirmed section. Move legacy `.blueprints/<slug>.md` to the directory layout. Ask before replacing other statuses. For drafts without `confirmed_sections`, ask where to resume rather than inferring approval from filled sections.
2. Check `git check-ignore`; if needed, add `.blueprints/` to the common Git directory's `info/exclude` and report it. Skip exclusion outside Git.
3. Set new metadata to `status: draft`, the local date, and the default `base_branch`, or `unknown`. Preserve metadata on resume. Confirm Goal, Non-goals, and constraints.
4. Inspect relevant models, migrations, API conventions, tests, fixtures, and UI integrations. Record actual paths and verification commands in Context.
5. Draft Domain models, APIs, Data flow, Logic to test, and Implementation steps in that order. Specify contracts, invariants, failure paths, and tests. Record decisions and alternatives. Reconfirm earlier contracts changed by later decisions.
6. Check undefined references, missing errors/tests, and steps that break required checks. Show model/API/test/step counts, assumptions, and open questions. Unresolved questions keep `draft`; only explicit final approval sets `approved`.

Track section approvals in `confirmed_sections`; section approval is not final approval. In quick mode, leave it empty until approval. End with the plan path and `/blueprint-build <slug>`; do not build automatically.
