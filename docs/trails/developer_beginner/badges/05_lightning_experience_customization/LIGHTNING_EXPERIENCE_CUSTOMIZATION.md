# Trailhead Badge Index: Lightning Experience Customization

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Est. Time:** ~3 hrs  
**Total Points:** +2,700 Points  
**Date Started:** July 19, 2026

---

## Overview

This badge covers customizing the Lightning Experience user interface for DreamHouse Realty in Salesforce without writing code, including compact layouts, page layouts, custom buttons, quick actions, and Lightning pages.

---

## Table of Contents

- [Overview](#overview)
- [Badge Units Index](#badge-units-index)
  - [1. [Unit 1: Set Up Your Org](UNIT_1_SET_UP_YOUR_ORG.md)](#1-unit-1-set-up-your-orgunit_1_set_up_your_orgmd)
  - [2. [Unit 2: Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)](UNIT_2_CREATE_AND_CUSTOMIZE_LIGHTNING_APPS.md)](#2-unit-2-create-and-customize-agentforce-360-platform-apps-formerly-lightning-appsunit_2_create_and_customize_lightning_appsmd)
  - [3. [Unit 3: Create and Customize List Views](UNIT_3_CREATE_AND_CUSTOMIZE_LIST_VIEWS.md)](#3-unit-3-create-and-customize-list-viewsunit_3_create_and_customize_list_viewsmd)
  - [4. [Unit 4: Customize Record Highlights with Compact Layouts](UNIT_4_CUSTOMIZE_RECORD_HIGHLIGHTS_WITH_COMPACT_LAYOUTS.md)](#4-unit-4-customize-record-highlights-with-compact-layoutsunit_4_customize_record_highlights_with_compact_layoutsmd)
- [Execution Protocol](#execution-protocol)

## Badge Units Index

### 1. [Unit 1: Set Up Your Org](UNIT_1_SET_UP_YOUR_ORG.md)

- **File Link (Absolute):** [UNIT_1_SET_UP_YOUR_ORG.md](file:///home/willard/repos/Dreamhouse/docs/trails/developer_beginner/badges/05_lightning_experience_customization/UNIT_1_SET_UP_YOUR_ORG.md)
- **Focus:** Custom Object `Energy_Audit__c` (`Energy Audit`), custom fields (`Type_of_Installation__c`, `Average_Annual_Electric_Cost__c`, `Annual_Energy_Usage_kWh__c`, `Audit_Notes__c`), Custom Tab (`Custom3: Sun`), and Chatter Feed Tracking (`enableFeeds`).
- **Tooling Paradigm:** 100% Hands-on SFDX CLI (`sf project deploy start` & `sf data query --use-tooling-api`).
- **Status:** **COMPLETED & VERIFIED**

---

### 2. [Unit 2: Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)](UNIT_2_CREATE_AND_CUSTOMIZE_LIGHTNING_APPS.md)

- **File Link (Absolute):** [UNIT_2_CREATE_AND_CUSTOMIZE_LIGHTNING_APPS.md](file:///home/willard/projects/Dreamhouse/docs/trails/developer_beginner/badges/05_lightning_experience_customization/UNIT_2_CREATE_AND_CUSTOMIZE_LIGHTNING_APPS.md)
- **Focus:** Custom Application `Energy Consultations` (`Energy_Consultations.app-meta.xml`), custom branding (`#FA8B05`), navigation items order (`Home`, `Chatter`, `Groups`, `Energy_Audit__c`, `Account`, `Contact`, `Product2`, `Task`), and profile application visibility (`Admin`).
- **Tooling Paradigm:** 100% Hands-on SFDX CLI (`sf project deploy start` & `sf data query --use-tooling-api`).
- **Status:** **DOCUMENTED (Ready for Execution)**

---

### 3. [Unit 3: Create and Customize List Views](UNIT_3_CREATE_AND_CUSTOMIZE_LIST_VIEWS.md)

- **File Link (Absolute):** [UNIT_3_CREATE_AND_CUSTOMIZE_LIST_VIEWS.md](file:///home/willard/repos/Dreamhouse/docs/trails/developer_beginner/badges/05_lightning_experience_customization/UNIT_3_CREATE_AND_CUSTOMIZE_LIST_VIEWS.md)
- **Focus:** Custom Opportunity List View `High Probability Opportunities` (`High_Probability_Opportunities`), filter logic (`Stage` in `Proposal/Price Quote`, `Negotiation/Review` AND `Probability >= 50%`), column configuration, list view chart (`Pipeline Total Value`).
- **Tooling Paradigm:** Declarative Salesforce UI & SOQL verification (`sf data query`).
- **Status:** **COMPLETED & VERIFIED**

---

### 4. [Unit 4: Customize Record Highlights with Compact Layouts](UNIT_4_CUSTOMIZE_RECORD_HIGHLIGHTS_WITH_COMPACT_LAYOUTS.md)

- **File Link (Absolute):** [UNIT_4_CUSTOMIZE_RECORD_HIGHLIGHTS_WITH_COMPACT_LAYOUTS.md](file:///home/willard/repos/Dreamhouse/docs/trails/developer_beginner/badges/05_lightning_experience_customization/UNIT_4_CUSTOMIZE_RECORD_HIGHLIGHTS_WITH_COMPACT_LAYOUTS.md)
- **Focus:** Compact Layouts (`Energy_Audit_Compact_Layout` on `Energy_Audit__c` and `New_Oppty_Compact_Layout` on `Opportunity`), primary compact layout assignment.
- **Tooling Paradigm:** 100% Hands-on SFDX CLI (`sf project deploy start` & `sf data query --use-tooling-api`).
- **Status:** **COMPLETED & VERIFIED**

---

## Execution Protocol

All activities in this badge follow the **[Global Badge Git Branching Protocol](../README.md#mandatory-git-version-control--feature-branching-protocol)** using 100% hands-on **SFDX CLI terminal commands** (`sf project deploy start` & `sf data query`).
