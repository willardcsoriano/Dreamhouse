# Trailhead Unit: Customize Record Highlights with Compact Layouts

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 4:** Customize Record Highlights with Compact Layouts  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_compact_layouts)

---

## Introduction & Learning Objectives

Compact layouts control which fields users see in the **Highlights Panel** at the top of a record page in Lightning Experience. They also control fields displayed in expanded lookup cards when hovering over a link in record details, and in the Salesforce mobile app record view.

After completing this unit, you'll be able to:

- Describe how compact layouts help users view key record information at a glance.
- Create custom compact layouts for standard and custom objects.
- Assign a compact layout as the primary default layout for an object.

---

## Conceptual Architecture: What Do Compact Layouts Do?

A **Compact Layout** organizes key fields for quick recognition across desktop and mobile interfaces.

### Core Functions & Key Display Areas

1. **Highlights Panel:** Displays up to 7 key fields at the top of a record page in Lightning Experience. The first field appears in bold at the top.
2. **Expanded Lookup Cards:** When hovering over record lookup links, the hover card displays fields defined by that target object's primary compact layout.
3. **Activity Timeline Detail Views:** Displays field summary info when expanding items in the activity timeline.
4. **Salesforce Mobile App:** Controls the primary record overview fields on mobile screens where space is limited.

---

## Consolidated Requirements & Solutions

### 1. `[REQ-5.4.G1]` Energy Audit Compact Layout (Guided Walk-Through)

Maria Jimenez wants to highlight the most critical energy metrics at the top of `Energy_Audit__c` records.

- **Target Object:** `Energy_Audit__c`
- **Compact Layout Label:** `Energy Audit Compact Layout`
- **Developer Name:** `Energy_Audit_Compact_Layout`
- **Fields (In Exact Order):**
  1. `Name` (Energy Audit Name)
  2. `Account__c` (Account)
  3. `Annual_Energy_Usage_kWh__c` (Annual Energy Usage (kWh))
  4. `Average_Annual_Electric_Cost__c` (Average Annual Electric Cost)
  5. `Type_of_Installation__c` (Type of Installation)
- **Assignment:** Set as Primary Compact Layout (`compactLayoutAssignment`)

---

### 2. `[REQ-5.4.C1]` Opportunity Compact Layout (Hands-On Challenge)

When Ursa Major Solar salespeople are on site with a customer, they need key opportunity metrics right at the top of the record.

- **Target Object:** `Opportunity`
- **Compact Layout Label:** `New Oppty Compact Layout`
- **Developer Name:** `New_Oppty_Compact_Layout`
- **Fields (In Exact Order):**
  1. `Name` (Opportunity Name)
  2. `Probability` (Probability (%))
  3. `CloseDate` (Close Date)
  4. `StageName` (Stage)
  5. `Amount` (Amount)
  6. `OwnerId` (Opportunity Owner)
- **Assignment:** Set as Primary Compact Layout (`compactLayoutAssignment`)

---

## Step-by-Step SFDX Deployment Protocol

### Step 1: Create Compact Layout Metadata Files

#### `force-app/main/default/objects/Energy_Audit__c/compactLayouts/Energy_Audit_Compact_Layout.compactLayout-meta.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CompactLayout xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Energy_Audit_Compact_Layout</fullName>
    <fields>Name</fields>
    <fields>Account__c</fields>
    <fields>Annual_Energy_Usage_kWh__c</fields>
    <fields>Average_Annual_Electric_Cost__c</fields>
    <fields>Type_of_Installation__c</fields>
    <label>Energy Audit Compact Layout</label>
</CompactLayout>
```

#### `force-app/main/default/objects/Opportunity/compactLayouts/New_Oppty_Compact_Layout.compactLayout-meta.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CompactLayout xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>New_Oppty_Compact_Layout</fullName>
    <fields>Name</fields>
    <fields>Probability</fields>
    <fields>CloseDate</fields>
    <fields>StageName</fields>
    <fields>Amount</fields>
    <fields>OwnerId</fields>
    <label>New Oppty Compact Layout</label>
</CompactLayout>
```

---

### Step 2: Assign Primary Compact Layouts on Object Metadata

#### Update `force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml`
```xml
<compactLayoutAssignment>Energy_Audit_Compact_Layout</compactLayoutAssignment>
```

#### Create `force-app/main/default/objects/Opportunity/Opportunity.object-meta.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <compactLayoutAssignment>New_Oppty_Compact_Layout</compactLayoutAssignment>
</CustomObject>
```

---

### Step 3: Atomic SFDX CLI Deployment

Deploy the metadata components directly to your connected Salesforce org (`myDevOrg`):

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

sf project deploy start \
  -d force-app/main/default/objects/Energy_Audit__c \
  -d force-app/main/default/objects/Opportunity \
  -o myDevOrg \
  --json | tee "$UNIT_DIR/UNIT_4_DEPLOY_COMPACT_LAYOUTS.json"
```

---

## Verification Audit

Verify the deployed `CompactLayout` metadata using Tooling API SOQL:

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

sf data query \
  -o myDevOrg \
  --use-tooling-api \
  -q "SELECT Id, DeveloperName, MasterLabel, SobjectType FROM CompactLayout WHERE DeveloperName IN ('Energy_Audit_Compact_Layout', 'New_Oppty_Compact_Layout')" \
  --json | tee "$UNIT_DIR/UNIT_4_VERIFICATION_AUDIT.json"
```

### Expected Tooling API Response (`--json`):

```json
{
  "status": 0,
  "result": {
    "records": [
      {
        "DeveloperName": "Energy_Audit_Compact_Layout",
        "MasterLabel": "Energy Audit Compact Layout",
        "SobjectType": "Energy_Audit__c"
      },
      {
        "DeveloperName": "New_Oppty_Compact_Layout",
        "MasterLabel": "New Oppty Compact Layout",
        "SobjectType": "Opportunity"
      }
    ],
    "totalSize": 2,
    "done": true
  }
}
```

---

## Resources & Reference Documentation

- [Salesforce Help: Compact Layouts](https://help.salesforce.com/s/articleView?id=sf.compact_layouts_overview.htm&type=5)
- [Salesforce Help: Assign Compact Layouts to Record Types](https://help.salesforce.com/s/articleView?id=sf.compact_layouts_assign.htm&type=5)
- [Metadata API Reference: CompactLayout](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_compactlayout.htm)

---

## Technical Post-Mortem & Engineering Learnings

1. **Tooling API SOQL Field Name Discrepancy:**
   - **Hiccup:** Attempting to query `TargetEntity` on `CompactLayout` via Tooling API threw `INVALID_FIELD: No such column 'TargetEntity' on entity 'CompactLayout'`.
   - **Resolution:** In Tooling API for `CompactLayout`, the target sObject entity field is named `SobjectType`. Querying `SobjectType` returned `Energy_Audit__c` and `Opportunity` cleanly.
