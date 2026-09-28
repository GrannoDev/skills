---
name: blueprint
description: Plan a feature with the user, section by section, into a blueprint file covering domain models, APIs, data flow, logic to test and implementation steps, ready for /blueprint-build. Run only when the user invokes it by name.
argument-hint: "[-q] [feature]"
disable-model-invocation: true
---

# Blueprint

Plan one feature with the user and write it to `.blueprints/<slug>.md`. Go one section at a time and get the user's confirmation on each before moving on. Don't write feature code; `/blueprint-build` does that.

The blueprint is the only thing `/blueprint-build` reads. It may run in a fresh session or on another model, so the file has to stand on its own.

## Quick mode with `-q`

If the user passes `-q` (`/blueprint -q <feature>`, or "blueprint -q"), don't stop for confirmation after each section:

- **Draft everything:** write all the sections in one pass, deciding each one yourself from the code and the user's request.
- **Assumptions:** mark every choice you made without the user's input with *(assumed)*.
- **Open questions:** when there's no reasonable default, such as a business rule or a product decision, add it to Open questions instead of guessing.
- **Review:** still run the critique in step 5, then show the whole blueprint and ask once for approval. Start with one line telling the user to check the *(assumed)* items and open questions first.

Everything else in this skill still applies.

## 1. Set up

Get the feature from the user's message. If they didn't name one, ask. Use a question tool if you have one.

Pick a short kebab-case slug (`team-invitations`). If `.blueprints/<slug>.md` already exists with `status: draft`, offer to resume it from its first unconfirmed section. If it exists with any other status, ask whether to start over or pick another slug.

Make sure `.blueprints/` is gitignored in the user's repo:

```bash
git check-ignore -q .blueprints/x.md || echo ".blueprints/" >> "$(git rev-parse --git-common-dir)/info/exclude"
```

This writes to `.git/info/exclude`, which is local and never committed, so the project's `.gitignore` stays untouched. Tell the user if you added the line. If the directory isn't a git repo, skip this and say so.

## 2. Pin the scope

Ask only what the request and the code don't already answer:

- **Goal:** what the user can do once this ships, in one or two sentences.
- **Non-goals:** what's deliberately left out.
- **Constraints:** deadlines, compatibility, performance targets, libraries to use or avoid.

Confirm the goal and non-goals before exploring. Then create the file from [references/blueprint-template.md](references/blueprint-template.md) with `status: draft`, the goal and non-goals filled in, and set `base_branch` to the repo's default branch.

## 3. Explore the code

Find what the feature builds on. Cover:

1. **Models:** existing entities, schemas and migrations the feature touches or sits next to.
2. **APIs:** existing routes, handlers or public functions nearby, and their conventions for naming, auth, validation and errors.
3. **Tests:** the test framework, where tests live, fixtures and helpers, how the clock and the network are handled.
4. **Touch points:** code the feature has to call or change, such as mailers, queues, permissions and UI entry points.

If your harness can start subagents, send one read-only agent per area in parallel with this brief:

```
Feature: <goal>
Area: <area>
Find the files, types and conventions in this repo that a developer adding
this feature would need to know about for <area>. Report file paths with a
one-line note each, plus the conventions to follow. Don't edit anything.
```

Otherwise, explore the areas yourself. Write the results into **Context** as file paths with one-line notes. Show Context to the user and ask if anything is missing.

## 4. Draft section by section

Draft each section, show it, and ask the user to confirm or change it. Write it to the file once they confirm, so a draft survives an interrupted session. Follow the template for format and diagrams.

1. **Domain models:** new and changed entities, their fields, relations and invariants. Include an `erDiagram`.
2. **APIs:** every endpoint, function or event the feature exposes, with inputs, outputs and each error case. Follow the conventions from Context.
3. **Data flow:** how data moves through the system for the main paths. Include a `sequenceDiagram` or `flowchart` and a short numbered walkthrough.
4. **Logic to test:** every rule that can break, as concrete test cases named after their scenario, grouped by the test file they belong in. Focus on invariants, validation, state changes, time and error paths. Skip glue code with no logic.
5. **Implementation steps:** ordered checkboxes. Each step is small enough to verify on its own and says how to verify it. Put tests in the same step as the code they cover. Order steps so the build compiles and passes its tests after every step.

Keep these two running while you go:

- **Decisions:** each time the user picks between real alternatives, record the choice, the alternative and why.
- **Open questions:** anything the user isn't sure about. Don't guess an answer to fill a gap.

If a later section changes an earlier one, such as an API needing a field the model doesn't have, say so and update the earlier section.

## 5. Critique

Before asking for approval, attack the draft. If your harness can start subagents, give a fresh agent the blueprint file with this brief. Otherwise, do it yourself.

```
Review this blueprint as if you had to build it tomorrow with no other
context. Report only real problems:
- Invariants the APIs or steps don't enforce.
- Error paths with no API response or no test.
- Steps in the wrong order, or steps that leave the build broken.
- Fields, files or functions referenced but never defined.
- Anything too vague to implement without asking.
```

Show the user each problem with a suggested fix and apply the ones they accept.

## 6. Approve

Show a short outline: the number of models, APIs, test cases and steps, plus any open questions.

- If Open questions isn't empty, keep `status: draft` and list them. The blueprint can't be built until they're answered.
- Otherwise ask the user to approve. On approval, set `status: approved`.

End with the file path and tell the user to run `/blueprint-build <slug>` when they're ready. Don't start building on your own.
