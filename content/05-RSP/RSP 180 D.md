---
title: RSP 180 D
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-hardened-direct-pdf-check
modified: 2026-05-09
tags: ["pbcs", "rsp", "source-hardened"]
---

# RSP 180 D

> [!summary] TL;DR
> RSP 180/D is the ADS-C data-link specification for surveillance-critical separation. The strictest RSP — position data must arrive within 180 seconds at 99.9% continuity.

---

## Source-hardened summary

RSP 180/D is the ADS-C data-link RSP specification. Appendix C allocates surveillance data delivery performance across ANSP, CSP, aircraft system, and aircraft operator responsibilities. This is the most demanding RSP specification and the most commonly prescribed alongside RCP 240/D for oceanic reduced-separation operations.

---

## Component allocation breakdown

The total 180-second SDDT budget is very tight:

| Component | Typical allocation | What it covers | Verified by |
|---|---|---|---|
| **ANSP (ATS ground system)** | ~20 sec | Processing from ground network handoff to controller display | ATS system specifications, integration testing |
| **CSP (air-ground data link)** | ~110 sec | Satellite transmission: aircraft → satellite → ground station → network | CSP service agreement, link budget |
| **Aircraft system** | ~30 sec | Position measurement (GNSS/INS), report generation, FMS processing, queuing | Type certificate, avionics compliance |
| **Aircraft operator** | ~20 sec | Crew: ensuring ADS-C contract is active, monitoring compliance | Training records, procedure validation |

**Total: 180 seconds**

> [!important] Even tighter than RCP 240/D
> At 180 seconds, the surveillance budget is tighter than the communication budget. The aircraft system must measure position, format the report, queue it, and transmit via the satellite link — all within a strict window. This is why RSP 180/D is often the harder specification for operators to meet.

---

## Verified source basis

| Claim | Verified source location |
|---|---|
| RSP 180/D allocations apply to surveillance data delivery via ADS-C | Appendix C, section 2.1, Doc 9869 PDF page 131 |
| RSP 180/D allocations are shared by ANSP, CSP, aircraft system, and aircraft operator | Appendix C, section 2.1; Table C-1, Doc 9869 PDF page 131 |
| RSMP time allocation is 180 seconds at 99.9% and 90 seconds at 95% | Appendix C, RSP data delivery time and continuity criteria, Doc 9869 PDF page 131 |
| RSTP ATSU allocation is 5 seconds at 99.9% and 3 seconds at 95% | Appendix C, Doc 9869 PDF page 132 |
| RSTP CSP allocation is 170 seconds at 99.9% and 84 seconds at 95% | Appendix C, Doc 9869 PDF page 132 |
| Availability service criteria include 0.9999 efficiency and 0.999 safety | Appendix C, RSP availability criteria, Doc 9869 PDF page 132 |

---

## How each allocation is verified

### ANSP allocation (~20 sec)

| Evidence type | What it proves |
|---|---|
| ATS system specifications | Maximum processing time for ADS-C report handling |
| Ground integration test results | End-to-end timing from network handoff |
| System performance monitoring | Ongoing measurement |

### CSP allocation (~110 sec)

| Evidence type | What it proves |
|---|---|
| Link budget analysis | Calculated transmission time for satellite link |
| CSP service agreement | Contracted latency for surveillance data |
| Historical link performance | Actual measured delivery times |
| Outage notification | Degradation reporting |

### Aircraft system allocation (~30 sec)

| Evidence type | What it proves |
|---|---|
| Type certificate / STC | ADS-C capability certification |
| Avionics compliance | Position measurement accuracy, report generation specifications |
| Interoperability testing | Aircraft → ground network integration |
| BITE / self-test | Continuous monitoring |

### Aircraft operator allocation (~20 sec)

| Evidence type | What it proves |
|---|---|
| Training records | ADS-C operations and contract management |
| Procedure documentation | ADS-C contract monitoring procedures |
| ORT results | Trial compliance measurement |
| Recurrent training | Ongoing proficiency |

---

## Common failure modes

| Component | Failure mode | Impact | Detection |
|---|---|---|---|
| ANSP | ATS delayed processing | Report arrives but not displayed in time | System monitoring |
| CSP | Satellite beam handover during report transmission | Delivery delayed or lost | Link continuity data |
| CSP | Ground station queuing | Report held in queue | CSP performance reports |
| Aircraft | ADS-C contract terminated before report | No position data generated | FMS log, ground system alert |
| Aircraft | GNSS signal loss | Position unavailable for report | FMS alert, report missing data |
| Operator | Crew unaware contract inactive | Contract not re-established | Ground monitoring, ANSP notification |

---

## Monitoring fields (from Appendix D)

| Field | What it measures | Source |
|---|---|---|
| **Data delivery time** | End-to-end per ADS-C report | Appendix D Table D-1 |
| **Continuity** | % reports delivered without issue | Appendix D Table D-2 |
| **Availability** | CSP/SSP service uptime | Appendix D Table D-3 |
| **Problem reports** | Count and category | Appendix D Table D-4 |

---

## Component routing

| Component | Table family to inspect |
|---|---|
| ANSP | Doc 9869 PDF pages 131-133 |
| CSP | Doc 9869 PDF pages 134-135 |
| Aircraft system | Doc 9869 PDF pages 135-136 |
| Aircraft operator | Doc 9869 PDF pages 136-138 |

---

## Company-use boundary

Do not treat RSP 180/D as applicable to a route, aircraft, or operator until State/regional prescription, operational approval, aircraft capability, service-provider arrangements, and monitoring responsibilities are confirmed.

---

## Related notes

- [[Required Surveillance Performance]]
- [[RSP Specification]]
- [[RSP Allocation]]
- [[RSP Compliance]]
- [[RSP Monitoring]]
- [[Appendix C RSP Table Verification]]
- [[Choosing Your RCP-RSP Specification]]
