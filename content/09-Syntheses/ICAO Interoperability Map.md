---
title: ICAO Interoperability Map
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "synthesis", "icao", "interoperability"]
---

# ICAO Interoperability Map

> [!summary] TL;DR
> Doc 9869 doesn't exist in isolation. PBCS concepts connect to other ICAO documents — Annexes, PANS, Regional Procedures, and global guidance. This page maps those connections so you know where Doc 9869 ends and other documents pick up.

---

## The ICAO PBCS document ecosystem

```
                    ┌─────────────────┐
                    │   Doc 9869      │
                    │  PBCS Manual    │
                    │  (framework)    │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Annex 10      │   │ Doc 4444      │   │ Doc 7030      │
│ Vol III       │   │ PANS-ATM      │   │ Regional      │
│ (technical)   │   │ (procedural)  │   │ SUPPs         │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                    ┌───────┴───────┐
                    │     GOLD      │
                    │  (operational │
                    │   guidance)   │
                    └───────────────┘

       ┌───────────────┐
       │ Doc 9613      │
       │ PBN Manual    │
       │ (navigation)  │
       └───────────────┘
       (complementary, not subordinate)
```

---

## Document-by-document mapping

### ICAO Annex 10 — Aeronautical Telecommunications, Volume III

**What it is:** Technical standards for communication systems.

**Relevance to PBCS:** Defines the protocols and performance characteristics of the systems PBCS relies on.

| Annex 10 topic | PBCS connection | This KB |
|---|---|---|
| CPDLC message set and protocol | The data-link that RCP 240/D and 400/D measure | [[Data Link Services]], [[RCP 240 D]] |
| ADS-C contract types and reporting | The surveillance data that RSP 180/D and 400/D measure | [[Data Link Services]], [[RSP 180 D]] |
| SATVOICE technical specifications | The voice system that RCP 400/VRO and RSP 400/VRO cover | [[SATVOICE]] |
| VHF Data Link (VDL) Mode 2 | One of the air-ground data links in the comm chain | [[Communication System Chain]] |
| ATN/OSI and FANS 1/A interoperability | How different systems talk to each other | [[Aircraft System Interfaces]] |

**Key relationship:** Doc 9869 says *what* performance is needed. Annex 10 says *how* the systems work. You need both for a complete picture.

---

### Doc 4444 — PANS-ATM (Procedures for Air Navigation Services — Air Traffic Management)

**What it is:** Operational procedures for air traffic controllers and flight crews.

**Relevance to PBCS:** Defines the separation minima and ATC procedures that PBCS enables.

| PANS-ATM topic | PBCS connection | This KB |
|---|---|---|
| Longitudinal separation minima (e.g., 5 min, 30 NM) | The separation standard that drives which RCP/RSP is needed | [[Choosing Your RCP-RSP Specification]] |
| CPDLC clearance procedures | How controllers use the comm system that RCP measures | [[Operational Approval]] |
| ADS-C position reporting procedures | How surveillance data is used operationally | [[RSP Specification]] |
| Contingency procedures (loss of comm/surv) | What happens when RCP/RSP degrades operationally | [[Corrective Action]] |
| Phraseology for data-link operations | Standardized communication that supports RCP | [[Flight Plan Requirements]] |

**Key relationship:** PANS-ATM defines the *procedural context* for why PBCS numbers matter. The RCP 240/D transaction time exists because PANS-ATM says separation at 5 minutes requires controller intervention within 240 seconds.

---

### Doc 7030 — Regional Supplementary Procedures

**What it is:** Region-specific ICAO procedures that supplement or differ from global standards.

**Relevance to PBCS:** This is where specific RCP/RSP prescriptions are published for each ICAO region.

| Region | Typical PBCS content in SUPPs | Status |
|---|---|---|
| **NAT** (North Atlantic) | Prescribes RCP 240/D and RSP 180/D for specific tracks | Active |
| **APAC** (Asia/Pacific) | FIT-ASIA implementation — RCP/RSP for Bay of Bengal, South China Sea | Active |
| **AFI** (Africa/Indian Ocean) | Data-link mandates for specific FIRs | Emerging |
| **CAR/SAM** (Caribbean/South America) | Regional PBCS implementation plans | Varies |
| **MID** (Middle East) | CPDLC/ADS-C requirements for specific routes | Emerging |
| **EUR** (Europe) | LINK2000+ programme (CPDLC) | Active |

**Key relationship:** Doc 7030 is where you find your *actual* obligation. Doc 9869 provides the framework, but the SUPP tells you exactly which RCP/RSP applies to your airspace.

> [!tip] Finding your region
> Doc 7030 is available from ICAO. Check your State's AIP for references to applicable SUPPs. This KB will expand with specific regional pages in `11-Regulatory-Mapping/` (planned).

---

### GOLD — Global Operational Data Link Document

**What it is:** Practical operational guidance for implementing data-link services worldwide.

**Relevance to PBCS:** Bridges the gap between technical standards (Annex 10) and operational procedures (PANS-ATM) for data-link.

| GOLD topic | PBCS connection | This KB |
|---|---|---|
| CPDLC implementation guidance | How to set up CPDLC operations that meet RCP | [[Implementation Path]] |
| ADS-C contract management | How to configure contracts for RSP compliance | [[Data Link Services]], [[RSP Allocation]] |
| Performance monitoring framework | How to collect and analyze ACP/ASP data | [[Post-Implementation Monitoring]] |
| Interoperability between FANS 1/A and ATN | How different aircraft generations work with ground systems | [[Aircraft System Interfaces]] |
| Problem reporting and resolution | Operational guidance for the corrective action process | [[Problem Reporting]], [[Corrective Action]] |

**Key relationship:** GOLD is the *practitioner's guide* — it tells you how to actually do what Doc 9869 says should be done.

---

### Doc 9613 — Performance-Based Navigation (PBN) Manual

**What it is:** The framework for navigation specifications (RNP, RNAV).

**Relevance to PBCS:** Complementary — PBCS covers comm/surv, PBN covers navigation. Operations often need both.

| PBN topic | PBCS interaction | This KB |
|---|---|---|
| RNP 4 (oceanic/remote) | Paired with RCP 240/D + RSP 180/D for oceanic operations | [[RCP vs RSP]] |
| RNP 2 (en-route) | May be used with CPDLC (RCP) in continental airspace | [[Operational Approval]] |
| RNP AR (authorization required) | Precision navigation that may require specific comm/surv support | See FAQ #9, [[Frequently Asked Questions]] |
| A-RNP (advanced RNP) | Future specification that may integrate comm/surv requirements | Future |
| PBN approval process | Similar structure to PBCS approval (capability → evidence → approval → monitoring) | [[Operational Approval]] |

**Key relationship:** PBCS and PBN are separate but often co-prescribed. An oceanic operation might need RNP 4 + RCP 240/D + RSP 180/D. Each is approved separately, but they work together operationally.

---

## How to use this map

### If you're reading Doc 9869 and need context

| Doc 9869 topic | The broader context is in... |
|---|---|
| "What CPDLC actually does technically?" | → Annex 10 Vol III |
| "What separation does this enable?" | → Doc 4444 PANS-ATM |
| "What does my region actually require?" | → Doc 7030 (Regional SUPPs) |
| "How do I actually implement this?" | → GOLD |
| "What about navigation?" | → Doc 9613 (PBN Manual) |

### If you're building a compliance package

A complete PBCS compliance package references:

1. **Doc 9869** — the framework and specification tables
2. **Doc 7030** — your region's specific prescriptions (if applicable)
3. **State AIP** — your State's published requirements
4. **Annex 10** — technical standards (for aircraft/avionics evidence)
5. **PANS-ATM** — operational procedures (for training/approval evidence)

---

> [!note] Coming soon
> This KB will expand with dedicated regional mapping pages under `11-Regulatory-Mapping/` covering specific ICAO regions (APAC, NAT, AFI, etc.) with actual State requirements and AIP references.

---

## Related

- [[Source - ICAO Doc 9869]] — the primary source
- [[Referenced Publications]] — RTCA and EUROCAE standards
- [[PBCS Evidence Ladder]] — how claims trace through the ecosystem
- [[Institution Adaptation Guide]] — how to add your regulatory layer
