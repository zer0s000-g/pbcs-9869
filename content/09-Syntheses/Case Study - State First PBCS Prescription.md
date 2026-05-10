---
title: Case Study — State First PBCS Prescription
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["case-study", "pbcs", "synthesis"]
---

# Case Study — State First PBCS Prescription

> [!summary] What this is
> An anonymized narrative of a State authority prescribing RCP/RSP for the first time — the policy process, stakeholder coordination, and lessons.

---

## Context

**Who:** The Civil Aviation Authority of a South Asian State with responsibility for an oceanic FIR.

**What:** The State's ATM Division needed to prescribe PBCS requirements for its oceanic airspace to enable reduced separation and align with the APAC FIT-ASIA programme.

**Why:** The APAC regional plan had designated this airspace for Phase 1 PBCS implementation. Without State prescription, operators couldn't get approval and the airspace couldn't transition to reduced separation.

**When:** No formal deadline, but APAC FIT-ASIA coordination pressure and operator requests made this a priority within 12 months.

---

## Challenge

### Starting state

| Element | Status |
|---|---|
| PBCS knowledge within CAA | ⚠️ ATM Division understood the concept; Legal and AIS divisions had no PBCS awareness |
| AIP ENR section | ❌ No PBCS entries existed |
| Approval process | ❌ No documented PBCS approval workflow |
| Operator readiness assessment | ❌ No survey of which operators could meet RCP/RSP |
| ANSP coordination | ⚠️ Informal — ANSP was ready but waiting for State prescription |
| Regional alignment | ⚠️ Participating in APAC TF but hadn't published anything |
| Legal review | ❌ No assessment of liability, oversight obligations |

### What needed to happen

1. Decide which RCP/RSP to prescribe (aligned with regional consensus)
2. Draft AIP ENR entries
3. Establish an approval process
4. Coordinate with the ANSP on monitoring
5. Coordinate with neighbouring States on prescription alignment
6. Notify operators with sufficient lead time
7. Publish and enforce

---

## Approach

### Phase 1: Policy decision (Months 1-3)

**Spec selection:** The ATM Division reviewed Doc 9869, APAC FIT-ASIA recommendations, and consultations with neighbouring States.

| Decision | Rationale |
|---|---|
| RCP 240/D prescribed | Oceanic reduced separation requires controller intervention within 240 seconds |
| RSP 180/D prescribed | ADS-C position delivery needed within 180 seconds for 5-minute separation |
| SATVOICE not prescribed separately | CPDLC is primary; SATVOICE is contingency — included in operator approval conditions |

**Stakeholder consultation (Month 2):**
- **Operators (3 airlines):** Surveyed readiness. Two ready within 12 months, one needed 18 months.
- **ANSP:** Confirmed monitoring programme design underway. Requested 6 months for operational readiness.
- **CSPs (2 providers):** Confirmed data provision capability for the airspace.
- **Neighbouring States (3):** All three had published or were about to publish identical RCP/RSP — no alignment conflicts.

**Legal review (Month 3):** CAA Legal confirmed:
- Liability: State prescription is a regulatory act — standard sovereign immunity applies
- Oversight obligations: Per ICAO SARPs, State must oversee approvals and monitor compliance
- Lead time: 12 months minimum between AIP publication and effective date (operator transition period)

### Phase 2: Documentation (Months 3-6)

**AIP ENR 1.8 drafted:**

```
AIP INDIA ENR 1.8-12 — PBCS Requirements for Bay of Bengal Oceanic FIR

1. Applicable specifications:
   - RCP 240/D — CPDLC data-link communication
   - RSP 180/D — ADS-C data-link surveillance

2. Operator eligibility:
   - Aircraft equipped with FANS 1/A (CPDLC + ADS-C)
   - Crew trained on CPDLC/ADS-C procedures
   - MEL includes CPDLC/ADS-C dispatch relief
   - Valid CSP contract with data provision clause

3. Approval requirements:
   - Completed PBCS compliance matrix
   - ORT results (minimum 10 flights)
   - Training records
   - CSP data provision agreement

4. Post-implementation monitoring:
   - Monthly performance data submission to ANSP
   - Participation in regional monitoring programme
   - Corrective action obligation per Appendix D/E

5. Effective date: [12 months from publication]
```

**Approval process designed:**

```
Operator submits package → CAA ATM Division reviews (30 days)
  → If complete: ORT observation (CAA inspector on 2 flights)
  → If satisfactory: Provisional approval (6 months)
  → Full approval after 6 months of compliant monitoring data
```

### Phase 3: Coordination & publication (Months 6-9)

- **Month 6:** Draft AIP circulated to operators and ANSP for comment period (30 days)
- **Month 7:** Two minor operator comments addressed (ORT flight count reduced from 15 to 10; provisional approval period clarified)
- **Month 8:** AIP published via AIRAC cycle
- **Month 9:** Operator briefing session — 3 airlines attended, Q&A on approval package requirements

### Phase 4: Transition (Months 9-21)

- **Months 9-21:** 12-month transition period. Operators could continue 10-minute separation tracks while preparing approval packages.
- **Month 15:** First operator submitted approval package.
- **Month 18:** First operator approved.
- **Month 21:** AIP effective date — all operators required to have approval or use alternate tracks.

---

## Outcome

**18 months after project start:**
- AIP ENR 1.8 published with clear RCP/RSP requirements
- 3 of 3 operators either approved or in-progress
- ANSP monitoring programme operational
- Regional alignment achieved — no prescription conflicts with neighbouring FIRs

---

## Key lessons

### 1. The prescription is the easy part — the lead time is the hard part

Deciding RCP 240/D + RSP 180/D took one meeting. The 12-month lead time debate took three meetings. Operators need time to train crews, update MELs, renegotiate CSP contracts, and run ORTs. The State that publishes with 6 months lead time will have zero operators ready on the effective date.

### 2. Survey your operators before publishing

The CAA's operator survey (month 2) revealed that one airline needed 18 months, not 12. Had they published first and surveyed later, they'd have either delayed the effective date (losing credibility) or forced an operator into non-compliance. Survey first, publish second.

### 3. Neighbouring State alignment is operational, not just diplomatic

If State A prescribes RCP 240/D and State B prescribes RCP 400/D for the same airspace block, operators get conflicting requirements. The CAA's check with three neighbours confirmed alignment before publication — this prevented a coordination nightmare.

### 4. The approval process must exist before the first application arrives

The CAA drafted the approval workflow during Phase 2 — 6 months before the first operator application. When that application arrived, the process was documented, staffed, and tested. States that wait until the first application arrives to design the process create backlogs.

### 5. Publish in the AIP, not just a circular

The CAA initially considered an "operational directive" (faster to issue). Legal advised that AIP publication carries regulatory force and international recognition. The extra 3 months for AIRAC cycle publication was worth the legal certainty.

---

## Related

- [[State Authority]] — the State's role in PBCS
- [[Applying RCP RSP Specifications]] — how States prescribe
- [[Operational Approval]] — what operators need from you
- [[ICAO Interoperability Map]] — Doc 7030 regional context
- [[APAC PBCS Regulatory Mapping]] — regional framework
- [[PBCS Institutional Maturity Model]] — assess your State's level
- [[Day 1 PBCS Action Guides]] — State day 1 actions
