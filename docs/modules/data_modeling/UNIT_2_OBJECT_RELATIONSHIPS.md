# Technical Report: Salesforce Data Modeling Unit 2 — Object Relationships Execution Protocol

**Author:** Business Applications Engineering  
**Module:** Data Modeling (Developer Beginner Trail)  
**Unit 2:** Create Object Relationships  
**Execution Paradigm:** 100% Salesforce Model Context Protocol Server (`@salesforce/mcp`)  
**Date:** July 19, 2026

---

## Executive Abstract

This technical report documents the architectural design, security configuration, and metadata deployment execution for linking the custom `Offer__c` object to parent standard and custom entities (`Property__c` and `Contact`) within the Salesforce Lightning Platform. The report details autonomous AI agent execution via the official Salesforce Model Context Protocol (`@salesforce/mcp`) server tools (`salesforce.deploy_metadata` and `salesforce.query_data`).

---

## Technical Requirements & Requirements Specification

The challenge requires creating two distinct relationship types on the `Offer__c` custom object:

- **`[REQ-2.1]` Master-Detail Relationship Field (`Property__c`):**
  - **Target API Name:** `Property__c`
  - **Field Label:** Property
  - **Related Object:** `Property__c`
  - **Child Relationship Name:** `Offers`
  - **Security Impact:** Tightly couples child records to parent `Property__c`. Field-Level Security (FLS) is inherited directly from the parent object.

- **`[REQ-2.2]` Lookup Relationship Field (`Contact__c`):**
  - **Target API Name:** `Contact__c`
  - **Field Label:** Contact
  - **Related Object:** `Contact`
  - **Child Relationship Name:** `Offers`
  - **Deletion Constraint:** `SetNull` (clears the lookup value if the referenced Contact is deleted).

---

## Directive Traceability & Execution Prompt

```text
Create Master-Detail relationship field Property__c and Lookup relationship field Contact__c on Offer__c, provision profile FLS security for Contact__c, deploy metadata to trailhead-playground via MCP protocol server, and verify org schema state via Tooling API SOQL.
```

---

## Solution Blueprint: Step-by-Step AI Agent MCP Execution Protocol

### Step 1: Create Master-Detail Relationship Field (`Property__c`) `[Satisfies REQ-2.1]`

#### Step 1.1: Generate Field Metadata XML

```bash
# Generate Master-Detail relationship field metadata referencing Property__c
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Property__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Property__c</fullName>
    <label>Property</label>
    <referenceTo>Property__c</referenceTo>
    <relationshipName>Offers</relationshipName>
    <relationshipLabel>Offers</relationshipLabel>
    <type>MasterDetail</type>
    <writeRequiresMasterRead>false</writeRequiresMasterRead>
    <reparentableMasterDetail>false</reparentableMasterDetail>
</CustomField>
EOF
```

> **Developer Architectural Note (FLS Inheritance):**  
> Master-Detail relationship fields automatically inherit security and visibility from the parent `Property__c` object. Explicit profile `fieldPermissions` entries are omitted because the Metadata API rejects profile permissions on Master-Detail fields.

---

### Step 2: Create Lookup Relationship Field & Provision FLS (`Contact__c`) `[Satisfies REQ-2.2]`

#### Step 2.1: Generate Field Metadata XML

```bash
# Generate Lookup relationship field metadata referencing Contact with SetNull deletion constraint
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Contact__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Contact__c</fullName>
    <label>Contact</label>
    <referenceTo>Contact</referenceTo>
    <relationshipName>Offers</relationshipName>
    <relationshipLabel>Offers</relationshipLabel>
    <deleteConstraint>SetNull</deleteConstraint>
    <type>Lookup</type>
</CustomField>
EOF
```

#### Step 2.2: Provision Field-Level Security (FLS) in Admin Profile

```bash
# Append fieldPermissions for Contact__c directly into Admin.profile-meta.xml before </Profile>
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Contact__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

---

### Step 3: Deploy Metadata to Salesforce Cloud via MCP Protocol (`salesforce.deploy_metadata`)

#### Step 3.1: MCP Protocol Invocation Input Payload

```json
// Invoke official Salesforce Model Context Protocol RPC tool to deploy metadata directories
salesforce.deploy_metadata({
  "metadata_dirs": [
    "force-app/main/default/objects/Offer__c",
    "force-app/main/default/profiles"
  ],
  "target_org": "trailhead-playground"
})
```

#### Step 3.2: MCP Protocol Response Output Payload

```json
{
  "status": "Succeeded",
  "numberComponentsDeployed": 6,
  "numberComponentsTotal": 6,
  "success": true
}
```

---

### Step 4: Verify Schema & Security State via MCP Protocol (`salesforce.query_data`)

#### Step 4.1: Query Schema Definitions Input Payload

```json
// Query Tooling API schema definitions to verify field data types on Offer__c
salesforce.query_data({
  "query": "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'",
  "use_tooling_api": true
})
```

#### Step 4.2: Query Schema Definitions Response Output Payload

```json
{
  "totalSize": 4,
  "done": true,
  "records": [
    { "QualifiedApiName": "Offer_Amount__c", "DataType": "Currency(16, 2)" },
    { "QualifiedApiName": "Target_Close_Date__c", "DataType": "Date" },
    { "QualifiedApiName": "Contact__c", "DataType": "Lookup(Contact)" },
    { "QualifiedApiName": "Property__c", "DataType": "Master-Detail(Property)" }
  ]
}
```

#### Step 4.3: Query FieldPermissions Security Input Payload

```json
// Query FieldPermissions security grants to confirm read/edit access
salesforce.query_data({
  "query": "SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE SobjectType='Offer__c'"
})
```

#### Step 4.4: Query FieldPermissions Security Response Output Payload

```json
{
  "totalSize": 3,
  "done": true,
  "records": [
    {
      "Field": "Offer__c.Offer_Amount__c",
      "PermissionsRead": true,
      "PermissionsEdit": true
    },
    {
      "Field": "Offer__c.Target_Close_Date__c",
      "PermissionsRead": true,
      "PermissionsEdit": true
    },
    {
      "Field": "Offer__c.Contact__c",
      "PermissionsRead": true,
      "PermissionsEdit": true
    }
  ]
}
```

---

## Architectural Findings & Key Engineering Insights

- **Atomic Schema & FLS Provisioning (The "Ghost Field" Anti-Pattern):** Creating a `CustomField` XML file physically instantiates the column in Salesforce, BUT Salesforce sets Field-Level Security (FLS) to `invisible/non-editable` by default for all user profiles. Deploying schema without profile `fieldPermissions` produces "ghost fields"—fields that exist in the database but are completely hidden from the GUI, throw `No such column` errors in SOQL queries, and fail Trailhead verification checks. Schema creation (`CustomField`) and Security provisioning (`fieldPermissions`) MUST always be executed as a single atomic unit.
- **Master-Detail Security Encapsulation:** Salesforce Metadata API strictly rejects explicit `fieldPermissions` entries for Master-Detail relationship fields (`Property__c`). Because Master-Detail relationships inherit security controls from the parent object, attempting to deploy profile permissions for `Offer__c.Property__c` results in a Metadata API deployment failure (`FieldPermissions cannot be specified for Master-Detail field`).
- **OAuth Target Org Overrides vs. Local VS Code State:** VS Code displays `"No Default Org Set"` when `.sf/config.json` lacks a global fallback key. However, passing explicit org alias flags (`-o trailhead-playground`) in CLI commands or `"target_org": "trailhead-playground"` in MCP tool calls references local OAuth 2.0 refresh tokens stored in `~/.sf/tokens.json`, allowing deployments and queries to succeed flawlessly without interactive login.
- **Protocol Interoperability:** Autonomous AI execution via `@salesforce/mcp` provides complete functional parity with standard CLI tools, returning machine-readable JSON structures that enable automated verification and real-time schema validation.
