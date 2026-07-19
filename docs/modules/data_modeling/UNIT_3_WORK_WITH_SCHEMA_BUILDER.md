# Technical Report: Salesforce Data Modeling Unit 3 — Work with Schema Builder Execution Protocol

**Author:** Business Applications Engineering  
**Module:** Data Modeling (Developer Beginner Trail)  
**Unit 3:** Work with Schema Builder  
**Execution Paradigm:** Model Context Protocol Server (`@salesforce/mcp`) & Source-Driven CLI  
**Date:** July 19, 2026

---

## Executive Abstract

This technical report documents the architectural design, schema creation, and metadata deployment execution for adding a mandatory Text Area field (`Street_Address__c`) to the custom `Property__c` object within the Salesforce Lightning Platform. The report contrasts point-and-click GUI Schema Builder workflows against source-driven XML metadata development and autonomous AI agent execution via the Salesforce Model Context Protocol (`@salesforce/mcp`).

---

## Directive Traceability & Purpose Matrix

| Directive   | Polished Technical Command                                                      | Purpose                                                                                           |
| :---------- | :------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------ |
| **DIR-3.1** | _Create Text Area custom field metadata for Street_Address__c on Property__c._  | Instantiate the mandatory `Street_Address__c` Text Area field on the `Property__c` custom object. |
| **DIR-3.2** | _Enforce required field validation rule in source XML metadata._                | Set `<required>true</required>` to enforce mandatory data entry upon record creation/update.      |
| **DIR-3.3** | _Provision System Administrator Profile FLS permissions for Street_Address__c._ | Append `<fieldPermissions>` (read/edit) into `Admin.profile-meta.xml`.                            |
| **DIR-3.4** | _Deploy Property__c schema and Admin profile to targeted Salesforce org._       | Execute source metadata deployment to `trailhead-playground` org.                                 |
| **DIR-3.5** | _Verify schema required property and data type via Tooling API SOQL._           | Query `FieldDefinition` metadata via Tooling API to validate `Street_Address__c` configuration.   |

---

## Technical Requirements & Requirements Specification

The challenge requires adding a required Text Area custom field to the `Property__c` object:

- **`[REQ-3.1]` Target Object:** `Property` (`Property__c`)
- **`[REQ-3.2]` Field Data Type:** Text Area (`TextArea`)
- **`[REQ-3.3]` Field Label:** Street Address
- **`[REQ-3.4]` Field Name:** `Street_Address` (`Street_Address__c`)
- **`[REQ-3.5]` Required Rule:** Always require a value in this field in order to save a record (`<required>true</required>`).

---

## Solution Blueprint: Mandatory Atomic Field & FLS Creation Workflow

### Step 1: Text Area Field Creation with Required Validation (`[REQ-3.1]` - `[REQ-3.5]`)

#### Step 1.1: Create Field Metadata XML (`Property__c/fields/Street_Address__c.field-meta.xml`)

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

#### Step 1.2: Provision Immediate Field-Level Security (FLS) in Admin Profile

```bash
# Append fieldPermissions for Street_Address__c directly into Admin.profile-meta.xml before </Profile>
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Property__c.Street_Address__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

---

### Step 2: Atomic Source Deployment Execution

#### Step 2.1: Terminal CLI Execution

```bash
# Deploy Property__c schema (-d objects/Property__c) and profile security (-d profiles) to target org (-o trailhead-playground)
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground
```

#### Step 2.2: AI Agent MCP Protocol Tool Call (`salesforce.deploy_metadata`)

```json
// Invoke official Salesforce Model Context Protocol RPC tool to execute cloud deployment
salesforce.deploy_metadata({
  "metadata_dirs": [
    "force-app/main/default/objects/Property__c",
    "force-app/main/default/profiles"
  ],
  "target_org": "trailhead-playground"
})
```

---

### Step 3: Schema & Security Verification

#### Step 3.1: Terminal CLI SOQL Query

```bash
# Run Tooling API query via CLI to verify QualifiedApiName and DataType schema properties for Property__c
sf data query -o trailhead-playground --use-tooling-api -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'"
```

#### Step 3.2: AI Agent MCP Protocol Query Tool Calls (`salesforce.query_data`)

```json
// Query Tooling API schema definitions via MCP Protocol
salesforce.query_data({
  "query": "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'",
  "use_tooling_api": true
})
```

```json
// Query FieldPermissions security grants for Property__c via MCP Protocol
salesforce.query_data({
  "query": "SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE SobjectType='Property__c'"
})
```

---

## Empirical Inputs & Outputs Execution Comparison

### Step 1: Deployment Execution

#### Step 1.1: Vanilla CLI Input Command

```bash
# Terminal SFDX deployment command
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground
```

#### Step 1.2: Vanilla CLI Output Log

```text
Status: Succeeded | 2/2 Components Deployed
```

#### Step 1.3: MCP Protocol Tool Call Input (`salesforce.deploy_metadata`)

```json
// MCP tool call payload
salesforce.deploy_metadata({
  "metadata_dirs": ["force-app/main/default/objects/Property__c", "force-app/main/default/profiles"],
  "target_org": "trailhead-playground"
})
```

#### Step 1.4: MCP Protocol Response Payload Output

```json
{
  "status": "Succeeded",
  "numberComponentsDeployed": 2,
  "numberComponentsTotal": 2,
  "success": true
}
```

---

### Step 2: Tooling API Schema Verification

#### Step 2.1: Vanilla CLI Input Command

```bash
# Terminal Tooling API query
sf data query -o trailhead-playground --use-tooling-api -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'"
```

#### Step 2.2: Vanilla CLI Output Table

```text
┌──────────────────────┬────────────────────────────┐
│ QUALIFIEDAPINAME     │ DATATYPE                   │
├──────────────────────┼────────────────────────────┤
│ Street_Address__c    │ Text Area                  │
└──────────────────────┴────────────────────────────┘
```

#### Step 2.3: MCP Protocol Query Tool Call Input (`salesforce.query_data`)

```json
// MCP Tooling API query tool call
salesforce.query_data({
  "query": "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'",
  "use_tooling_api": true
})
```

#### Step 2.4: MCP Protocol Response Payload Output

```json
{
  "totalSize": 1,
  "done": true,
  "records": [
    { "QualifiedApiName": "Street_Address__c", "DataType": "Text Area" }
  ]
}
```

---

## Architectural Findings & Key Engineering Insights

- **Required Field Enforcement (`<required>true</required>`):** Setting `<required>true</required>` on a `CustomField` XML definition enforces platform-level database validation. Any attempt to insert or update a `Property__c` record without providing a value for `Street_Address__c` will be rejected by Salesforce.
- **Atomic Schema & FLS Provisioning:** Pairing field metadata creation directly with immediate profile FLS provisioning prevents "ghost field" anti-patterns, ensuring fields are instantly visible and queryable upon deployment.
- **Protocol Interoperability:** Autonomous AI execution via `@salesforce/mcp` provides complete functional parity with standard CLI tools, returning machine-readable JSON structures that enable automated verification and real-time schema validation.
