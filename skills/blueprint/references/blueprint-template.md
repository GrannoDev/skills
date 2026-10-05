# Blueprint template

Preserve these headings and metadata for build/resume/cleanup. Replace fields with concrete behavior and real paths. Empty sections say `None.`; approved plans have no unresolved placeholders.

```markdown
---
title: <feature>
slug: <kebab-case slug>
status: draft
created: <YYYY-MM-DD>
base_branch: <default branch or unknown>
confirmed_sections: []
---
# <feature>

## Goal
<Observable outcome and constraints>
## Non-goals
<Excluded work>
## Context
<Relevant files, conventions, test fixtures, focused and required commands>
## Domain models
<Fields, types, relationships, migrations, invariants; ER diagram if relationships exist>
## APIs
<Signatures, auth, inputs, outputs, validation, errors, side effects; None if unchanged>
## Data flow
<Sequence diagram or flowchart, plus a walkthrough of failures and transactions>
## Logic to test
<Test file/suite: concrete scenario and expected result>
## Implementation steps
- [ ] 1. <Change paired with tests. Verify: exact command or observable check.>
## Decisions
<Choice, reason, rejected alternative>
## Open questions
None.
```

Steps must be independently verifiable and keep required checks passing. Explain diagrams in prose. `confirmed_sections` records exact approved headings, including Goal and Non-goals.

Build adds `base_sha`, `## Deviations`, and `## Summary`. Statuses are `draft`, `approved`, `building`, `done`. User approval permits `approved`; completed required steps/checks permit `done`. Open questions block building regardless of status.
