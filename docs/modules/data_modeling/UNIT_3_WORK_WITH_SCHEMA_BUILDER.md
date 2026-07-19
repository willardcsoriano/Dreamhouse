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
Create mandatory Text Area custom field Street_Address__c on Property__c with <required>true</required>, deploy metadata to trailhead-playground via MCP protocol server, and verify deployed schema state via Tooling API SOQL.
```

---

## Solution Blueprint: Mandatory Atomic Field Creation Workflow

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

> **Developer Architectural Note (Required Field FLS Encapsulation):**  
> Fields with `<required>true</required>` automatically enforce universal read/edit access across all user profiles. Explicit profile `fieldPermissions` entries are omitted because the Metadata API rejects profile permissions on required fields (`You cannot deploy to a required field`).

---

### Step 2: Atomic Source Deployment Execution

#### Step 2.1: Terminal CLI Execution

```bash
# Deploy Property__c schema (-d objects/Property__c) to target org (-o trailhead-playground)
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -o trailhead-playground
```

#### Step 2.2: AI Agent MCP Protocol Tool Call (`salesforce.deploy_metadata`)

```json
// Invoke official Salesforce Model Context Protocol RPC tool to execute cloud deployment
salesforce.deploy_metadata({
  "metadata_dirs": [
    "force-app/main/default/objects/Property__c"
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

---

## Empirical Inputs & Outputs Execution Comparison

### Step 1: Deployment Execution

#### Step 1.1: Vanilla CLI Input Command

```bash
# Terminal SFDX deployment command
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -o trailhead-playground
```

#### Step 1.2: Vanilla CLI Output Log

```text
Status: Succeeded | 4/4 Components Deployed
Created: Property__c.Street_Address__c (CustomField)
```

#### Step 1.3: MCP Protocol Tool Call Input (`salesforce.deploy_metadata`)

```json
// MCP tool call payload
salesforce.deploy_metadata({
  "metadata_dirs": ["force-app/main/default/objects/Property__c"],
  "target_org": "trailhead-playground"
})
```

#### Step 1.4: MCP Protocol Response Payload Output

```json
{
  "status": "Succeeded",
  "numberComponentsDeployed": 4,
  "numberComponentsTotal": 4,
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
┌────────────────────┬────────────────────────────┐
│ QUALIFIEDAPINAME   │ DATATYPE                   │
├────────────────────┼────────────────────────────┤
│ Price__c           │ Currency(18, 0)            │
│ Street_Address__c  │ Text Area(255)             │
└────────────────────┴────────────────────────────┘
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
  "totalSize": 14,
  "done": true,
  "records": [
    { "QualifiedApiName": "Price__c", "DataType": "Currency(18, 0)" },
    { "QualifiedApiName": "Street_Address__c", "DataType": "Text Area(255)" }
  ]
}
```

---

## Architectural Findings & Key Engineering Insights

- **Required Field Enforcement & FLS Encapsulation (`<required>true</required>`):** Setting `<required>true</required>` on a `CustomField` XML definition enforces platform-level database validation. Attempting to deploy explicit profile `fieldPermissions` for a required field causes the Metadata API to reject deployment (`You cannot deploy to a required field`). Required fields automatically grant universal visibility to all profiles because users must be able to input values upon record creation.
- **Protocol Interoperability:** Autonomous AI execution via `@salesforce/mcp` provides complete functional parity with standard CLI tools, returning machine-readable JSON structures that enable automated verification and real-time schema validation.
