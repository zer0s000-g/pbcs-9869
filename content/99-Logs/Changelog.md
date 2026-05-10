---
title: Changelog
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
publish: false
tags: ["pbcs", "meta", "log"]
---

# Changelog

All notable changes to the PBCS Doc 9869 Knowledge Base.

---

## 2026-05-09 — Institutional Trust & Structure

### Added
- [[Verification Standards]] — formal definition of all verification badge levels (`source-linked`, `source-hardened-direct-pdf-check`, aspirational `peer-reviewed` and `regulatory-cross-checked`)
- [[Quick Reference Card]] — printable one-pager covering all specs, stakeholders, lifecycle, monitoring fields, and Doc 9869 page references
- [[Institution Adaptation Guide]] — how institutions fork, customize, and layer on private evidence
- [[ICAO Interoperability Map]] — how Doc 9869 connects to Annex 10, Doc 4444, Doc 7030, Doc 9613, and GOLD

### Changed
- Homepage: added Quick References section linking to all new utility pages
- PBCS MOC: added Governance section with verification standards and changelog; added Tools & References section
- Footer navigation updated across all path pages

---

## 2026-05-09 — User Experience & Learning Design

### Added
- [[How to Use This Knowledge Base]] — 3-minute site orientation: navigation methods, graph view, search, features
- [[Frequently Asked Questions]] — 10 real questions from PBCS implementers with sourced answers
- [[Choosing Your RCP-RSP Specification]] — decision tree for selecting the right specification
- [[Is Your Aircraft PBCS-Capable]] — 5-branch capability checklist decision tree
- [[Monitoring Shows Degradation - What Now]] — corrective action response tree by metric type
- [[Learning Tracks]] — 6 role-specific learning plans with timed reading sequences

### Changed
- Homepage: redesigned with path picker table, time budgets, emoji-section organization
- [[Beginner Path]]: rewritten as guided 3-step journey with checkpoints and TL;DR
- [[Implementation Path]]: restructured with "What you produce" column and common mistakes section
- [[Compliance Path]]: added lifecycle diagram, compliance gaps, and warning callouts
- [[PBCS MOC]]: restructured with emoji sections and getting-started section

---

## 2026-05-09 — Branding & Quick Wins

### Added
- [[PBCS Compliance Worked Example]] — fictional Mumbai Oceanic FIR example with filled compliance matrix
- [[Acronyms and Terms]] — complete glossary redesigned with categorized tables, spec naming decoder, and document references

### Changed
- Core concept pages ([[Performance-Based Communication and Surveillance]], [[Required Communication Performance]], [[Required Surveillance Performance]], [[RCP vs RSP]]): added TL;DR summaries, callout boxes, and real-world examples
- [[Performance-Based Communication and Surveillance]]: added comprehensive ASCII lifecycle diagram for presentations
- [[PBCS Compliance Matrix Template]]: linked to worked example
- All path pages: added ⬅ ➡ navigation footers

---

## 2026-05-09 — Branding Alignment

### Fixed
- Sidebar title correctly shows "PBCS Doc 9869 Knowledge Base" on all pages (no "Quartz" brand leakage)
- `quartz.config.ts`: `baseUrl` set to `zer0s000-g.github.io/pbcs-9869`
- `Head.tsx`: meta generator tag changed from "Quartz" to "PBCS Doc 9869 Knowledge Base"
- All OG meta tags, RSS feed links, and sitemap URLs reference the correct domain

---

## 2026-05-06 — Source Hardening

### Added
- [[Appendix B RCP Table Verification]] — source-verified pass for all RCP table families
- [[Appendix C RSP Table Verification]] — source-verified pass for all RSP table families
- [[Appendix D and E Monitoring Table Verification]] — verified monitoring data families

### Changed
- Source-hardened pages: [[PBCS Responsibility Matrix]], [[PBCS Compliance Matrix Template]], [[RCP 240 D]], [[RSP 180 D]], [[Doc 9869 Tables and Figures]], [[Post-Implementation Monitoring]], [[Evidence and Traceability Map]], [[PBCS MOC]], [[Monitoring Report Template]]
- All hardened pages carry `verification_status: source-hardened-direct-pdf-check` badge

---

## 2026-05-06 — Initial Build

### Added
- 83 Markdown files extracted from ICAO Doc 9869 PDF (212 pages, 2nd Edition, 2017)
- Full vault structure: 00-Navigation, 01-Source, 02-Core-Concepts, 03-Roles, 04-RCP, 05-RSP, 06-System-Architecture, 07-Implementation, 08-Monitoring-and-Reporting, 09-Syntheses, 10-Templates, 99-Logs
- Quartz v4.5.2 build pipeline with GitHub Actions deployment
- Source backbone: document identity, section map, definitions, tables/figures, referenced publications
- Core concepts: PBCS, RCP, RSP, availability, continuity, integrity
- Stakeholder pages: State, ANSP, operator, CSP, SSP, manufacturer, avionics supplier
- Specification branches: all 6 RCP/RSP specifications with allocations, compliance, monitoring
- Implementation: lifecycle, checklists, risk assessment
- Monitoring: programme, data collection, analysis, problem reporting, corrective action
- Syntheses: responsibility matrix, evidence ladder, RCP vs RSP, implementation risks
- Templates: compliance matrix, implementation checklist, monitoring report, responsibility assignment
