---
title: Training Companion
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["navigation", "pbcs", "training"]
---

# Training Companion

> [!summary] What this is
> A page for instructors, team leads, and presenters. Slide-ready summaries, workshop agendas, and suggested exercises for teaching PBCS using this knowledge base.

---

## Workshop agendas

### 30-minute briefing (awareness)

| Time | Topic | Method |
|---|---|---|
| 0-3 min | What is PBCS? (TL;DR from [[Performance-Based Communication and Surveillance]]) | Presenter read-aloud |
| 3-8 min | RCP vs RSP — the two pillars | Show the comparison table from [[RCP vs RSP]] |
| 8-15 min | Who does what? | Show [[PBCS Responsibility Matrix]] table — ask "who's missing?" |
| 15-22 min | The lifecycle | Show the Mermaid diagram from PBCS overview page |
| 22-28 min | What this means for us | Discussion: which airspace do we operate in? |
| 28-30 min | Q&A + where to learn more | Point to [[Beginner Path]] and [[Quick Reference Card]] |

**Slide materials:** The TL;DR callout, RCP vs RSP table, responsibility matrix, lifecycle diagram.

---

### 60-minute deep dive (role-specific)

| Time | Topic | Method |
|---|---|---|
| 0-5 min | Agenda + objectives | Set expectations |
| 5-15 min | Beginner Path walkthrough | Presenter guides team through [[Beginner Path]] live on screen |
| 15-25 min | Role-specific deep dive | Switch to relevant [[Learning Tracks]] section — team reads their track |
| 25-35 min | Decision tree exercise | Team uses [[Choosing Your RCP-RSP Specification]] to determine which spec applies to their operation |
| 35-45 min | Capability checklist | Team runs [[Is Your Aircraft PBCS-Capable]] against their own aircraft/org |
| 45-55 min | Monitoring response drill | Team walks through [[Monitoring Shows Degradation - What Now]] for a given scenario |
| 55-60 min | Next steps + assignments | Assign [[Day 1 PBCS Action Guides]] to each role |

---

### 90-minute workshop (full implementation team)

| Time | Topic | Method |
|---|---|---|
| 0-10 min | Objectives + pre-assessment | [[PBCS Institutional Maturity Model]] — everyone finds their level |
| 10-25 min | Beginner Path | Guided tour of all 3 steps |
| 25-35 min | Breakout: role-specific reading | Groups read their [[Learning Tracks]] path |
| 35-50 min | Breakout: fill the compliance matrix | Groups fill one row each of [[PBCS Compliance Matrix Template]] |
| 50-60 min | Report back | Each group presents their row |
| 60-70 min | Walk through a case study | Read [[Case Study - Operator PBCS Approval]] aloud, discuss parallels |
| 70-85 min | Gap identification | Each group lists their top 3 gaps (per [[Day 1 PBCS Action Guides]]) |
| 85-90 min | Commitments and timeline | Each role commits to one Day 1 action, deadline set |

---

## Slide-ready key points

### Why PBCS exists (3 bullet slide)

- Before PBCS: "What equipment do you have?" ➔ locked to specific technology
- After PBCS: "What performance can you deliver?" ➔ any technology that meets the bar
- Result: objective, measurable, technology-neutral criteria for comm and surv

### RCP vs RSP (side-by-side slide)

| | RCP | RSP |
|---|---|---|
| Domain | Communication | Surveillance |
| Key metric | CTT | SDDT |
| Specs | 240/D, 400/D, 400/VRO | 180/D, 400/D, 400/VRO |
| Source | Appendix B | Appendix C |

### The five lifecycle stages (one slide)

```
1. DEVELOP → 2. APPLY → 3. PROVE → 4. MONITOR → 5. CORRECT
```

(Show Mermaid diagram from PBCS overview page)

### Stakeholder one-liners

- **State:** "Prescribe and approve"
- **ANSP:** "Implement and monitor"
- **Operator:** "Demonstrate and comply"
- **CSP/SSP:** "Provide data and support"

---

## Group exercises

### Exercise 1: "Which spec applies?"

**Setup:** Give each group an operational scenario:

| Group | Scenario |
|---|---|
| A | Oceanic FIR, 5-min separation, CPDLC + ADS-C used |
| B | Domestic en-route, radar coverage, CPDLC used |
| C | Remote polar, SATVOICE only, no data-link |

**Task:** Use [[Choosing Your RCP-RSP Specification]] to determine which RCP/RSP applies.

**Answers:** A = RCP 240/D + RSP 180/D, B = RCP 240/D (no RSP), C = RCP 400/VRO (no RSP unless position reporting).

### Exercise 2: "Find the gaps"

**Setup:** Give each group the Oceanic Airways case study from [[Case Study - Operator PBCS Approval]], but only the "Challenge" section.

**Task:** List the gaps Oceanic Airways had BEFORE reading the "Approach" section. Then compare with the actual gaps.

**Answers:** No PBCS owner, CSP data gap, MEL silence, training records gap.

### Exercise 3: "You're on call — degradation detected"

**Setup:** Present this scenario:

> "Monitoring report for March shows RCP 240/D continuity at 98.5% for flights OA123, OA124, OA126 — all on the same track, same day. Continuity threshold is 99.9%."

**Task:** Use [[Monitoring Shows Degradation - What Now]] to answer:
- Who investigates first?
- What data do you need?
- Who do you notify?
- What's the closure criteria?

---

## Assessment questions

Use these to check understanding after any session:

1. What problem does PBCS solve that prescription-based regulation couldn't?
2. Name the six PBCS stakeholders and their main responsibility.
3. Which appendix contains RCP specifications? Which contains RSP?
4. What's the difference between RCP and ACP?
5. An oceanic operation needs controller intervention within 180 seconds for 3-minute separation. Which RCP applies?
   - Answer: None — the fastest RCP is 240/D. 180-second intervention would require a new or modified specification.
6. Your monitoring shows 3 consecutive months of CTT exceeding 400 sec. What do you do first?

---

## Resources to print for sessions

- [[Quick Reference Card]] — one per participant
- [[Acronyms and Terms]] — reference sheet
- The decision tree from [[Choosing Your RCP-RSP Specification]] — one per group
- The capability checklist from [[Is Your Aircraft PBCS-Capable]] — one per aircraft type

---

## Related

- [[Beginner Path]] — the foundation
- [[Learning Tracks]] — role-specific plans
- [[Quick Reference Card]] — printable reference
- [[PBCS Institutional Maturity Model]] — pre/post assessment
- [[Verification Standards]] — trust the source
