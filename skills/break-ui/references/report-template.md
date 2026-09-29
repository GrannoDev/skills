# UI bug report

Order bugs by severity, then affected flow. Counts include only reproduced or observed intermittent failures. Keep reproduction steps sufficient for another person to repeat them.

```markdown
## Break UI: <app>

<n> bugs: <n> critical, <n> high, <n> medium, <n> low
Target: <environment and scope>
Angles exercised: <angles>

### 1. [<Severity>] <observable failure>
Where: <screen/URL and control>
Angle: <one or more angles>
Impact: <consequence supporting severity>
Preconditions: <test role/data/state; no secrets>
Steps:
1. <action>
Expected: <behavior and contract/source>
Actual: <observed result>
Reproduction: <repeatable or intermittent; successes/attempts>
Evidence: <screenshot paths, relevant console/network/log details>

### Not reproduced
- <finding, attempts, and uncertainty; or None.>

### Coverage
- Exercised: <screens/flows and key checks>
- Not covered: <angle/screen/check and reason; or None.>
```

With zero bugs, omit bug entries and retain Coverage. Evidence paths must refer to actual captured artifacts; do not invent screenshots or claim inaccessible checks were performed.
