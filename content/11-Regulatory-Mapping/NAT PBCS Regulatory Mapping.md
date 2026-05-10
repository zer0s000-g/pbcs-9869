---
title: NAT PBCS Regulatory Mapping
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "regulatory"]
---

# NAT PBCS Regulatory Mapping

> [!summary] TL;DR
> The North Atlantic (NAT) is the most mature PBCS region. RCP 240/D and RSP 180/D are prescribed for the Organized Track System (OTS) and adjacent airspace. This page maps the actual requirements.

---

## Why NAT matters for PBCS

The NAT is the world's busiest oceanic airspace — over 1,000 flights daily. The NAT SPG (Systems Planning Group) was the first ICAO regional group to implement PBCS at scale. Their implementation is the reference model for other regions.

---

## NAT regional framework

| Layer | What it covers |
|---|---|
| **NAT SPG** | Systems Planning Group — coordinates PBCS policy and implementation |
| **NAT Doc 007** | NAT Operations Manual — contains PBCS requirements |
| **NAT SUPPs** | Doc 7030 — NAT-specific PBCS procedures |
| **State AIPs** | Individual OACC State requirements (Shanwick, Gander, Santa Maria, New York, etc.) |

---

## NAT OACC airspace blocks

| OACC / FIR | Controlling State | Prescribed specs | Status |
|---|---|---|---|
| **Shanwick OACC** | UK / Ireland | RCP 240/D, RSP 180/D | Active |
| **Gander OACC** | Canada | RCP 240/D, RSP 180/D | Active |
| **Santa Maria OACC** | Portugal | RCP 240/D, RSP 180/D | Active |
| **New York OACC** | USA | RCP 240/D, RSP 180/D | Active |
| **Reykjavik OACC** | Iceland | RCP 240/D, RSP 180/D | Active |
| **Bodo OACC** | Norway | RCP 240/D, RSP 180/D | Active |

All six OACCs prescribe the same RCP 240/D + RSP 180/D combination — regional alignment is complete.

---

## Organized Track System (OTS) requirements

The OTS uses two track systems daily (Westbound and Eastbound). PBCS enables:

| Separation | Before PBCS | With PBCS (RCP 240/D + RSP 180/D) |
|---|---|---|
| **Lateral** | 60 NM (non-PBCS) | 30 NM (PBCS) |
| **Longitudinal** | 10 minutes | 5 minutes |
| **Vertical** | 1,000 ft | 1,000 ft (unchanged) |

### PBCS track designations

| Track type | What it means | Requires |
|---|---|---|
| **PBCS tracks** | Tracks where reduced separation applies | RCP 240/D + RSP 180/D approval |
| **Non-PBCS tracks** | Tracks with standard separation | No PBCS approval needed |
| **Mixed tracks** | Some segments require PBCS | Check NAT Doc 007 track message |

> [!important] Track message conventions
> NAT track messages use designators indicating PBCS requirements. Operators must decode these to know which tracks they can file.

---

## NAT monitoring programme

The NAT has the most established regional monitoring:

| Element | Description |
|---|---|
| **NAT CMA** (Central Monitoring Agency) | UK NATS manages the CMA — collects and analyzes PBCS data from all OACCs |
| **Data sources** | All six OACCs submit monthly performance data |
| **Report frequency** | Monthly operator-level reports, quarterly NAT CMA regional summaries |
| **Public reports** | NAT CMA publishes anonymized performance reports on the ICAO NAT website |
| **Corrective action** | Per-OACC process; coordinated through NAT SPG for regional issues |

---

## NAT AIP ENR structure

When reviewing NAT State AIPs:

```
AIP ENR 2.2 — NAT Region, NAT HLA (High Level Airspace)
  ├── 2.2.x — PBCS requirements for OTS
  ├── RCP 240/D and RSP 180/D prescription
  ├── RCP/RSP allocation values
  ├── Operator eligibility and approval requirements
  ├── Flight plan Item 10a/18 requirements
  └── Monitoring data submission obligations
```

Each OACC publishes substantially identical requirements, with minor variations in approval processes.

---

## NAT vs APAC — comparison

| Dimension | NAT | APAC |
|---|---|---|
| **Maturity** | Most mature (operational for 5+ years) | Active (FIT-ASIA Phase 1-2) |
| **Specs prescribed** | RCP 240/D + RSP 180/D (all FIRs) | RCP 240/D + RSP 180/D (most FIRs) |
| **Monitoring** | Centralized (NAT CMA, UK NATS) | Distributed (APAC PBCS TF coordination) |
| **Track system** | Twice-daily OTS | Individual FIR procedures |
| **Non-PBCS fallback** | Available on separate tracks | 10-min separation tracks available |
| **Performance data public** | Yes (NAT CMA reports) | Limited (TF-level reports) |

---

## Operator guidance for NAT PBCS

### What to expect in the NAT compared to APAC

| Aspect | NAT expectations |
|---|---|
| **Approval recognition** | NAT States generally recognize each other's approvals |
| **Monitoring data sharing** | Your data goes to the OACC, then to NAT CMA — centralized analytics |
| **Degradation response** | NAT CMA flags are taken seriously — expect follow-up from your OACC |
| **CSP requirements** | Both Inmarsat and Iridium supported — your CSP must provide data to the OACC |
| **Contingency** | SATVOICE backup is strongly recommended (not always prescribed) |

---

## Key resources

| Resource | Link / Access |
|---|---|
| **NAT Doc 007** | ICAO NAT Office — NAT Operations Manual |
| **NAT CMA reports** | Published on ICAO NAT website |
| **NAT SPG** | Coordination body — State/ANSP representation |
| **Gander/Shanwick OACC** | Individual AIPs for operational requirements |

---

> [!warning] Disclaimer
> This page provides a regional overview for planning purposes. **Always verify current requirements against the actual State AIP, the latest NAT Doc 007, and Doc 7030 NAT SUPPs.** Contact details and specific OACC requirements change — this is a structural guide, not a legally binding reference.

---

## Related

- [[APAC PBCS Regulatory Mapping]] — APAC comparison
- [[ICAO Interoperability Map]] — document ecosystem
- [[Choosing Your RCP-RSP Specification]] — which spec
- [[Implementation Path]] — how to implement
- [[Institution Adaptation Guide]] — customize for your State
