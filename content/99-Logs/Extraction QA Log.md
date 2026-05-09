---
title: Extraction QA Log
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "qa", "log"]
---

# Extraction QA Log

## Extraction method
PyMuPDF text extraction. This is appropriate for a text-based PDF but may flatten table layouts.

## Known limitations
- Tables are not guaranteed to preserve visual row/column geometry.
- Figures are identified by nearby text, not reproduced graphically.
- Formal compliance matrices must be checked against the PDF.

## Initial QA tasks
- Confirm table rendering in Quartz.
- Audit wikilinks.
- Audit for local/private paths.
- Validate major appendix coverage.
