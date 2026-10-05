---
name: setup-project
description: Confirm exact startup, verification, and test instructions, then save them in the root AGENTS.md. Run only when invoked by name.
argument-hint: "[-q]"
disable-model-invocation: true
---

# Setup project

Use [the setup template](references/setup-template.md). Save only the block between `<!-- setup-project:start -->` and `<!-- setup-project:end -->` in root `AGENTS.md`.

## Inspect and review

Read existing instructions, README, service/build/framework configs, environment examples, auth setup, migrations, and representative tests. Inspect files relevant to this stack. Extract exact commands, directories, service ownership/order, readiness checks, ports, and test conventions. Do not print secrets.

Default: show and confirm Running the app, Verifying changes, and Tests in order. `-q`: show the entire draft and confirm once. Display the actual draft inline before asking; reuse prior answers. Mark proposed choices *(assumed)* and missing facts `Unresolved`; omit inapplicable rows. Re-review only affected sections.

Specify:

- Running: prerequisites; agent/user ownership; startup/readiness/data-preserving stop commands; migrations, seeds, authorized resets, and off-limits environments. Proposed default is agent-managed local services in dependency order; production/shared environments are off-limits.
- Verification: required build/lint/type/test commands; affected UI flows and browser/simulator/emulator targets; test accounts per role; enabled API-token method; auth blockers. Keep saved instructions agent-neutral, including carried-over wording. Include cleanup before commit/push, respecting evidence-retention rules.
- Tests: write/run/leave-alone policy, all/single-test commands, dependencies, fixtures, naming/mocking conventions, and slow/flaky exceptions. Follow existing conventions; do not invent coverage targets.

## Save and optionally verify

After confirmation, remove confirmed assumption labels and replace only the marked block, preserving other content. Create `AGENTS.md` if absent. Move a legacy marked block from `CLAUDE.md`; offer `@AGENTS.md` there if it is not imported.

Reference existing credential locations. Store newly supplied local/dev/staging test credentials only in `.agents/test-accounts.md` after verifying it is untracked and ignored. Add a local `info/exclude` entry if needed and report it; otherwise record the blocker. Never save passwords in `AGENTS.md` or use personal/production accounts.

Offer a trial unless already requested. When requested, check startup, login/token flows per available role, one test per chosen kind, and required checks. Correct disproved commands and mark unperformed/blocked checks *(unverified)*. Leave services running unless stopping was requested. Report the saved path and unresolved items.
