# Deslop fallback

Use only when the installed `deslop` skill is unavailable. Review the diff for this task and remove AI-generated code slop:

- Unnecessary comments inconsistent with local style.
- Defensive checks or try/catch blocks abnormal for trusted code paths.
- Casts used only to bypass type issues.
- Deep nesting that can be simplified with early returns.
- Other patterns inconsistent with the surrounding codebase.

Keep behavior unchanged unless fixing a clear bug. Prefer minimal, focused edits over broad rewrites. Do not change unrelated work.
