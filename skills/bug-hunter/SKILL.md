---
name: bug-hunter
description: Reproduce correctness and security bugs across UI, APIs, and persistence. Use for feature hunts, permission checks, retries, concurrency, and verifying reported bugs; excludes cosmetic review.
---

# Bug hunter

Hunt/report by default; implement fixes only when requested.

## Scope and probes

1. Identify feature, environment, revision, test identities, and permitted effects. Without a feature, prioritize high-impact workflows and state the selected coverage.
2. Use local/test targets and disposable records. Live/shared targets and effects require authorization. Control payment/message/callback dependencies. Bound retries/concurrency; stop probes affecting unrelated data, incurring unexpected costs, or destabilizing the target.
3. Map UI action, API operation, durable state, and external effects. Identify actors, roles, tenants, ownership, transitions, and invariants. Derive expectations from requirements/contracts; flag ambiguous product rules.
4. Load [evidence-based-verification](../evidence-based-verification/SKILL.md), locating it by name if installed separately. If unavailable, disclose it and still save reproducible before/after checks and Why/How explanations.
5. Choose relevant [checklist probes](references/bug-checklist.md), prioritizing trust boundaries and persistent/irreversible effects. Establish valid behavior, then vary actors, inputs, order, timing, and failures. Use separate identity sessions; compare allowed/forbidden API requests against controlled records. Hidden UI controls do not prove server authorization.
6. Observe responses and independently reread durable state. Rejected writes must leave protected state unchanged. Respect documented eventual-consistency behavior. For races, record small coordinated overlaps and final state; for retries, test committed writes with lost responses. Record intermittent successes/attempts.

## Findings and requested fixes

Reduce findings to exact reproductions; preserve failing evidence. Separate runtime-confirmed defects from code-only suspicions. Merge duplicates with the same demonstrated cause. Rank concrete impact separately from confidence: Critical for broad compromise/widespread loss; High for unauthorized access, substantial corruption, or core-flow failure; Medium for bounded recoverable failures; Low for minor defects.

Track `Reproduced`, `Suspected`, `Fixed and verified`, or `Fix not verified`. For requested fixes, rerun the original scenario, nearby allowed/forbidden cases, invariants, and required checks. Preserve legitimate behavior. Code changes or unrelated passing tests do not verify a fix.

Use [the report](references/report-template.md), with linked evidence and coverage gaps. Without a fix, after evidence is not applicable. Continue accessible-layer checks when another layer is blocked. Finish selected probes/fix verification within any user budget; explain blockers. With zero findings, report tested scope rather than claiming security or bug-free behavior.
