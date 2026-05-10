---
title: Required Communication Performance
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["concept", "pbcs"]
---

# Required Communication Performance

> [!summary] TL;DR
> RCP specifies the communication performance an ATM operation needs — measured in transaction time, continuity, availability, and integrity. Think: "How fast and reliably must my CPDLC message complete?"

---

## What RCP measures

RCP breaks communication performance into these dimensions:

| Dimension | What it means | Example (RCP 240/D) |
|---|---|---|
| **Transaction time** | How long from pilot action to delivery confirmation | ≤ 240 seconds |
| **Continuity** | Probability the transaction completes without interruption | ≥ 99.9% |
| **Availability** | Probability the service is operational when needed | ≥ 99.99% |
| **Integrity** | Probability of undetected errors | ≤ 10⁻⁵ per flight hour |

> [!tip] Key distinction
> **RCP** = Required (what the operation needs)  
> **ACP** = Actual (what the system actually delivers, measured through monitoring)

The gap between RCP and ACP is what monitoring reveals. If ACP < RCP, corrective action is needed.

---

## RCP specification families

Not all operations need the same communication performance. Doc 9869 defines multiple specifications:

| Specification | Application | Key transaction time |
|---|---|---|
| [[RCP 240 D]] | CPDLC — controller intervention | 240 sec |
| [[RCP 400 D]] | Data-link communication | 400 sec |
| [[RCP 400 VRO]] | SATVOICE — voice relay | 400 sec |

---

## How RCP is allocated

A single RCP number is the *total* performance budget. It gets split across system components:

```
Total RCP transaction time (e.g., 240 sec)
  ├── Aircraft system processing
  ├── Air-ground data link
  ├── Ground network
  └── ATS ground system
```

Each component gets an *allocation*. The sum of allocations must not exceed the total. See [[RCP Allocation]].

> [!example] Allocation example
> For RCP 240/D in an oceanic FIR using Inmarsat Classic Aero:
> - Aircraft system: 40 sec
> - Air-ground link: 150 sec
> - Ground network: 30 sec
> - ATS system: 20 sec
> **Total: 240 sec** ✓

---

## Source basis

- Doc 9869 Chapter 2 and Appendix B define RCP specifications
- For source navigation: [[Source - ICAO Doc 9869]], [[RCP Specification]]

---

## Related notes

- [[Beginner Path]] — learning sequence
- [[Required Surveillance Performance]] — the companion for surveillance
- [[RCP 240 D]]
- [[RCP 400 D]]
- [[RCP 400 VRO]]
- [[RCP Allocation]]
- [[RCP Compliance]]
- [[RCP Monitoring]]
---

## 🧭 Where next?

⬅ Back to: [[RCP vs RSP]]

➡ Continue to: [[Required Surveillance Performance]]

📋 Return to: [[Beginner Path]] | [[Beginner Path]] | [[PBCS MOC]]
