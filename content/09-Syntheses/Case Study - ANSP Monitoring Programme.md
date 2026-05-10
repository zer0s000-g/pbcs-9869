---
title: Case Study — ANSP Monitoring Programme
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["case-study", "pbcs", "synthesis"]
---

# Case Study — ANSP Standing Up a Regional Monitoring Programme

> [!summary] What this is
> An anonymized narrative of an ANSP building a PBCS monitoring programme from nothing. Fictional names, real operational challenges.

---

## Context

**Who:** Bay of Bengal Area Control Centre (ACC) — part of a national ANSP serving one of the busiest oceanic FIRs in the APAC region.

**Where:** Bay of Bengal oceanic airspace. ~200 flights per day. Predominantly east-west traffic between South Asia and Southeast Asia.

**What changed:** APAC FIT-ASIA Phase 1 prescribed RCP 240/D and RSP 180/D for the Bay of Bengal. The ANSP's State authority mandated that the ANSP establish and operate a post-implementation monitoring programme before any operator approvals could be issued.

**When:** State directive received with a 6-month deadline to have the monitoring programme operational.

---

## Challenge

### Starting state

| Element | Status |
|---|---|
| ATS system CPDLC/ADS-C logging | ⚠️ Logs exist but in raw format — no aggregation, no analysis |
| Monitoring programme design | ❌ None existed |
| Data fields defined | ❌ No selection from Appendix D/E tables |
| Reporting cadence | ❌ Not established |
| Corrective action process | ❌ Not documented |
| Regional coordination | ❌ Not connected to APAC PBCS TF |
| Staff assigned | ❌ No dedicated monitoring team |

### What monitoring needed to deliver

Per Doc 9869 Appendices D and E:

1. Collect CPDLC transaction time, continuity, and availability data
2. Collect ADS-C data delivery time, continuity, and availability data
3. Produce monthly performance reports per standardized format
4. Detect degradation and trigger corrective action
5. Coordinate with the regional PBCS Task Force

---

## Approach

### Month 1-2: Design

**Team formed:** 3-person monitoring cell within ATM Operations — one data analyst, one ATS system engineer, one operational liaison.

**Fields selected:**

| Data category | Fields (from Appendix D) |
|---|---|
| CPDLC performance | Transaction time (per transaction, aggregated monthly), continuity (% completing without issue) |
| ADS-C performance | Data delivery time (per report, aggregated monthly), continuity |
| Availability | CSP service uptime (from CSP-provided reports), ATS system uptime (internal monitoring) |
| Problem reports | Count and category (per Appendix D Table D-4 format) |

**Reporting cadence:** Monthly reports to State authority, quarterly to APAC PBCS Task Force.

### Month 3-4: Build

**Data pipeline:**

```
ATS system raw logs → automated ETL script → monitoring database → monthly report generator
```

The ETL script (Python, ~200 lines) extracts transaction records from the ATS system's SQL logs, filters for Bay of Bengal airspace, calculates aggregate statistics (mean, 95th percentile, min/max for CTT and SDDT), and writes to a monitoring database.

**Report template:** Standardized per Appendix D format. Includes:
- Monthly summary statistics
- Per-operator breakdown (anonymized by operator code)
- Degradation alerts (any metric below RCP 240/D or RSP 180/D threshold)
- Problem report summary

### Month 4-5: Test

**Dry run:** Ran the pipeline against 3 months of historical ATS system logs. Validated that:
- CTT and SDDT extraction was accurate (spot-checked 100 random transactions against raw logs)
- Report format was accepted by State authority (pre-submission review)
- Degradation alert thresholds were correctly configured

### Month 5-6: Launch

**Corrective action process:** Documented a 5-step workflow:

```
Alert triggered → Analyst verifies (not false positive)
  → Liaison contacts affected operator/CSP (within 24 hours)
  → Joint investigation (operator logs + CSP data + ANSP data)
  → Root cause identified and fix implemented
  → Closure: 30 consecutive days meeting spec + State notification
```

**Regional coordination:** Joined APAC PBCS Task Force. Began submitting quarterly data.

**First live month:** June. 14,200 CPDLC transactions monitored. 3 transactions exceeded 240 sec CTT (all traced to a single CSP satellite beam handover event — one-time, not recurring).

---

## Timeline

| Month | Milestone |
|---|---|
| 1-2 | Fields selected, team assigned |
| 3-4 | Data pipeline built, report template finalized |
| 4-5 | Dry run with historical data, corrective action process drafted |
| 5-6 | Go-live — first live monitoring month |
| 6+ | Operational — monthly reports, quarterly regional submissions |

**Total: 6 months from directive to operational monitoring programme.**

---

## Key lessons

### 1. Start with the fields, not the system

The team's first instinct was to "buy a monitoring tool." Instead, they defined the 12 data fields from Appendix D/E first. Only then did they realize their existing ATS system already logged everything — they just needed an extraction script, not new hardware.

### 2. Historical data dry runs prevent go-live surprises

The 3-month dry run caught three issues: (a) some ADS-C reports were missing timestamps, (b) the CSP's outage data format didn't match the ANSP's import script, and (c) one operator's aircraft registration codes had changed. All fixed before go-live.

### 3. Corrective action needs named contacts, not departments

"We'll contact the operator" failed during the dry run because no one knew who to call. The ANSP now maintains a contact list: operator PBCS leads, CSP technical account managers, State oversight officers.

### 4. Regional coordination adds workload but necessary credibility

The APAC PBCS TF requires quarterly submissions. This added ~2 days of work per quarter. But the TF coordination gave the ANSP's monitoring programme regional legitimacy — operators trusted the data more because it was independently validated at the regional level.

### 5. Start manual, automate later

The first two monthly reports were manually compiled (Excel). This was deliberate — it forced the team to understand every data field before automating. Month 3 onward was fully automated. The manual phase prevented automation-from-ignorance errors.

---

## Related

- [[Monitoring Programme]] — the Doc 9869 framework
- [[Post-Implementation Monitoring]] — the full monitoring lifecycle
- [[Data Collection]] — data fields and methods
- [[Corrective Action]] — the process they built
- [[APAC PBCS Regulatory Mapping]] — the regional context
- [[Day 1 PBCS Action Guides]] — ANSP day 1 actions
