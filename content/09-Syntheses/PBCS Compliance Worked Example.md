---
title: PBCS Compliance Worked Example
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "synthesis"]
---

# PBCS Compliance Worked Example

> [!summary] What this is
> A fully worked example of a PBCS compliance matrix for a fictional ANSP implementing RCP 240/D in oceanic airspace. Use this as a model when filling in your own [[PBCS Compliance Matrix Template]].

---

## Scenario

| Element | Value |
|---|---|
| **Operation** | Oceanic FIR, reducing longitudinal separation from 10 min to 5 min using CPDLC |
| **Specification** | RCP 240/D (Appendix B, Doc 9869 PDF pp 93-127) |
| **Airspace** | Mumbai Oceanic FIR (fictional) |
| **Service provider** | Inmarsat Classic Aero (CSP) |
| **State** | India (fictional assignment) |
| **Operator** | Oceanic Airways Flight OA123 (fictional) |
| **Status** | Pre-operational — preparing approval package |

---

## Filled compliance matrix

| Compliance item | Doc 9869 source route | Applicable actor | Evidence to attach | Status | Owner | Review date |
|---|---|---|---|---|---|---|
| Applicable ATM operation identified | Chapter 1 sections 1.4-1.6; Chapter 3 section 3.2 | State / ANSP | Mumbai FIR AIP ENR 1.8 (PBCS requirements), Doc 9869 section 3.2 operational concept | ✅ Done | ANSP ATS Planning | 2026-01-15 |
| Applicable RCP specification selected | Chapter 2; Appendix B | State / ANSP / operator | RCP 240/D specification table (Appendix B Table B-1), State letter prescribing RCP 240/D for Mumbai FIR | ✅ Done | State CAA — ATM Division | 2026-02-01 |
| Applicable RSP specification selected | Chapter 2; Appendix C | State / ANSP / operator | **Not required** — radar coverage exists, ADS-C not prescribed for this operation | N/A | — | — |
| RCP component criteria checked | Appendix B; [[Appendix B RCP Table Verification]] | ANSP / operator / CSP / aircraft system | Component allocation evidence: aircraft 40 sec, air-ground 150 sec, ground network 30 sec, ATS 20 sec = 240 sec total. Aircraft system compliance per RTCA DO-306. Ground network SLA with CSP. | ✅ Done | ANSP + Operator + CSP | 2026-02-10 |
| Operational approval evidence available | Chapter 4 sections 4.2-4.4 | State / operator | Operator training records (CPDLC procedures), MEL revision (CPDLC dispatch relief), ORT plan (10 flights), flight plan filing procedures | 🔄 In progress | Operator — Flight Ops | 2026-03-01 |
| Flight plan requirements implemented | Chapter 4 section 4.4 | operator / ANSP | Flight plan Item 10a: J2 (CPDLC FANS 1/A) and Item 18: PBN/PBCS indicators. Dispatch checklist updated. | 🔄 In progress | Operator — Dispatch | 2026-03-01 |
| Monitoring programme established | Chapter 4 section 4.5; Appendices D/E | ANSP / regional monitor / operator / CSP | Monitoring fields selected (Appendix D Table D-1: transaction time, continuity, availability). Data feed from CSP agreed. Monthly reporting cadence. Regional monitoring coordination via APAC PBCS TF. | 🔄 In progress | ANSP — ATM Monitoring | 2026-03-15 |
| Corrective-action process established | Appendices D/E problem reporting sections | all stakeholders | Problem report template created. Escalation: operator identifies → ANSP investigates → CSP provides data → State notified if safety-impacting. Closure criteria: 30 consecutive days meeting RCP 240/D. | 🔄 In progress | ANSP — Safety | 2026-03-15 |

---

## Key decisions documented

> [!note] Why RSP was not prescribed
> Mumbai FIR has secondary surveillance radar (SSR) coverage above FL290. ADS-C is available but not required for separation. The State determined RSP 180/D is not needed for this airspace based on radar coverage. However, operators with ADS-C may still use it voluntarily — it just won't be a compliance requirement.

> [!note] Why RCP 240/D was chosen over RCP 400/D
> CPDLC is used for controller intervention capability (route changes, altitude changes). The ATM safety assessment determined that a 240-second transaction time is needed to maintain safe separation at 5-minute intervals. RCP 400/D would not provide adequate intervention time.

---

## Lessons from this example

1. **Start with the ATM operation, not the spec.** The need for 5-min separation drove the choice of RCP 240/D — not the other way around.

2. **Not every row needs to be filled.** RSP was deliberately marked N/A. The compliance matrix should reflect real requirements, not a bureaucratic checklist.

3. **Evidence is specific, not generic.** "Training records" isn't enough — the matrix says which training (CPDLC procedures), which MEL provision (dispatch relief), and how many ORT flights (10). Specificity is what makes it auditable.

4. **Monitoring is designed during approval, not after.** The monitoring fields, data feed, reporting cadence, and regional coordination are all specified *before* the first flight.

5. **Corrective action has closure criteria.** "We'll fix it" is not a process. "30 consecutive days meeting RCP 240/D" is.

---

## Related notes

- [[PBCS Compliance Matrix Template]] — the blank template to fill in
- [[PBCS Evidence Ladder]] — how claims trace to evidence
- [[Implementation Path]] — the full implementation sequence
- [[Appendix B RCP Table Verification]]
