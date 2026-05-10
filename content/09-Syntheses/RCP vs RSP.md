---
title: RCP vs RSP
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "synthesis"]
---

# RCP vs RSP

> [!summary] TL;DR
> RCP is for communication (CPDLC, SATVOICE). RSP is for surveillance (ADS-C, position reports). They use the same performance dimensions (time, continuity, availability, integrity) applied to different domains. Many operations need both.

---

## Side-by-side comparison

| Dimension | RCP | RSP |
|---|---|---|
| **Domain** | Communication | Surveillance |
| **Core question** | "Did my message arrive in time?" | "Did my position data arrive in time?" |
| **Performance metric** | Communication Transaction Time (CTT) | Surveillance Data Delivery Time (SDDT) |
| **Actual measurement** | ACP (Actual Communication Performance) | ASP (Actual Surveillance Performance) |
| **Source appendix** | Appendix B | Appendix C |
| **Spec examples** | RCP 240/D, RCP 400/D, RCP 400/VRO | RSP 180/D, RSP 400/D, RSP 400/VRO |

---

## The naming convention decoded

```
RCP 240 / D
 │    │    │
 │    │    └── D = Data-link (VRO = Voice Relay Operations)
 │    └─────── Transaction time in seconds
 └──────────── Required Communication Performance
```

```
RSP 180 / D
 │    │    │
 │    │    └── D = Data-link
 │    └─────── Data delivery time in seconds
 └──────────── Required Surveillance Performance
```

---

## When do you need which?

> [!example] Scenario 1: Oceanic CPDLC + ADS-C
> **AIM:** Reduce lateral separation from 60 NM to 30 NM in oceanic airspace.
>
> **What's needed:**
> - **RCP 240/D** — CPDLC clearance must complete within 240 sec
> - **RSP 180/D** — ADS-C position must arrive within 180 sec
>
> **Why both?** The controller needs to issue clearances (comm), but also needs to know where the aircraft is (surv). If either degrades, separation must revert.

> [!example] Scenario 2: Domestic CPDLC only
> **AIM:** Replace voice position reports with CPDLC in domestic radar airspace.
>
> **What's needed:**
> - **RCP 240/D** — CPDLC transaction time
> - **No RSP** — radar provides surveillance, not ADS-C
>
> **Why comm only?** The surveillance picture comes from radar — no data-link surveillance specification needed.

---

## Common confusion

> [!warning] "We have CPDLC, so we must be RCP-compliant"
> **False.** Having CPDLC equipment installed does not prove RCP compliance. You need to show that your actual communication performance (ACP) against the required specification (RCP) meets the numbers — including procedures, training, service provider performance, and monitoring.

> [!warning] "RSP is only for ADS-C"
> **Mostly true, but not entirely.** RSP applies to any data-link surveillance. ADS-C is the most common, but SATVOICE-based position reporting can also fall under RSP (see RSP 400/VRO).

---

## Related notes

- [[Required Communication Performance]]
- [[Required Surveillance Performance]]
- [[Communication Transaction Time]]
- [[Surveillance Data Delivery Time]]
- [[PBCS Evidence Ladder]]
---

## 🧭 Where next?

⬅ Back to: [[Performance-Based Communication and Surveillance]]

➡ Continue to: [[Required Communication Performance]]

📋 Return to: [[Beginner Path]] | [[Beginner Path]] | [[PBCS MOC]]
