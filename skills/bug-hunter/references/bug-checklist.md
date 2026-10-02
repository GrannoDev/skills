# Bug checklist

Select probes relevant to the feature. Each probe needs an expected result and an observable check. These are investigation prompts, not claims that every application needs the same controls.

## Permissions and identity

- Authorization: compare owner, peer, privileged, anonymous, and cross-tenant actors. Check object access, privileged operations, writable fields, batch endpoints, exports, and nested resources. Verify both reads and mutations.
- Identity: switch accounts and tenants, use equal display names with different stable IDs, and change ownership. Check attribution, cached identity, and background jobs acting as the wrong user.
- Authentication and sessions: exercise expiry, logout, revocation, role removal, and recovery or invitation token reuse. Check that existing sessions follow the documented policy after an identity or permission change.
- Data exposure: inspect response fields, search results, errors, logs, downloads, and cache reuse between identities for information the actor should not receive.

## Inputs and business rules

- Validation: test missing, null, empty, duplicate, malformed, oversized, and boundary values. Compare UI and API enforcement, including unknown fields and conflicting parameters.
- Workflow bypass: skip, repeat, reorder, or resume steps after cancellation or expiry. Check server-derived prices, totals, ownership, and state rather than trusting client-supplied values.
- Time and numbers: exercise timezone and daylight-saving boundaries, expiry instants, rounding, units, negative values, and range limits appropriate to the domain.
- Query correctness: check stable pagination, sorting ties, filters, empty results, and records inserted or removed between pages. Look for omissions and duplicates.
- Injection and unsafe interpretation: trace untrusted values into rendering, queries, commands, file paths, and parsers. Use harmless markers and controlled fixtures to verify interpretation without destructive payloads.

## Timing and state

- Race conditions: overlap update/update, update/delete, claim/claim, or permission-change/action requests on the same test record. Check lost updates and violations of uniqueness, inventory, or ownership.
- State synchronization: compare optimistic UI, fresh reads, other tabs, caches, and stored state. Deliver stale responses out of order and verify that they cannot overwrite newer state.
- Idempotency: replay an operation after a timeout, double submission, or reconnect. Where keys exist, test reuse with the same and different payloads and across actors. Count durable and external effects.
- Atomicity: fail between related writes or between a commit and event publication. Check for partial records, missing events, duplicate effects, and the documented recovery or compensation behavior.
- Navigation and lifecycle: exercise back/forward, deep links, reload, unmount, cancellation, and resumption during pending work. Check lost input, stale updates, and repeated submissions.

## Failures and integrations

- Failure handling: inject timeouts, disconnection, malformed responses, and dependency errors. Check truthful status, recoverability, retry bounds, and whether failure leaves state intact.
- Persistence integrity: test uniqueness and relationship constraints, deletion and soft-deletion behavior, rollback, and read-after-restart when applicable. Use disposable fixtures for schema compatibility or migration checks.
- Asynchronous delivery: duplicate, delay, reorder, or replay jobs and webhooks. Verify authenticity, deduplication, correct ownership, and recovery from worker failure.
- External trust: check handling of third-party responses, redirects, uploads, and user-supplied fetch URLs. Use controlled destinations for server-side request forgery checks; do not probe unrelated networks.
- Resource and abuse limits: test small bounded cases around documented quotas, pagination limits, upload sizes, and costly workflows. Inspect enforcement without turning a feature hunt into load testing.
- Configuration and old routes: compare alternate API versions, debug routes, cross-origin behavior, and cookie-based request protections where relevant. Confirm an observable exposure rather than reporting configuration style alone.

## Research sources

The security prompts draw on [OWASP API Security Top 10, 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/), including object and property authorization, resource consumption, unsafe integrations, and API inventory.

Workflow, replay, and concurrency checks also draw on the [OWASP Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html). The remaining prompts translate common feature invariants into practical checks; this list is not a compliance standard or exhaustive security audit.
