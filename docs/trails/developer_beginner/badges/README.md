# Trailhead Badges Architecture & Git Branching Protocol

**Scope:** All Developer Beginner Trailhead Badges (`docs/trails/developer_beginner/badges/`)  
**Author:** Business Applications Engineering  
**Date:** July 19, 2026

---

## Overview

This directory (`docs/trails/developer_beginner/badges/`) contains the technical reports, solution blueprints, and execution protocols for all Salesforce developer training badges in the **Developer Beginner** trail.

---

## Execution Paradigms & The Hybrid CLI `--json` Protocol

To maximize both hands-on developer learning retention and machine-readable payload traceability, activities in this trail adhere to the following execution standards:

- **Badges 01–04 (Baseline & MCP Evaluation):** Demonstrated standard terminal CLI workflows and autonomous `@salesforce/mcp` protocol RPC tool calls.
- **Badges 05 Onwards (The Hybrid SFDX CLI + `--json` Protocol):** All activities from Badge 05 onwards execute using **hands-on SFDX CLI commands appended with the `--json` flag** (`sf project deploy start ... --json` and `sf data query ... --json`).

### Why the Hybrid `--json` Protocol is the Optimal Developer Standard:

1. **100% Hands-On CLI Mastery:** Engineers execute terminal commands, mastering SFDX flags (`-d`, `-o`, `-q`, `--use-tooling-api`).
2. **100% Deterministic JSON Traceability:** Appending `--json` forces the CLI to output structured, unformatted JSON payloads matching MCP RPC standards for auditability.
3. **Clean Technical Reports:** Technical blueprints document the exact CLI command alongside the structured JSON response payload.

---

## Mandatory Git Version Control & Feature Branching Protocol

Before executing schema creation, Apex development, security provisioning, or cloud deployment for ANY unit in ANY badge, engineers MUST adhere to strict feature-branch isolation:

1. **Never develop or commit directly on `main` or `master`.** Always preserve `master` as the clean, production-ready baseline.
2. **Branch Out First:** Before starting any unit task, create a dedicated, feature-isolated branch from `master` (e.g. `git checkout -b feature/<badge-unit-name>`).
3. **Atomic Unit Development:** Keep schema XML metadata (`CustomField`), Apex code, security profiles (`fieldPermissions`), and unit technical documentation organized together on the feature branch.
4. **Ship via Pull Request:** Ship completed unit deliverables to `master` strictly through code review Pull Requests (`gh pr create`) and squashed merges (`gh pr merge --squash --delete-branch`).

---

## Badges Directory Sitemap

|   #    | Badge Name                                     | Directory Path                                                                                                            | Execution Paradigm & Status                                  |
| :----: | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------- |
| **01** | **Agentforce 360 Platform Development Basics** | **[01_agentforce_360.../](01_agentforce_360_platform_development_basics/AGENTFORCE_360_PLATFORM_DEVELOPMENT_BASICS.md)**  | Standard Overview **[COMPLETED]**                            |
| **02** | **Get Started with Salesforce Development**    | **[02_get_started.../](02_get_started_with_salesforce_development/GET_STARTED_WITH_SALESFORCE_DEVELOPMENT.md)**           | Standard Overview **[COMPLETED]**                            |
| **03** | **Quick Start: Tour the Sample App Gallery**   | **[03_quick_start.../](03_quick_start_tour_the_sample_app_gallery/QUICK_START_TOUR_THE_SAMPLE_APP_GALLERY.md)**           | Standard Overview **[COMPLETED]**                            |
| **04** | **Data Modeling**                              | **[04_data_modeling/](04_data_modeling/DATA_MODELING.md)**                                                                | CLI & MCP Protocol Evaluation **[PASSED & VERIFIED]**        |
| **05** | **Lightning Experience Customization**         | **[05_lightning_experience_customization/](05_lightning_experience_customization/LIGHTNING_EXPERIENCE_CUSTOMIZATION.md)** | **Hybrid SFDX CLI + `--json` Protocol** ⏳ **[IN PROGRESS]** |
| **06** | **Formulas and Validations**                   | **[06_formulas_and_validations/](06_formulas_and_validations/FORMULAS_AND_VALIDATIONS.md)**                               | **Hybrid SFDX CLI + `--json` Protocol** ⏸️ **[PENDING]**     |
| **07** | **Flow Builder Basics**                        | **[07_flow_builder_basics/](07_flow_builder_basics/FLOW_BUILDER_BASICS.md)**                                              | **Hybrid SFDX CLI + `--json` Protocol** ⏸️ **[PENDING]**     |
| **08** | **Apex Basics & Database**                     | **[08_apex_basics_and_database/](08_apex_basics_and_database/APEX_BASICS_AND_DATABASE.md)**                               | **Hybrid SFDX CLI + `--json` Protocol** ⏸️ **[PENDING]**     |
| **09** | **Apex Triggers**                              | **[09_apex_triggers/](09_apex_triggers/APEX_TRIGGERS.md)**                                                                | **Hybrid SFDX CLI + `--json` Protocol** ⏸️ **[PENDING]**     |
| **10** | **Lightning Web Components Basics**            | **[10_lightning_web_components_basics/](10_lightning_web_components_basics/LIGHTNING_WEB_COMPONENTS_BASICS.md)**          | **Hybrid SFDX CLI + `--json` Protocol** ⏸️ **[PENDING]**     |
