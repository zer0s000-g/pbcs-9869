---
title: Contributor Guide
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "governance", "meta"]
---

# Contributor Guide

> [!summary] TL;DR
> How to contribute to the PBCS Doc 9869 Knowledge Base. Whether you're fixing a typo, adding a regional mapping, or performing a verification pass — this guide covers the process.

---

## Ways to contribute

### 1. Fix errors (typos, broken links, incorrect claims)

If you find an error in any page:
1. Open an issue on the [GitHub repository](https://github.com/zer0s000-g/pbcs-9869/issues)
2. Describe the page, the error, and what the correct content should be
3. If you know the Doc 9869 source reference, include it

Or submit a pull request directly with the fix.

### 2. Add regional regulatory mapping

The `11-Regulatory-Mapping/` directory is designed for expansion. To add a new region:

1. Copy the template from [[APAC PBCS Regulatory Mapping]]
2. Fill in: airspace blocks, prescribed specs, States, monitoring programmes, AIP structure
3. Add a clear disclaimer: "Verify against current State AIP"
4. Submit as a pull request

### 3. Perform verification passes

If you have access to the Doc 9869 PDF and want to upgrade a page from `source-linked` to `source-hardened-direct-pdf-check`:

1. Open the page in your editor
2. Open the source PDF to the referenced section
3. Verify each claim against the source text
4. Document your check in a new `99-Logs/` note
5. Update the page's `verification_status` and `modified` date
6. See [[Verification Standards]] for the full process

### 4. Add worked examples or case studies

Real (anonymized) implementation experience is extremely valuable:
- Follow the format in [[PBCS Compliance Worked Example]]
- Use fictional names but realistic data
- Include lessons learned
- Add to `09-Syntheses/`

---

## Formatting standards

### File naming

- Use the page title as the filename: `Required Communication Performance.md`
- Spaces are fine — Quartz normalizes them to hyphens for URLs
- No special characters except hyphens and spaces

### Frontmatter

Every page must have YAML frontmatter between `---` fences:

```yaml
---
title: Page Title
doc_source: ICAO Doc 9869, Performance-based Communication and Surveillance Manual, Second Edition, 2017
status: draft
verification_status: source-linked
tags: ["pbcs", "relevant-tag"]
---
```

### Wikilinks

- Use `[[Page Name]]` syntax — exactly the target page's title
- Quartz resolves `[[My Page]]` to `My-Page.html`
- Always create the linked page, or the link will be broken

### Callout boxes

Use Obsidian callout syntax:

```
> [!note] Title
> Content

> [!warning]
> Content without a custom title

> [!tip]
> Content

> [!example]
> Content
```

Available types: `note`, `info`, `tip`, `example`, `warning`, `caution`, `danger`, `important`, `summary`, `question`.

### Tables

Use pipe-table format. Every row must have the same number of columns:

```markdown
| Header 1 | Header 2 |
|---|---|
| Cell 1 | Cell 2 |
```

Do not use `||` as an empty cell — use a space: `| |`.

---

## Pull request process

### Before submitting

1. Run a local build to verify no errors:
   ```
   npx quartz build
   ```
2. Check for broken wikilinks:
   ```
   grep -r '\[\[' content/ | grep -oE '\[\[([^]]+)\]\]' | sed 's/\[\[//g; s/\]\]//g' | while read link; do
     [ ! -f "content/${link// /-}.md" ] && echo "MISSING: content/${link// /-}.md"
   done
   ```
3. Verify no local paths or private data:
   ```
   grep -rE '/Users/|/home/|api_key|token|secret' content/ | grep -v node_modules
   ```

### Submitting

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-change`
3. Commit with a descriptive message: `region: add NAT regulatory mapping`
4. Push to your fork and open a PR against `zer0s000-g/pbcs-9869/main`

### Review criteria

PRs are reviewed for:
- ✅ Factual accuracy against Doc 9869
- ✅ Proper frontmatter format
- ✅ No broken wikilinks
- ✅ No local paths or private data
- ✅ Appropriate verification status
- ✅ TL;DR summary for new concept pages

---

## Issue templates

### Bug report

```
**Page:** [URL or page name]
**Issue:** [What's wrong]
**Expected:** [What it should say]
**Source reference:** [Doc 9869 section/page if applicable]
```

### Content request

```
**Topic:** [What's missing]
**Audience:** [Who needs this — operator, ANSP, State, etc.]
**Source reference:** [Doc 9869 section if applicable]
**Why it matters:** [How this would help users]
```

### Regional mapping request

```
**Region:** [APAC, NAT, AFI, CAR/SAM, MID, EUR]
**Airspace blocks:** [Which blocks and FIRs]
**Known specs:** [RCP/RSP prescribed, if known]
**Source:** [Doc 7030 reference or AIP, if available]
```

---

## Style conventions

### Terminology

- Use "Doc 9869" (not "Document 9869" or "PBCS Manual" — though the latter is acceptable as clarification)
- "RCP" and "RSP" — always capitalized
- "CPDLC" and "ADS-C" — always all-caps
- "State" (capitalized) when referring to State authority
- "operator" (lowercase) when referring to an aircraft operator generically

### Page structure

New concept pages should follow this order:
1. TL;DR callout
2. Main content (what and why)
3. Examples or worked scenarios
4. Source basis
5. Related notes

### Length

- Concept pages: 500-3000 words — enough to explain the concept without being encyclopedic
- Synthesis/template pages: whatever the content requires
- Log pages: brief and dated

---

## Code of Conduct

- Be respectful and professional
- Cite your sources
- Don't publish proprietary or controlled ICAO content — paraphrase and reference, don't copy verbatim
- If you're unsure about licensing, ask before contributing

---

## Related

- [[Verification Standards]] — what badges mean
- [[Institution Adaptation Guide]] — forking and customizing
- [[Changelog]] — version history
- [GitHub Repository](https://github.com/zer0s000-g/pbcs-9869)
