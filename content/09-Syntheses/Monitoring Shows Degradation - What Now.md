---
title: Monitoring Shows Degradation — What Now
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "decision-tree", "synthesis"]
---

# Monitoring Shows Degradation — What Now?

> [!summary] TL;DR
> Your post-implementation monitoring just flagged a problem. Who do you call first? What data do you need? This decision tree walks you through the exact sequence.

---

## The degradation response tree

```
START: Your monitoring report shows degradation.
       Which metric is affected?
        │
        ├── Transaction Time / Data Delivery Time exceeded
        │      │
        │      └── Is this a single event or a pattern?
        │             │
        │             ├── SINGLE EVENT → Log it.
        │             │     If no recurrence in 7 days → No action needed.
        │             │     Document in monitoring report as anomaly.
        │             │
        │             └── RECURRING PATTERN → Go to STEP A: Isolate component
        │
        ├── Continuity below threshold
        │      │
        │      └── Go to STEP A: Isolate component (disconnections = link issue)
        │
        ├── Availability below threshold
        │      │
        │      └── Is the outage scheduled or unscheduled?
        │             │
        │             ├── SCHEDULED (e.g., satellite maintenance) → Not a degradation.
        │             │     Document as planned outage. Ensure operators were NOTAM'd.
        │             │
        │             └── UNSCHEDULED → CSP must investigate. Go to STEP B.
        │
        ├── Integrity alert triggered
        │      │
        │      └── 🚨 CRITICAL. Immediately:
        │             1. Notify State authority
        │             2. Suspend affected operations if safety-impacting
        │             3. Isolate: aircraft, link, or ground system?
        │             4. Root cause analysis (mandatory)
        │             5. Do not resume until verified clean for 30 days
        │
        └── Multiple metrics degraded simultaneously
               │
               └── Likely a systemic issue (CSP outage, ATS system failure).
                  Go to STEP B: Notify and coordinate.


STEP A: Isolate which component
────────────────────────────────
Which part of the chain is failing?
  │
  ├── Aircraft system? → Operator investigates.
  │     Check: FMS logs, pilot reports, avionics self-test
  │     If confirmed → Operator fixes (maintenance, software update)
  │
  ├── Air-ground link? → CSP investigates.
  │     Check: satellite logs, ground earth station data, link budget
  │     If confirmed → CSP restores or provides outage timeline
  │
  ├── Ground network? → CSP / ANSP investigates.
  │     Check: AFTN/AMHS logs, routing delays, ground-to-ground latency
  │     If confirmed → CSP/ANSP resolves routing issue
  │
  └── ATS ground system? → ANSP investigates.
        Check: FDP/controller workstation logs, system performance data
        If confirmed → ANSP maintenance/engineering resolves


STEP B: Notify and coordinate
──────────────────────────────
Who needs to know, and when?

   ┌─────────────────────────────────────────────┐
   │  IMMEDIATE (within 24 hours)                 │
   │  ├── ANSP monitoring team                    │
   │  ├── Affected CSP/SSP                        │
   │  └── Regional monitoring programme (if part) │
   ├─────────────────────────────────────────────┤
   │  WITHIN 72 HOURS                             │
   │  ├── Affected operators                      │
   │  └── State authority (if safety-significant) │
   ├─────────────────────────────────────────────┤
   │  NEXT SCHEDULED REPORT                       │
   │  └── Document in regular monitoring report   │
   └─────────────────────────────────────────────┘
```

---

## By stakeholder: your immediate actions

### If you are the Operator and you notice the degradation

1. Check your own aircraft data first — was this your equipment?
2. Pull FMS logs for the affected flights
3. Contact your CSP: "We see transaction times exceeding 240 sec on flights OA123-OA126. Can you check link performance for those times?"
4. File a problem report using the format in [[Problem Reporting]]
5. If safety-impacting: notify the ANSP and State immediately
6. Do not operate in PBCS airspace until the issue is resolved or you have alternate means of compliance

### If you are the ANSP and monitoring flags the issue

1. Verify the data — is this a measurement error or a real degradation?
2. Identify which operator(s) and which airspace are affected
3. Contact the operator(s) and CSP simultaneously
4. If multiple operators affected → likely CSP issue; if single operator → likely operator issue
5. If safety-impacting: coordinate with State authority on operational restrictions
6. Lead the corrective action coordination

### If you are the CSP and an operator contacts you

1. Pull link performance data for the reported time window
2. Check for scheduled maintenance (should have been NOTAM'd)
3. If your fault: provide an estimated restoration time and root cause
4. If not your fault: provide data showing your link was nominal (points investigation elsewhere)
5. Support the operator and ANSP with investigation data

---

## Closure criteria: when is it "fixed"?

| Severity | Closure requirement |
|---|---|
| **Single anomaly** | No recurrence for 7 days |
| **Recurring non-safety degradation** | 14 consecutive days meeting spec |
| **Safety-significant degradation** | 30 consecutive days meeting spec + State acceptance |
| **Integrity alert** | Root cause analysis complete + 30 days clean + State re-approval |

> [!warning] Don't declare "fixed" too early
> The most common corrective action error: declaring the issue resolved after one day of good data. The closure period is designed to confirm stability, not just a lucky day.

---

## Problem reporting template

Use this format when filing a PBCS problem report:

```
PROBLEM REPORT — PBCS MONITORING

Date identified: [YYYY-MM-DD]
Reported by: [Name, Organization]
Affected operation: [Airspace, Route, Flight numbers]
Specification affected: [RCP 240/D, RSP 180/D, etc.]

Metric degraded:
  [ ] Transaction Time / Data Delivery Time
  [ ] Continuity
  [ ] Availability
  [ ] Integrity

Description of degradation:
[What was observed, when, on which flights]

Suspected component:
[ ] Aircraft system
[ ] Air-ground data link
[ ] Ground network
[ ] ATS ground system
[ ] Unknown — investigation needed

Data attached:
[List of logs, reports, screenshots]

Investigation owner: [Name, Organization]
Estimated resolution date: [YYYY-MM-DD]

Safety significance: [YES / NO]
If YES, State notified on: [YYYY-MM-DD]
```

> **Source:** Doc 9869 Appendices D and E. See [[Problem Reporting]] for the full framework.

---

## Related

- [[Corrective Action]] — the full framework
- [[Post-Implementation Monitoring]] — the monitoring programme
- [[Problem Reporting]] — report format and workflow
- [[PBCS Responsibility Matrix]] — who owns what
