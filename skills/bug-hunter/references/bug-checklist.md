# Bug checklist

Select applicable probes with a contract-backed expected result and observable check.

| Area | Probe and assertion |
| --- | --- |
| Authorization | Compare owner, peer, privileged, anonymous, and cross-tenant reads/writes; include writable fields, batches, exports, nested records. Forbidden calls must not change protected state. |
| Identity/sessions | Switch accounts/tenants; equal display names with distinct IDs; ownership/role changes; expiry/logout/revocation/token replay. Check cache/job attribution and documented session policy. |
| Exposure | Inspect fields, searches, errors, logs, downloads, and caches across identities for unauthorized data. |
| Validation | Missing/null/empty/duplicate/malformed/oversized/boundary inputs; unknown/conflicting fields. Compare UI/API enforcement. |
| Business rules | Skip/repeat/reorder/resume steps after cancel/expiry; challenge client-supplied totals, prices, owner, and state. |
| Time/numbers/queries | Expiry/DST/timezones, rounding/units/negative/range limits; stable pagination, tie ordering, filters, insertion/removal between pages. |
| Interpretation | Harmless markers through HTML/SQL/commands/paths/parsers; controlled fetch destinations and uploads. Do not probe unrelated networks. |
| Races/stale state | Overlap update/update, update/delete, claim/claim, permission/action; deliver stale responses last. Verify uniqueness/inventory/ownership and fresh reads across UI/cache/storage. |
| Retries/events | Replay timed-out writes, idempotency keys with same/different payloads and actors, duplicate/delayed/reordered jobs/webhooks. Verify authenticity, ownership, deduplication, and effect counts. |
| Atomicity/persistence | Fail between writes or commit/publication; check rollback/recovery, constraints, deletion, restart reads, and disposable migration fixtures. |
| Failures/lifecycle | Offline/timeouts/malformed dependencies, navigation/unmount/cancel/resume during work. Check truthful status, retained input/state, recovery, and bounded retries. |
| Limits/configuration | Small quota/upload/pagination cases; alternate API/debug routes, cross-origin and cookie protections. Require observable exposure; avoid load tests. |

Security references: [OWASP API Top 10](https://api-security.owasp.org/editions/2023/en/0x11-t10/) and [Business Logic Security](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html). These are feature probes, not a compliance audit.
