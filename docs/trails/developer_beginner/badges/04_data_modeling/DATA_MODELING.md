# Trailhead Badge Index: Data Modeling

**Trail:** Developer Beginner  
**Badge 04:** Data Modeling  
**Total Points:** +1,500 Points  
**Date Completed:** July 18, 2026  
**Date Re-Polished (Pipeline Compliance):** July 21, 2026

---

## Overview

This badge covers custom objects, field types, and object relationships for DreamHouse Realty in Salesforce — the foundation the rest of the trail builds on (`Property__c`, `Offer__c`, and `Favorite__c` are all created here). All tasks in this badge adhere to the **[Global Badge Git Branching Protocol](../../DEVELOPER_BEGINNER_TRAIL.md#mandatory-git-version-control--feature-branching-protocol)**.

Each unit doc was originally drafted before `docs/reference/PIPELINE.md` existed and documented only the Hands-On Challenge. All three were re-polished against the pipeline on July 21, 2026: the previously-missing Guided Activity content (harvested separately and archived under [`raw/`](raw/)) was folded in, every requirement re-tagged to the `[REQ-4.<unit>.<G|C><item>.<step>]` format, and every field verified against the actual deployed metadata in `force-app/` rather than trusted as originally written. That verification pass surfaced two real findings worth knowing before touching this badge's objects again — see the table below.

---

## Table of Contents

- [Overview](#overview)
- [Badge Units Index](#badge-units-index)
  - [1. [Unit 1: Optimize Customer Data with Standard and Custom Objects](UNIT_1_STANDARD_CUSTOM_OBJECTS.md)](#1-unit-1-optimize-customer-data-with-standard-and-custom-objectsunit_1_standard_custom_objectsmd)
  - [2. [Unit 2: Create Object Relationships](UNIT_2_OBJECT_RELATIONSHIPS.md)](#2-unit-2-create-object-relationshipsunit_2_object_relationshipsmd)
  - [3. [Unit 3: Work with Schema Builder](UNIT_3_WORK_WITH_SCHEMA_BUILDER.md)](#3-unit-3-work-with-schema-builderunit_3_work_with_schema_buildermd)
- [Findings Surfaced During Pipeline Re-Polish](#findings-surfaced-during-pipeline-re-polish)
- [Developer Insight: Target Org Flags vs. VS Code "No Default Org Set"](#developer-insight-target-org-flags-vs-vs-code-no-default-org-set)
- [Execution Protocol](#execution-protocol)

## Badge Units Index

### 1. [Unit 1: Optimize Customer Data with Standard and Custom Objects](UNIT_1_STANDARD_CUSTOM_OBJECTS.md)

- **Focus:** Guided Activity — custom object `Property__c` and required Currency field `Price__c`. Hands-On Challenge — custom object `Offer__c` (Auto Number `OF-{0000}`), Currency field `Offer_Amount__c`, and Date field `Target_Close_Date__c`.
- **Tooling Paradigm:** 100% hand-authored SFDX CLI (`sf project deploy start` & `sf data query --use-tooling-api`), all `[CLI]`.
- **Status:** **COMPLETED & VERIFIED**

---

### 2. [Unit 2: Create Object Relationships](UNIT_2_OBJECT_RELATIONSHIPS.md)

- **Focus:** Guided Activity — custom object `Favorite__c` with a Lookup to `Contact` and a Master-Detail to `Property__c`. Hands-On Challenge — the same two relationship types added to `Offer__c` (Master-Detail to `Property__c`, Lookup to `Contact`).
- **Tooling Paradigm:** 100% hand-authored SFDX CLI, all `[CLI]`. Originally executed via the Salesforce MCP server (`@salesforce/mcp`) before this badge's CLI-first re-polish — preserved as a historical finding in the unit doc's Post-Mortem section, not as this doc's primary framing.
- **Status:** **COMPLETED & VERIFIED**

---

### 3. [Unit 3: Work with Schema Builder](UNIT_3_WORK_WITH_SCHEMA_BUILDER.md)

- **Focus:** Guided Activity — Schema Builder tour (Auto-Layout visualization plus an explicitly open-ended demo object/field Trailhead itself doesn't grade; no fixed artifact, so it carries no Requirement IDs). Hands-On Challenge — required Text Area field `Street_Address__c` on `Property__c`.
- **Tooling Paradigm:** 100% hand-authored SFDX CLI, `[CLI]` for the Challenge; Part 1 has no deployable artifact.
- **Status:** **COMPLETED & VERIFIED**

---

## Findings Surfaced During Pipeline Re-Polish

Verifying every field in this badge against the deployed `force-app/` metadata (rather than trusting the original pre-pipeline docs as written) surfaced two things worth knowing before reusing or extending this badge's objects:

1. **`Offer_Amount__c` precision was documented wrong.** The original Unit 1 doc said `<precision>16</precision>`; the deployed field is actually `<precision>18</precision>` (Salesforce's `precision` is total digits — integer + scale — not the Setup wizard's "Length" field). Corrected in the Unit 1 rewrite.
2. **`Favorite__c` has an open Ghost Field / Ghost Tab gap, unresolved.** `Admin.profile-meta.xml` has zero entries for `Favorite__c` — no `fieldPermissions` for its `Contact__c` Lookup field and no `tabVisibilities` for its custom tab — and there's no `Favorite__c.tab-meta.xml` in source at all. The Guided Activity that created these was executed entirely through the Trailhead GUI wizard before this repo's CLI-first, retrieve-everything standard existed, and the resulting grants were never pulled back into local source (Rule 1.1 drift). This is the same anti-pattern documented for `Energy_Audit__c` in Badge 05 Unit 1 (`docs/REPORT.md`), just never caught here. The Unit 2 doc's CLI payload is written to close this gap the next time it's actually deployed (Stage 4) — see its Post-Mortem section for the full trace.

---

## Developer Insight: Target Org Flags vs. VS Code "No Default Org Set"

> **Key Takeaway:**
>
> - **VS Code "No Default Org Set":** VS Code's status bar displays "No Default Org Set" when no workspace-level fallback key (`target-org`) is configured in `.sf/config.json`.
> - **Why Deploys & Checks Succeed:** Passing explicit org alias flags (`-o trailhead-playground`) in CLI commands bypasses workspace defaults entirely. The CLI looks up the saved OAuth refresh tokens stored locally on your machine for `trailhead-playground` and authenticates silently without requiring re-login.
> - **Fixing the VS Code Status Bar:** Running `sf config set target-org trailhead-playground` sets the workspace default so VS Code's status bar displays `trailhead-playground`.

---

## Execution Protocol

All activities in this badge follow the **[Global Badge Git Branching Protocol](../../DEVELOPER_BEGINNER_TRAIL.md#mandatory-git-version-control--feature-branching-protocol)** using 100% hands-on **SFDX CLI terminal commands** (`sf project deploy start` & `sf data query`), per Rule 3.4 in `docs/reference/SALESFORCE_DEVELOPMENT_RULES.md`.
