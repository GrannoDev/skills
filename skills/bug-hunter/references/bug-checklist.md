# Bug checklist

Select checks relevant to the feature, with an expected result from its contract. Use normal app operations and existing test harnesses with controlled accounts, records, and dependencies.

| Area | Check and assertion |
| --- | --- |
| Permissions | Compare allowed and denied reads/writes using supplied test accounts, including separate owners or tenants when relevant. Check APIs as well as UI controls. Denied writes must leave records unchanged. |
| Identity/sessions | Switch test accounts, change roles, log out, and expire sessions through fixtures. Check documented access rules, cache isolation, and job attribution. |
| Validation | Test missing, empty, duplicate, malformed, and boundary values; compare UI/API results. Exercise size limits with small fixtures. |
| Business rules | Repeat, reorder, cancel, and resume steps. Check totals, ownership, and state transitions against the contract. |
| Time/numbers/queries | Check timezones, expiry, rounding, units, range limits, sorting ties, pagination, and records changing between pages. |
| Rendering/files | Use plain text and project file fixtures to check escaping, filenames, upload validation, and download results. |
| Races/stale state | Coordinate a few overlapping updates or claims; deliver stale responses last. Check final values, uniqueness, inventory, and fresh reads. |
| Retries/events | Retry a timed-out write; vary idempotency keys and payloads. Duplicate or reorder mock jobs/events. Count stored changes and mocked external effects. |
| Atomicity/persistence | Inject failures through test hooks between related writes. Check rollback, constraints, deletion, restart reads, and disposable migration fixtures. |
| Failures/lifecycle | Simulate offline, timeouts, and malformed dependency responses. Navigate, cancel, and resume pending work. Check truthful status, retained input, recovery, and bounded retries. |
