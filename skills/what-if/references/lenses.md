# General edge-case lenses

Turn applicable risks into concrete scenarios using this feature's real fields and states. These are candidate generators, not a requirement to ask every question. Deduplicate against [checklist.md](checklist.md).

| Lens | Candidate risks |
| --- | --- |
| Boundaries | Zero/one/many; minimum/maximum and adjacent values; inclusive/exclusive cutoffs; final pagination page. |
| Data shape | Missing/null/wrong-type values at external boundaries; duplicates/casing; unexpected ordering. |
| Time | Exact expiry; work spanning a deadline; midnight/month/year/leap-day boundaries; daylight saving gaps/repeats; clock skew. |
| Lifecycle | First run; partial writes/retries; repeated actions; old records/migrations; deletion/archive during use; undo/cancel. |
| Concurrency | Stale reads; duplicate/out-of-order/missing events; background work racing with edits. |
| Dependencies | Quotas; timeout; missing/locked files; disk full. |
| Permissions | Role changes mid-flow; user-controlled data entering SQL/HTML/shell/path/template boundaries. |
| Numbers and money | Rounding; floating point; currency precision; negative totals after credits; locale decimal separators. |
| Configuration | Flags changing mid-session; missing/invalid config; differing languages/locales. |
