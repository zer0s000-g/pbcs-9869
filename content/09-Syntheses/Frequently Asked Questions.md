---
title: Frequently Asked Questions
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "synthesis"]
---

# Frequently Asked Questions

Real questions from institutions implementing PBCS. If your question isn't here, use the search bar — it covers every word in this knowledge base.

---

## 1. We already have CPDLC installed. Are we automatically PBCS-compliant?

**No.** Having the equipment is step one — but PBCS compliance requires more:

- **Procedures and training:** Your crew must be trained on CPDLC procedures specific to the airspace
- **MEL provisions:** Your Minimum Equipment List must address CPDLC dispatch relief (can you depart with CPDLC inoperative?)
- **Service provider agreements:** Your CSP must agree to provide performance and outage data
- **Operational approval:** The State must approve your operation against the prescribed RCP/RSP
- **Monitoring:** You must participate in post-implementation monitoring

Equipment = necessary, not sufficient. Think of it as having a driver's license but no car, no insurance, and no knowledge of the road rules.

> **Source:** Doc 9869 Chapter 4 sections 4.2-4.4. Read [[Operational Approval]] for the full requirements.

---

## 2. Can we use this knowledge base as our State's safety case?

**Not alone.** This KB is a source-routed reference — it tells you what Doc 9869 says and where. But a State safety case requires:

- The actual State regulations that prescribe the RCP/RSP
- The specific airspace and operation being assessed
- Real operational data and evidence from your ANSP, operators, and service providers
- A safety assessment conducted by qualified personnel per your State's SMS framework

This KB gives you the source backbone. Your safety case is the evidence layer you build on top of it.

> **Source:** Doc 9869 Chapter 4 section 4.1 and [[Safety Assessment]]. See also [[PBCS Evidence Ladder]].

---

## 3. What's the difference between ACP and RCP?

| | RCP | ACP |
|---|---|---|
| **Stands for** | Required Communication Performance | Actual Communication Performance |
| **Question it answers** | "What must the operation deliver?" | "What is actually being delivered?" |
| **Source** | Appendix B specification tables | Post-implementation monitoring data |
| **Fixed or variable?** | Fixed (prescribed by State) | Variable (measures real-world conditions) |
| **Who sets it?** | State / ANSP (based on Doc 9869) | Reality (measured through monitoring) |

**RSP and ASP** are the surveillance equivalents — same relationship.

> [!important] The gap matters
> If ACP < RCP, your operation is not meeting requirements and corrective action is needed. This is exactly what monitoring reveals. See [[Post-Implementation Monitoring]].

---

## 4. Do we need RSP if we have radar coverage?

**Usually no — but check your State's prescription.**

- If your airspace has **radar coverage**, the surveillance picture comes from ground radar, not from data-link surveillance. RSP would not apply.
- If your airspace is **oceanic or remote** (no radar), and ADS-C is being used for separation, RSP likely applies.
- Some States prescribe both RCP and RSP even where radar exists — always verify the actual AIP/SUPP entry.

The key question: *"Is ADS-C being used as the primary means of surveillance for separation?"* If yes → RSP applies. If radar is primary → RSP is usually not needed.

> **Source:** Doc 9869 Chapter 2 and Appendix C. See [[RSP Specification]] and the [[PBCS Compliance Worked Example]], which documents a case where RSP was deliberately marked N/A due to radar coverage.

---

## 5. Can we use different service providers for communication and surveillance?

**Yes — and this is common.** An operator might use:

- **CSP A** (e.g., Inmarsat) for CPDLC communication (RCP domain)
- **CSP B** (e.g., Iridium) for ADS-C surveillance (RSP domain)

What matters is that each provider meets the component allocations for the specification they support. They don't need to be the same provider.

> [!warning] However
> Your monitoring programme must be able to separate the performance data by provider. If Inmarsat goes down but Iridium is fine, you can't treat both as degraded. See [[Data Collection]] and [[CSP SSP Checklist]].

---

## 6. What happens when our monitoring shows performance degradation?

Don't panic — but act deliberately. The Doc 9869 corrective action framework:

1. **Identify:** Which metric (transaction time? continuity? availability?) and which component (aircraft? air-ground link? ground network? ATS?)
2. **Investigate:** Gather data from the affected stakeholder(s) — operator logs, CSP outage reports, ATS system logs
3. **Determine root cause:** Was it a one-time event, an equipment failure, or a systemic issue?
4. **Implement fix:** Correct the root cause — equipment repair, procedure change, service provider escalation
5. **Re-prove:** Demonstrate that the fix restored performance — typically 30 consecutive days meeting the specification
6. **Notify State:** If safety-impacting, notify the State authority per your approved procedures

> **Source:** Doc 9869 Appendices D and E problem reporting sections. See [[Corrective Action]] and [[Problem Reporting]].

---

## 7. Who owns the corrective action process?

**It depends on where the degradation occurred:**

| Degradation source | Who investigates | Who fixes |
|---|---|---|
| Aircraft system | Operator | Operator + avionics supplier |
| Crew procedures | Operator | Operator (training/procedure update) |
| Air-ground data link | CSP | CSP (service restoration) |
| Ground network | CSP / ANSP | CSP / ANSP |
| ATS ground system | ANSP | ANSP |
| Multiple components | ANSP coordinates | Per-component owner |

The ANSP typically coordinates the overall process, especially when multiple stakeholders are involved. The State oversees the process for safety-significant issues.

> **Source:** [[PBCS Responsibility Matrix]] and [[Corrective Action]].

---

## 8. How often must we report monitoring results?

Doc 9869 does **not** prescribe a universal reporting frequency. It depends on:

- **Your State's requirements** — some States mandate monthly, some quarterly
- **The regional monitoring programme** — NAT and APAC programmes have their own cadences
- **The operational context** — new operations often report more frequently (monthly) before transitioning to a reduced cadence (quarterly) after stability is demonstrated

> [!tip] Best practice
> Monthly reporting for the first 12 months after approval, then quarterly if performance is stable. This aligns with most regional PBCS monitoring programmes.

> **Source:** Doc 9869 Chapter 4 section 4.5. See [[Monitoring Programme]] and [[Performance Analysis]].

---

## 9. How does PBCS relate to RNP / RNP AR?

PBCS and RNP are complementary but separate ICAO frameworks:

| | PBCS | RNP |
|---|---|---|
| **Domain** | Communication + surveillance | Navigation |
| **ICAO source** | Doc 9869 | Doc 9613 |
| **Performance spec** | RCP / RSP | RNP value (e.g., RNP 4, RNP 2, RNP AR 0.3) |
| **Monitoring** | ACP / ASP data | Navigation system monitoring |

**They interact operationally:** An oceanic operation might require RNP 4 (navigation accuracy), RCP 240/D (CPDLC communication), and RSP 180/D (ADS-C surveillance) — all three working together to achieve the separation standard.

You can't substitute one for the other. RNP doesn't cover CPDLC transaction time; RCP doesn't cover navigation accuracy.

---

## 10. Can we use this knowledge base commercially? What's the license?

Currently this KB uses default Quartz licensing. For institutional reuse, we recommend:

- **Content:** Apply a CC BY-SA 4.0 license — allows adaptation and commercial use, requires attribution and share-alike
- **Code (Quartz framework):** MIT license (already in `package.json`)

Check with the repository owner for the current license status. If you fork and adapt this KB for your institution, you should add your own license file.

---

## 🧭 Didn't find your answer?

- **Search** the site (Cmd+K / Ctrl+K) — covers every word
- Browse the [[PBCS MOC]] — complete content map
- Check the [[Evidence and Traceability Map]] — source routing for specific claims
- If it's a term you don't recognize, see [[Acronyms and Terms]]

---

## Related

- [[Beginner Path]] — start learning
- [[Implementation Path]] — step-by-step implementation
- [[Learning Tracks]] — role-based training
- [[How to Use This Knowledge Base]] — navigating this site
