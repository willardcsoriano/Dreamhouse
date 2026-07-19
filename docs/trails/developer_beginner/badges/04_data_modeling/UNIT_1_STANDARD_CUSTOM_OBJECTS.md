# Technical Report: Salesforce Data Modeling Unit 1 — Standard & Custom Objects Execution Protocol

**Author:** Business Applications Engineering  
**Module:** Data Modeling (Developer Beginner Trail)  
**Unit 1:** Optimize Customer Data with Standard and Custom Objects  
**Execution Paradigm:** 100% Salesforce CLI (`sf project deploy start` & `sf data query`)  
**Date:** July 19, 2026

---

## Executive Abstract

This technical report documents the architectural design, schema creation, and metadata deployment execution for creating the custom `Offer__c` object and its core fields (`Offer_Amount__c` and `Target_Close_Date__c`) within the Salesforce Lightning Platform. The report outlines source-driven metadata development using standard Salesforce CLI workflows.

---

## Technical Requirements & Requirements Specification

The challenge requires creating the `Offer__c` custom object along with two custom fields:

- **`[REQ-1.1]` Custom Object `Offer__c`:**
  - **Label:** Offer
  - **Plural Label:** Offers
  - **Object Name:** `Offer` (`Offer__c`)
  - **Record Name:** Offer Name
  - **Data Type:** Auto Number
  - **Display Format:** `OF-{0000}`
  - **Starting Number:** 1

- **`[REQ-1.2]` Custom Currency Field `Offer_Amount__c`:**
  - **Data Type:** Currency
  - **Field Label:** Offer Amount
  - **Field Name:** `Offer_Amount` (`Offer_Amount__c`)
  - **Precision:** 16, **Scale:** 2

- **`[REQ-1.3]` Custom Date Field `Target_Close_Date__c`:**
  - **Data Type:** Date
  - **Field Label:** Target Close Date
  - **Field Name:** `Target_Close_Date` (`Target_Close_Date__c`)

---

## Directive Traceability & Execution Prompt

```text
Create custom object Offer__c (Auto Number OF-{0000}), Currency field Offer_Amount__c, and Date field Target_Close_Date__c, provision profile FLS security in Admin.profile-meta.xml, deploy metadata to trailhead-playground via SFDX CLI, and verify schema via Tooling API SOQL.
```

---

## Solution Blueprint: Mandatory Atomic Field & FLS Creation Workflow

### Step 1: Custom Object Metadata Creation (`[REQ-1.1]`)

```bash
# 1. Create local target directory structure for Offer__c fields
mkdir -p force-app/main/default/objects/Offer__c/fields

# 2. Write custom object XML metadata file defining AutoNumber format OF-{0000}
cat << 'EOF' > force-app/main/default/objects/Offer__c/Offer__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Offer</label>
    <pluralLabel>Offers</pluralLabel>
    <nameField>
        <displayFormat>OF-{0000}</displayFormat>
        <label>Offer Name</label>
        <type>AutoNumber</type>
    </nameField>
    <sharingModel>ReadWrite</sharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
</CustomObject>
EOF
```

---

### Step 2: Currency Field Creation & Immediate FLS Provisioning (`[REQ-1.2]`)

#### Step 2.1: Create Field Metadata XML

```bash
# Generate Currency custom field XML metadata with 16-digit precision and 2-decimal scale
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Offer_Amount__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Offer_Amount__c</fullName>
    <label>Offer Amount</label>
    <type>Currency</type>
    <precision>16</precision>
    <scale>2</scale>
</CustomField>
EOF
```

#### Step 2.2: Provision Immediate Field-Level Security (FLS) in Admin Profile

```bash
# Append fieldPermissions for Offer_Amount__c directly into Admin.profile-meta.xml before </Profile>
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Offer_Amount__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

---

### Step 3: Date Field Creation & Immediate FLS Provisioning (`[REQ-1.3]`)

#### Step 3.1: Create Field Metadata XML

```bash
# Generate Date custom field XML metadata for target sale close date
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Target_Close_Date__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Target_Close_Date__c</fullName>
    <label>Target Close Date</label>
    <type>Date</type>
</CustomField>
EOF
```

#### Step 3.2: Provision Immediate Field-Level Security (FLS) in Admin Profile

```bash
# Append fieldPermissions for Target_Close_Date__c directly into Admin.profile-meta.xml before </Profile>
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Target_Close_Date__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

---

### Step 4: Atomic Source Deployment to Salesforce Cloud

```bash
# Deploy object schema (-d objects/Offer__c) and profile security (-d profiles) to target org (-o trailhead-playground)
sf project deploy start \
  -d force-app/main/default/objects/Offer__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground
```

---

### Step 5: Schema & Security Verification via Tooling API SOQL

```bash
# Run Tooling API query (--use-tooling-api) to verify deployed field data types in the target org (-o trailhead-playground)
sf data query -o trailhead-playground --use-tooling-api -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'"
```

---

## Architectural Findings & Key Engineering Insights

- **Atomic Schema & FLS Provisioning (The "Ghost Field" Anti-Pattern):** Creating a `CustomField` XML file physically instantiates the column in Salesforce, BUT Salesforce sets Field-Level Security (FLS) to `invisible/non-editable` by default for all user profiles. Deploying schema without profile `fieldPermissions` produces "ghost fields"—fields that exist in the database but are completely hidden from the GUI, throw `No such column` errors in SOQL queries, and fail Trailhead verification checks. Schema creation (`CustomField`) and Security provisioning (`fieldPermissions`) MUST always be executed as a single atomic unit.
- **GUI Wizard vs. CLI Automation Parity:** In the Salesforce Setup GUI, Step 3 of the field creation wizard displays a page of checkboxes that automatically grants FLS visibility to profiles. When working via CLI/source XML, non-interactive Stream Editing (`sed -i '/<\/Profile>/i ...'`) acts as the exact CLI equivalent of checking those GUI visibility boxes.
- **Source-Driven Metadata Tracking:** Defining object names, auto-number formats (`OF-{0000}`), and custom field types directly in source files ensures standard SFDX source tracking compatibility.
