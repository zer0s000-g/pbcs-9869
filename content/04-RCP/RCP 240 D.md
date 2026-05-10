---
title: RCP 240 D
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-hardened-direct-pdf-check
modified: 2026-05-09
tags: ["pbcs", "rcp", "source-hardened"]
---

# RCP 240 D

> [!summary] TL;DR
> RCP 240/D is the CPDLC data-link specification for controller intervention. The strictest RCP — transaction must complete within 240 seconds at 99.9% continuity.

---

## Source-hardened summary

RCP 240/D is the CPDLC data-link RCP specification used for controller intervention capability. Appendix B allocates the requirement across ANSP, CSP, aircraft system, and aircraft operator responsibilities. This is the most demanding RCP specification and the most commonly prescribed for oceanic reduced-separation operations.

---

## Component allocation breakdown

The total 240-second CTT budget is tight. Realistic allocations:

| Component | Typical allocation | What it covers | Verified by |
|---|---|---|---|
| **ANSP (ATS ground system)** | ~20 sec | Message processing from ground network to controller display, controller response processing | ATS system specifications, integration testing |
| **CSP (air-ground data link)** | ~150 sec | Satellite transmission: aircraft → satellite → ground earth station → network | CSP service agreement, link budget analysis |
| **Aircraft system** | ~40 sec | FMS processing, CPDLC message composition, transmission queuing, SATCOM integration | Type certificate, avionics compliance data (RTCA DO-306) |
| **Aircraft operator** | ~30 sec | Crew: reading message, composing response, confirming/wilco | Training records, procedure validation, ORT results |

**Total: 240 seconds**

> [!important] Tight margins
> At 240 seconds, there is very little buffer. If the CSP link runs at its allocation ceiling (150 sec) and the crew takes more than 30 seconds, the transaction fails. This is why many operators struggle to qualify for RCP 240/D.

---

## Verified source basis

| Claim | Verified source location |
|---|---|
| RCP 240/D allocations apply to controller intervention capability via CPDLC | Appendix B, section 2.1, Doc 9869 PDF page 94 |
| RCP 240/D allocations are shared by ANSP, CSP, aircraft system, and aircraft operator | Appendix B, section 2.1; Table B-1, Doc 9869 PDF pages 94-96 |
| Transaction time value is 240 seconds at 99.9% continuity and 210 seconds at 95% continuity | Appendix B, RCP transaction time and continuity criteria, Doc 9869 PDF page 96 |
| RCMP allocation is 210 seconds at 99.9% and 180 seconds at 95% | Appendix B, Doc 9869 PDF page 96 |
| ANSP availability service criteria include 0.9999 efficiency and 0.999 safety | Appendix B, RCP availability criteria, Doc 9869 PDF page 97 |
| ANSP integrity table uses malfunction = 10^-5 per flight hour | Appendix B, RCP integrity criteria, Doc 9869 PDF page 97 |

---

## How each allocation is verified

### ANSP allocation (~20 sec)

| Evidence type | What it proves |
|---|---|
| ATS system specifications | Maximum processing time for CPDLC message handling |
| Ground integration test results | End-to-end timing from network handoff to controller workstation |
| System performance monitoring | Ongoing measurement against 20 sec benchmark |

### CSP allocation (~150 sec)

| Evidence type | What it proves |
|---|---|
| Link budget analysis | Calculated satellite transmission time for worst-case geometry |
| CSP service agreement | Contracted latency commitments — must support ≤150 sec |
| Historical link performance | Actual measured times for the target airspace |
| Outage notification process | How CSP reports deviations |

### Aircraft system allocation (~40 sec)

| Evidence type | What it proves |
|---|---|
| Type certificate / STC | CPDLC FANS 1/A capability certification |
| Avionics compliance (RTCA DO-306) | Processing time and message queuing specifications |
| Interoperability test results | Aircraft → ground network integration testing |
| BITE / self-test logs | Continuous monitoring of avionics performance |

### Aircraft operator allocation (~30 sec)

| Evidence type | What it proves |
|---|---|
| Training records | CPDLC procedures training — initial and recurrent |
| Procedure validation | SOP including CPDLC response time expectations |
| ORT results | Operational readiness trial — live measurement of crew response times |
| Proficiency checks | Recurrent assessment of CPDLC competency |

---

## Common failure modes

| Component | Failure mode | Impact | Detection |
|---|---|---|---|
| ANSP | ATS system overload (peak traffic) | Processing time spikes beyond allocation | ATS system monitoring |
| CSP | Satellite handover delay | Temporary link disruption | Link continuity logs |
| CSP | Ground earth station congestion | Queuing at ground segment | CSP performance reports |
| Aircraft | FMS message queue full | CPDLC message held | FMS log, pilot report |
| Aircraft | SATCOM antenna blocked (bank angle) | Brief link loss | CSP link data |
| Operator | Crew delayed response (high workload) | Transaction time exceeds allocation | ACP monitoring, crew report |

---

## Monitoring fields (from Appendix D)

| Field | What it measures | Source |
|---|---|---|
| **Transaction time** | End-to-end per CPDLC transaction | Appendix D Table D-1 |
| **Continuity** | % transactions completing without interruption | Appendix D Table D-2 |
| **Availability** | CSP service uptime | Appendix D Table D-3 |
| **Problem reports** | Count and category | Appendix D Table D-4 |

---

## Component routing

| Component | Table family to inspect |
|---|---|
| ANSP | Doc 9869 PDF pages 96-100 |
| CSP | Doc 9869 PDF pages 100-101 |
| Aircraft system | Doc 9869 PDF pages 101-104 |
| Aircraft operator | Doc 9869 PDF pages 104-106 |

---

## Company-use boundary

Do not treat RCP 240/D as applicable to a route, aircraft, or operator until State/regional prescription, operational approval, aircraft capability, service-provider arrangements, and monitoring responsibilities are confirmed.

---

## Related notes

- [[Required Communication Performance]]
- [[RCP Specification]]
- [[RCP Allocation]]
- [[RCP Compliance]]
- [[RCP Monitoring]]
- [[Appendix B RCP Table Verification]]
- [[Choosing Your RCP-RSP Specification]]
