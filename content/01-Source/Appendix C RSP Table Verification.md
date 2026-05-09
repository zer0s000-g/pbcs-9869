---
title: Appendix C RSP Table Verification
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-hardened-direct-pdf-check
modified: 2026-05-06
tags: ["pbcs", "source", "table-verification", "rsp"]
---

# Appendix C RSP Table Verification

## Scope
This note records the table-verification pass for Doc 9869 Appendix C, RSP specifications. It verifies table families and selected high-value numeric fields used by the RSP pages and company templates.

## Verification method
- Directly inspected the source PDF with PyMuPDF table detection and page-text review.
- Checked Doc 9869 PDF pages 129-151, corresponding to Appendix C printed pages App C-1 through App C-23.
- Stored machine-readable extraction inventory outside the published vault in the private working area.

## Appendix C table inventory verified
| Doc 9869 PDF page | Verified table family |
|---:|---|
| 129-130 | RSP specification overview and RSP parameter values |
| 131-138 | RSP 180/D allocation table and ANSP/CSP/aircraft system/operator criteria |
| 139-142 | RSP 400/D criteria and references back to RSP 180/D where applicable |
| 143-151 | RSP 400/VRO allocation, component criteria, and SATVOICE/RO tables |

## RSP 180/D fields checked
| Field | Verified value / structure | Source location |
|---|---|---|
| Specification | RSP 180/D | Appendix C section 2.1, Doc 9869 PDF pages 131-138 |
| Application | ADS-C | Doc 9869 PDF pages 131-138 |
| Allocation components | ANSP, CSP, aircraft system, aircraft operator | Table C-1, Doc 9869 PDF page 131 |
| RSMP time allocation | OT 180 seconds at C = 99.9%; DT 90 seconds at C = 95% | Doc 9869 PDF page 131 |
| RSTP ATSU allocation | OT 5 seconds; DT 3 seconds | Doc 9869 PDF page 132 |
| RSTP CSP allocation | OT 170 seconds; DT 84 seconds | Doc 9869 PDF page 132 |
| Availability service | Efficiency 0.9999; safety 0.999 | Doc 9869 PDF page 132 |

## RSP 400/D fields checked
| Field | Verified value / structure | Source location |
|---|---|---|
| Specification | RSP 400/D | Appendix C section 3.1, Doc 9869 PDF pages 139-142 |
| Application | ADS-C | Doc 9869 PDF pages 140-142 |
| Relationship to RSP 180/D | Multiple criteria reuse or point back to RSP 180/D criteria | Doc 9869 PDF pages 141-142 |

## RSP 400/VRO fields checked
| Field | Verified value / structure | Source location |
|---|---|---|
| Specification | RSP 400/VRO | Appendix C section 3.2, Doc 9869 PDF pages 143-151 |
| Application | SATVOICE/RO | Doc 9869 PDF pages 144-151 |
| Allocation components | ANSP, CSP, aircraft system, aircraft operator | Table C-2 and component tables, Doc 9869 PDF pages 143-151 |
| Safety requirements relationship | RSP 400/VRO safety requirements are routed to RCP 400/VRO where indicated | Doc 9869 PDF page 144 and related component tables |

## Boundary for company use
Use this note to route colleagues to verified source locations. Do not use extracted table values as a substitute for current procedure applicability or aircraft/operator authorization.

## Related notes
- [[Source - ICAO Doc 9869]]
- [[Doc 9869 Tables and Figures]]
- [[Appendix B RCP Table Verification]]
- [[PBCS Evidence Ladder]]
