---
title: Case Study — Operator PBCS Approval
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["case-study", "pbcs", "synthesis"]
---

# Case Study — Operator First PBCS Approval

> [!summary] What this is
> An anonymized real-world narrative of an operator going from zero to PBCS approval. Fictional names, real timelines and hurdles.

---

## Context

**Who:** Oceanic Airways — a medium-sized international carrier with 12 wide-body aircraft (mixed Boeing 777 and Airbus A350 fleet).

**Where:** Operating routes through Mumbai Oceanic FIR and Bay of Bengal.

**What changed:** The prescribing State (India) published AIP ENR 1.8 requiring RCP 240/D and RSP 180/D for reduced longitudinal separation (5-minute standard) in the Bay of Bengal. Operators without PBCS approval would be restricted to 10-minute separation tracks — adding 15-20 minutes to every crossing.

**When:** AIP effective date was 12 months out. Oceanic Airways started planning 10 months before deadline.

---

## Challenge

### What they had

| Asset | Status |
|---|---|
| CPDLC FANS 1/A avionics | ✅ Installed on all 12 aircraft |
| ADS-C capability | ✅ Installed (part of FANS 1/A package) |
| SATVOICE | ✅ Installed on 8 of 12 aircraft |
| CSP contract (Inmarsat Classic Aero) | ✅ Active but without data provision clause |
| CPDLC crew training | ⚠️ Partial — some crews trained, records incomplete |
| MEL CPDLC entry | ❌ No dispatch relief defined |
| PBCS knowledge | ❌ No formal owner, no compliance planning |

### The real blockers

1. **No PBCS owner.** "Operations handles it" and "Engineering handles it" meant no one handled it.

2. **CSP contract gap.** The Inmarsat agreement provided connectivity but no performance/outage data provision. Without this, monitoring was impossible.

3. **MEL silence.** The MEL didn't mention CPDLC at all. A pilot could dispatch with CPDLC inoperative and never know they'd violated their clearance requirements.

4. **Training records gap.** Some pilots had done CPDLC training during type rating (3 years ago). No one had records. Recurrent training had never included PBCS concepts.

---

## Approach

### Month 1-2: Foundation

- **Assigned PBCS lead** — Flight Ops Standards Captain promoted to "PBCS Programme Manager." Executive sponsor: VP Flight Operations.
- **Completed beginner path** as a team — flight ops, engineering, dispatch leads all did the 15-minute [[Beginner Path]] together.
- **AIP verification** — confirmed exact RCP 240/D and RSP 180/D requirements from India AIP ENR 1.8-12.

### Month 2-4: Gap closure

| Gap | Action | Timeline |
|---|---|---|
| MEL CPDLC entry | Engineering drafted CPDLC dispatch relief (Cat C — 10 days). Submitted to State CAA. | 8 weeks for approval |
| CSP data provision | Renegotiated Inmarsat contract. Added Appendix: monthly performance data delivery. CSP agreed — no cost increase. | 4 weeks |
| Training records | Conducted full CPDLC/PBCS training for all 180 pilots. 4-hour module including FMS simulator. Records centralized. | 6 weeks |
| Flight plan filing | Updated dispatch system — Item 10a now auto-populates J2/J5 based on aircraft registration. Dispatchers trained. | 3 weeks |

### Month 4-7: Evidence building

- Completed the [[PBCS Compliance Matrix Template]] row by row.
- Ran operational readiness trial (ORT): 15 flights through Bay of Bengal, all CPDLC transactions logged and timed.
- ORT results: average CTT 195 seconds, continuity 99.95% — well within RCP 240/D limits.

### Month 7-8: Submission

- Submitted approval application to India CAA (ATM/ANS Division).
- Package included: filled compliance matrix, ORT results, training records, MEL amendment approval, CSP data provision amendment.
- State responded within 6 weeks: approved with standard conditions (monthly monitoring for first 12 months).

### Month 8: Go-live

- Oceanic Airways operated first PBCS-compliant flight through Bay of Bengal on month 8.
- All 12 aircraft approved. 8 aircraft with SATVOICE also qualified for RCP 400/VRO contingency.

---

## Timeline summary

| Phase | Duration | What happened |
|---|---|---|
| Foundation | Months 1-2 | Owner assigned, AIP verified, team trained |
| Gap closure | Months 2-4 | MEL, CSP, training, flight plan — four blockers resolved |
| Evidence building | Months 4-7 | Compliance matrix, ORT, monitoring setup |
| Submission | Months 7-8 | Application submitted and approved |
| Go-live | Month 8 | PBCS operations live |

**Total: 8 months from zero to approval.** (Met the 12-month AIP deadline with 4 months to spare.)

---

## Key lessons

### 1. The first step is assigning an owner

Three departments assumed someone else was handling PBCS. Nothing happened until a named person was given the remit and executive backing. Day 1 action: find your PBCS owner.

### 2. The CSP contract is the hidden blocker

Oceanic Airways assumed their connectivity contract covered everything. It took the [[Is Your Aircraft PBCS-Capable]] checklist to reveal the data provision gap. This is the most common surprise for operators.

### 3. ORT data is your best evidence

The State didn't just want paperwork — they wanted actual flight data. The 15-flight ORT with real transaction times was the strongest piece of the approval package. Start logging CPDLC data early, even before you're ready to submit.

### 4. Training records must be documented, not assumed

"We trained everyone" was not sufficient. The approval required: dates, attendees, syllabus, assessment results, and recurrent schedule. Build the records as you build the training.

### 5. The 12-month AIP deadline was tight but achievable

Oceanic Airways started at month 2 (10 months before deadline) and finished at month 8. A late start (month 6 or later) would have risked missing the deadline and losing access to reduced-separation tracks.

---

## Related

- [[Is Your Aircraft PBCS-Capable]] — the checklist that revealed the gaps
- [[Operational Approval]] — the approval process
- [[PBCS Compliance Worked Example]] — the template they filled
- [[Day 1 PBCS Action Guides]] — what Oceanic Airways did on day 1
- [[PBCS Institutional Maturity Model]] — track your own journey
