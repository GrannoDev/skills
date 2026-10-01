---
name: setup-project
description: Inspect a repo, confirm how to run and verify it, and save the setup in AGENTS.md. Run only when invoked by name.
argument-hint: "[-q]"
disable-model-invocation: true
---

# Setup Project

Save reusable project instructions between `<!-- setup-project:start -->` and `<!-- setup-project:end -->` in the root `AGENTS.md`. Use [references/setup-template.md](references/setup-template.md) for the draft and saved output.

## Modes and review

- **Default:** show and confirm Running the app, Verifying changes, and Tests in that order. If the user requests a change, ask only about the affected parts, revise, and show the section again.
- **`-q`:** show the whole draft and confirm once.

Before every confirmation, print the section or draft being confirmed as inline markdown in your message, then ask. Never call a question tool before the user can see what they are confirming; keep the question itself short and do not rely on it to carry the draft. Use an available question tool when suitable. Reuse choices and authorization already provided by the user.

## 1. Inspect

Use an existing setup as the starting point. Read applicable `AGENTS.md`/`CLAUDE.md`, README, service/container configs, build scripts, framework configs, version files, env examples, migrations, seed data, auth config, and representative tests. Inspect only files relevant to this stack.

Extract commands, working directories, dependency order, readiness checks, ports, test conventions, and auth requirements. Distinguish repo evidence from guesses; never print secrets while inspecting config.

## 2. Draft and confirm

Fill the template with actual commands and evidence. Omit rows that do not apply. Mark reasonable proposed defaults *(assumed)* and unknown commands or credentials as unresolved rather than inventing them.

- **Running the app:** service ownership (agent or user/IDE), prerequisites, startup/readiness/stop commands, migrations, seed/reset procedures, and off-limits actions. Separate data-preserving stops from resets. Proposed default: the agent starts local services in dependency order; production and shared environments are off-limits.
- **Verifying changes:** exact required build/lint/type/test checks, when UI verification applies, preferred UI tool and fallback, auth/roles, API token method, and login blockers. Prefer the harness's supported browser or mobile tooling. Confirm that any proposed token grant is enabled in the app's config.
- **Tests:** kinds to write/run/leave alone, all-tests and single-test commands, dependencies, fixtures/mocking/naming conventions, and slow/flaky-suite exceptions. Proposed default: follow existing test styles and run required existing checks; do not invent coverage targets.

For authenticated flows, reference existing test accounts or ask for missing accounts per relevant role. Use local/dev/staging test accounts, not personal or production credentials. Missing accounts may remain an explicit verification blocker; do not claim login is verified.

## 3. Save

After confirmation, remove confirmed *(assumed)* labels and write only the marked block, preserving the rest of `AGENTS.md`. Create the file if absent. Move an older marked setup from `CLAUDE.md` if present; offer `@AGENTS.md` there if it does not already import it.

Reference existing credential locations. For newly supplied credentials, use the local-only account-file format in the template. Before writing secrets, verify `.agents/test-accounts.md` is ignored (add it to the common git directory's `info/exclude` if necessary) and not tracked. If that cannot be ensured, do not write secrets; record the blocker. Never put passwords in the setup block. Report any exclusion added and that teammates need their own account file.

## 4. Verify when requested

Offer a trial run unless already requested. Start or check services in order, exercise the documented login/token flow for each available role, run one test per selected kind, and run required done checks. Correct commands disproved by the trial; report changes. Mark checks not performed or blocked as *(unverified)*.

Leave services running unless stopping is requested. End with the saved path, what is covered, and any unresolved or unverified items.
