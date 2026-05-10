---
title: Required Surveillance Performance
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "concept"]
---

# Required Surveillance Performance

> [!summary] TL;DR
> RSP specifies the surveillance performance an ATM operation needs — measured in data delivery time, continuity, availability, and integrity. Think: "How fast and reliably must my ADS-C position report arrive?"

---

## What RSP measures

RSP breaks surveillance performance into the same dimensions as RCP, applied to surveillance data:

| Dimension | What it means | Example (RSP 180/D) |
|---|---|---|
| **Data delivery time** | How long from measurement to delivery at ATS unit | ≤ 180 seconds |
| **Continuity** | Probability the data delivery completes without interruption | ≥ 99.9% |
| **Availability** | Probability the surveillance service is operational | ≥ 99.99% |
| **Integrity** | Probability of undetected errors in surveillance data | ≤ 10⁻⁵ per flight hour |

> [!tip] Key distinction
> **RSP** = Required (what the operation needs)  
> **ASP** = Actual (what the system actually delivers, measured through monitoring)

---

## RSP specification families

| Specification | Application | Key data delivery time |
|---|---|---|
| [[RSP 180 D]] | ADS-C — data-link surveillance | 180 sec |
| [[RSP 400 D]] | Data-link surveillance | 400 sec |
| [[RSP 400 VRO]] | SATVOICE — voice relay surveillance context | 400 sec |

---

## How RSP is allocated

Like RCP, the total RSP budget is split across the surveillance chain:

```
Total RSP data delivery time (e.g., 180 sec)
  ├── Aircraft system (measurement + processing)
  ├── Air-ground data link
  ├── Ground network (CSP)
  └── ATS ground system processing
```

See [[RSP Allocation]] for detailed component allocations.

> [!example] Allocation example
> For RSP 180/D using ADS-C over Iridium:
> - Aircraft measurement/processing: 30 sec
> - Air-ground link: 110 sec
> - Ground network: 20 sec
> - ATS processing: 20 sec
> **Total: 180 sec** ✓

---

## RCP vs RSP — when do you need both?

Many operations need both RCP and RSP:

| Operation type | RCP? | RSP? | Notes |
|---|---|---|---|
| CPDLC only (no reduced separation) | ✓ | ✗ | State may only require comm |
| ADS-C for separation reduction | ✓ | ✓ | Both needed — comm for clearance, surv for position |
| SATVOICE position reporting | ✓ | ✓ | Voice relay comm + position data delivery |
| Pre-departure clearance (PDC) | ✓ | ✗ | Comm only, no surveillance dimension |

> [!note]
> Always check your specific State/regional requirements. Some States prescribe both even when Doc 9869 only requires one.

---

## Source basis

- Doc 9869 Chapter 2 and Appendix C define RSP specifications
- For source navigation: [[Source - ICAO Doc 9869]], [[RSP Specification]]

---

## Related notes

- [[Beginner Path]] — learning sequence
- [[Required Communication Performance]] — the companion for communication
- [[RSP 180 D]]
- [[RSP 400 D]]
- [[RSP 400 VRO]]
- [[RSP Allocation]]
- [[RSP Compliance]]
- [[RSP Monitoring]]
