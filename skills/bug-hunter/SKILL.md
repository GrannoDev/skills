---
name: bug-hunter
description: Hunt feature correctness and security bugs across UI, APIs, and persistence. Use for exploratory bug hunts, permission and identity checks, edge cases, failures, retries, concurrency, and reproduction or verification of reported bugs. Focus on observable defects rather than cosmetic review.
---

# Bug hunter

Find violations of intended behavior, reproduce them, and verify fixes with evidence. Hunt and report by default. Implement fixes when the user has requested them; do not interpret a hunt alone as permission to change product behavior.

## Establish the scope and expected behavior

Use the request and project instructions to identify the feature, environment, revision, test accounts, and permitted side effects. If no feature is specified, map the application and prioritize its highest-impact workflows. State the selected coverage rather than implying an exhaustive audit.

Work in local or test environments with disposable records. Testing a live or shared target requires authorization for that target and the proposed effects. Use controlled dependencies for payments, messages, and callbacks. Bound retries and concurrency to the smallest useful reproduction; stop a probe if it affects unrelated data, incurs unexpected costs, or destabilizes the environment.

Map each selected workflow from UI action to API operation to durable state and external side effects. Identify actors, roles, tenants, ownership, state transitions, and invariants such as "only the owner can read this record" or "one reservation consumes one unit." Derive expectations from requirements, documented contracts, and established behavior. Flag ambiguous product rules instead of inventing bugs.

Load [evidence-based-verification](../evidence-based-verification/SKILL.md) before capturing evidence or changing code. If installed separately, locate that skill by name. If unavailable, disclose the missing dependency and still capture reproducible before evidence, comparable after evidence for fixes, and concise Why / How explanations.

## Select and run probes

Read [the bug checklist](references/bug-checklist.md) and choose applicable probes based on the workflow and implementation. Prioritize trust boundaries, persistent mutations, and costly or irreversible side effects. Do not run every category indiscriminately.

Establish a valid baseline first, then vary actors, inputs, ordering, timing, and failure points. Use separate sessions for separate identities. For permission checks, compare an allowed request with a forbidden one against controlled records. Exercise the API directly where authorized, since a hidden button does not establish server-side authorization.

Observe the response and resulting state. After writes, reread through an independent request or session and inspect persistence when available. A denied request must also leave protected state unchanged. Distinguish expected eventual consistency from a broken invariant using the system's stated convergence behavior.

For race conditions, coordinate a small number of overlapping operations and record their ordering, responses, and final state. For retries, test the ambiguous case where the server commits but the client never receives the response. Use deterministic failure injection or synchronization where practical; record attempts and reproduction frequency for intermittent failures.

Use source inspection to guide experiments and explain causes. Keep code-only concerns separate from runtime-confirmed defects. If one layer is inaccessible, continue useful checks in accessible layers and record the coverage gap.

## Reproduce and assess

Reduce each finding to the smallest repeatable scenario from known state. Preserve the failing evidence before fixing. Include the expected behavior and its source, actual behavior, actor and ownership context, exact steps or requests, and relevant final state. Remove credentials and private data from evidence.

Merge duplicate symptoms with the same demonstrated cause. Rank by concrete impact, affected users or records, and exploit prerequisites. Keep severity separate from confidence. Use Critical for demonstrated broad compromise or severe widespread loss, High for unauthorized access or substantial corruption or core-flow failure, Medium for bounded functional failures with recovery, and Low for minor observable defects. Explain the assigned impact; do not inflate an untested possibility into a confirmed exploit.

Track findings as Reproduced, Suspected, Fixed and verified, or Fix not verified. A reproduced intermittent defect remains a finding with its observed frequency. Do not label a fix verified solely because code changed or an unrelated suite passed.

## Verify requested fixes

When fixing is in scope, address the demonstrated cause and rerun the original reproduction using comparable conditions. Check the nearest relevant allowed and forbidden cases, state invariants, and applicable project checks. Confirm that closing an unauthorized path preserves the legitimate workflow.

Follow evidence-based-verification for before-and-after UI videos, screenshot fallback, non-UI checks, and the concise Why / How summary. Without a fix, deliver the failing evidence and mark after evidence as not applicable. If the baseline cannot be recovered, state the limitation.

## Report and stop

Use [the report template](references/report-template.md). Lead with ranked confirmed findings, followed by suspicions and coverage gaps. Keep the summary short and put reproduction details beside the linked evidence.

Finish when the selected checks and requested fix verification are complete, or report the concrete blockers when further work cannot proceed. Honor a user-specified time or action budget. If no bugs reproduce, report what was tested and what remains untested; do not claim the feature is bug-free or secure.
