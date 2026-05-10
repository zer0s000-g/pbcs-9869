---
title: Performance-Based Communication and Surveillance
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "concept"]
---

# Performance-Based Communication and Surveillance

> [!summary] TL;DR
> PBCS replaces "what equipment do you have?" with "what performance can you deliver?" It gives ATM operations objective, measurable criteria for communication and surveillance — so any technology that meets the bar can be approved.

---

## The problem PBCS solves

Before PBCS, air-ground communication and surveillance approval was prescription-based:

> *"Do you have VHF radio? CPDLC? ADS-C equipment installed?"*

This approach had two problems:

1. **Technology lock-in.** A new system that performed better couldn't easily be used because the regulation specified equipment, not outcomes.
2. **No objective baseline.** Two operators with identical equipment could have vastly different operational performance (different training, procedures, service providers).

PBCS flips this:

> *"Can your communication transaction complete within 240 seconds, with 99.9% continuity and 99.99% availability?"*

If you can prove it — regardless of which equipment you use — you're compliant.

---

## The two pillars

| | RCP | RSP |
|---|---|---|
| **Domain** | Communication | Surveillance |
| **Question it answers** | "Did my CPDLC message get through in time?" | "Did my position report arrive when needed?" |
| **Key metric** | Communication Transaction Time (CTT) | Surveillance Data Delivery Time (SDDT) |
| **Source** | Doc 9869 Appendix B | Doc 9869 Appendix C |

> [!example] Real-world example
> An oceanic FIR wants to reduce longitudinal separation from 10 minutes to 5 minutes using CPDLC and ADS-C. They prescribe:
> - **RCP 240/D** for the CPDLC communication (transaction must complete within 240 seconds)
> - **RSP 180/D** for the ADS-C surveillance (position data must be delivered within 180 seconds)
>
> Any operator who can show their aircraft + crew + service provider meets these numbers can fly the reduced separation. The State doesn't care if they use Inmarsat, Iridium, or a future satellite system — only that the numbers are met.

---

## The PBCS lifecycle

PBCS isn't a one-time check. It's a continuous loop:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PBCS LIFECYCLE                                   │
│                                                                         │
│  1. DEVELOP             2. APPLY              3. PROVE                  │
│  ┌──────────┐         ┌──────────┐          ┌──────────┐              │
│  │ What does │ ──────→ │ Prescribe│ ───────→ │ Show you  │              │
│  │ the ATM   │         │ RCP/RSP  │          │ can meet  │              │
│  │ operation │         │ in AIP   │          │ the spec  │              │
│  │ need?     │         │ or SUPP  │          │           │              │
│  └──────────┘         └──────────┘          └─────┬─────┘              │
│       ↑                                           │                    │
│       │                                           ↓                    │
│       │                                    4. MONITOR                  │
│       │                                    ┌──────────┐               │
│       │                                    │ Collect  │               │
│       │                                    │ ACP/ASP  │               │
│       │                                    │ data,    │               │
│       │                                    │ analyze, │               │
│       │                                    │ report   │               │
│       │                                    └─────┬─────┘               │
│       │                                          │                     │
│       │                                   ┌──────┴──────┐             │
│       │                                   │  Meets RCP/  │             │
│       │                                   │  RSP spec?   │             │
│       │                                   └──────┬──────┘             │
│       │                                ┌─────────┴─────────┐         │
│       │                            YES │                    │ NO      │
│       │                                ↓                    ↓         │
│       │                          Continue          5. CORRECT          │
│       │                        monitoring       ┌──────────┐         │
│       │                                         │Investi-  │         │
│       │                                         │gate root │         │
│       │                                         │cause,    │         │
│       │                                         │implement │         │
│       │                                         │fix       │         │
│       │                                         └────┬─────┘         │
│       │                                              │               │
│       └──────────────────────────────────────────────┘               │
│                   Re-assess and re-prove                              │
└─────────────────────────────────────────────────────────────────────────┘
```

**Key questions at each stage:**

| Stage | Who asks | The question |
|---|---|---|
| 1. DEVELOP | ANSP + State | "What communication/surveillance performance does the ATM operation need?" |
| 2. APPLY | State | "Which RCP/RSP specification will we prescribe, and where is it published?" |
| 3. PROVE | Operator | "Can we demonstrate our aircraft, crew, and providers meet the numbers?" |
| 4. MONITOR | ANSP + Regional | "Does actual performance (ACP/ASP) match required performance (RCP/RSP)?" |
| 5. CORRECT | All stakeholders | "When performance degrades, who investigates, fixes, and re-proves?" |

**Doc 9869 source routing for each stage:**

- **Develop:** Chapter 2, [[Developing RCP RSP Specifications]]
- **Apply:** Chapter 3, [[Applying RCP RSP Specifications]]
- **Prove:** Chapter 4.2-4.4, [[Operational Approval]]
- **Monitor:** Chapter 4.5, Appendices D-E, [[Post-Implementation Monitoring]]
- **Correct:** Appendices D-E, [[Corrective Action]]

> [!tip] Screenshot this
> This lifecycle diagram is designed to be screenshot and used in presentations or training materials. The box-and-arrow structure fits cleanly on a single slide.

---

## Source basis

- Doc 9869 Chapter 1 explains the PBCS framework
- For source navigation: [[Source - ICAO Doc 9869]], [[Doc 9869 Section Map]]

---

## Related notes

- [[Beginner Path]] — start here if you're new
- [[Required Communication Performance]]
- [[Required Surveillance Performance]]
- [[RCP vs RSP]]
- [[PBCS Responsibility Matrix]]
- [[PBCS Implementation Lifecycle]]
