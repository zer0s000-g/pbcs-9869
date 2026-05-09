---
title: Appendix D and E Monitoring Table Verification
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-hardened-direct-pdf-check
modified: 2026-05-06
tags: ["pbcs", "source", "table-verification", "monitoring"]
---

# Appendix D and E Monitoring Table Verification

## Scope
This note records the table-verification pass for Doc 9869 Appendices D and E, covering post-implementation monitoring and corrective action for CPDLC, ADS-C, and SATVOICE.

## Verification method
- Directly inspected the source PDF with PyMuPDF table detection and page-text review.
- Checked Appendix D Doc 9869 PDF pages 153-196 and Appendix E Doc 9869 PDF pages 197-210.
- Verified the minimum data-field lists, CSV examples, reporting examples, availability-data fields, filtering/analysis guidance, and problem-reporting sections at source-location level.

## Appendix D verified table/data families: CPDLC and ADS-C
| Source area | Verified content | Source location |
|---|---|---|
| CPDLC transaction data | Minimum CPDLC data collection points, CSV example, ACP/ACTP/PORT calculation guidance | Appendix D sections 2.1.2-2.1.3, Doc 9869 PDF pages 154-156 |
| ADS-C report data | Minimum ADS-C data collection points, CSV example, transit-time calculation guidance | Appendix D sections 2.2.2-2.2.3, Doc 9869 PDF pages 159-160 |
| CPDLC/ADS-C availability | CSP-notified and detected outages; notification time, CSP name, start/end, duration | Appendix D section 2.3, Doc 9869 PDF page 161 |
| Filtering and analysis | CPDLC/ADS-C filtering, outage-period removal, cumulative distributions, sample-size considerations | Appendix D sections 3.1.2-3.1.5, Doc 9869 PDF pages 162-164 |
| Local/regional reports | Example service availability, RCP, RSP, operator, and regional monitoring reports | Appendix D section 4, Doc 9869 PDF pages 175-181 |
| Problem reporting | Data collection, analysis, coordination, database tracking, stakeholder feedback | Appendix D section 5, Doc 9869 PDF pages 186-190 |

## Appendix D minimum CPDLC data fields verified
| Ref | Field |
|---:|---|
| 1 | ANSP |
| 2 | Aircraft registration for FANS 1/A or aircraft address for ATN B1 |
| 3 | Aircraft type designator |
| 4 | Operator designator |
| 5 | Date |
| 6 | MAS RGS |
| 7 | OPS RGS |
| 8 | Uplink time |
| 9 | MAS/LACK receipt time |
| 10 | MAS/LACK round-trip time |
| 11 | Aircraft FMS timestamp |
| 12 | ANSP timestamp on receipt of operational response |
| 13 | Operational message round-trip time |
| 14 | Downlink response transit time |
| 15 | Uplink message elements |
| 16 | Downlink message elements |
| 17 | ACTP |
| 18 | ACP |
| 19 | PORT |

Source basis: Appendix D, Table D-1, Doc 9869 PDF pages 154-156.

## Appendix D minimum ADS-C data fields verified
| Ref | Field |
|---:|---|
| 1 | ANSP |
| 2 | Aircraft registration |
| 3 | Aircraft type designator |
| 4 | Operator designator |
| 5 | Date |
| 6 | RGS |
| 7 | Report type |
| 8 | Latitude |
| 9 | Longitude |
| 10 | Aircraft time |
| 11 | Received time |
| 12 | Transit time |

Source basis: Appendix D, Table D-3, Doc 9869 PDF pages 159-160.

## Appendix E verified table/data families: SATVOICE
| Source area | Verified content | Source location |
|---|---|---|
| SATVOICE clearance transactions | Minimum clearance transaction collection points and ACP calculation | Appendix E sections 2.1.2-2.1.3, Doc 9869 PDF pages 198-199 |
| SATVOICE position reports | Minimum position report collection points and ASP/position-report delivery calculation | Appendix E sections 2.2.2-2.2.3, Doc 9869 PDF pages 200-201 |
| SATVOICE service availability | CSP-notified and detected outages; notification time, CSP name, outage start/end, duration | Appendix E section 2.3, Doc 9869 PDF page 201 |
| SATVOICE filtering and analysis | Filtering, cumulative distributions, analysis by media/operators/aircraft/airframes | Appendix E section 3.1, Doc 9869 PDF pages 202-207 |
| Regional reporting | Monthly reports for observed availability, SATVOICE transaction time, and position report delivery time | Appendix E section 4, Doc 9869 PDF pages 207-208 |
| Problem reporting | Problem form fields, data collection, data analysis, and resolution workflow | Appendix E section 5, Doc 9869 PDF pages 208-210 |

## Appendix E minimum SATVOICE clearance transaction fields verified
| Ref | Field |
|---:|---|
| 1 | ANSP facility |
| 2 | Aircraft call sign |
| 3 | Operator designator |
| 4 | Aircraft type designator |
| 5 | Date |
| 6 | Clearance media |
| 7 | Clearance send time |
| 8 | ANSP timestamp on receipt of read-back response |
| 9 | ACP |

Source basis: Appendix E, Table E-1, Doc 9869 PDF page 198.

## Appendix E minimum SATVOICE position report fields verified
| Ref | Field |
|---:|---|
| 1 | ANSP facility |
| 2 | Aircraft call sign |
| 3 | Operator designator |
| 4 | Aircraft type designator |
| 5 | Date |
| 6 | Position report media |
| 7 | Report type |
| 8 | Latitude |
| 9 | Longitude |
| 10 | Position time |
| 11 | ANSP receipt time |
| 12 | ASP |

Source basis: Appendix E, Table E-2, Doc 9869 PDF page 200.

## Boundary for company use
The monitoring templates now route to verified field families. Before use in a live monitoring programme, align the fields with company databases, State/regional reporting requirements, and applicable RCP/RSP specifications.

## Related notes
- [[Appendix B RCP Table Verification]]
- [[Appendix C RSP Table Verification]]
- [[PBCS Evidence Ladder]]
