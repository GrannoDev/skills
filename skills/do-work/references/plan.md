# Full plan

Use this for every feature and any bug that does not meet the small-bug criteria. Maximum 250 words, excluding link targets. Keep the seven rows in this order. Replace bracketed instructions with concrete facts; use `None` for an empty field.

## Template

### Plan

| Field | Plan |
| --- | --- |
| Problem | [Bug: trigger, observed behavior, and evidenced cause. Feature: intended behavior. Include the scope boundary.] |
| Domains | [Affected business domains or subsystems and their responsibilities. Link the relevant entry points.] |
| Contract changes | [Name added, changed, and removed types, API routes/signatures, schemas, events, or dependencies. State compatibility/migration impact, or None.] |
| Implementation | [2-4 ordered steps with actual file links. Include caller migrations and removal of obsolete paths when applicable.] |
| Trade-offs | [Chosen approach, its main cost, and the relevant alternative rejected with a reason. Use None when there is no meaningful choice.] |
| Verification | [Concrete expected behavior, reproduction/acceptance checks, and relevant regressions. Name any blocker or assumption.] |
| Delivery | [Required before/after evidence or feature demo; proposed runtime and entry point for the try-it link. Disclose capture/runtime limitations.] |

Approve this plan?

The [do-work skill](<absolute path to this skill's SKILL.md>) says "Present the plan and wait for the user's confirmation before implementation."

## Constraints

- Domains describe ownership and behavior, not just directories or languages.
- Contract changes distinguish additions from changes and removals. List actual names and effects; do not substitute a list of changed files.
- State a product assumption in Problem or a technical assumption in Verification. Resolve assumptions that materially change the implementation before asking for approval.
- Steps describe intended edits; checks describe independently observable results.
- File links use the host's supported format. In Codex, use absolute paths with verified line numbers where helpful.
- The approval-rule link must point to the actual installed `SKILL.md`, not the placeholder above.
