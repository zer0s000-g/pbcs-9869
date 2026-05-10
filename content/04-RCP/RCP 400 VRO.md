---
title: RCP 400 VRO
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "rcp"]
---

# RCP 400 VRO

> [!summary] TL;DR
> RCP 400/VRO is the SATVOICE voice-relay RCP specification. It applies when voice communication uses satellite relay (aircraft → satellite → ground operator → ATC) instead of direct pilot-controller voice.

---

## What SATVOICE VRO means

**VRO** = Voice Relay Operations. The communication chain is:

```
Pilot → Aircraft SATCOM → Satellite → Ground Earth Station → CSP Operator → ATC
```

This differs from direct CPDLC data-link because a **human relay operator** sits between the satellite link and ATC.

---

## Where RCP 400/VRO applies

| Scenario | RCP 400/VRO applies? |
|---|---|
| Oceanic/remote airspace, using satellite voice (no VHF coverage) | ✅ Yes |
| SATVOICE as primary means of ATC communication | ✅ Yes |
| SATVOICE as backup to CPDLC (voice contingency) | Depends on State prescription |
| Domestic airspace with VHF voice coverage | ❌ No |

---

## Component allocation breakdown

The total 400-second CTT budget:

| Component | Typical allocation | What it covers | Verified by |
|---|---|---|---|
| **ANSP (ATC)** | ~20 sec | Controller receives relayed message, responds | ATC procedures, controller proficiency |
| **CSP (SATVOICE service)** | ~300 sec | Satellite transmission + ground operator relay time | CSP service agreement, SATVOICE specifications |
| **Aircraft system** | ~50 sec | SATCOM equipment processing, voice quality | Aircraft SATCOM certification |
| **Aircraft operator (crew)** | ~30 sec | Pilot voice communication, readback procedures | Training records, voice procedure validation |

**Total: 400 seconds**

> [!tip] The CSP + relay operator dominates
> Unlike RCP 400/D (data-link), the SATVOICE chain includes a human relay operator. This typically adds 30-60 seconds beyond the satellite transmission time alone.

---

## How the relay works

```
1. Pilot initiates voice call via SATCOM
2. Satellite routes to ground earth station
3. CSP ground operator receives call, identifies aircraft
4. Ground operator relays message to ATC (via dedicated line or voice)
5. ATC responds → ground operator → satellite → aircraft
```

Each step consumes time. The 400-second budget must accommodate the entire loop.

---

## Common failure modes

| Component | Failure mode | Impact | Detection |
|---|---|---|---|
| CSP (satellite) | Satellite beam congestion in busy oceanic sectors | Call setup delay | CSP performance reports |
| CSP (relay operator) | Relay operator unavailable (shift change, overload) | Message delayed until operator available | CSP staffing logs, problem reports |
| Aircraft | SATCOM equipment fault | No voice capability | SATCOM BITE, pilot report |
| Operator (crew) | Unclear voice quality → repeated readbacks | Transaction time exceeds allocation | Pilot report, ATC report |
| ANSP | ATC unable to take call (busy frequency) | Voice relay on hold | ATC operational log |

---

## Monitoring fields (from Appendix E)

For RCP 400/VRO, the monitoring programme collects:

| Field | What it measures | Source |
|---|---|---|
| **Clearance delivery time** | Time from pilot request to ATC clearance relayed back | Appendix E Table E-1 |
| **Call setup time** | Time for SATVOICE call establishment | Appendix E Table E-2 |
| **Service availability** | SATVOICE service uptime percentage | Appendix E Table E-3 |
| **Problem reports** | Count and category of voice relay issues | Appendix E Table E-4 |

> See [[SATVOICE Monitoring]] for the full framework.

---

## When SATVOICE is used alongside CPDLC

Many operations use both:
- **CPDLC (RCP 240/D)** as the primary data-link for routine communication
- **SATVOICE (RCP 400/VRO)** as backup voice for contingencies or urgent situations

Some States prescribe both; others only prescribe the CPDLC spec.

---

## Source basis

- Doc 9869 Appendix B, RCP 400/VRO specification
- For detailed source routing: [[Appendix B RCP Table Verification]]
- For SATVOICE context: [[SATVOICE]]

---

## Related notes

- [[Required Communication Performance]]
- [[Communication Transaction Time]]
- [[RCP Specification]]
- [[RCP Compliance]]
- [[RCP Monitoring]]
- [[SATVOICE]]
- [[Choosing Your RCP-RSP Specification]]
