---
name: do-work
description: Investigate a bug fix or feature with 1-3 exploratory agents, present a fixed concise plan for approval, then implement and deliver evidence plus a working try-it link.
---

# Do work

Input: `/do-work <bug fix or feature>` or `$do-work <request>`, according to the host's supported invocation syntax.

## 1. Explore

Read repository instructions and the relevant code. Send **1-3 exploratory agents** before presenting a plan, including for small bugs. Use one for a local change, two for separate behavior and contract investigations, and three when another affected domain needs investigation.

Give each agent a distinct question, scope, and read-only assignment. Require file:line evidence, current behavior, affected domains/contracts, verification options, and unresolved facts. They must not edit code, spawn more agents, or operate a shared UI session. The main agent owns reproduction and evidence capture. If delegation is unavailable, disclose it and perform the same investigation yourself.

Check their findings against the code. Reproduce bugs before proposing a fix; distinguish observations from hypotheses if reproduction is blocked. Read [delivery requirements](references/delivery.md) and capture applicable before evidence while the original behavior still exists. For features, establish the expected behavior and current baseline. Resolve only questions that materially change the plan.

## 2. Plan and wait

Use [the full plan](references/plan.md) for features and substantial bugs. Use [the small-bug plan](references/small-bug-plan.md) only when the cause is reproduced, the fix is local to one domain, there are no contract changes, and there is no meaningful design choice. Security, authorization, and data migration changes always use the full plan.

Follow the chosen template's exact fields and order. Keep every field; write `None` where appropriate. Merge exploration into the plan instead of appending agent reports.

**Approval rule:** Present the plan and wait for the user's confirmation before implementation. Invocation authorizes investigation, not approval of an unseen plan. End with the template's approval question and explanation quoting this rule and linking to the actual `SKILL.md`. A missing answer is not approval. If the user explicitly waived plan approval for this task, present the plan and proceed.

On feedback, revise the same template. On confirmation, carry out the approved plan. Do not ask again for routine implementation choices; obtain confirmation for material changes to behavior, domains, contracts, or trade-offs.

## 3. Implement and verify

The main agent implements the work. Preserve unrelated changes and follow established repository patterns. Check each substantial unit before building on it. Verify the actual changed behavior against the plan's acceptance criteria and run the relevant regression checks. Record failures, skipped checks, and remaining unknowns.

Capture after evidence and prepare the working demo using [delivery requirements](references/delivery.md). Before finishing, open the try-it link and exercise the intended flow. Keep its runtime available for the user. Resume interrupted work from the approved plan and existing artifacts; recapture evidence only when stale. If the original baseline is lost, report it instead of labeling the changed state as before.

## 4. Deliver

Use [the completion template](references/completion.md). Report verified behavior, link the required evidence and actual files, and finish with the working try-it link. If a required check, capture, or demo is blocked, state the missing deliverable and reason; finish all independent work and do not claim full completion.
