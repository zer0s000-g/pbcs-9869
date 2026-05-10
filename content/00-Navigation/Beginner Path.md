---
title: Beginner Path
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "navigation", "beginner"]
---

# Beginner Path

> This path takes about **15 minutes**. When you finish, you'll understand what PBCS is, why it exists, and who does what. No prior knowledge needed.

---

## 🎯 What you'll learn

- Why PBCS exists and what problem it solves
- What RCP and RSP actually mean (with real examples)
- Who is responsible for what in a PBCS operation
- How to think about the full PBCS lifecycle

---

## 📍 Step 1: The big picture (5 min)

Before the details, understand the **why**.

Read: [[Performance-Based Communication and Surveillance]]

Key question to ask yourself: *"Before PBCS, how did we know if a communication or surveillance system was good enough?"*

- [ ] I understand the problem PBCS solves
- [ ] I can name the two pillars: RCP (communication) and RSP (surveillance)

---

## 📍 Step 2: The two pillars (5 min)

PBCS has two specifications. They're similar concepts, applied to different domains.

Read: [[RCP vs RSP]]

You can also read the individual pages for more depth:
- [[Required Communication Performance]]
- [[Required Surveillance Performance]]

Key question: *"If I'm using CPDLC to talk to ATC, which specification applies to me?"*

- [ ] I can explain what RCP covers versus what RSP covers
- [ ] I know which appendix in Doc 9869 contains which specification

---

## 📍 Step 3: Who does what? (5 min)

PBCS is a team sport. Understanding the roles prevents the most common implementation mistake — assuming someone else is handling your piece.

Read: [[PBCS Responsibility Matrix]]

Key question: *"If I'm an aircraft operator, what do I need to prove versus what my ANSP needs to prove?"*

- [ ] I can name the six stakeholders and their main PBCS responsibility
- [ ] I understand that Doc 9869 routes responsibilities but doesn't prove anyone is currently compliant

---

## ✅ You did it

You now have the mental model for PBCS. Where to go from here:

| You are a... | Next step |
|---|---|
| **Regulator / State authority** | [[Compliance Path]] — how approvals work |
| **ANSP / service provider** | [[Implementation Path]] — sequence and checklists |
| **Operator / pilot / dispatcher** | [[Operational Approval]] — what your aircraft needs |
| **Engineer / avionics specialist** | [[Communication System Chain]] / [[Surveillance System Chain]] |
| **Just curious** | [[PBCS MOC]] — explore freely |

---

> [!tip] Learning tip
> Use the **graph view** (right sidebar) to see how concepts connect. Click any node to jump to that page. It's a faster way to explore than clicking through lists.

---

## 📖 Minimal mental model (TL;DR)

- **PBCS** = the performance-based approach to specifying, approving, and monitoring communication and surveillance for ATM
- **RCP** = communication performance (how fast/reliable is my CPDLC or SATVOICE?)
- **RSP** = surveillance performance (how fast/reliable is my ADS-C position report?)
- **Doc 9869** = the ICAO manual that links specs → stakeholders → evidence → monitoring
