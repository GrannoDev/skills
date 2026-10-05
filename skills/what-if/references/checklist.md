# Edge-case checklist

Choose feature-specific scenarios; these are prompts, not mandatory coverage. Propose destructive/load checks only with authorization.

| Area | Concrete cases |
| --- | --- |
| Boundaries/data | Zero/one/many; min/max and adjacent values; inclusive/exclusive cutoff; missing/null/wrong-type; duplicates/casing/order; final pagination page |
| Time/money | Exact expiry, deadline crossing, midnight/month/year/leap day, DST gap/repeat, skew; rounding/currency precision/negative credits/locale decimals |
| Lifecycle | First run, old records/migrations, partial writes/retry, undo/cancel/delete/archive during use |
| Concurrency | Stale reads/responses arriving last, double submission, two-tab edits, duplicate/out-of-order/missing events |
| Dependencies/config | Offline/reconnect, errors/timeouts/quotas, null/partial/malformed data, failure after effects, locked files/disk full, invalid config, flags/locales changing mid-session |
| Permissions | Anonymous/cross-user/cross-tenant requests, role/session changes, untrusted SQL/HTML/shell/path/template values |
| UI input/display | Whitespace/long/unbroken text, emoji/combining/RTL/paste; small/touch screens, 50%-400% zoom, long translations, dark mode, rendering fallback |
| UI accessibility | Keyboard-only use, focus/labels/announcements, large fonts, reduced motion, forced colors |
| API/data | Missing/unknown/conflicting fields, oversized bodies/uploads, incompatible clients, pagination/N+1/index/large-result behavior |
| Exposure | Errors/logs/URLs exposing stack traces, SQL, personal data, or secrets |
