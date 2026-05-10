---
title: RSP 400 VRO
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "rsp"]
---

# RSP 400 VRO

> [!summary] TL;DR
> RSP 400/VRO is the SATVOICE RSP specification from the surveillance/position-reporting perspective. When position data is delivered via voice relay (not ADS-C data-link), this specification applies.

---

## What makes VRO different for surveillance

RSP 400/VRO covers position data delivery through the **voice relay chain**:

```
Pilot reports position → Aircraft SATCOM → Satellite → Ground Earth Station → CSP Relay Operator → ATC
```

This is fundamentally different from RSP 180/D and RSP 400/D, which use **automated ADS-C data-link** for position delivery. The voice relay adds a human in the loop.

---

## Where RSP 400/VRO applies

| Scenario | RSP 400/VRO applies? |
|---|---|
| SATVOICE used for position reporting (no ADS-C) | ✅ Yes |
| Oceanic/remote, voice is the only comm/surv link | ✅ Yes |
| ADS-C available — position data via data-link | ❌ No (use RSP 180/D or 400/D) |
| Radar coverage provides surveillance | ❌ No |

---

## Component allocation breakdown

| Component | Typical allocation | What it covers | Verified by |
|---|---|---|---|
| **ANSP (ATC)** | ~20 sec | Controller receives position report, acknowledges | ATC procedures |
| **CSP (SATVOICE + relay)** | ~300 sec | Satellite transmission + relay operator time | CSP agreement, relay staffing |
| **Aircraft system** | ~50 sec | SATCOM equipment, position data preparation | SATCOM certification |
| **Aircraft operator (crew)** | ~30 sec | Pilot reads position, communicates via SATVOICE | Training, voice procedure validation |

**Total: 400 seconds**

---

## Position data flow (voice relay)

```
1. Aircraft system measures position (from GNSS/INS)
2. Pilot reads position from instruments
3. Pilot initiates SATVOICE call
4. Pilot reports position to relay operator
5. Relay operator transcribes and delivers to ATC
6. ATC acknowledges receipt
7. Relay operator confirms delivery to pilot
```

Each step introduces potential for delay and human transcription error.

---

## Common failure modes

| Component | Failure mode | Impact | Detection |
|---|---|---|---|
| CSP (satellite) | Beam congestion | Call setup delay | CSP reports |
| CSP (relay) | Relay operator transcribes position incorrectly | Wrong position delivered to ATC | ATC cross-check, readback |
| CSP (relay) | Relay operator unavailable | Position report delayed | Staffing logs |
| Aircraft | SATCOM voice quality poor | Position garbled, needs repeat | Pilot report |
| Operator (crew) | Pilot misreads position from display | Incorrect position reported | Cross-check with next report |
| ANSP | ATC busy — cannot take relay call | Position report on hold | ATC operational log |

> [!warning] Transcription risk
> Unlike ADS-C (automated, error-checked data-link), SATVOICE position delivery involves human transcription. The relay operator must accurately transcribe position coordinates, altitude, and time. Two-person verification at the relay station is a best practice.

---

## Monitoring fields (from Appendix E)

| Field | What it measures | Source |
|---|---|---|
| **Position report delivery time** | Time from aircraft measurement to ATC receipt | Appendix E Table E-1 |
| **Call setup time** | SATVOICE call establishment time | Appendix E Table E-2 |
| **Service availability** | SATVOICE uptime | Appendix E Table E-3 |
| **Problem reports** | Voice relay issues including transcription errors | Appendix E Table E-4 |

---

## RSP 400/VRO vs data-link RSP

| Dimension | RSP 400/VRO (voice) | RSP 400/D (data-link) |
|---|---|---|
| **Delivery method** | Voice relay (human) | ADS-C data-link (automated) |
| **Error risk** | Transcription errors | CRC/error-checked protocol |
| **Position source** | Pilot reads from instruments | FMS automation |
| **Key CSP role** | Relay operator proficiency | Link performance |
| **Monitoring complexity** | Higher (two human steps) | Lower (automated collection) |

---

## Source basis

- Doc 9869 Appendix C, RSP 400/VRO specification
- For detailed source routing: [[Appendix C RSP Table Verification]]
- For SATVOICE monitoring: [[SATVOICE Monitoring]]

---

## Related notes

- [[Required Surveillance Performance]]
- [[Surveillance Data Delivery Time]]
- [[RSP Specification]]
- [[RSP Compliance]]
- [[RSP Monitoring]]
- [[SATVOICE]]
- [[Choosing Your RCP-RSP Specification]]
