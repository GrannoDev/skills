# Platform checks

Use only the relevant platform sections. Convert each applicable risk into a feature-specific scenario, deduplicating against [lenses.md](lenses.md). Propose checks here; do not run destructive or load tests without authorization.

## Frontend

| Area | Candidate risks |
| --- | --- |
| Network | Slow/offline/reconnected; 4xx/5xx/timeout; empty/malformed result; stale response arriving last; expired session. |
| Input | Empty/whitespace; long text or unbroken words; emoji/combining/RTL/mixed scripts; pasted line breaks; empty or very large lists. |
| Interaction | Repeated submission; back/reload/navigation during work; concurrent edits in tabs. |
| Accessibility | Keyboard-only use; focus/labels/announcements; larger default fonts; reduced motion; forced colors. |
| Display | Narrow/touch screens; zoom from 50% to 400%; long translations; dark mode; rendering without hardware acceleration where relevant. |

## Backend

| Area | Candidate risks |
| --- | --- |
| Requests | Missing/wrong-type/unknown fields; oversized body/upload; duplicate requests; incompatible client version. |
| Authorization | Unauthenticated calls; another user's/tenant's IDs; changed permissions. |
| Dependencies | Errors/timeouts/rate limits; null/partial/malformed data; failure after a side effect. |
| Data and load | Concurrent updates; unexpectedly large results; pagination/N+1/index problems; load sensitivity; differing timezones. |
| Errors and logs | Stack traces, SQL, internal details, personal data, or secrets exposed in responses/logs/URLs. |
