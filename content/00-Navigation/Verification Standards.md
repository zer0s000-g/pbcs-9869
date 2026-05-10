---
title: Verification Standards
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "governance", "verification", "meta"]
---

# Verification Standards

> [!summary] TL;DR
> Every page in this knowledge base carries a verification badge. This page defines what each badge means, who performed the check, and what you should verify yourself before relying on the content.

---

## Verification levels

### `source-linked`

**Definition:** The concept has been traced to its source section in Doc 9869, but has not been word-for-word verified against the PDF text.

**What was done:**
- The page author identified the relevant Doc 9869 chapter, section, and appendix
- Source routes (e.g., "Chapter 2, Appendix B") were documented
- The content reflects the general meaning of the source, but may contain paraphrasing or synthesis

**What was NOT done:**
- Every sentence verified against the exact PDF wording
- Specific table values independently re-checked
- Cross-reference to other ICAO documents (Annex 10, Doc 4444)

**When to trust this level:**
- For learning and understanding PBCS concepts
- For general guidance and orientation
- For identifying which source section to consult

**When to verify further:**
- For formal compliance submissions
- For operational decisions with safety implications
- For regulatory filings or approvals

---

### `source-hardened-direct-pdf-check`

**Definition:** The content has been directly cross-checked against the actual Doc 9869 PDF text and page images.

**What was done:**
- Page author (or designated reviewer) opened the source PDF
- Specific claims, values, and table entries were compared against the source
- Verification was documented in a source hardening log note
- The page's `modified` date reflects the last verification pass

**What was NOT done:**
- Verification against the latest ICAO amendment (the PDF may not be the current edition)
- Cross-validation with current State regulations or AIP entries
- Peer review by a second qualified person

**When to trust this level:**
- For implementation planning
- For compliance matrix development
- For evidence ladder construction
- As input to safety assessments (but not as the assessment itself)

**When to verify further:**
- If the page's `modified` date is older than 12 months (Doc 9869 may have been amended)
- If your State has published newer or additional requirements
- For formal submission to a State authority

---

### `peer-reviewed` (not yet implemented — aspirational)

**Definition:** The page has been reviewed by at least one additional qualified person who independently verified the content against the source.

**What this would require:**
- A second reviewer with PBCS domain knowledge
- Independent source check against Doc 9869
- Agreement on factual accuracy
- Reviewer credentials documented

**Status:** This level is aspirational. No pages currently carry this badge.

---

### `regulatory-cross-checked` (not yet implemented — aspirational)

**Definition:** The content has been validated against a specific State's regulatory requirements (regulations, AIP, SUPP) in addition to Doc 9869.

**What this would require:**
- Verification against a named State's published requirements
- Source citation to the specific AIP entry, regulation, or SUPP reference
- Review date reflecting the currency of the regulatory source

**Status:** This level is aspirational. No pages currently carry this badge. Institutions should add this level when they layer regulatory evidence onto the KB.

---

## How verification is performed

### Source hardening workflow

1. **Select** the page to verify
2. **Open** the source PDF at the referenced page(s)
3. **Compare** each claim, value, and table entry against the source
4. **Document** findings in a verification log note
5. **Update** the page's `verification_status` and `modified` date
6. **Log** the pass in a source hardening log (e.g., `99-Logs/`)

### What gets checked

| Content type | Check |
|---|---|
| **Conceptual claims** | Does Doc 9869 actually say this? |
| **Numeric values** | Does the source table contain these exact numbers? |
| **Source routes** | Do the cited sections and pages actually exist and contain this content? |
| **Stakeholder assignments** | Does Doc 9869 assign this responsibility to this actor? |
| **Procedural sequences** | Is the order correct per the source? |

### What does NOT get checked

- Currency against the latest ICAO amendment
- Compliance with specific State regulations
- Operational validity for a specific airspace or operator
- Accuracy of external references (RTCA/EUROCAE standards) beyond Doc 9869's reference list

---

## For institutions using this KB

> [!important] Your responsibility
> The verification badges in this KB reflect checks against Doc 9869 as extracted. They do not reflect:
> - Your State's current regulatory requirements
> - Your specific operational context
> - Your aircraft/operator/service-provider configuration
>
> Before using any KB content for formal compliance, you must verify it against the current source document and your applicable regulations.

### How to add your own verification layer

1. Fork this KB
2. Create a private evidence folder (e.g., `_private/`)
3. For each page you rely on:
   - Verify against your State's current AIP/SUPP
   - Add your own `verification_status: regulatory-cross-checked-<STATE>` badge
   - Document your check in a private log
4. Consider contributing source-hardened verification back to the upstream KB

---

## Verification status summary

As of the last source hardening pass (2026-05-06):

| Badge | Count | Typical pages |
|---|---|---|
| `source-linked` | ~80 pages | Most concept and navigation pages |
| `source-hardened-direct-pdf-check` | ~10 pages | Responsibility matrix, compliance matrix, key concept pages |
| `peer-reviewed` | 0 | Not yet implemented |
| `regulatory-cross-checked` | 0 | Not yet implemented — institution layer |

---

## Related

- [[Source Hardening Log - 2026-05-06]] — last verification pass
- [[Appendix B RCP Table Verification]] — table verification detail
- [[Appendix C RSP Table Verification]]
- [[Appendix D and E Monitoring Table Verification]]
- [[Source - ICAO Doc 9869]] — extraction method and source identity
- [[PBCS Evidence Ladder]] — how claims trace to evidence
