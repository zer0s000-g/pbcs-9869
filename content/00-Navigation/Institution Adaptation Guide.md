---
title: Institution Adaptation Guide
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["guide", "navigation", "pbcs"]
---

# Institution Adaptation Guide

> [!summary] TL;DR
> How to fork this knowledge base, layer on your institution's regulatory and operational evidence, and maintain it as a living resource. For ANSPs, States, operators, and service providers.

---

## Why adapt this KB?

Doc 9869 provides the framework. This KB provides the source-routed reference. What's missing for your institution is:

- Your **State's specific regulations** — which RCP/RSP are actually prescribed in your AIP?
- Your **operational evidence** — which aircraft, operators, and providers are approved?
- Your **monitoring data** — what does your actual performance look like?
- Your **internal procedures** — who does corrective action in your organization?

This guide shows you how to add that layer.

---

## Step 1: Fork the repository

1. Go to https://github.com/zer0s000-g/pbcs-9869
2. Click **Fork** → create your own copy
3. Clone your fork locally:
```
git clone https://github.com/YOUR-ORG/pbcs-9869.git
cd pbcs-9869
npm install
```

---

## Step 2: Customize branding

Edit `quartz.config.ts`:

```ts
configuration: {
  pageTitle: "YOUR INSTITUTION — PBCS Knowledge Base",
  baseUrl: "YOUR-DOMAIN.com",  // or USERNAME.github.io/REPO
}
```

Edit `quartz/components/Head.tsx` line 87:

```tsx
<meta name="generator" content="YOUR INSTITUTION — PBCS Knowledge Base" />
```

Add your logo: replace `quartz/static/icon.png` with your institution's logo.

Rebuild:
```
npx quartz build
```

---

## Step 3: Add your private evidence layer

Create a private folder structure alongside the public content. This folder is **not committed** to the public repository — it stays in your private branch or separate repo.

Recommended structure:

```
pbcs-9869/
├── content/              # Public KB (shared with community)
│   └── ...               # (existing pages)
└── _institution/         # Private evidence layer
    ├── README.md          # Internal access and usage notes
    ├── regulatory/        # Your State's specific requirements
    │   ├── AIP-Entries.md          # Relevant AIP ENR sections
    │   ├── SUPP-Requirements.md    # Regional supplementary procedures
    │   └── State-Approvals.md      # Approval policies and forms
    ├── operational/       # Your live operational evidence
    │   ├── Approved-Operators.md   # Operator list with approval dates
    │   ├── Aircraft-Register.md    # Aircraft with PBCS capability
    │   ├── CSP-Contracts.md        # Service provider agreements
    │   └── Route-Applicability.md  # Which routes/airspace use PBCS
    ├── monitoring/        # Your monitoring data and reports
    │   ├── Monthly-Reports/        # Archived monitoring reports
    │   ├── Performance-Dashboard.md # Summary of current performance
    │   └── Problem-Reports/        # Corrective action records
    └── training/          # Institution-specific training materials
        ├── Operator-Training.md
        ├── ANSP-Training.md
        └── Competency-Checklist.md
```

> [!tip] Symlink for local dev
> For local preview, symlink your private evidence into `content/`:
> ```
> ln -s _institution/regulatory content/Institution-Regulatory
> ```
> Remove the symlink and add to `.gitignore` before pushing to public repo.

---

## Step 4: Add verification badges for your evidence

When you verify a public KB page against your State's requirements, add your own badge.

Example — adding a regulatory cross-check to the RCP 240/D page:

**In your fork's `content/04-RCP/RCP 240 D.md`, append:**

```markdown
---

## Institution verification

| Check | Status | Verified by | Date | Reference |
|---|---|---|---|---|
| India AIP ENR 1.8 prescribes RCP 240/D for Mumbai FIR | ✅ Verified | ATS Planning | 2026-05-10 | AIP India ENR 1.8-12 |
| Operator OA123 has valid approval | ✅ Verified | Flight Ops | 2026-05-10 | Approval ref: IND/CAA/PBCS/2026-001 |
| CSP Inmarsat contract includes data provision | ✅ Verified | Contracts | 2026-03-01 | Contract ref: CSP-2026-IOR-001 |
```

Update the page's frontmatter:

```
verification_status: regulatory-cross-checked-INDIA
```

---

## Step 5: Set up monitoring integration

If your institution runs a PBCS monitoring programme, integrate the data:

1. Create a `_institution/monitoring/Performance-Dashboard.md` that references the [[Quick Reference Card]] specs
2. For each monthly report, create a note in `_institution/monitoring/Monthly-Reports/YYYY-MM.md`
3. Link each report back to the relevant specification page (e.g., "See [[RCP 240 D]] for the required thresholds")

---

## Step 6: Maintain your fork

### Pull upstream improvements

When the public KB adds new content or fixes:

```
git remote add upstream https://github.com/zer0s000-g/pbcs-9869.git
git fetch upstream
git merge upstream/main
```

Your private evidence layer (`_institution/`) won't be affected — it's only in your fork.

### Contribute back

If you add source-hardened verification or new content that isn't institution-specific, contribute it back:

1. Make the changes in your fork's `content/` directory
2. Submit a pull request to the upstream repository
3. Include your verification log or source reference

---

## Step 7: Deploy your adapted KB

### Option A: GitHub Pages (recommended)

1. Go to your fork's Settings → Pages
2. Source: **GitHub Actions**
3. Under "Custom domain", enter your institution's domain (if applicable)
4. Check "Enforce HTTPS"
5. The existing `.github/workflows/deploy.yml` will handle the build

Update the workflow's `baseUrl` in `quartz.config.ts` before pushing.

### Option B: Internal server

```
cd pbcs-9869
npx quartz build
# Serve public/ from your internal web server
rsync -avz public/ user@internal-server:/var/www/pbcs/
```

### Option C: Private access only

Keep the Quartz site as internal documentation. Build locally:
```
npx quartz build --serve
```
Access at `http://localhost:8080` — no deployment needed.

---

## What to customize — checklist

| Item | Priority | Done? |
|---|---|---|
| Fork repository | Required | ☐ |
| Update `pageTitle` in `quartz.config.ts` | Required | ☐ |
| Update `baseUrl` in `quartz.config.ts` | Required | ☐ |
| Replace `icon.png` with your logo | Recommended | ☐ |
| Update meta generator tag in `Head.tsx` | Recommended | ☐ |
| Create `_institution/` structure | Recommended | ☐ |
| Add AIP/SUPP regulatory references | If applicable | ☐ |
| Add operator/aircraft approval evidence | If applicable | ☐ |
| Add CSP/SSP contract references | If applicable | ☐ |
| Add monitoring dashboard | If applicable | ☐ |
| Add institution verification badges | If applicable | ☐ |
| Deploy to GitHub Pages or internal server | Required | ☐ |

---

> [!note] Questions?
> See [[Frequently Asked Questions]] or the [[PBCS MOC]] for general PBCS queries. For adaptation-specific questions, open an issue on the GitHub repository.

---

## Related

- [[Verification Standards]] — what badges mean
- [[Quick Reference Card]] — key facts at a glance
- [[Frequently Asked Questions]] — real-world answers
- [[PBCS MOC]] — complete content map
