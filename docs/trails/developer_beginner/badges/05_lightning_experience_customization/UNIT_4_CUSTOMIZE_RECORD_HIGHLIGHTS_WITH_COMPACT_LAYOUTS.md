# Trailhead Unit: Customize Record Highlights with Compact Layouts

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 4:** Customize Record Highlights with Compact Layouts  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_compact_layouts)

---

## Requirement to CLI Command Mapping Matrix

| Activity Type | Requirement ID | Summary | Target Component | Solved By CLI Command |
| :--- | :--- | :--- | :--- | :--- |
| **Guided Activity** | **`[REQ-5.4.G1.1]`** | Create `Energy_Audit_Compact_Layout` | `Energy_Audit__c` Compact Layout | `cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/compactLayouts/Energy_Audit_Compact_Layout.compactLayout-meta.xml` |
| **Guided Activity** | **`[REQ-5.4.G1.2]`** | Assign Primary Compact Layout | `Energy_Audit__c` Metadata | Update `compactLayoutAssignment` in `Energy_Audit__c.object-meta.xml` |
| **Guided Activity** | **`[REQ-5.4.G1.DEP]`**| Deploy Guided Activity | `Energy_Audit__c` | `sf project deploy start -d force-app/main/default/objects/Energy_Audit__c -o myDevOrg` |
| **Guided Activity** | **`[REQ-5.4.G1.AUD]`**| Audit Guided Activity | Tooling API Query | `sf data query -o myDevOrg --use-tooling-api -q "SELECT Id, DeveloperName, SobjectType FROM CompactLayout WHERE DeveloperName='Energy_Audit_Compact_Layout'"` |
| **Hands-On Challenge** | **`[REQ-5.4.C1.1]`** | Create `New_Oppty_Compact_Layout` | `Opportunity` Compact Layout | `cat << 'EOF' > force-app/main/default/objects/Opportunity/compactLayouts/New_Oppty_Compact_Layout.compactLayout-meta.xml` |
| **Hands-On Challenge** | **`[REQ-5.4.C1.2]`** | Assign Primary Compact Layout | `Opportunity` Metadata | `cat << 'EOF' > force-app/main/default/objects/Opportunity/Opportunity.object-meta.xml` |
| **Hands-On Challenge** | **`[REQ-5.4.C1.DEP]`**| Deploy Challenge Metadata | `Opportunity` | `sf project deploy start -d force-app/main/default/objects/Opportunity -o myDevOrg` |
| **Hands-On Challenge** | **`[REQ-5.4.C1.AUD]`**| Audit Challenge Metadata | Tooling API Query | `sf data query -o myDevOrg --use-tooling-api -q "SELECT Id, DeveloperName, SobjectType FROM CompactLayout WHERE DeveloperName='New_Oppty_Compact_Layout'"` |

---

## Introduction & Learning Objectives

Compact layouts control which fields users see in the **Highlights Panel** at the top of a record page in Lightning Experience. They also control fields displayed in expanded lookup cards when hovering over a link in record details, and in the Salesforce mobile app record view.

After completing this unit, you'll be able to:

- Describe how compact layouts help users view key record information at a glance.
- Create custom compact layouts for standard and custom objects.
- Assign a compact layout as the primary default layout for an object.

---

## Part 1: Guided Activity (`Energy_Audit__c`)

Maria Jimenez wants to highlight the most critical energy metrics at the top of `Energy_Audit__c` records.

### 1. `[REQ-5.4.G1.1]` & `[REQ-5.4.G1.2]` Create Metadata & Assign Primary Layout

- **Target Object:** `Energy_Audit__c`
- **Compact Layout Label:** `Energy Audit Compact Layout`
- **Developer Name:** `Energy_Audit_Compact_Layout`
- **Fields (In Exact Order):**
  1. `Name` (Energy Audit Name)
  2. `Account__c` (Account)
  3. `Annual_Energy_Usage_kWh__c` (Annual Energy Usage (kWh))
  4. `Average_Annual_Electric_Cost__c` (Average Annual Electric Cost)
  5. `Type_of_Installation__c` (Type of Installation)

```bash
# Create target directory for Energy_Audit__c compact layout metadata
mkdir -p force-app/main/default/objects/Energy_Audit__c/compactLayouts

# 1. Generate XML metadata file for Energy Audit compact layout
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/compactLayouts/Energy_Audit_Compact_Layout.compactLayout-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Salesforce Compact Layout Definition for Energy_Audit__c Custom Object -->
<CompactLayout xmlns="http://soap.sforce.com/2006/04/metadata">
    <!-- Unique developer API name of the compact layout -->
    <fullName>Energy_Audit_Compact_Layout</fullName>
    <!-- Ordered field list displayed in the Highlights Panel -->
    <fields>Name</fields> <!-- Energy Audit Name (primary bold header field) -->
    <fields>Account__c</fields> <!-- Parent Account Lookup -->
    <fields>Annual_Energy_Usage_kWh__c</fields> <!-- Custom numeric usage field -->
    <fields>Average_Annual_Electric_Cost__c</fields> <!-- Custom currency cost field -->
    <fields>Type_of_Installation__c</fields> <!-- Custom picklist installation type -->
    <!-- Human-readable label displayed in Setup UI -->
    <label>Energy Audit Compact Layout</label>
</CompactLayout>
EOF

# 2. Assign Primary Compact Layout in Energy_Audit__c Metadata
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Custom Object Metadata Definition for Energy_Audit__c -->
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Energy Audit</label>
    <pluralLabel>Energy Audits</pluralLabel>
    <!-- Sets Energy_Audit_Compact_Layout as primary default compact layout -->
    <compactLayoutAssignment>Energy_Audit_Compact_Layout</compactLayoutAssignment>
    <nameField>
        <label>Energy Audit Name</label>
        <type>Text</type>
        <trackFeedHistory>true</trackFeedHistory>
    </nameField>
    <sharingModel>ReadWrite</sharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableSearch>true</enableSearch>
    <enableFeeds>true</enableFeeds>
</CustomObject>
EOF
```

---

### 2. `[REQ-5.4.G1.DEP]` Deploy Guided Activity Metadata

```bash
# Set up output directory for SFDX deploy JSON logs
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

# Deploy Energy_Audit__c metadata to target org (myDevOrg)
sf project deploy start \
  -d force-app/main/default/objects/Energy_Audit__c \
  -o myDevOrg \
  --json | tee "$UNIT_DIR/UNIT_4_GUIDED_DEPLOY_COMPACT_LAYOUT.json"
```

---

### 3. `[REQ-5.4.G1.AUD]` Audit Guided Activity Deployment

```bash
# Set up output directory for audit logs
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

# Query deployed Energy Audit compact layout via Tooling API
sf data query \
  -o myDevOrg \
  --use-tooling-api \
  -q "SELECT Id, DeveloperName, MasterLabel, SobjectType FROM CompactLayout WHERE DeveloperName='Energy_Audit_Compact_Layout'" \
  --json | tee "$UNIT_DIR/UNIT_4_GUIDED_AUDIT.json"
```

---

## Part 2: Hands-On Challenge (`Opportunity`)

When Ursa Major Solar salespeople are on site with a customer, they need key opportunity metrics right at the top of the record.

### 1. `[REQ-5.4.C1.1]` & `[REQ-5.4.C1.2]` Create Metadata & Assign Primary Layout

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

```bash
# Create target directory for Opportunity compact layout metadata
mkdir -p force-app/main/default/objects/Opportunity/compactLayouts

# 1. Generate XML metadata file for Opportunity compact layout
cat << 'EOF' > force-app/main/default/objects/Opportunity/compactLayouts/New_Oppty_Compact_Layout.compactLayout-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Salesforce Compact Layout Definition for Opportunity Standard Object -->
<CompactLayout xmlns="http://soap.sforce.com/2006/04/metadata">
    <!-- Unique developer API name matching Trailhead challenge requirement -->
    <fullName>New_Oppty_Compact_Layout</fullName>
    <!-- Ordered fields for key record metrics visible in the Highlights Panel -->
    <fields>Name</fields> <!-- 1. Opportunity Name (bold header) -->
    <fields>Probability</fields> <!-- 2. Win Probability (%) -->
    <fields>CloseDate</fields> <!-- 3. Expected Close Date -->
    <fields>StageName</fields> <!-- 4. Sales Opportunity Stage -->
    <fields>Amount</fields> <!-- 5. Revenue / Deal Amount -->
    <fields>OwnerId</fields> <!-- 6. Opportunity Record Owner -->
    <!-- Human-readable UI label -->
    <label>New Oppty Compact Layout</label>
</CompactLayout>
EOF

# 2. Assign Primary Compact Layout in Opportunity Object Metadata
cat << 'EOF' > force-app/main/default/objects/Opportunity/Opportunity.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Object Metadata Definition for Opportunity Standard Object -->
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <!-- Sets New_Oppty_Compact_Layout as primary default compact layout -->
    <compactLayoutAssignment>New_Oppty_Compact_Layout</compactLayoutAssignment>
</CustomObject>
EOF
```

---

### 2. `[REQ-5.4.C1.DEP]` Deploy Challenge Metadata

```bash
# Set up output directory for SFDX deploy JSON logs
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

# Deploy Opportunity metadata to target org (myDevOrg)
sf project deploy start \
  -d force-app/main/default/objects/Opportunity \
  -o myDevOrg \
  --json | tee "$UNIT_DIR/UNIT_4_CHALLENGE_DEPLOY_COMPACT_LAYOUT.json"
```

---

### 3. `[REQ-5.4.C1.AUD]` Audit Challenge Deployment

```bash
# Set up output directory for audit logs
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

# Query deployed Opportunity compact layout via Tooling API
sf data query \
  -o myDevOrg \
  --use-tooling-api \
  -q "SELECT Id, DeveloperName, MasterLabel, SobjectType FROM CompactLayout WHERE DeveloperName='New_Oppty_Compact_Layout'" \
  --json | tee "$UNIT_DIR/UNIT_4_CHALLENGE_AUDIT.json"
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
