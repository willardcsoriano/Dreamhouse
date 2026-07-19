# Technical Report: Salesforce Data Modeling Unit 3 — Work with Schema Builder Execution Protocol

**Author:** Business Applications Engineering  
**Module:** Data Modeling (Developer Beginner Trail)  
**Unit 3:** Work with Schema Builder  
**Execution Paradigm:** 100% Salesforce CLI (`sf project deploy start` & `sf data query`)  
**Date:** July 19, 2026

---

## Executive Abstract

This technical report documents the architectural design, schema creation, and metadata deployment execution for adding a mandatory Text Area field (`Street_Address__c`) to the custom `Property__c` object within the Salesforce Lightning Platform. The report outlines source-driven metadata development using standard Salesforce CLI workflows.

---

## Technical Requirements & Requirements Specification

The challenge requires adding a required Text Area custom field to the `Property__c` object:

- **`[REQ-3.1]` Target Object:** `Property` (`Property__c`)
- **`[REQ-3.2]` Field Data Type:** Text Area (`TextArea`)
- **`[REQ-3.3]` Field Label:** Street Address
- **`[REQ-3.4]` Field Name:** `Street_Address` (`Street_Address__c`)
- **`[REQ-3.5]` Required Rule:** Always require a value in this field in order to save a record (`<required>true</required>`).

---

## Directive Traceability & Execution Prompt

```text
Create mandatory Text Area custom field Street_Address__c on Property__c with <required>true</required>, deploy metadata to trailhead-playground via SFDX CLI, and verify deployed schema state via Tooling API SOQL.
```

---

## Solution Blueprint: Step-by-Step CLI Execution Protocol

### Step 1: Create Text Area Field Metadata with Required Validation (`[REQ-3.1]` - `[REQ-3.5]`)

```bash
# 1. Ensure target fields directory exists under Property__c object
mkdir -p force-app/main/default/objects/Property__c/fields

# 2. Write Text Area custom field XML metadata with mandatory required rule (<required>true</required>)
cat << 'EOF' > force-app/main/default/objects/Property__c/fields/Street_Address__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Street_Address__c</fullName>
    <label>Street Address</label>
    <type>TextArea</type>
    <required>true</required>
</CustomField>
EOF
```

> **Developer Architectural Note (Required Field FLS Encapsulation):**  
> Fields with `<required>true</required>` automatically enforce universal read/edit access across all user profiles. Explicit profile `fieldPermissions` entries are omitted because the Metadata API rejects profile permissions on required fields (`You cannot deploy to a required field`).

---

### Step 2: Deploy Metadata to Salesforce Cloud (`sf project deploy start`)

#### Step 2.1: Terminal CLI Deployment Command

```bash
# Deploy Property__c schema (-d objects/Property__c) to target org (-o trailhead-playground)
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -o trailhead-playground
```

#### Step 2.2: Terminal Deployment Output Log

```text
Deployed Source
┌───────────┬───────────────────────────────┬──────────────┬───────────────────┐
│ State     │ Name                          │ Type         │ Path              │
├───────────┼───────────────────────────────┼──────────────┼───────────────────┤
│ Unchanged │ Property__c.Price__c          │ CustomField  │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/fields/P │
│           │                               │              │ rice__c.field-met │
│           │                               │              │ a.xml             │
│ Created   │ Property__c.Street_Address__c │ CustomField  │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/fields/S │
│           │                               │              │ treet_Address__c. │
│           │                               │              │ field-meta.xml    │
│ Unchanged │ Property__c                   │ CustomObject │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/Property │
│           │                               │              │ __c.object-meta.x │
│           │                               │              │ ml                │
│ Unchanged │ Property__c.All               │ ListView     │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/listView │
│           │                               │              │ s/All.listView-me │
│           │                               │              │ ta.xml            │
└───────────┴───────────────────────────────┴──────────────┴───────────────────┘

Status: Succeeded | Elapsed Time: 3.19s
```

---

### Step 3: Verify Schema State via Tooling API SOQL (`sf data query`)

#### Step 3.1: Tooling API Query Input Command

```bash
# Run Tooling API query via CLI to verify QualifiedApiName and DataType schema properties for Property__c
sf data query -o trailhead-playground --use-tooling-api -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'"
```

#### Step 3.2: Tooling API Query Output Table

```text
┌────────────────────┬────────────────────────────┐
│ QUALIFIEDAPINAME   │ DATATYPE                   │
├────────────────────┼────────────────────────────┤
│ Price__c           │ Currency(18, 0)            │
│ Street_Address__c  │ Text Area(255)             │
└────────────────────┴────────────────────────────┘

Total number of records retrieved: 14.
```

---

## Architectural Findings & Key Engineering Insights

- **Required Field Enforcement & FLS Encapsulation (`<required>true</required>`):** Setting `<required>true</required>` on a `CustomField` XML definition enforces platform-level database validation. Attempting to deploy explicit profile `fieldPermissions` for a required field causes the Metadata API to reject deployment (`You cannot deploy to a required field`). Required fields automatically grant universal visibility to all profiles because users must be able to input values upon record creation.
- **Source-Driven Metadata Tracking:** Defining object names and custom field types directly in local source files ensures standard SFDX source tracking compatibility across developer sandbox environments.
