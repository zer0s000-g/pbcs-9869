---
title: RCP 240 D
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-hardened-direct-pdf-check
modified: 2026-05-06
tags: ["pbcs", "rcp", "source-hardened"]
---

# RCP 240 D

## Source-hardened summary
RCP 240/D is the CPDLC data-link RCP specification used for controller intervention capability. Appendix B allocates the requirement across ANSP, CSP, aircraft system, and aircraft operator responsibilities.

## Verified source basis
| Claim | Verified source location |
|---|---|
| RCP 240/D allocations apply to controller intervention capability via CPDLC | Appendix B, section 2.1, Doc 9869 PDF page 94 |
| RCP 240/D allocations are shared by ANSP, CSP, aircraft system, and aircraft operator | Appendix B, section 2.1; Table B-1, Doc 9869 PDF pages 94-96 |
| Transaction time value is 240 seconds at 99.9% continuity and 210 seconds at 95% continuity | Appendix B, RCP transaction time and continuity criteria, Doc 9869 PDF page 96 |
| RCMP allocation is 210 seconds at 99.9% and 180 seconds at 95% | Appendix B, Doc 9869 PDF page 96 |
| ANSP availability service criteria include 0.9999 efficiency and 0.999 safety | Appendix B, RCP availability criteria, Doc 9869 PDF page 97 |
| ANSP integrity table uses malfunction = 10^-5 per flight hour | Appendix B, RCP integrity criteria, Doc 9869 PDF page 97 |

## Component routing
| Component | Table family to inspect |
|---|---|
| ANSP | Doc 9869 PDF pages 96-100 |
| CSP | Doc 9869 PDF pages 100-101 |
| Aircraft system | Doc 9869 PDF pages 101-104 |
| Aircraft operator | Doc 9869 PDF pages 104-106 |

## Company-use boundary
Do not treat RCP 240/D as applicable to a route, aircraft, or operator until State/regional prescription, operational approval, aircraft capability, service-provider arrangements, and monitoring responsibilities are confirmed.

## Related notes
- [[Required Communication Performance]]
- [[RCP Specification]]
- [[RCP Allocation]]
- [[RCP Compliance]]
- [[RCP Monitoring]]
- [[Appendix B RCP Table Verification]]
