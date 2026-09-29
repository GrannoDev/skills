# Blueprint template

Keep the headings and status values below: the build and cleanup skills use them. Replace placeholders with repo-specific content. Write `None.` for empty sections. Do not leave example business rules or unresolved placeholders in an approved blueprint.

The file must stand alone in a fresh session: name real files, specify observable behavior, and avoid “as discussed”.

```markdown
---
title: <feature title>
slug: <kebab-case slug>
status: draft
created: <YYYY-MM-DD>
base_branch: <default branch, or unknown>
confirmed_sections: []
---

# <feature title>

## Goal
<What the user can do when this ships. Include constraints.>

## Non-goals
- <Explicitly excluded work.>

## Context
- `<path>`: <relevant types, behavior, and conventions>
- Tests: <framework, fixtures, locations, focused and required commands>

## Domain models
<New/changed entities: fields, types, relationships, migrations, invariants.>
<An erDiagram when there are entity relationships; otherwise explain why none applies.>

## APIs
<For each endpoint/function/event: signature, auth, inputs, outputs,
validation, errors, and side effects. Say “None.” if no interface changes.>

## Data flow
<A sequenceDiagram or flowchart for the main paths, followed by a
numbered walkthrough including failure handling and transaction boundaries.>

## Logic to test
**<test file or suite>**
- <Scenario → expected result; identify the rule or error path covered.>

## Implementation steps
- [ ] 1. <Concrete change, with its tests. Verify: exact command or observable check.>

## Decisions
- **<Choice>**: <reason>. Alternative: <other choice and why it was rejected>.

## Open questions
None.
```

## Planning progress

`confirmed_sections` contains the exact headings approved by the user, including Goal and Non-goals when scope is confirmed. It records section review, not final blueprint approval. In quick mode, leave it empty until the user approves the draft. For older drafts without this field, ask which section to resume rather than inferring approval from populated text.

## Build fields and sections

`/blueprint-build` adds `base_sha` on the first build and preserves it on resume. It appends these sections:

```markdown
## Deviations
- Step <n>: <change or skipped check, reason, and approval if required>

## Summary
<Use the blueprint-build summary template.>
```

Statuses: `draft` → `approved` → `building` → `done`. Only user approval permits `approved`; only completed steps and successful required verification permit `done`. Open questions block a build even if the status says approved.

Keep diagrams focused on this feature. Use an ER diagram for relationships, a sequence diagram for component interactions, and a flowchart for branching logic. Explain them in prose so the blueprint is usable without Mermaid rendering.

Cover relevant invariants, validation, state changes, time boundaries, and error paths in Logic to test. Keep implementation steps independently verifiable, pairing tests with their code and ordering work so the build and required checks pass after each step.
