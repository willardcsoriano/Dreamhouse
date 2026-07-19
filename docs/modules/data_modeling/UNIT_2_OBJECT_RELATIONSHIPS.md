# Technical Report: Salesforce Data Modeling Unit 2 — Object Relationships Execution Protocol

**Author:** Business Applications Engineering  
**Module:** Data Modeling (Developer Beginner Trail)  
**Unit 2:** Create Object Relationships  
**Execution Paradigm:** Model Context Protocol Server (`@salesforce/mcp`) vs. Vanilla Salesforce CLI (`sf`)  
**Date:** July 19, 2026

---

## Executive Abstract

This technical report documents the architectural design, security configuration, and metadata deployment execution for linking the custom `Offer__c` object to parent standard and custom entities (`Property__c` and `Contact`) within the Salesforce Lightning Platform. The report contrasts traditional developer terminal workflows against autonomous AI agent execution via the official Salesforce Model Context Protocol (`@salesforce/mcp`) server, proving complete functional and data state parity across both deployment paradigms.

---

## Directive Traceability & Purpose Matrix

| Directive   | Polished Technical Command                                                                 | Purpose                                                                                                                                        |
| :---------- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **DIR-2.1** | _Establish feature-isolated version control branch for Object Relationships module._       | Establish a feature-isolated Git branch (`feature/object-relationships`) adhering to trunk-based development rules.                            |
| **DIR-2.2** | _Provision and integrate Salesforce Model Context Protocol server for AI agent execution._ | Provision the `@salesforce/mcp` Model Context Protocol server, creating an RPC bridge for automated deployments and Tooling API queries.       |
| **DIR-2.3** | _Synthesize implementation blueprints into a comparative dual-workflow matrix._            | Structure solution blueprints into a 50/50 dual-column grid contrasting manual developer CLI scripts against automated AI protocol tool calls. |
| **DIR-2.4** | _Evaluate org state and data equivalence across CLI and MCP protocol executions._          | Evaluate semantic parity between terminal ASCII table outputs and JSON RPC response payloads to confirm identical org state mutations.         |
| **DIR-2.5** | _Document complete input invocation commands alongside cloud org response payloads._       | Map exact input arguments (`salesforce.deploy_metadata`, `salesforce.query_data`) alongside corresponding cloud org JSON response payloads.    |
| **DIR-2.6** | _Standardize CSS Flexbox layout architecture and dark-themed code container styling._      | Apply CSS Flexbox layout rules (`display: flex; flex: 1; width: 50%;`), isolating raw metadata and CLI code inside styled dark containers.     |
| **DIR-2.7** | _Architect modular documentation hierarchy under dedicated sub-directories._               | Refactor documentation into dedicated sub-directories (`docs/modules/data_modeling/`) to optimize maintainability and Markdown rendering.      |

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

## Solution Blueprint: Mandatory Atomic Field & FLS Creation Workflow

### Step 1: Master-Detail Field Creation (`Property__c.field-meta.xml`) `[Satisfies REQ-2.1]`

#### Step 1.1: Create Field Metadata XML

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

### Step 2: Lookup Field Creation & Immediate FLS Provisioning (`Contact__c.field-meta.xml`) `[Satisfies REQ-2.2]`

#### Step 2.1: Create Field Metadata XML

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

#### Step 2.2: Provision Immediate Field-Level Security (FLS) in Admin Profile

```bash
# Append fieldPermissions for Contact__c directly into Admin.profile-meta.xml before </Profile>
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Contact__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

---

### Step 3: Atomic Source Deployment Execution

#### Step 3.1: Terminal CLI Execution

```bash
# Deploy metadata directories (-d) to target org (-o trailhead-playground) via standard CLI
sf project deploy start \
  -d force-app/main/default/objects/Offer__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground
```

#### Step 3.2: AI Agent MCP Protocol Tool Call (`salesforce.deploy_metadata`)

```json
// Invoke official Salesforce Model Context Protocol RPC tool to execute cloud deployment
salesforce.deploy_metadata({
  "metadata_dirs": [
    "force-app/main/default/objects/Offer__c",
    "force-app/main/default/profiles"
  ],
  "target_org": "trailhead-playground"
})
```

---

### Step 4: Schema & Security Verification

#### Step 4.1: Terminal CLI SOQL Query

```bash
# Run Tooling API query via CLI to verify QualifiedApiName and DataType schema properties
sf data query -o trailhead-playground --use-tooling-api -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'"
```

#### Step 4.2: AI Agent MCP Protocol Query Tool Calls (`salesforce.query_data`)

```json
// Query Tooling API schema definitions via MCP Protocol
salesforce.query_data({
  "query": "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'",
  "use_tooling_api": true
})
```

```json
// Query FieldPermissions security grants via MCP Protocol
salesforce.query_data({
  "query": "SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE SobjectType='Offer__c'"
})
```

---

## Empirical Inputs & Outputs Execution Comparison

### Step 1: Deployment Execution

#### Step 1.1: Vanilla CLI Input Command

```bash
# Terminal SFDX deployment command
sf project deploy start \
  -d force-app/main/default/objects/Offer__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground
```

#### Step 1.2: Vanilla CLI Output Log

```text
Status: Succeeded | 6/6 Components Deployed
```

#### Step 1.3: MCP Protocol Tool Call Input (`salesforce.deploy_metadata`)

```json
// MCP tool call payload
salesforce.deploy_metadata({
  "metadata_dirs": ["force-app/main/default/objects/Offer__c", "force-app/main/default/profiles"],
  "target_org": "trailhead-playground"
})
```

#### Step 1.4: MCP Protocol Response Payload Output

```json
{
  "status": "Succeeded",
  "numberComponentsDeployed": 6,
  "numberComponentsTotal": 6,
  "success": true
}
```

---

### Step 2: Tooling API Schema Verification

#### Step 2.1: Vanilla CLI Input Command

```bash
# Terminal Tooling API query
sf data query -o trailhead-playground --use-tooling-api -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'"
```

#### Step 2.2: Vanilla CLI Output Table

```text
┌──────────────────────┬────────────────────────────┐
│ QUALIFIEDAPINAME     │ DATATYPE                   │
├──────────────────────┼────────────────────────────┤
│ Offer_Amount__c      │ Currency(16, 2)            │
│ Target_Close_Date__c │ Date                       │
│ Contact__c           │ Lookup(Contact)            │
│ Property__c          │ Master-Detail(Property)    │
└──────────────────────┴────────────────────────────┘
```

#### Step 2.3: MCP Protocol Query Tool Call Input (`salesforce.query_data`)

```json
// MCP Tooling API query tool call
salesforce.query_data({
  "query": "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'",
  "use_tooling_api": true
})
```

#### Step 2.4: MCP Protocol Response Payload Output

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

---

### Step 3: FieldPermissions Security Verification

#### Step 3.1: Vanilla CLI Input Command

```bash
# Terminal FieldPermissions SOQL query
sf data query -o trailhead-playground -q "SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE SobjectType='Offer__c'"
```

#### Step 3.2: Vanilla CLI Output Table

```text
┌──────────────────────────────┬─────────────────┬─────────────────┐
│ FIELD                        │ PERMISSIONSREAD │ PERMISSIONSEDIT │
├──────────────────────────────┼─────────────────┼─────────────────┤
│ Offer__c.Offer_Amount__c     │ true            │ true            │
│ Offer__c.Target_Close_Date__c│ true            │ true            │
│ Offer__c.Contact__c          │ true            │ true            │
└──────────────────────────────┴─────────────────┴─────────────────┘
```

#### Step 3.3: MCP Protocol Query Tool Call Input (`salesforce.query_data`)

```json
// MCP FieldPermissions query tool call
salesforce.query_data({
  "query": "SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE SobjectType='Offer__c'"
})
```

#### Step 3.4: MCP Protocol Response Payload Output

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
- **GUI Wizard vs. CLI Automation Parity:** In the Salesforce Setup GUI, Step 3 of the field creation wizard displays a page of checkboxes that automatically grants FLS visibility to profiles. When working via CLI/source XML, non-interactive Stream Editing (`sed -i '/<\/Profile>/i ...'`) acts as the exact CLI equivalent of checking those GUI visibility boxes.
- **Master-Detail Security Encapsulation:** Salesforce Metadata API strictly rejects explicit `fieldPermissions` entries for Master-Detail relationship fields (`Property__c`). Because Master-Detail relationships inherit security controls from the parent object, attempting to deploy profile permissions for `Offer__c.Property__c` results in a Metadata API deployment failure (`FieldPermissions cannot be specified for Master-Detail field`).
- **OAuth Target Org Overrides vs. Local VS Code State:** VS Code displays `"No Default Org Set"` when `.sf/config.json` lacks a global fallback key. However, passing explicit org alias flags (`-o trailhead-playground`) in CLI commands or `"target_org": "trailhead-playground"` in MCP tool calls references local OAuth 2.0 refresh tokens stored in `~/.sf/tokens.json`, allowing deployments and queries to succeed flawlessly without interactive login.
- **Protocol Interoperability:** Autonomous AI execution via `@salesforce/mcp` provides complete functional parity with standard CLI tools, returning machine-readable JSON structures that enable automated verification and real-time schema validation.
