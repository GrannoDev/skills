# Handback

Keep the summary short and readable. Use these headings in order; mark inapplicable items **Not applicable** and blocked items **Unavailable** with the reason.

## Why
One sentence on the problem or goal.

## What
What changed. Name tests and their results; state any unverified behavior. Note if bundled deslop was used.

**Independent verification:** Identify the verifying agent and report its pass/fail or blocked result, interface, steps, expected and observed results, and evidence. Never mark the work complete without a pass on the final implementation.

**Cleanup:** State whether temporary test resources were removed; identify any retained artifacts or blocked cleanup.

## Where
- **Code:** Key file paths.
- **Try it:** Tailscale URL and relevant route. State what was verified, whether the app is still running, and any process-lifetime limitation.
- **Ready-to-test scenario:** Identify the prepared entities by name and ID, with direct links where supported. State the relevant configuration, starting state, relationships, and test-account role. Keep the scenario and required data available after cleanup, ready for the recipient to exercise the change without prerequisite setup. Report missing setup as a blocker, not as a ready scenario.
- **Credentials:** For every application link, provide the authorized test-account username and password needed to try it. Never disclose production credentials, tokens, or personal secrets; give exact sign-in or safe credential-retrieval instructions instead when credentials cannot be shared. Explicitly state if no sign-in is required. If access is unavailable, say why rather than inventing credentials.
- **Step-by-step guide:** For every application link, give numbered steps to open it, connect to Tailscale if needed, sign in, open the prepared entities, and exercise the relevant flow from their ready-to-test starting state. Do not make the recipient create or configure prerequisite entities. Include necessary inputs and the expected visible result so the recipient can verify the change without guessing.
- **Phone:** Display the QR image for the exact URL when possible; otherwise link its accessible artifact path. For non-UI work, mark not applicable.
- **Screenshots:** Link labeled before and after images for applicable UI work; explain any missing image.

## What I need from you
Number any actions needed to unblock or test the work. If none, write “Nothing needed from you right now” and say whether the work is finished.
