---
title: Appendix B RCP Table Verification
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-hardened-direct-pdf-check
modified: 2026-05-06
tags: ["pbcs", "source", "table-verification", "rcp"]
---

# Appendix B RCP Table Verification

## Scope
This note records the table-verification pass for Doc 9869 Appendix B, RCP specifications. It verifies table families and selected high-value numeric fields used by the RCP pages and company templates.

## Verification method
- Directly inspected the source PDF with PyMuPDF table detection and page-text review.
- Checked Doc 9869 PDF pages 93-127, corresponding to Appendix B printed pages App B-1 through App B-35.
- Stored machine-readable extraction inventory outside the published vault in the private working area.
- Table geometry is verified enough for routing and source hardening; formal compliance still requires checking the PDF page image.

## Appendix B table inventory verified
| Doc 9869 PDF page | Verified table family |
|---:|---|
| 93-94 | RCP specification overview and RCP parameter values |
| 95-106 | RCP 240/D allocation figure/table and ANSP/CSP/aircraft system/operator criteria |
| 107-114 | RCP 400/D specification and component criteria |
| 115-127 | RCP 400/VRO allocation, safety-requirement, component criteria, and SATVOICE/RO tables |

## RCP 240/D fields checked
| Field | Verified value / structure | Source location |
|---|---|---|
| Specification | RCP 240/D | Appendix B section 2.1, Doc 9869 PDF pages 94-106 |
| Application | CPDLC | Doc 9869 PDF pages 96-106 |
| Allocation components | ANSP, CSP, aircraft system, aircraft operator | Table B-1, Doc 9869 PDF pages 95-96 |
| Transaction time value | ET 240 seconds at C = 99.9%; TT 210 seconds at C = 95% | Doc 9869 PDF page 96 |
| RCMP allocation | ET 210 seconds; TT 180 seconds | Doc 9869 PDF page 96 |
| Availability service | Efficiency 0.9999; safety 0.999 | Doc 9869 PDF page 97 |
| Integrity value | Malfunction = 10^-5 per flight hour for ANSP integrity table | Doc 9869 PDF page 97 |

## RCP 400/D fields checked
| Field | Verified value / structure | Source location |
|---|---|---|
| Specification | RCP 400/D | Appendix B section 3.1, Doc 9869 PDF pages 107-114 |
| Application | CPDLC | Doc 9869 PDF pages 108-114 |
| Allocation components | ANSP, CSP, aircraft system, aircraft operator | Appendix B, Doc 9869 PDF pages 107-114 |
| Relationship to RCP 240/D | Several integrity/availability/monitoring tables reuse or refer to RCP 240/D criteria | Doc 9869 PDF pages 110-114 |

## RCP 400/VRO fields checked
| Field | Verified value / structure | Source location |
|---|---|---|
| Specification | RCP 400/VRO | Appendix B section 3.2, Doc 9869 PDF pages 115-127 |
| Application | SATVOICE/RO | Doc 9869 PDF pages 118-127 |
| Allocation components | ANSP, CSP, aircraft system, aircraft operator | Table B-2 and component tables, Doc 9869 PDF pages 116-127 |
| Safety requirements | RCP 400/VRO safety requirements table links RCP parameters to SR requirements | Table B-3, Doc 9869 PDF page 117 |

## Boundary for company use
Use this note to route colleagues to verified source locations. For formal compliance documents, check the original PDF page image and the current State/regional requirement before reusing any table value.

## Downstream notes hardened from this verification
- [[RCP Specification]]
- [[RCP 240 D]]
- [[RCP 400 D]]
- [[RCP 400 VRO]]
- [[PBCS Compliance Matrix Template]]
- [[Monitoring Report Template]]

## Related notes
- [[Source - ICAO Doc 9869]]
- [[Doc 9869 Tables and Figures]]
- [[Appendix C RSP Table Verification]]
- [[PBCS Evidence Ladder]]
