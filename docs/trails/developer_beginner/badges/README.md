# Trailhead Badges Architecture & Git Branching Protocol

**Scope:** All Developer Beginner Trailhead Badges (`docs/trails/developer_beginner/badges/`)  
**Author:** Business Applications Engineering  
**Date:** July 19, 2026

---

## Overview

This directory (`docs/trails/developer_beginner/badges/`) contains the technical reports, solution blueprints, and execution protocols for all Salesforce developer training badges in the **Developer Beginner** trail.

---

## Mandatory Git Version Control & Feature Branching Protocol

Before executing schema creation, Apex development, security provisioning, or cloud deployment for ANY unit in ANY badge, engineers MUST adhere to strict feature-branch isolation:

1. **Never develop or commit directly on `main` or `master`.** Always preserve `master` as the clean, production-ready baseline.
2. **Branch Out First:** Before starting any unit task, create a dedicated, feature-isolated branch from `master` (e.g. `git checkout -b feature/<badge-unit-name>`).
3. **Atomic Unit Development:** Keep schema XML metadata (`CustomField`), Apex code, security profiles (`fieldPermissions`), and unit technical documentation organized together on the feature branch.
4. **Ship via Pull Request:** Ship completed unit deliverables to `master` strictly through code review Pull Requests (`gh pr create`) and squashed merges (`gh pr merge --squash --delete-branch`).

---

## Badges Directory Sitemap

|   #    | Badge Name                                     | Directory Path                                                                                                            | Description & Status                                                                                          |
| :----: | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------ |
| **01** | **Agentforce 360 Platform Development Basics** | **[01_agentforce_360.../](01_agentforce_360_platform_development_basics/AGENTFORCE_360_PLATFORM_DEVELOPMENT_BASICS.md)**  | Platform development tools & technologies. **[COMPLETED]**                                                    |
| **02** | **Get Started with Salesforce Development**    | **[02_get_started.../](02_get_started_with_salesforce_development/GET_STARTED_WITH_SALESFORCE_DEVELOPMENT.md)**           | App development & sandbox setup. **[COMPLETED]**                                                              |
| **03** | **Quick Start: Tour the Sample App Gallery**   | **[03_quick_start.../](03_quick_start_tour_the_sample_app_gallery/QUICK_START_TOUR_THE_SAMPLE_APP_GALLERY.md)**           | Sample app configurations & tools. **[COMPLETED]**                                                            |
| **04** | **Data Modeling**                              | **[04_data_modeling/](04_data_modeling/DATA_MODELING.md)**                                                                | Objects, Auto-Numbering, Master-Detail, Lookup, Schema Builder (`Street_Address__c`). **[PASSED & VERIFIED]** |
| **05** | **Lightning Experience Customization**         | **[05_lightning_experience_customization/](05_lightning_experience_customization/LIGHTNING_EXPERIENCE_CUSTOMIZATION.md)** | Compact Layouts, Page Layouts, Quick Actions, Custom Buttons, Lightning Pages. **[IN PROGRESS]**              |
| **06** | **Formulas and Validations**                   | **[06_formulas_and_validations/](06_formulas_and_validations/FORMULAS_AND_VALIDATIONS.md)**                               | Point-and-click formula logic & validation rules. **[PENDING]**                                               |
| **07** | **Flow Builder Basics**                        | **[07_flow_builder_basics/](07_flow_builder_basics/FLOW_BUILDER_BASICS.md)**                                              | Process automation & Flow Builder logic. **[PENDING]**                                                        |
| **08** | **Apex Basics & Database**                     | **[08_apex_basics_and_database/](08_apex_basics_and_database/APEX_BASICS_AND_DATABASE.md)**                               | Apex OOP, SOQL queries, and DML operations. **[PENDING]**                                                     |
| **09** | **Apex Triggers**                              | **[09_apex_triggers/](09_apex_triggers/APEX_TRIGGERS.md)**                                                                | Custom database triggers & event handling. **[PENDING]**                                                      |
| **10** | **Lightning Web Components Basics**            | **[10_lightning_web_components_basics/](10_lightning_web_components_basics/LIGHTNING_WEB_COMPONENTS_BASICS.md)**          | Modern JavaScript web components & UI. **[PENDING]**                                                          |
