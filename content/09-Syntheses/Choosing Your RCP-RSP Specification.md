---
title: Choosing Your RCP-RSP Specification
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "synthesis"]
---

# Choosing Your RCP/RSP Specification

> [!summary] TL;DR
> Not sure which specification applies to your operation? Answer these questions and follow the branches. You'll end up at the right RCP and RSP.

---

## Part 1: Which RCP specification?

```
START: Do you use CPDLC for controller intervention?
        │
        ├── YES → Do you need ≤ 240 second transaction time?
        │           │
        │           ├── YES → 📋 [[RCP 240 D]]
        │           │          (CPDLC data-link, 240 sec CTT)
        │           │
        │           └── NO → Do you need ≤ 400 second transaction time?
        │                      │
        │                      ├── YES → 📋 [[RCP 400 D]]
        │                      │          (Data-link comm, 400 sec CTT)
        │                      │
        │                      └── NO → Re-assess your operation.
        │                                 PBCS may not be needed.
        │
        └── NO → Do you use SATVOICE for voice relay operations?
                 │
                 ├── YES → 📋 [[RCP 400 VRO]]
                 │          (SATVOICE voice relay, 400 sec CTT)
                 │
                 └── NO → PBCS communication specification
                          may not apply to your operation.
```

### How to answer the time question

The 240 vs 400 decision depends on:

| Factor | Points toward 240/D | Points toward 400/D |
|---|---|---|
| **Separation standard** | ≤ 5 min longitudinal | ≥ 10 min longitudinal |
| **Intervention need** | Controller must intervene quickly (route changes, conflict resolution) | Routine communication (position reports, clearances with long lead time) |
| **Airspace density** | High traffic | Low traffic (oceanic, remote) |

> [!tip] If unsure, choose the stricter spec
> RCP 400/D is less demanding than RCP 240/D. If your operation can meet 240/D, you also meet 400/D. Start strict — you can always downgrade if your State allows it. Upgrading later means re-approval.

---

## Part 2: Which RSP specification?

```
START: Is ADS-C used as the primary means of surveillance for separation?
        │
        ├── NO → Do you have radar coverage?
        │         │
        │         ├── YES → 📋 RSP NOT REQUIRED
        │         │          (Radar provides surveillance)
        │         │
        │         └── NO → Re-assess. If you need surveillance
        │                   without radar, RSP likely applies.
        │
        └── YES → Do you need ≤ 180 second data delivery time?
                  │
                  ├── YES → 📋 [[RSP 180 D]]
                  │          (ADS-C data-link, 180 sec SDDT)
                  │
                  └── NO → Do you need ≤ 400 second data delivery time?
                            │
                            ├── YES → 📋 [[RSP 400 D]]
                            │          (Data-link surveillance, 400 sec SDDT)
                            │
                            └── NO → Do you use SATVOICE for position
                                      reporting in surveillance context?
                                      │
                                      ├── YES → 📋 [[RSP 400 VRO]]
                                      │          (SATVOICE surveillance, 400 sec SDDT)
                                      │
                                      └── NO → Re-assess. Your surveillance
                                                needs may not need RSP.
```

### Does your operation need both?

Many operations need both RCP and RSP:

| Operation profile | RCP needed? | RSP needed? | Example |
|---|---|---|---|
| CPDLC only, radar surveillance | ✓ RCP 240/D or 400/D | ✗ | Domestic en-route CPDLC |
| CPDLC + ADS-C, no radar | ✓ RCP 240/D or 400/D | ✓ RSP 180/D or 400/D | Oceanic reduced separation |
| SATVOICE only | ✓ RCP 400/VRO | ✗ (unless position reporting) | Remote voice communication |
| SATVOICE + position reporting | ✓ RCP 400/VRO | ✓ RSP 400/VRO | SATVOICE relay operations |

---

## Part 3: Quick reference — all specifications

| Spec | Domain | Key time | Typical use | Detail page |
|---|---|---|---|---|
| RCP 240/D | Communication (CPDLC) | ≤ 240 sec CTT | Controller intervention | [[RCP 240 D]] |
| RCP 400/D | Communication (data-link) | ≤ 400 sec CTT | Routine data-link comm | [[RCP 400 D]] |
| RCP 400/VRO | Communication (SATVOICE) | ≤ 400 sec CTT | Voice relay operations | [[RCP 400 VRO]] |
| RSP 180/D | Surveillance (ADS-C) | ≤ 180 sec SDDT | ADS-C position data | [[RSP 180 D]] |
| RSP 400/D | Surveillance (data-link) | ≤ 400 sec SDDT | Data-link surveillance | [[RSP 400 D]] |
| RSP 400/VRO | Surveillance (SATVOICE) | ≤ 400 sec SDDT | SATVOICE surveil. context | [[RSP 400 VRO]] |

---

> [!warning] Always verify with your State
> This decision tree identifies which specification Doc 9869 offers for your scenario. The actual specification you must comply with is whatever your State prescribes in your AIP or SUPP. The State may prescribe a stricter specification than Doc 9869 suggests, or may prescribe one where Doc 9869 recommends none.

---

## Related

- [[RCP vs RSP]] — conceptual comparison
- [[RCP Specification]] / [[RSP Specification]] — spec details
- [[Implementation Path]] — implement once you've chosen
- [[PBCS Compliance Worked Example]] — see how specs are chosen in practice
