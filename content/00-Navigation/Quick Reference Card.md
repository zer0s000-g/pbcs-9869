---
title: Quick Reference Card
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "reference", "printable"]
---

# Quick Reference Card

> [!summary] Print this page
> Designed to print on a single sheet (Cmd+P / Ctrl+P). Bring to meetings, use for training, or keep as a desk reference. No graph required.

---

## PBCS at a glance

| | RCP (Communication) | RSP (Surveillance) |
|---|---|---|
| **Domain** | Comm (CPDLC, SATVOICE) | Surv (ADS-C) |
| **Key metric** | CTT — Comm Transaction Time | SDDT — Surv Data Delivery Time |
| **Actual measurement** | ACP | ASP |
| **Source appendix** | Appendix B (pp 93-127) | Appendix C (pp 129-151) |

---

## Specifications

| Spec | Domain | Key time | Typical use |
|---|---|---|---|
| RCP 240/D | CPDLC data-link | CTT ≤ 240 sec | Controller intervention |
| RCP 400/D | Data-link comm | CTT ≤ 400 sec | Routine data-link comm |
| RCP 400/VRO | SATVOICE voice relay | CTT ≤ 400 sec | Voice relay operations |
| RSP 180/D | ADS-C data-link | SDDT ≤ 180 sec | ADS-C position delivery |
| RSP 400/D | Data-link surv | SDDT ≤ 400 sec | Data-link surveillance |
| RSP 400/VRO | SATVOICE surv context | SDDT ≤ 400 sec | SATVOICE position reporting |

---

## Performance dimensions (all specs)

| Dimension | What it means | Typical threshold |
|---|---|---|
| Transaction/Delivery Time | How fast the transaction completes | ≤ 240 or 400 sec |
| Continuity | Probability of completing without interruption | ≥ 99.9% |
| Availability | Probability service is operational | ≥ 99.99% |
| Integrity | Probability of undetected error | ≤ 10⁻⁵ per flight hour |

---

## Stakeholders

| Actor | Main PBCS responsibility |
|---|---|
| **State** | Prescribe RCP/RSP, approve operations, oversee compliance |
| **ANSP** | Implement operation, run monitoring, coordinate corrective action |
| **Operator** | Demonstrate capability, obtain approval, maintain compliance |
| **CSP** | Provide comm service, outage data, support investigation |
| **SSP** | Provide surv service, performance data, support monitoring |

---

## PBCS lifecycle

```
DEVELOP → APPLY → PROVE → MONITOR → CORRECT → (loop back)
```

| Stage | Key question | Doc 9869 source |
|---|---|---|
| DEVELOP | What does the ATM operation need? | Chapter 2 |
| APPLY | Which RCP/RSP is prescribed? | Chapter 3 |
| PROVE | Can the operator meet the spec? | Chapter 4.2-4.4 |
| MONITOR | Does ACP/ASP match RCP/RSP? | Chapter 4.5, App D-E |
| CORRECT | Who fixes degradation and re-proves? | App D-E |

---

## Monitoring data fields

| Data category | CPDLC fields (App D) | ADS-C fields (App D) | SATVOICE fields (App E) |
|---|---|---|---|
| **Performance** | Transaction time, continuity | Data delivery time, continuity | Clearance time, position report time |
| **Availability** | Service uptime, outages | Service uptime, outages | Service uptime, outages |
| **Reporting** | Monthly report format | Monthly report format | Monthly report format |
| **Problems** | Problem report template | Problem report template | Problem report template |

---

## Operational documents

| Document | What it contains |
|---|---|
| **AIP** (Aeronautical Information Publication) | State-published PBCS requirements for specific airspace |
| **SUPP** (Regional Supplementary Procedure) | ICAO Doc 7030 — region-specific PBCS prescriptions |
| **MEL** (Minimum Equipment List) | Aircraft document — CPDLC/ADS-C dispatch relief conditions |
| **ORT** (Operational Readiness Trial) | Trial period demonstrating PBCS capability before formal approval |
| **Flight Plan** (Item 10a / 18) | Equipment codes (J2, J5) and PBN/PBCS indicators |

---

## Key Doc 9869 page references

| Chapter / Appendix | Content | PDF pages |
|---|---|---|
| Chapter 1 | PBCS framework, concepts | ~1-30 |
| Chapter 2 | RCP/RSP specification development | ~31-50 |
| Chapter 3 | Applying specifications to operations | ~51-70 |
| Chapter 4 | Approval, compliance, monitoring | ~71-92 |
| Appendix B | RCP specification tables | 93-127 |
| Appendix C | RSP specification tables | 129-151 |
| Appendix D | CPDLC/ADS-C monitoring | 153-190 |
| Appendix E | SATVOICE monitoring | 191-210 |

---

## Related ICAO documents

| Document | Relevance |
|---|---|
| Annex 10 Vol III | CPDLC, ADS-C, SATVOICE technical standards |
| Doc 4444 (PANS-ATM) | Separation minima, ATC procedures |
| Doc 7030 | Regional supplementary procedures |
| GOLD | Global operational data-link guidance |
| Doc 9613 (PBN Manual) | Navigation (RNP) — complementary to PBCS |

---

## Common acronyms

| Acronym | Full |
|---|---|
| PBCS | Performance-Based Communication and Surveillance |
| RCP | Required Communication Performance |
| RSP | Required Surveillance Performance |
| ACP | Actual Communication Performance |
| ASP | Actual Surveillance Performance |
| CTT | Communication Transaction Time |
| SDDT | Surveillance Data Delivery Time |
| CPDLC | Controller-Pilot Data Link Communications |
| ADS-C | Automatic Dependent Surveillance — Contract |
| SATVOICE | Satellite Voice Communications |
| VRO | Voice Relay Operations |
| ANSP | Air Navigation Service Provider |
| CSP | Communication Service Provider |
| SSP | Surveillance Service Provider |

---

> [!tip] More detail
> This is the quick reference. For full explanations, see:
> - [[Beginner Path]] — learning sequence
> - [[Acronyms and Terms]] — complete glossary with links
> - [[PBCS MOC]] — map of all content
> - [[Frequently Asked Questions]] — real-world answers
