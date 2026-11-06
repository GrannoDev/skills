---
name: climb
description: Implement a Jira ticket or work description and deliver a testable result.
argument-hint: "<Jira ticket, URL, or work description>"
disable-model-invocation: true
---

# Climb

1. Read the request and project instructions. For Jira, use available integrations or authenticated access to read the ticket and relevant acceptance criteria; never guess its contents. If essential requirements or access are missing, ask for them. Inspect the working tree and preserve unrelated changes.
2. Inspect the affected code and setup. For a bug, reproduce it before fixing; if reproduction is blocked, report why. For an applicable UI change, capture a baseline screenshot before editing, or record why it was unavailable.
3. Implement the smallest clean solution and relevant tests. Do not add code comments. Follow project conventions and do not alter unrelated work.
4. Run the installed `deslop` skill on the work from this task. If unavailable, run the bundled [deslop instructions](references/deslop.md) instead and say so in the handback. Preserve behavior and unrelated changes.
5. Run relevant tests and exercise the changed behavior after deslop. For applicable UI changes, capture a matching after screenshot at native resolution with the same viewport, state, and representative data as the baseline. Save evidence outside the repository or in its designated artifact directory; exclude secrets and personal data.
6. For work testable through an application, start it using the project's documented development setup and keep it running for handback. Expose only to the tailnet: prefer binding to the Jetson's Tailscale IP; use Tailscale Serve only if it will not overwrite existing configuration. Never use Funnel, disable authentication, or expose sensitive data. Verify the actual URL responds on the Tailscale endpoint and exercise the relevant flow where possible; distinguish local verification from access verified on another device. For UI work, generate a scannable QR code for that exact URL locally, without a third-party service, and include the image or its accessible artifact path.
7. Finish using the [handback template](references/handback.md). Never invent a URL, screenshot, QR code, test result, or verification. If a dependency, access, process lifetime, safe exposure, or verification is blocked, report what was attempted and what is needed instead of claiming success.
