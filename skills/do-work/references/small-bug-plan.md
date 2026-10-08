# Small-bug plan

Use only for a reproduced bug with a local fix in one domain, no contract changes, and no meaningful design choice. Maximum 100 words, excluding link targets. Keep these three rows in order. Evidence and demo requirements still apply.

## Template

### Small bug

| Field | Plan |
| --- | --- |
| Cause | [Trigger and why the current code fails, with a link to the responsible file/line.] |
| Fix | [The minimal change and affected domain, with a file link.] |
| Verification and delivery | [Concrete expected result and targeted check; required before/after evidence and try-it entry point. For a remote box, name Tailscale or Cloudflare Tunnel.] |

Approve this fix?

The [do-work skill](<absolute path to this skill's SKILL.md>) says "Present the plan and wait for the user's confirmation before implementation."

Replace the approval-rule link with the actual installed `SKILL.md` path. If investigation reveals a contract change or design choice, switch to the full plan before implementation.
