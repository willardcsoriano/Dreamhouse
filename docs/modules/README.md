# Trailhead Modules Architecture & Git Branching Protocol

**Scope:** All Developer Beginner Trailhead Modules (`docs/modules/`)  
**Author:** Business Applications Engineering  
**Date:** July 19, 2026

---

## Overview

This directory (`docs/modules/`) contains the modular technical reports, solution blueprints, and execution protocols for all Salesforce developer training modules.

---

## Mandatory Git Version Control & Feature Branching Protocol

Before executing schema creation, Apex development, security provisioning, or cloud deployment for ANY unit in ANY module, engineers MUST adhere to strict feature-branch isolation:

1. **Never develop or commit directly on `main` or `master`.** Always preserve `master` as the clean, production-ready baseline.
2. **Branch Out First:** Before starting any unit task, create a dedicated, feature-isolated branch from `master` (e.g. `git checkout -b feature/<module-unit-name>`).
3. **Atomic Unit Development:** Keep schema XML metadata (`CustomField`), Apex code, security profiles (`fieldPermissions`), and unit technical documentation organized together on the feature branch.
4. **Ship via Pull Request:** Ship completed unit deliverables to `master` strictly through code review Pull Requests (`gh pr create`) and squashed merges (`gh pr merge --squash --delete-branch`).

---

## Modules Directory Sitemap

| Module Name       | Directory Path                                                    | Description & Status                                                                                                                |
| :---------------- | :---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **Data Modeling** | **[docs/modules/data_modeling/](data_modeling/DATA_MODELING.md)** | Custom Objects, Auto-Numbering, Master-Detail & Lookup Relationships, Schema Builder (`Street_Address__c`). **[PASSED & VERIFIED]** |
