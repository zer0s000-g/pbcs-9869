---
title: Acronyms and Terms
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "glossary", "navigation"]
---

# Acronyms and Terms

> Every PBCS acronym and key term in one place. Use this as your quick decoder when reading any page in this knowledge base.

---

## Core PBCS framework

| Term | Full form | What it means | Learn more |
|---|---|---|---|
| **PBCS** | Performance-Based Communication and Surveillance | The ICAO framework for specifying, approving, and monitoring communication and surveillance using objective, measurable criteria | [[Performance-Based Communication and Surveillance]] |
| **RCP** | Required Communication Performance | The specification of communication performance an ATM operation needs (time, continuity, availability, integrity) | [[Required Communication Performance]] |
| **RSP** | Required Surveillance Performance | The specification of surveillance performance an ATM operation needs (data delivery time, continuity, availability, integrity) | [[Required Surveillance Performance]] |
| **ACP** | Actual Communication Performance | The communication performance actually delivered by the system, measured through post-implementation monitoring | [[RCP Monitoring]] |
| **ASP** | Actual Surveillance Performance | The surveillance performance actually delivered, measured through monitoring | [[RSP Monitoring]] |

---

## Performance dimensions

| Term | What it measures |
|---|---|
| **CTT** — Communication Transaction Time | How long from pilot action (or ATC initiation) to delivery confirmation at the other end |
| **SDDT** — Surveillance Data Delivery Time | How long from the aircraft measurement to delivery at the ATS ground system |
| **Continuity** | Probability that an operation completes without unscheduled interruption |
| **Availability** | Probability that the service is operational when needed |
| **Integrity** | Probability that an undetected error occurs (must be extremely low) |

---

## Communication technologies

| Term | Full form | Domain |
|---|---|---|
| **CPDLC** | Controller-Pilot Data Link Communications | Data-link text messaging between ATC and pilots | [[Data Link Services]] |
| **SATVOICE** | Satellite Voice Communications | Voice communication via satellite (replaces HF in remote/oceanic) | [[SATVOICE]] |
| **VRO** | Voice Relay Operations | SATVOICE used in a relay configuration (aircraft → satellite → ground operator → ATC) | [[RCP 400 VRO]] |

---

## Surveillance technologies

| Term | Full form | What it does |
|---|---|---|
| **ADS-C** | Automatic Dependent Surveillance — Contract | Aircraft automatically sends position reports via data link per a "contract" (periodic, event-based, or on-demand) | [[Data Link Services]] |

---

## Specification naming convention

```
RCP 240 / D         RSP 180 / D
 │    │    │          │    │    │
 │    │    │          │    │    └── D = Data-link (VRO = Voice Relay Operations)
 │    │    │          │    └─────── Data delivery time in seconds
 │    │    └──────────└──────────── Transaction / delivery time in seconds
 │    └──────────────────────────── Communication Performance (vs Surveillance)
 └───────────────────────────────── Required (vs Actual = ACP/ASP)
```

**Active specifications in this KB:**

| Spec | Applies to | Key metric | Source | Detail |
|---|---|---|---|---|
| RCP 240/D | CPDLC controller intervention | CTT ≤ 240 sec | Appendix B | [[RCP 240 D]] |
| RCP 400/D | Data-link communication | CTT ≤ 400 sec | Appendix B | [[RCP 400 D]] |
| RCP 400/VRO | SATVOICE voice relay | CTT ≤ 400 sec | Appendix B | [[RCP 400 VRO]] |
| RSP 180/D | ADS-C data-link surveillance | SDDT ≤ 180 sec | Appendix C | [[RSP 180 D]] |
| RSP 400/D | Data-link surveillance | SDDT ≤ 400 sec | Appendix C | [[RSP 400 D]] |
| RSP 400/VRO | SATVOICE surveillance context | SDDT ≤ 400 sec | Appendix C | [[RSP 400 VRO]] |

---

## Stakeholders

| Term | Full form | Main PBCS role | Detail |
|---|---|---|---|
| **State** | State Authority / Regulator | Prescribe RCP/RSP, approve operations, oversee compliance | [[State Authority]] |
| **ANSP** | Air Navigation Service Provider | Implement ATM operations, run monitoring, coordinate corrective action | [[Air Navigation Service Provider]] |
| **Operator** | Aircraft Operator | Demonstrate aircraft/operator capability, obtain approval, file correctly, maintain compliance | [[Aircraft Operator]] |
| **CSP** | Communication Service Provider | Provide contracted comm service, outage data, support investigation | [[Communication Service Provider]] |
| **SSP** | Surveillance Service Provider | Provide surveillance-related service, performance data, support monitoring | [[Surveillance Service Provider]] |

---

## Operational documents & artifacts

| Term | Full form | What it is |
|---|---|---|
| **AIP** | Aeronautical Information Publication | State publication containing PBCS requirements and procedures for specific airspace |
| **SUPP** | Supplementary Procedure | Regional ICAO procedure (Doc 7030) that may prescribe RCP/RSP for specific regions |
| **MEL** | Minimum Equipment List | Aircraft document listing equipment that may be inoperative while still dispatching — PBCS-capable aircraft must address CPDLC/ADS-C in MEL |
| **ORT** | Operational Readiness Trial | Trial period where an operator demonstrates PBCS capability before formal approval |

---

## Document sources

| Doc | Title | Relevance |
|---|---|---|
| **Doc 9869** | PBCS Manual (2nd Ed, 2017) | The primary source for this knowledge base | [[Source - ICAO Doc 9869]] |
| **Annex 10 Vol III** | Aeronautical Telecommunications — Communication Systems | Defines CPDLC, ADS-C, and SATVOICE technical standards |
| **Doc 4444** | PANS-ATM (Procedures for Air Navigation Services) | Defines separation minima and ATC procedures that PBCS enables |
| **Doc 7030** | Regional Supplementary Procedures | Region-specific PBCS requirements (e.g., NAT, APAC, AFI) |
| **GOLD** | Global Operational Data Link Document | Operational guidance for data-link implementation worldwide |

---

## Source route

- [[Doc 9869 Definitions]]
- [[Source - ICAO Doc 9869]]
- [[Doc 9869 Section Map]]
