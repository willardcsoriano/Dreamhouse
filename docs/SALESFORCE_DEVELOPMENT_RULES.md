# Salesforce Development Rules & Best Practices Reference Guide

**Author:** Business Applications Engineering  
**Scope:** Salesforce CLI (`sf`), Model Context Protocol (`@salesforce/mcp`), Metadata API, & FLS Security  
**Date:** July 19, 2026

---

## Executive Abstract

The Salesforce Lightning Platform is a heavily stateful, cloud-hosted multi-tenant engine. Unlike traditional database development, changes made in local source code do not alter the platform until deployed, and schema changes deployed without explicit security permissions result in hidden "ghost fields." This document establishes mandatory rules and operational standards for developing with the Salesforce CLI (`sf`) and AI agent protocol tools (`@salesforce/mcp`).

---

## Section 1: Statefulness & Source-Driven Development Rules

### Rule 1.1: Local Repository is the Single Source of Truth (SSOT)

- **Directive:** Always create and edit XML metadata files, Apex classes, and LWC components locally on disk before deploying to Salesforce Cloud.
- **Rationale:** Making manual point-and-click changes directly in the Salesforce Setup GUI without pulling them back via `sf project retrieve start` causes source tracking drift and version control conflicts.

### Rule 1.2: Atomic Schema & Security Deployments

- **Directive:** Always deploy object schema directories (`objects/`) and profile security directories (`profiles/`) together in a single atomic command.
- **CLI Example:**
  ```bash
  sf project deploy start \
    -d force-app/main/default/objects/Offer__c \
    -d force-app/main/default/profiles \
    -o trailhead-playground
  ```

---

## Section 2: Security & Field-Level Security (FLS) Rules

### Rule 2.1: The Atomic Schema + FLS Provisioning Rule (Preventing "Ghost Fields")

- **Directive:** Every custom field (`CustomField`) MUST have a corresponding profile permission (`fieldPermissions`) appended to `Admin.profile-meta.xml` and deployed atomically with it.
- **The "Ghost Field" Anti-Pattern:** Deploying a field without FLS instantiates the column in the database, but Salesforce hides the field from all profiles by default. This causes:
  1. The field to be 100% invisible in the GUI.
  2. SOQL queries referencing the field to fail with `No such column`.
  3. Trailhead automated challenge verification to fail.
- **Mandatory `sed` Stream Editing Pattern:**
  ```bash
  sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Offer_Amount__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
  ```

### Rule 2.2: Master-Detail Relationship FLS Exception Rule

- **Directive:** **NEVER** append explicit `fieldPermissions` for Master-Detail relationship fields (`type=MasterDetail`).
- **Rationale:** Master-Detail fields automatically inherit security and visibility controls from the parent object (`ControlledByParent`). Attempting to deploy profile `fieldPermissions` for a Master-Detail field causes the Metadata API deployment to fail (`FieldPermissions cannot be specified for Master-Detail field`).

### Rule 2.3: Lookup Relationship Deletion Constraints

- **Directive:** Always explicitly define `<deleteConstraint>SetNull</deleteConstraint>` or `<deleteConstraint>Restrict</deleteConstraint>` on Lookup relationship fields.
- **Rationale:** Omitting deletion constraints on Lookup fields defaults to unsafe deletion behavior. `SetNull` safely clears the foreign key if the parent record is deleted.

---

## Section 3: CLI & MCP Protocol Execution Rules

### Rule 3.1: Explicit Target Org Overrides (`-o` / `target_org`)

- **Directive:** Always specify explicit target org flags in CLI commands (`-o trailhead-playground`) and MCP tool calls (`"target_org": "trailhead-playground"`).
- **Rationale:** VS Code frequently displays `"No Default Org Set"` when workspace config keys are missing. Explicit target flags bypass default fallbacks by leveraging local OAuth 2.0 refresh tokens stored in `~/.sf/tokens.json`.

### Rule 3.2: Non-Interactive Stream Editing (`sed`)

- **Directive:** Use non-interactive Stream Editing (`sed -i '/<\/Profile>/i ...'`) to insert profile permissions right above `</Profile>`.
- **Rationale:** Acts as the exact non-interactive CLI equivalent of checking visibility boxes in Step 3 of the Salesforce Setup GUI wizard.

### Rule 3.3: Tooling API for Schema Inspection

- **Directive:** Always pass `--use-tooling-api` (`sf data query --use-tooling-api`) or MCP `"use_tooling_api": true` when querying `FieldDefinition` metadata.
- **Rationale:** Standard SOQL queries fail when inspecting metadata definitions. Tooling API queries expose internal data types (`Currency(16, 2)`, `Master-Detail(Property)`, `Lookup(Contact)`).

### Rule 3.4: The Hybrid SFDX CLI + `--json` Protocol (Mandatory Badge 05 Onwards)

- **Directive:** From Badge 05 onwards, all developer activities MUST be executed using **hands-on SFDX CLI commands appended with the `--json` flag** (`sf project deploy start ... --json` and `sf data query ... --json`).
- **Rationale:** Standard terminal text logs can be noisy ASCII tables, whereas `--json` CLI output guarantees **100% hands-on developer learning retention** combined with **100% deterministic JSON payload traceability** matching MCP protocol auditability standards.

---

## Section 4: Version Control & Shipping Hygiene Rules

### Rule 4.1: Feature Branch Isolation

- **Directive:** All work must be conducted on feature-isolated Git branches (`feature/...`). Never commit directly to `main` or `master`.

### Rule 4.2: Strict Shipping Prohibition

- **Directive:** Never run `git push`, open Pull Requests (`gh pr create`), or merge code unless explicitly commanded by the user in that exact turn.

### Rule 4.3: Uncommitted Working Tree Review

- **Directive:** Leave experimental visual formatting, documentation updates, and schema refactoring uncommitted in the local working tree until the user reviews and explicitly approves the rendering.
