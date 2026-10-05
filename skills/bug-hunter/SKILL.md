---
name: bug-hunter
description: Find and reproduce feature bugs in the user's project across UI, APIs, and stored state. Use for functional testing, test-account permission checks, retries, concurrency, and reported bugs; excludes cosmetic review.
---

# Bug hunter

Find and report bugs. Implement fixes only when requested.

## Scope and checks

1. Identify the feature, environment, revision, test accounts, and permitted effects. State selected workflows and coverage. Use requirements and contracts for expected behavior; flag ambiguous rules.
2. Use the user's local project or authorized test environment with disposable records and controlled dependencies. Live/shared testing needs authorization for the target and effects. Stop unexpected costs, disruption, or effects on unrelated data.
3. Default to functional testing. Check permissions with normal app operations and controlled test accounts. Broader security testing needs an explicitly scoped request. Report Codex blocks and continue permitted checks; never switch tools or rephrase an action to bypass a block.
4. Map UI actions, API operations, stored state, and external effects. Choose relevant [checks](references/bug-checklist.md). Establish valid behavior, then vary inputs, accounts, ordering, timing, and failures. Hidden buttons do not prove API permission enforcement.
5. Observe responses and independently reread stored state. Denied writes must leave protected state unchanged. Respect documented eventual consistency. Coordinate small overlaps for races; simulate lost responses after commits for retries. Record intermittent reproduction frequency.
6. Load [evidence-based-verification](../evidence-based-verification/SKILL.md), locating it by name if needed. If unavailable, disclose it and save reproducible checks with Why/How explanations. Remove secrets from evidence.

## Findings and requested fixes

Preserve the smallest failing reproduction. Separate observed defects from code-only suspicions; merge findings with the same demonstrated cause. Rank impact separately from confidence: Critical for demonstrated widespread loss; High for unauthorized access, substantial corruption, or core-flow failure; Medium for bounded recoverable failures; Low for minor defects.

Track `Reproduced`, `Suspected`, `Fixed and verified`, or `Fix not verified`. For requested fixes, rerun the original scenario, nearby allowed/forbidden cases, invariants, and required checks. Preserve legitimate behavior. Code changes or unrelated passing tests do not verify a fix.

Use [the report](references/report-template.md) with evidence and coverage gaps. Without a fix, after evidence is not applicable. Finish selected checks within the user's budget; explain blockers. With zero findings, report the tested scope.
