# Salesforce Development Rules & Best Practices Reference Guide

**Author:** Business Applications Engineering  
**Scope:** Salesforce CLI (`sf`), Model Context Protocol (`@salesforce/mcp`), Metadata API, & FLS Security  
**Date:** July 19, 2026

---

## Executive Abstract

The Salesforce Lightning Platform is a heavily stateful, cloud-hosted multi-tenant engine. Unlike traditional database development, changes made in local source code do not alter the platform until deployed, and schema changes deployed without explicit security permissions result in hidden "ghost fields." This document establishes mandatory engineering rules, architectural philosophies, and operational standards for developing with the Salesforce CLI (`sf`) and AI agent protocol tools (`@salesforce/mcp`).

---

## Section 1: Statefulness & Source-Driven Development Rules

### Rule 1.1: Local Repository is the Single Source of Truth (SSOT)

- **Directive:** Always create and edit XML metadata files, Apex classes, and LWC components locally on disk before deploying to Salesforce Cloud.
- **Rationale:** Making manual point-and-click changes directly in the Salesforce Setup GUI without pulling them back via `sf project retrieve start` causes source tracking drift and version control conflicts.

### Rule 1.2: Atomic Schema & Security Deployments

- **Directive:** Always deploy object schema directories (`objects/<CustomObject>`) and profile security directories (`profiles/`) together in a single atomic command.
- **CLI Example:**
  ```bash
  sf project deploy start \
    -d force-app/main/default/objects/<CustomObject> \
    -d force-app/main/default/profiles \
    -o <target-org-alias> \
    --json
  ```

### Rule 1.3: The Roll-Forward Rule (No Destructive Rollbacks Allowed)

- **Directive:** **Destructive rollbacks are strictly prohibited.** When deployment errors, missing FLS permissions, or schema flaws occur, engineers MUST NOT attempt to delete or roll back org metadata state. Always fix the issue locally in source code and **roll forward** with a patch deployment.
- **Rationale:** Attempting destructive metadata rollbacks in multi-tenant environments risks wiping production record data, corrupting database foreign keys, and breaking dependent Apex/LWC components. Roll-forward patch deployments preserve database integrity and maintain clean version history.

---

## Section 2: Security & Field-Level Security (FLS) Rules

### Rule 2.1: The Atomic Schema + FLS Provisioning Rule (Preventing "Ghost Fields")

- **Directive:** Every custom field (`CustomField`) MUST have a corresponding profile permission (`fieldPermissions`) appended to `Admin.profile-meta.xml` and deployed atomically with it (except fields with `<required>true</required>` or `MasterDetail` types, which encapsulate security automatically).
- **The "Ghost Field" Anti-Pattern:** Deploying a field without FLS instantiates the column in the database, but Salesforce hides the field from all user profiles by default. This causes:
  1. The field to be 100% invisible in the GUI layout.
  2. SOQL queries referencing the field to fail with `No such column`.
  3. Platform API verification checks to fail.
- **Generic Stream Editing Pattern (`sed`):**
  ```bash
  sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field><CustomObject>.<CustomField></field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
  ```

### Rule 2.2: Master-Detail Relationship FLS Exception Rule

- **Directive:** **NEVER** append explicit `fieldPermissions` for Master-Detail relationship fields (`type=MasterDetail`).
- **Rationale:** Master-Detail fields automatically inherit security and visibility controls from the parent object (`ControlledByParent`). Attempting to deploy profile `fieldPermissions` for a Master-Detail field causes the Metadata API deployment to fail (`FieldPermissions cannot be specified for Master-Detail field`).

### Rule 2.3: Required Field FLS Encapsulation Rule

- **Directive:** **NEVER** append explicit `fieldPermissions` for fields configured with `<required>true</required>`.
- **Rationale:** Fields marked mandatory automatically grant universal visibility to all profiles because users must be able to input values upon record creation. Attempting to deploy profile `fieldPermissions` for a required field causes the Metadata API deployment to reject the deployment (`You cannot deploy to a required field`).

### Rule 2.4: Lookup Relationship Deletion Constraints

- **Directive:** Always explicitly define `<deleteConstraint>SetNull</deleteConstraint>` or `<deleteConstraint>Restrict</deleteConstraint>` on Lookup relationship fields.
- **Rationale:** Omitting deletion constraints on Lookup fields defaults to unsafe deletion behavior. `SetNull` safely clears the foreign key if the referenced parent record is deleted.

---

## Section 3: CLI & MCP Protocol Execution Rules

### Rule 3.1: Explicit Target Org Overrides (`-o` / `target_org`)

- **Directive:** Always specify explicit target org flags in CLI commands (`-o <target-org-alias>`) and MCP tool calls (`"target_org": "<target-org-alias>"`).
- **Rationale:** Development tools frequently display `"No Default Org Set"` when workspace config keys are missing. Explicit target flags bypass default fallbacks by leveraging local OAuth 2.0 refresh tokens stored in `~/.sf/tokens.json`.

### Rule 3.2: Non-Interactive Stream Editing (`sed`)

- **Directive:** Use non-interactive Stream Editing (`sed -i '/<\/Profile>/i ...'`) to insert profile permissions directly above `</Profile>`.
- **Rationale:** Serves as the exact non-interactive CLI equivalent of checking visibility boxes in the Salesforce Setup GUI wizard.

### Rule 3.3: Tooling API for Schema Inspection

- **Directive:** Always pass `--use-tooling-api` (`sf data query --use-tooling-api`) or MCP `"use_tooling_api": true` when querying `FieldDefinition` metadata.
- **Rationale:** Standard SOQL queries fail when inspecting metadata definitions. Tooling API queries expose internal data types (`Currency(16, 2)`, `Master-Detail`, `Lookup`, `Text Area`).

### Rule 3.4: The Hybrid SFDX CLI + `--json` Protocol

- **Directive:** Execute developer CLI activities using **hands-on SFDX CLI commands appended with the `--json` flag** (`sf project deploy start ... --json` and `sf data query ... --json`).
- **Rationale:** Guarantees **100% hands-on developer learning retention** (mastering flags like `-d`, `-o`, `-q`) combined with **100% deterministic JSON payload traceability** matching MCP protocol auditability standards.

---

## Section 4: Version Control & Shipping Hygiene Rules

### Rule 4.1: Feature Branch Isolation

- **Directive:** All work must be conducted on feature-isolated Git branches (`feature/...`). Never commit directly to `main` or `master`.

### Rule 4.2: Strict Shipping Prohibition

- **Directive:** Never run `git push`, open Pull Requests (`gh pr create`), or merge code unless explicitly commanded by the user in that exact turn.

### Rule 4.3: Uncommitted Working Tree Review

- **Directive:** Leave experimental visual formatting, documentation updates, and schema refactoring uncommitted in the local working tree until the user reviews and explicitly approves the rendering.

### Rule 4.4: File Editing vs. Command Execution Boundaries

- **Directive:** The AI agent is **100% permitted** to create, edit, and refine workspace files (`write_to_file`, `replace_file_content`) and inspect the codebase (`view_file`, `grep_search`).
- **Prohibition:** The AI agent **MUST NOT** execute terminal commands (`run_command`) or perform Git operations (`git commit`, `git push`, `gh pr create`) unless explicitly commanded by the user in that exact turn. All CLI commands belong to the developer's hands-on terminal workflow.
