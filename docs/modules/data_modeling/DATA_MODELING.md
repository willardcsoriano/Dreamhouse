# Trailhead Module Index: Data Modeling

**Trail:** Developer Beginner  
**Module:** Data Modeling  
**Date:** July 19, 2026

---

## Overview

This module covers custom objects, field types, relationships, and deployment paradigms for DreamHouse Realty in Salesforce.

Each unit is documented in its own dedicated file:

---

## Module Units Index

### 1. [Unit 1: Optimize Customer Data with Standard and Custom Objects](UNIT_1_STANDARD_CUSTOM_OBJECTS.md)

- **File Link (Absolute):** [UNIT_1_STANDARD_CUSTOM_OBJECTS.md](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_1_STANDARD_CUSTOM_OBJECTS.md)
- **Focus:** Custom Object `Offer__c` (Auto Number `OF-{0000}`), Currency field (`Offer_Amount__c`), and Date field (`Target_Close_Date__c`).
- **Tooling Paradigm:** 100% Vanilla Salesforce CLI (`sf project deploy start` and `sf data query`).
- **Status:** **PASSED & VERIFIED**

---

### 2. [Unit 2: Create Object Relationships](UNIT_2_OBJECT_RELATIONSHIPS.md)

- **File Link (Absolute):** [UNIT_2_OBJECT_RELATIONSHIPS.md](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_2_OBJECT_RELATIONSHIPS.md)
- **Focus:** Linking `Offer__c` to `Property__c` (Master-Detail) and `Contact` (Lookup).
- **Tooling Paradigm:** Salesforce Model Context Protocol (`@salesforce/mcp`) Server.
- **Status:** **PASSED & VERIFIED**

---

### 3. [Unit 3: Work with Schema Builder](UNIT_3_WORK_WITH_SCHEMA_BUILDER.md)

- **File Link (Absolute):** [UNIT_3_WORK_WITH_SCHEMA_BUILDER.md](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_3_WORK_WITH_SCHEMA_BUILDER.md)
- **Focus:** Custom Text Area field `Street_Address__c` on `Property__c` with mandatory `<required>true</required>` validation.
- **Tooling Paradigm:** Salesforce Model Context Protocol (`@salesforce/mcp`) Server & SFDX CLI.
- **Status:** **PASSED & VERIFIED**

---

### Challenge Satisfying Commands Matrix

| Requirement Tag | Challenge Requirement Description                    | Unit Blueprint Document                                                                                                                                                                    | Status     |
| :-------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
| **`[REQ-1.1]`** | Custom Object `Offer__c` (Auto Number `OF-{0000}`)   | [UNIT_1_STANDARD_CUSTOM_OBJECTS.md](UNIT_1_STANDARD_CUSTOM_OBJECTS.md) ([Absolute](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_1_STANDARD_CUSTOM_OBJECTS.md))    | **PASSED** |
| **`[REQ-1.2]`** | Custom Currency Field `Offer_Amount__c`              | [UNIT_1_STANDARD_CUSTOM_OBJECTS.md](UNIT_1_STANDARD_CUSTOM_OBJECTS.md) ([Absolute](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_1_STANDARD_CUSTOM_OBJECTS.md))    | **PASSED** |
| **`[REQ-1.3]`** | Custom Date Field `Target_Close_Date__c`             | [UNIT_1_STANDARD_CUSTOM_OBJECTS.md](UNIT_1_STANDARD_CUSTOM_OBJECTS.md) ([Absolute](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_1_STANDARD_CUSTOM_OBJECTS.md))    | **PASSED** |
| **`[REQ-2.1]`** | Master-Detail Field `Property__c` (to `Property__c`) | [UNIT_2_OBJECT_RELATIONSHIPS.md](UNIT_2_OBJECT_RELATIONSHIPS.md) ([Absolute](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_2_OBJECT_RELATIONSHIPS.md))             | **PASSED** |
| **`[REQ-2.2]`** | Lookup Field `Contact__c` (to `Contact`)             | [UNIT_2_OBJECT_RELATIONSHIPS.md](UNIT_2_OBJECT_RELATIONSHIPS.md) ([Absolute](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_2_OBJECT_RELATIONSHIPS.md))             | **PASSED** |
| **`[REQ-3.1]`** | Text Area Field `Street_Address__c` (`<required>`)   | [UNIT_3_WORK_WITH_SCHEMA_BUILDER.md](UNIT_3_WORK_WITH_SCHEMA_BUILDER.md) ([Absolute](file:///home/willard/repos/Dreamhouse/docs/modules/data_modeling/UNIT_3_WORK_WITH_SCHEMA_BUILDER.md)) | **PASSED** |

---

### Developer Insight: Target Org Flags vs. VS Code "No Default Org Set"

> **Key Takeaway:**
>
> - **VS Code "No Default Org Set":** VS Code's status bar displays "No Default Org Set" when no workspace-level fallback key (`target-org`) is configured in `.sf/config.json`.
> - **Why Deploys & Checks Succeed:** Passing explicit org alias flags (`-o trailhead-playground`) in CLI/MCP commands bypasses workspace defaults entirely. The CLI looks up the saved OAuth refresh tokens stored locally on your machine for `trailhead-playground` and authenticates silently without requiring re-login.
> - **Fixing the VS Code Status Bar:** Running `sf config set target-org trailhead-playground` sets the workspace default so VS Code's status bar displays `trailhead-playground`.
