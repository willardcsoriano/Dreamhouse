# Confluence Documentation Standard

## Overview

This document defines the writing and formatting bar every Markdown file under `docs/confluence/` must clear before it is published to the corporate Confluence wiki. It exists because the backlog in `wiki_documentation_list.md` commits us to a dozen SOPs and reference guides that will be read by engineers who never touched the systems they describe, so consistency in structure, voice, and security handling matters more than it would for throwaway notes. The standard covers required page structure (metadata block, Overview, Prerequisites, Procedure, Verification, Troubleshooting, References, Revision History), voice and formatting rules, command/code documentation requirements, and non-negotiable security and PII handling. Anyone drafting or reviewing a backlog doc should treat this file as the acceptance bar, not a suggestion, and run the checklist at the end before marking a document Approved.

## Table of Contents

- [Overview](#overview)
- [Purpose & Scope](#purpose-scope)
- [Required Metadata Block](#required-metadata-block)
- [Required Structure](#required-structure)
- [Voice & Style](#voice-style)
- [Formatting Conventions](#formatting-conventions)
- [Command & Code Documentation](#command-code-documentation)
- [Security, Secrets & PII](#security-secrets-pii)
- [Diagrams & Screenshots](#diagrams-screenshots)
- [Linking & Cross-References](#linking-cross-references)
- [File Naming & Confluence Placement](#file-naming-confluence-placement)
- [Review, Approval & Deprecation](#review-approval-deprecation)
- [Pre-Publish Checklist](#pre-publish-checklist)

## Purpose & Scope

This standard applies to every Markdown file in `docs/confluence/` that is destined to become a Confluence page — SOPs, reference guides, onboarding checklists, policy docs. It does not govern `docs/trails/` (which follows `docs/reference/PIPELINE.md` instead) or any other doc set in this repo.

## Required Metadata Block

Every doc opens with this table immediately after its title, before the Overview:

| Field                          | Value                                                                   |
| ------------------------------ | ----------------------------------------------------------------------- |
| Owner                          | \<team or individual accountable for accuracy>                          |
| Status                         | Draft / In Review / Approved / Deprecated                               |
| Last Reviewed                  | YYYY-MM-DD                                                              |
| Review Cadence                 | Quarterly, or immediately after any process/tooling change it documents |
| Confluence Space / Parent Page | \<target location once published>                                       |

## Required Structure

In this order, skipping only what's genuinely not applicable:

1. **Title** (H1) — matches the Confluence page title exactly.
2. **Metadata block** — as above.
3. **Overview** — 3-5 sentences: why this doc exists, who it's for, what they'll be able to do after reading it.
4. **Prerequisites** — access, tooling, permissions, or prior reading needed before following the doc.
5. **Procedure / Body** — the actual content, headed to mirror the real workflow, not an arbitrary outline.
6. **Verification** — how a reader confirms they did it right (expected output, a query to run, a screen to check).
7. **Troubleshooting** — known issues and their resolutions, framed as Q&A or problem → fix pairs.
8. **References** — links to source docs, related SOPs, vendor documentation.
9. **Revision History** — table of Date, Author, Change.

## Voice & Style

- Second person, imperative mood: "Run `sf org login web`," not "You should run the command to log in."
- Active voice, plain language. Define any acronym or product-specific term on first use.
- One idea per sentence; short paragraphs. Long walls of text get broken into lists or subheadings.
- When referring to an unspecified person (a future reader, "the reviewer," "the on-call engineer"), use they/them rather than guessing a gender.

## Formatting Conventions

- Heading hierarchy: exactly one H1 (the title), H2 for major sections, H3 for sub-steps. Never skip a level.
- Numbered lists for anything sequential (steps to execute in order); bullets for anything that isn't ordered (options, considerations, a list of prerequisites).
- Every code block carries a language identifier — no bare triple-backtick fences.
- Callouts (`> **Note:**`, `> **Warning:**`, `> **Tip:**`) are used sparingly and only when the information changes what the reader should do next — not as decoration.
- Tables for anything comparative or structured (permission matrices, field lists, environment comparisons) rather than prose trying to describe a grid.

## Command & Code Documentation

- Every command block states its target environment explicitly (`-o <org-alias>`, `--env staging`, etc.) — never assume the reader knows which system it hits.
- Every non-trivial command gets a one-line comment directly above it stating its intent, not just what it literally does.
- No untested commands ship: an SOP only includes a command after it has actually been run successfully at least once. If a command is provided but genuinely unverified, the doc says so explicitly rather than implying otherwise.
- Destructive or irreversible commands (deletes, force operations, production deploys) get a `> **Warning:**` callout immediately above them, stating what's irreversible about it.

## Security, Secrets & PII

- Never paste real API keys, tokens, passwords, session IDs, org IDs, or client secrets — use placeholders (`<YOUR_TOKEN>`) even in "redacted-looking" examples.
- Never include real customer or employee data — names, emails, phone numbers, addresses, or any other PII — in example payloads, sample records, or screenshots. Use synthetic data.
- Screenshots are cropped to exclude anything showing real production data, and get descriptive alt text.
- Any doc that touches regulated data (GDPR, CCPA, HIPAA, PCI-DSS scope) flags that explicitly in the metadata block and names the applicable regime.

## Diagrams & Screenshots

- Prefer diagrams over screenshots for anything that will go stale on the next UI change.
- Every image has descriptive alt text — this is an accessibility requirement, not optional polish.
- Screenshots are annotated (arrows, boxes) rather than relying on surrounding prose alone to point at the relevant UI element.

## Linking & Cross-References

- Link to the single source of truth. Never fork or duplicate content that already lives in another SOP — link to it instead.
- No dead links: verify every link resolves before marking a doc Approved.
- External links to content that changes over time (vendor docs, RFCs) are dated ("as of July 2026") so a future reader knows how stale the reference might be.

## File Naming & Confluence Placement

- The Markdown file name mirrors the eventual Confluence page title in kebab-case (e.g., `version-control-workflow-sop.md`).
- The target Confluence space and parent page are recorded in the metadata block before the doc is published, not decided after the fact.

## Review, Approval & Deprecation

- Every doc has a named owner accountable for its accuracy, recorded in the metadata block.
- Minimum review cadence is quarterly, or immediately after any process or tooling change the doc describes.
- Status moves Draft → In Review → Approved → Deprecated. A deprecated doc stays published with a banner linking to its replacement — it is never silently deleted, to preserve the audit trail of what the org's process used to be.

## Pre-Publish Checklist

- [ ] Metadata block complete (Owner, Status, Last Reviewed, Space)
- [ ] Overview answers "why am I reading this" in under 5 sentences
- [ ] Every command has been run and confirmed working at least once
- [ ] No secrets, tokens, org IDs, or real PII anywhere in text or images
- [ ] All links resolve
- [ ] Destructive commands carry an explicit warning callout
- [ ] Reviewed by someone other than the author before Status moves to Approved
