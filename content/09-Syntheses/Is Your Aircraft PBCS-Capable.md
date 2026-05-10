---
title: Is Your Aircraft PBCS-Capable
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "decision-tree", "synthesis"]
---

# Is Your Aircraft PBCS-Capable?

> [!summary] TL;DR
> A step-by-step decision tree to determine whether your aircraft meets PBCS requirements. If you answer YES to every branch, you're ready for operational approval. Any NO is a gap you need to fix first.

---

## Decision tree

```
START: Is the required avionics installed and certified?
        │
        ├── YES → Is CPDLC/ADS-C in your MEL?
        │           │
        │           ├── YES (with dispatch relief defined) → Are crew trained?
        │           │                                          │
        │           │                           ┌──────────────┴──────────────┐
        │           │                           │                             │
        │           │                      YES (all crew)            NO or partial
        │           │                           │                             │
        │           │        ┌──────────────────┤                    Return to training
        │           │        │                  │                    before proceeding
        │           │   ┌────┴────┐      ┌─────┴─────┐
        │           │   │ Initial │      │ Recurrent │
        │           │   │ training│      │ training  │
        │           │   │ complete│      │ up to date│
        │           │   └────┬────┘      └─────┬─────┘
        │           │        │                  │
        │           │        └────────┬─────────┘
        │           │                 │
        │           │    Do you have a CSP service agreement?
        │           │                 │
        │           │    ┌────────────┴────────────┐
        │           │    │                         │
        │           │   YES (with data provision)  NO
        │           │    │                         │
        │           │    │              Contract must include
        │           │    │              performance data + outage
        │           │    │              notification provisions
        │           │    │
        │           │ Do you have flight plan filing procedures?
        │           │    │
        │           │    ├── YES (dispatch trained, Item 10a/18 configured)
        │           │    │
        │           │   ✅ AIRCRAFT IS PBCS-CAPABLE
        │           │      Proceed to [[Operational Approval]]
        │           │
        │           └── NO → Update MEL before dispatch
        │
        └── NO → Avionics must be installed and certified first.
                  See [[Aircraft Manufacturer]] and [[Avionics Supplier]].
```

---

## Detailed checklist by branch

### Branch 1: Avionics installed and certified

| Check | What to verify | Reference |
|---|---|---|
| CPDLC FANS 1/A installed | Aircraft has FANS 1/A capable flight management system | [[Data Link Services]] |
| ADS-C capability confirmed | Aircraft can accept and execute ADS-C contracts | [[Data Link Services]] |
| SATVOICE (if applicable) | Satcom voice system installed and certified | [[SATVOICE]] |
| Certification basis | Type certificate or STC references PBCS capability | [[Aircraft Manufacturer]] |
| Interoperability evidence | Aircraft system tested with ground network | [[Aircraft System Interfaces]] |

### Branch 2: MEL provisions

| Check | What to verify | Reference |
|---|---|---|
| CPDLC in MEL | MEL entry for CPDLC with dispatch relief category | [[Operational Approval]] |
| ADS-C in MEL | MEL entry for ADS-C if RSP applies | [[Operational Approval]] |
| Dispatch conditions | Clear conditions for dispatch with inoperative equipment | Your approved MEL |
| Placarding | Required placards/decal notifications | Operator procedures |

### Branch 3: Crew training

| Check | Initial | Recurrent | Reference |
|---|---|---|---|
| PBCS concepts | ✅ | ✅ | [[Beginner Path]] |
| CPDLC procedures | ✅ | ✅ | Operator training manual |
| ADS-C procedures | ✅ (if RSP applies) | ✅ | Operator training manual |
| Flight plan filing | ✅ | ✅ | [[Flight Plan Requirements]] |
| Abnormal operations | ✅ | ✅ | Operator procedures |
| Problem reporting | ✅ | ✅ | [[Problem Reporting]] |

### Branch 4: Service provider agreement

| Check | What to verify | Reference |
|---|---|---|
| Active CSP contract | Contract in place with approved CSP | [[Communication Service Provider]] |
| Data provision clause | CSP agrees to provide performance and outage data | [[CSP SSP Checklist]] |
| SSP contract (if RSP) | If separate SSP, data provision included | [[Surveillance Service Provider]] |
| Investigation support | CSP/SSP will support corrective action investigations | [[Corrective Action]] |

### Branch 5: Flight plan filing

| Check | What to verify | Reference |
|---|---|---|
| Flight plan item 10a | Equipment codes: J2 (CPDLC FANS 1/A), J5 (SATVOICE if applicable) | [[Flight Plan Requirements]] |
| Flight plan item 18 | Performance-based navigation/surveillance indicators | [[Flight Plan Requirements]] |
| Dispatch training | Dispatchers know how to file and interpret PBCS codes | Operator procedures |
| Verification procedure | Process to verify filed codes match actual capability | Operator procedures |

---

## Common capability gaps

> [!warning] Gap: SATVOICE installation without CPDLC integration
> Some aircraft have SATVOICE installed for voice communication but lack the data-link integration needed for CPDLC. If your operation requires RCP 240/D (CPDLC), SATVOICE alone won't satisfy it.

> [!warning] Gap: Training completed but not documented
> "Everyone knows how to use CPDLC" is not sufficient. Approval requires documented training records — dates, attendees, syllabus, assessment results.

> [!warning] Gap: CSP contract exists but without data provisions
> A standard connectivity contract may not include performance data reporting. Your CSP must specifically agree to provide monitoring data per Appendix D/E requirements.

> [!warning] Gap: Aircraft is capable but State hasn't prescribed the spec
> Even if your aircraft meets all criteria, you can't operate under PBCS until the State formally prescribes the RCP/RSP for the airspace. Check the AIP.

---

## If any branch fails

If you hit a NO at any branch, don't try to proceed with a partial package. States and ANSPs check all five branches during operational approval.

Prioritize fixing gaps in this order:
1. Avionics (can't proceed without it)
2. CSP contract (no monitoring without data)
3. MEL + training (can be done in parallel)
4. Flight plan procedures (last piece)

---

## Related

- [[Choosing Your RCP-RSP Specification]] — which spec applies
- [[Operational Approval]] — the approval process
- [[Implementation Path]] — end-to-end implementation
- [[PBCS Compliance Worked Example]] — real example
