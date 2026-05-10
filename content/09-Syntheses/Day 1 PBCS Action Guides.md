---
title: Day 1 PBCS Action Guides
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "synthesis"]
---

# Day 1 PBCS Action Guides

> [!summary] TL;DR
> You've been told "we're doing PBCS." What do you actually DO on day one? These guides give you the concrete first steps for your role. No theory — just action.

---

## ✈️ Operator Day 1

**Your situation:** You operate in (or plan to operate in) airspace requiring PBCS. You need to get approved.

### Immediate actions (today)

1. **Pull your MEL**
   - Does it have a CPDLC entry?
   - Does it define dispatch relief conditions?
   - If not, contact your engineering/maintenance department. This is a blocker.
   - Source: [[Operational Approval]], [[Is Your Aircraft PBCS-Capable]] Branch 2

2. **Check your CSP contract**
   - Find your satellite communication service agreement
   - Does it include a data provision clause? (CSP must provide performance and outage data)
   - If not, contact your CSP account manager. Without this, monitoring is impossible.
   - Source: [[CSP SSP Checklist]], [[Is Your Aircraft PBCS-Capable]] Branch 4

3. **Pull last month's CPDLC logs** (if you already operate CPDLC)
   - You need a baseline of your current actual communication performance
   - Transaction times, continuity, availability
   - If you can't pull these, figure out how. You'll need this capability for monitoring.
   - Source: [[Data Collection]], [[Post-Implementation Monitoring]]

### First week actions

- [ ] Complete the [[Beginner Path]] (your entire flight ops/dispatch team)
- [ ] Identify which airspace you operate in that requires PBCS (check AIP)
- [ ] Start filling in the [[PBCS Compliance Matrix Template]] — just the "operator" rows
- [ ] Review crew training records — who has CPDLC training on file?
- [ ] Check your flight plan filing system: do you file Item 10a codes J2/J5 correctly?
- [ ] Assign a PBCS owner in your flight ops department

### Don't do this

> [!warning] Don't submit an approval application without evidence
> States reject incomplete packages. Build your evidence first.

> [!warning] Don't assume your aircraft is ready
> Having CPDLC installed ≠ PBCS-capable. Run the [[Is Your Aircraft PBCS-Capable]] checklist.

---

## 🛠️ ANSP Day 1

**Your situation:** Your airspace requires PBCS (or will require it), and you're responsible for implementation and monitoring.

### Immediate actions (today)

1. **Verify your AIP ENR section**
   - Pull your current AIP ENR 1.8 (or equivalent)
   - Does it prescribe a specific RCP/RSP?
   - Is it current? When was it last updated?
   - If missing or outdated, flag it to your AIS/AIM department.
   - Source: [[APAC PBCS Regulatory Mapping]], [[Choosing Your RCP-RSP Specification]]

2. **Check your monitoring feed**
   - Is your ATS system collecting CPDLC/ADS-C performance data?
   - Can you extract: transaction times, continuity, availability, problem reports?
   - If you can't extract this data, contact your ATM engineering team. Monitoring cannot run without it.
   - Source: [[Monitoring Programme]], [[Data Collection]]

3. **Identify your corrective action owner**
   - When monitoring shows degradation, who investigates?
   - Do you have a named person or team?
   - If not, assign one now. "We'll figure it out when it happens" leads to regulatory findings.
   - Source: [[Corrective Action]], [[Monitoring Shows Degradation - What Now]]

### First week actions

- [ ] Join the regional PBCS coordination group (APAC TF, NAT CMG, or equivalent)
- [ ] Coordinate with neighbouring FIRs on specification alignment
- [ ] Review your ANSP-specific checklist: [[ANSP Implementation Checklist]]
- [ ] Set up a monthly monitoring data pull — even if manually, start collecting
- [ ] Draft the corrective action process — who gets notified, in what order, within what timeframe
- [ ] Survey operators using your airspace: who already has PBCS approval? Who needs it?

### Don't do this

> [!warning] Don't prescribe a spec without operator consultation
> If operators in your airspace can't meet RCP 240/D yet, don't prescribe it without a transition plan.

> [!warning] Don't set up monitoring after operations begin
> The most common ANSP gap: approving operations with no monitoring programme in place. Build both simultaneously.

---

## 🏛️ State Authority Day 1

**Your situation:** Your State needs to prescribe PBCS requirements and oversee approvals and compliance.

### Immediate actions (today)

1. **Audit your current PBCS prescriptions**
   - What RCP/RSP specifications has your State already published?
   - Where are they published? (AIP, regulation, directive)
   - Are they consistent with Doc 9869 and the latest regional SUPPs?
   - Source: [[Applying RCP RSP Specifications]], [[State Authority]]

2. **Check your approval backlog**
   - How many operators have PBCS approval applications pending?
   - How long have they been pending?
   - Do you have a documented approval process?
   - If there's a backlog, prioritize clearing it.
   - Source: [[Operational Approval]]

3. **Identify your regional obligations**
   - Which regional PBCS coordination groups is your State in?
   - Are there SUPPs (Doc 7030) that bind your State?
   - Are you meeting your reporting obligations?
   - Source: [[ICAO Interoperability Map]], [[APAC PBCS Regulatory Mapping]]

### First week actions

- [ ] Review the [[Beginner Path]] and [[Quick Reference Card]] with your ATM/ANS division
- [ ] Map your State's airspace blocks to the applicable RCP/RSP (per Doc 7030)
- [ ] Verify your AIP is current — if not, start the update process
- [ ] Contact neighbouring States about approval recognition (bilateral/multilateral)
- [ ] Assign a PBCS oversight officer
- [ ] Review your State's safety oversight obligations for PBCS (per Doc 9869 Chapter 4)
- [ ] Establish a regular reporting cadence to the regional PBCS coordination group

### Don't do this

> [!warning] Don't copy another State's AIP entry verbatim
> Your airspace, traffic mix, and operator base are unique. Adapt, don't copy.

> [!warning] Don't approve operations without requiring monitoring participation
> An approval without a monitoring obligation is a compliance gap waiting to happen.

---

## 🔑 The first-day universal rule

Regardless of your role, the most important Day 1 action is the same:

> **Find out who owns PBCS in your organization.**

If there's no owner, nothing happens. The rest of these guides assume an owner exists. If you're reading this and no one has been assigned… congratulations, you just became the owner.

---

## Your current maturity level

Not sure where you are on the journey? Check the [[PBCS Institutional Maturity Model]]:
- Level 1-2: Focus on the "Immediate actions" — awareness and planning
- Level 2-3: Focus on "First week actions" — building evidence
- Level 3-4: You should be operational — focus on monitoring and corrective action
- Level 4-5: Focus on automation and improvement

---

## Related

- [[PBCS Institutional Maturity Model]] — assess your organization's level
- [[Is Your Aircraft PBCS-Capable]] — full capability checklist
- [[Monitoring Shows Degradation - What Now]] — corrective action response
- [[Implementation Path]] — end-to-end sequence
- [[Learning Tracks]] — role-specific training plans
