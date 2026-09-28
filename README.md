# skills

Agent skills by [GrannoDev](https://github.com/GrannoDev).

## Install

```bash
npx skills add GrannoDev/skills
```

Install a single skill:

```bash
npx skills add GrannoDev/skills --skill <name>
```

## Skills

| Skill | Description |
| --- | --- |
| [blueprint](skills/blueprint/SKILL.md) | Plans a feature section by section into a blueprint: domain models, APIs, data flow, logic to test and steps. |
| [blueprint-build](skills/blueprint-build/SKILL.md) | Builds an approved blueprint tests-first and summarizes how it works, why, and which files changed. |
| [blueprint-clean](skills/blueprint-clean/SKILL.md) | Deletes finished blueprints and lists the ones still in progress. |
| [break-ui](skills/break-ui/SKILL.md) | Sends agents to break a UI in a browser, simulator or emulator and reports ranked, reproduced bugs. |
| [commit](skills/commit/SKILL.md) | Summarizes changes as conventional-commit bullets and proposes a commit message. |
| [use-tdd](skills/use-tdd/SKILL.md) | Fixes a bug test-first: a focused regression test that fails before the fix and passes after. |
| [what-if](skills/what-if/SKILL.md) | Walks through a feature's edge cases one question at a time and ends with a test plan. |

## Adding a skill

Each skill is a folder under `skills/` with a `SKILL.md`:

```
skills/<name>/
  SKILL.md        # frontmatter (name, description) + instructions
  references/     # optional: extra docs loaded on demand
  scripts/        # optional: helper scripts
```

`name` must match the folder name. `description` says what the skill does and when to use it; agents read it to decide when to load the skill.
