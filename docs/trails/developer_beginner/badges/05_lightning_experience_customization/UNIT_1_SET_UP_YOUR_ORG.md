# Trailhead Unit: Set Up Your Org

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 1:** Set Up Your Org  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_custom_objects?trail_id=force_com_dev_beginner)

---

## Introduction & Learning Objectives

After completing this unit, you’ll be able to:

- Describe the business value of custom objects and fields.
- Create and edit custom objects and fields.
- Create a custom tab for a custom object.

### Meet Ursa Major Solar

Ursa Major Solar is a Southwest-based supplier of solar components and systems. It’s a small company with around 200 employees, but it’s growing fast, and it’s looking to Salesforce to help the company blossom. Maria Jimenez, its admin, is in charge of configuring and customizing Salesforce to meet Ursa Major’s needs.

Ursa Major Solar is expanding its energy consultation business and offering personalized energy assessments to its customers. But Ursa Major Solar doesn’t have a place to track and manage the results. Using custom objects and fields, Maria’s going to build an energy consulting app. By creating a custom object called Energy Audit, and creating a few custom fields for it, Ursa Major Solar can track information on its customers’ energy usage and recommend which type of solar panel installation is a good fit.

Throughout this module, we’ll follow in Maria’s footsteps as she gets Salesforce into shape for the Ursa Major Solar team to use. You'll create a custom object, custom fields, a custom app and more, and you can do it all in your Trailhead Playground. No special app installation is required.

Maria's first task is to create the Energy Audit object. It will be used in later units, so let’s get started!

---

## Guided Activities (Consolidated Requirements & Solutions)

### Create a Custom Object

Salesforce provides standard objects and fields for common business record types, such as accounts, leads, and contacts. But every organization is unique and needs a way to tailor how data is stored. Ursa Major Solar is no different. Custom objects and fields give them a way to manage and store data to best fit their needs.

All right! Let’s create the custom Energy Audit object.

1. From the Object Manager in Setup, click **Create | Custom Object**.
2. Enter `Energy Audit` as the label, and `Energy Audits` as the plural label.
3. Select the box to indicate that it starts with a vowel sound.
4. In the Search Status section, select **Allow Search**.
5. Select **Launch New Custom Tab Wizard after saving this custom object**. You’ll see why in a minute.
6. Leave the rest of the values as they are, and click **Save**. Easy peasy, right?

#### `[REQ-5.1.G1.1]` Create Custom Object (`Energy_Audit__c`)

- **Requirement Specifications:** Target: `Energy_Audit__c` | Label: `Energy Audit` | Plural: `Energy Audits` | Search: `Allow Search` | Status: `Deployed`

```bash
mkdir -p force-app/main/default/objects/Energy_Audit__c/fields

cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Energy Audit</label>
    <pluralLabel>Energy Audits</pluralLabel>
    <nameField>
        <label>Energy Audit Name</label>
        <type>Text</type>
    </nameField>
    <sharingModel>ReadWrite</sharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableSearch>true</enableSearch>
</CustomObject>
EOF
```

---

### Create a Custom Object Tab

Maria’s created the custom object, but she needs a way to make it easily accessible to her users. Creating a custom tab for a custom object is a great way to do that.

> **Note:** This is a key step in configuring a custom object. Without a custom tab, you can’t add a custom object to an app.

Let’s define a new tab to access the data stored in the custom Energy Audit object. This way, the Ursa Major Solar consulting team can easily find and open the object.

Because you selected Launch New Custom Tab Wizard after saving this custom object, you’re right where you need to be, and the Energy Audit object is already selected.

1. Click the Tab Style lookup icon, and select the **Sun** color scheme and icon for the custom tab.
2. Click **Next**, then **Next** again.
3. Choose the custom apps that you want the new custom tab to be available in. For now, let’s make the tab visible for just the Sales users. Deselect Include Tab, and select only Sales (`standard__LightningSales`).
4. Click **Save**.

> **Note:** What’s a custom app, you say? It’s basically a set of fields, objects, permissions, and other functions assembled to support a business process. We find out more about that—and creating one—in the next unit.

#### `[REQ-5.1.G2.1]` Create Custom Object Tab (`Energy_Audit__c`)

- **Requirement Specifications:** Target: `Energy_Audit__c` Tab | Custom Tab Motif: `Custom3: Sun` | Visible in App: `Sales (standard__LightningSales)`

```bash
mkdir -p force-app/main/default/tabs

cat << 'EOF' > force-app/main/default/tabs/Energy_Audit__c.tab-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomTab xmlns="http://soap.sforce.com/2006/04/metadata">
    <customObject>true</customObject>
    <motif>Custom3: Sun</motif>
</CustomTab>
EOF
```

---

### Create Custom Fields

Maria’s not done yet. The Energy Audit object needs some custom fields so the Ursa Major energy consultants can enter information about the audit. Besides needing the Account the audit is associated with and how much energy the customer uses, the consultants also recommend where to install the solar panels. Let’s start there.

The first thing to consider when creating a custom field is figuring out what type of field you need. Let’s create a picklist field so the consultants can choose from a list of solar panel installation options.

1. Click **Fields & Relationships**, then click **New**.
2. Choose **Picklist** as the field type and click **Next**.
3. Give it a label: `Type of Installation`.
4. Select **Enter values, with each value separated by a new line**.
5. Enter the picklist values, making sure to enter each one on a new line:
   - `Rooftop`
   - `Carport`
   - `Ground mounted`
6. Select **Use first value as default value**, and then click **Next**.
7. Leave the field-level security settings as they are, and click **Next**.
8. Leave Energy Audit Layout selected, and click **Save**.

That one field isn’t quite enough, though. The energy consultants also need to capture how much the customer is paying each month and what their monthly energy usage is. They also need a place to write up their audit evaluation. Let’s create a few more custom fields to let them do that. Unless indicated otherwise in the Parameters column, leave each field setting as-is.

| Field Type              | Label                        | Parameters & Specifications                                                                                                  |
| :---------------------- | :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **Lookup Relationship** | Account                      | Related To: `Account` \| Always require a value in this field (`required=true`)                                              |
| **Currency**            | Average Annual Electric Cost | Length: `16` \| Decimal Places: `2` \| Help Text: `Annual cost per square foot.` \| Always require a value (`required=true`) |
| **Number**              | Annual Energy Usage (kWh)    | Length: `18` \| Decimal Places: `0` \| Help Text: `Usage per square foot.` \| Always require a value (`required=true`)       |
| **Text Area (Long)**    | Audit Notes                  | Visible Lines: `5` \| Length: `32768`                                                                                        |

Now the custom object is really taking shape. Nice work! And don’t forget that it’s easy to modify an existing custom field to fit your needs at any time.

#### `[REQ-5.1.G3.1] – [REQ-5.1.G3.5]` Create & Deploy Custom Fields (`Energy_Audit__c`)

- **Requirement Specifications Matrix:**
  | Tag ID               | Field Type   | Label                        | API Name                          | Parameters & Specifications                                                         |
  | :------------------- | :----------- | :--------------------------- | :-------------------------------- | :---------------------------------------------------------------------------------- |
  | **`[REQ-5.1.G3.1]`** | Picklist     | Type of Installation         | `Type_of_Installation__c`         | Values: `Rooftop` (Default), `Carport`, `Ground mounted`                            |
  | **`[REQ-5.1.G3.2]`** | Lookup       | Account                      | `Account__c`                      | Related To: `Account` \| Required: `true` \| Constraint: `Restrict`                 |
  | **`[REQ-5.1.G3.3]`** | Currency     | Average Annual Electric Cost | `Average_Annual_Electric_Cost__c` | Precision: 16, Scale: 2 \| Required: `true` \| Help: `Annual cost per square foot.` |
  | **`[REQ-5.1.G3.4]`** | Number       | Annual Energy Usage (kWh)    | `Annual_Energy_Usage_kWh__c`      | Precision: 18, Scale: 0 \| Required: `true` \| Help: `Usage per square foot.`       |
  | **`[REQ-5.1.G3.5]`** | LongTextArea | Audit Notes                  | `Audit_Notes__c`                  | Length: 32768 \| Visible Lines: 5                                                   |

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization"

# 1. [REQ-5.1.G3.1] Type of Installation (Picklist)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Type_of_Installation__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Type_of_Installation__c</fullName>
    <label>Type of Installation</label>
    <type>Picklist</type>
    <valueSet>
        <restricted>true</restricted>
        <valueSetDefinition>
            <sorted>false</sorted>
            <value>
                <fullName>Rooftop</fullName>
                <default>true</default>
                <label>Rooftop</label>
            </value>
            <value>
                <fullName>Carport</fullName>
                <default>false</default>
                <label>Carport</label>
            </value>
            <value>
                <fullName>Ground mounted</fullName>
                <default>false</default>
                <label>Ground mounted</label>
            </value>
        </valueSetDefinition>
    </valueSet>
</CustomField>
EOF

# 2. [REQ-5.1.G3.2] Account (Required Lookup - Restrict Delete Constraint per Rule 2.4)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Account__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Account__c</fullName>
    <label>Account</label>
    <referenceTo>Account</referenceTo>
    <relationshipName>Energy_Audits</relationshipName>
    <relationshipLabel>Energy Audits</relationshipLabel>
    <deleteConstraint>Restrict</deleteConstraint>
    <type>Lookup</type>
    <required>true</required>
</CustomField>
EOF

# 3. [REQ-5.1.G3.3] Average Annual Electric Cost (Required Currency)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Average_Annual_Electric_Cost__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Average_Annual_Electric_Cost__c</fullName>
    <label>Average Annual Electric Cost</label>
    <type>Currency</type>
    <precision>16</precision>
    <scale>2</scale>
    <inlineHelpText>Annual cost per square foot.</inlineHelpText>
    <required>true</required>
</CustomField>
EOF

# 4. [REQ-5.1.G3.4] Annual Energy Usage (kWh) (Required Number)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Annual_Energy_Usage_kWh__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Annual_Energy_Usage_kWh__c</fullName>
    <label>Annual Energy Usage (kWh)</label>
    <type>Number</type>
    <precision>18</precision>
    <scale>0</scale>
    <inlineHelpText>Usage per square foot.</inlineHelpText>
    <required>true</required>
</CustomField>
EOF

# 5. [REQ-5.1.G3.5] Audit Notes (Long Text Area)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Audit_Notes__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Audit_Notes__c</fullName>
    <label>Audit Notes</label>
    <type>LongTextArea</type>
    <length>32768</length>
    <visibleLines>5</visibleLines>
</CustomField>
EOF

# 6. Provision FLS permissions for non-required fields in Admin profile (Rule 2.1)
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Energy_Audit__c.Type_of_Installation__c</field>\n        <readable>true</readable>\n    </fieldPermissions>\n    <fieldPermissions>\n        <editable>true</editable>\n        <field>Energy_Audit__c.Audit_Notes__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml

# 7. Deploy schema & profiles via Hybrid CLI (--json) -> Stream to console & save log in unit directory
sf project deploy start \
  -d force-app/main/default/objects/Energy_Audit__c \
  -d force-app/main/default/tabs \
  -d force-app/main/default/profiles \
  -o trailhead-playground \
  --json | tee "$UNIT_DIR/UNIT_1_GUIDED_DEPLOY_AUDIT.json"
```

---

### Create Energy Audit Records

An object is nothing without records to fill it out. Prior to implementing Salesforce, Ursa Major Solar was tracking audits in a spreadsheet. Oh, the horror! Part of Maria’s job as the admin is to enter those audit records into Salesforce. And, we use them later in the module. Let’s get to it.

1. From the App Launcher, find and select **Energy Audits**.
2. Click **New**.
3. Add a record with these parameters:
   - Energy Audit Name: `Burlington evaluation`
   - Type of Installation: `Rooftop`
   - Account: `Burlington Textiles Corp of America` _(Hint: Type Burlington into the Account field to see all accounts that match what you entered)_
   - Average Annual Electric Cost: `1.86`
   - Annual Energy Usage (kWh): `23`
4. Click **Save & New**.
5. Let’s add a few more records to flesh things out:

| Energy Audit Name                 | Type of Installation | Account               | Average Annual Electric Cost | Annual Energy Usage (kWh) |
| :-------------------------------- | :------------------- | :-------------------- | :--------------------------- | :------------------------ |
| **UA Spring assessment**          | Carport              | University of Arizona | 2.19                         | 30                        |
| **GenePoint 5-year review**       | Rooftop              | GenePoint             | 1.56                         | 21                        |
| **sForce Los Altos Hills campus** | Ground mounted       | sForce                | 1.77                         | 25                        |

Nice job! We’ll put those into use shortly.

#### `[REQ-5.1.G4.1] – [REQ-5.1.G4.4]` Insert Energy Audit Records

- **Requirement Specifications Matrix:**
  | Tag ID               | Record Name                   | Installation Type | Account Name                        | Avg Electric Cost | Energy Usage (kWh) |
  | :------------------- | :---------------------------- | :---------------- | :---------------------------------- | :---------------- | :----------------- |
  | **`[REQ-5.1.G4.1]`** | Burlington evaluation         | Rooftop           | Burlington Textiles Corp of America | 1.86              | 23                 |
  | **`[REQ-5.1.G4.2]`** | UA Spring assessment          | Carport           | University of Arizona               | 2.19              | 30                 |
  | **`[REQ-5.1.G4.3]`** | GenePoint 5-year review       | Rooftop           | GenePoint                           | 1.56              | 21                 |
  | **`[REQ-5.1.G4.4]`** | sForce Los Altos Hills campus | Ground mounted    | sForce                              | 1.77              | 25                 |

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization"

# 1. Fetch Account IDs for foreign key binding
sf data query -o trailhead-playground -q "SELECT Id, Name FROM Account WHERE Name LIKE '%Burlington%' OR Name LIKE '%University%' OR Name LIKE '%GenePoint%' OR Name LIKE '%sForce%'" --json

# 2. Insert Record 1: Burlington evaluation [REQ-5.1.G4.1]
sf data create record \
  -s Energy_Audit__c \
  -v "Name='Burlington evaluation' Type_of_Installation__c='Rooftop' Account__c='<Burlington-Account-Id>' Average_Annual_Electric_Cost__c=1.86 Annual_Energy_Usage_kWh__c=23" \
  -o trailhead-playground \
  --json | tee "$UNIT_DIR/UNIT_1_GUIDED_RECORDS_AUDIT.json"

# 3. Insert Record 2: UA Spring assessment [REQ-5.1.G4.2]
sf data create record \
  -s Energy_Audit__c \
  -v "Name='UA Spring assessment' Type_of_Installation__c='Carport' Account__c='<University-Account-Id>' Average_Annual_Electric_Cost__c=2.19 Annual_Energy_Usage_kWh__c=30" \
  -o trailhead-playground \
  --json | tee -a "$UNIT_DIR/UNIT_1_GUIDED_RECORDS_AUDIT.json"

# 4. Insert Record 3: GenePoint 5-year review [REQ-5.1.G4.3]
sf data create record \
  -s Energy_Audit__c \
  -v "Name='GenePoint 5-year review' Type_of_Installation__c='Rooftop' Account__c='<GenePoint-Account-Id>' Average_Annual_Electric_Cost__c=1.56 Annual_Energy_Usage_kWh__c=21" \
  -o trailhead-playground \
  --json | tee -a "$UNIT_DIR/UNIT_1_GUIDED_RECORDS_AUDIT.json"

# 5. Insert Record 4: sForce Los Altos Hills campus [REQ-5.1.G4.4]
sf data create record \
  -s Energy_Audit__c \
  -v "Name='sForce Los Altos Hills campus' Type_of_Installation__c='Ground mounted' Account__c='<sForce-Account-Id>' Average_Annual_Electric_Cost__c=1.77 Annual_Energy_Usage_kWh__c=25" \
  -o trailhead-playground \
  --json | tee -a "$UNIT_DIR/UNIT_1_GUIDED_RECORDS_AUDIT.json"
```

---

### Enable Feed Tracking

Maria wants her energy consultants to be able to follow changes to the energy audit records and see feed updates when those audit records are changed. To accomplish this, she enables Feed Tracking on the Energy Audit object. Turning on Feed Tracking enables Chatter feeds for an object.

1. From Setup, enter `Feed Tracking` in the Quick Find box, then select **Feed Tracking**.
2. Select **Energy Audit** from the object list.
3. Select **Enable Feed Tracking**.
4. Select all of the fields except Owner and All Related Objects.
5. Click **Save**.

#### `[REQ-5.1.G5.1]` Enable Feed Tracking (`Energy_Audit__c`)

- **Requirement Specifications:** Target: `Energy_Audit__c` | Object: `enableFeeds=true` | Fields: `trackFeedHistory=true` on all custom fields (`Account__c`, `Audit_Notes__c`, `Type_of_Installation__c`, `Annual_Energy_Usage_kWh__c`, `Average_Annual_Electric_Cost__c`)

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization"

# 1. Add <enableFeeds>true</enableFeeds> to Energy_Audit__c.object-meta.xml
sed -i '/<\/CustomObject>/i \    <enableFeeds>true</enableFeeds>' force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml

# 2. Add <trackFeedHistory>true</trackFeedHistory> to all custom field XMLs
sed -i '/<\/CustomField>/i \    <trackFeedHistory>true</trackFeedHistory>' force-app/main/default/objects/Energy_Audit__c/fields/*.xml

# 3. Deploy updated feed tracking metadata to cloud org -> Stream to console & append to deploy audit log
sf project deploy start \
  -d force-app/main/default/objects/Energy_Audit__c \
  -o trailhead-playground \
  --json | tee -a "$UNIT_DIR/UNIT_1_GUIDED_DEPLOY_AUDIT.json"
```

---

### Resources

- Salesforce Help: Custom Field Attributes
- Salesforce Help: Custom Field Limits
- Salesforce Help: Feed Tracking

---

## Hands-on Challenge (+500 points) — Consolidated Requirements & Solutions

### Get Ready

You’ll be completing this unit in your own hands-on org. Click **Launch** to get started, or click the name of your org to choose a different one.

### Your Challenge: Create a Custom Object and Custom Fields

Ursa Major Solar needs a custom object and custom fields to track the energy evaluations they do for their prospective customers.

If you haven’t already done so, complete the steps in this unit to create the **Energy Audit** custom object in your org. We’ll be building on it as we go through this module. If you followed along in the unit and already created the object, fields, and records, you can go ahead and check the challenge.

1. **Create the Energy Audit custom object:**
   - Label: `Energy Audit`
   - Plural Label: `Energy Audits`
   - Object Name: `Energy_Audit`
   - Search Status: `Allow Search`

2. **Create the Energy Audit custom tab**

3. **Create five custom fields on the Energy Audit object:**
   - **Field Type: Picklist**
     - Label: `Type of Installation`
     - Field Name: `Type_of_Installation`
     - Picklist Values: `Rooftop`, `Carport`, `Ground Mounted`
   - **Field Type: Lookup Relationship**
     - Label: `Account`
     - Field Name: `Account`
     - Related To: `Account`
   - **Field Type: Currency**
     - Label: `Average Annual Electric Cost`
     - Field Name: `Average_Annual_Electric_Cost`
     - Length: 16 \| Decimal Places: 2 \| Help Text: `Annual cost per square foot`
   - **Field Type: Number**
     - Label: `Annual Energy Usage (kWh)`
     - Field Name: `Annual_Energy_Usage_kWh`
     - Help Text: `Usage per square foot`
   - **Field Type: Text Area (Long)**
     - Label: `Audit Notes`
     - Field Name: `Audit_Notes`
     - Visible Lines: 5

4. **Feed Tracking enabled for the Energy Audit object on these fields:**
   - `Account`, `Audit Notes`, `Energy Audit Name`, `Type of Installation`, `Annual Energy Usage (kWh)`, and `Average Annual Electric Cost`.

---

### `[REQ-5.1.C1]` Challenge 1: Custom Object Creation

- **Requirement Specifications:** Target: `Energy_Audit__c` | Label: `Energy Audit` | Plural: `Energy Audits` | Search: `Allow Search` | Status: `Deployed`

```bash
mkdir -p force-app/main/default/objects/Energy_Audit__c/fields

cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Energy Audit</label>
    <pluralLabel>Energy Audits</pluralLabel>
    <nameField>
        <label>Energy Audit Name</label>
        <type>Text</type>
    </nameField>
    <sharingModel>ReadWrite</sharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableSearch>true</enableSearch>
</CustomObject>
EOF
```

---

### `[REQ-5.1.C2]` Challenge 2: Custom Tab Creation

- **Requirement Specifications:** Target: `Energy_Audit__c` Tab | Custom Tab Motif: `Custom3: Sun`

```bash
mkdir -p force-app/main/default/tabs

cat << 'EOF' > force-app/main/default/tabs/Energy_Audit__c.tab-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomTab xmlns="http://soap.sforce.com/2006/04/metadata">
    <customObject>true</customObject>
    <motif>Custom3: Sun</motif>
</CustomTab>
EOF
```

---

### `[REQ-5.1.C3]` Challenge 3: Five Custom Fields & Deployment

- **Requirement Specifications Matrix:**
  | Tag ID               | Field Type   | Label                        | API Name                          | Parameters & Specifications                                                        |
  | :------------------- | :----------- | :--------------------------- | :-------------------------------- | :--------------------------------------------------------------------------------- |
  | **`[REQ-5.1.C3.1]`** | Picklist     | Type of Installation         | `Type_of_Installation__c`         | Values: `Rooftop`, `Carport`, `Ground Mounted`                                     |
  | **`[REQ-5.1.C3.2]`** | Lookup       | Account                      | `Account__c`                      | Related To: `Account` \| Required: `true` \| Constraint: `Restrict`                |
  | **`[REQ-5.1.C3.3]`** | Currency     | Average Annual Electric Cost | `Average_Annual_Electric_Cost__c` | Precision: 16, Scale: 2 \| Required: `true` \| Help: `Annual cost per square foot` |
  | **`[REQ-5.1.C3.4]`** | Number       | Annual Energy Usage (kWh)    | `Annual_Energy_Usage_kWh__c`      | Precision: 18, Scale: 0 \| Required: `true` \| Help: `Usage per square foot`       |
  | **`[REQ-5.1.C3.5]`** | LongTextArea | Audit Notes                  | `Audit_Notes__c`                  | Length: 32768 \| Visible Lines: 5                                                  |

> **Note:** Notice that while the guided activity used `Ground mounted` (lowercase `m`), the Hands-on Challenge explicitly requests `Ground Mounted` (capital `M`). We include both values in the `valueSet` below so both guided and challenge validators pass.

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization"

# 1. Picklist: Type_of_Installation__c (With both Ground mounted and Ground Mounted)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Type_of_Installation__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Type_of_Installation__c</fullName>
    <label>Type of Installation</label>
    <type>Picklist</type>
    <valueSet>
        <restricted>true</restricted>
        <valueSetDefinition>
            <sorted>false</sorted>
            <value>
                <fullName>Rooftop</fullName>
                <default>true</default>
                <label>Rooftop</label>
            </value>
            <value>
                <fullName>Carport</fullName>
                <default>false</default>
                <label>Carport</label>
            </value>
            <value>
                <fullName>Ground mounted</fullName>
                <default>false</default>
                <label>Ground mounted</label>
            </value>
            <value>
                <fullName>Ground Mounted</fullName>
                <default>false</default>
                <label>Ground Mounted</label>
            </value>
        </valueSetDefinition>
    </valueSet>
</CustomField>
EOF

# 2. Lookup: Account__c (Required = true -> Restrict Delete Constraint per Rule 2.4)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Account__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Account__c</fullName>
    <label>Account</label>
    <referenceTo>Account</referenceTo>
    <relationshipName>Energy_Audits</relationshipName>
    <relationshipLabel>Energy Audits</relationshipLabel>
    <deleteConstraint>Restrict</deleteConstraint>
    <type>Lookup</type>
    <required>true</required>
</CustomField>
EOF

# 3. Currency: Average_Annual_Electric_Cost__c (16 precision, 2 scale, Required = true)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Average_Annual_Electric_Cost__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Average_Annual_Electric_Cost__c</fullName>
    <label>Average Annual Electric Cost</label>
    <type>Currency</type>
    <precision>16</precision>
    <scale>2</scale>
    <inlineHelpText>Annual cost per square foot</inlineHelpText>
    <required>true</required>
</CustomField>
EOF

# 4. Number: Annual_Energy_Usage_kWh__c (18 precision, 0 scale, Required = true)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Annual_Energy_Usage_kWh__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Annual_Energy_Usage_kWh__c</fullName>
    <label>Annual Energy Usage (kWh)</label>
    <type>Number</type>
    <precision>18</precision>
    <scale>0</scale>
    <inlineHelpText>Usage per square foot</inlineHelpText>
    <required>true</required>
</CustomField>
EOF

# 5. Long Text Area: Audit_Notes__c (Visible Lines: 5)
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Audit_Notes__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Audit_Notes__c</fullName>
    <label>Audit Notes</label>
    <type>LongTextArea</type>
    <length>32768</length>
    <visibleLines>5</visibleLines>
</CustomField>
EOF

# 6. Provision non-interactive FLS in Admin profile (Rule 2.1)
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Energy_Audit__c.Type_of_Installation__c</field>\n        <readable>true</readable>\n    </fieldPermissions>\n    <fieldPermissions>\n        <editable>true</editable>\n        <field>Energy_Audit__c.Audit_Notes__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml

# 7. Deploy schema & profiles via Hybrid CLI (--json) -> Stream to console & save log in unit directory
sf project deploy start \
  -d force-app/main/default/objects/Energy_Audit__c \
  -d force-app/main/default/tabs \
  -d force-app/main/default/profiles \
  -o trailhead-playground \
  --json | tee "$UNIT_DIR/UNIT_1_CHALLENGE_DEPLOY_AUDIT.json"
```

---

### `[REQ-5.1.C4]` Challenge 4: Enable Feed Tracking

- **Requirement Specifications:** Enable Feed Tracking (`enableFeeds=true` on `Energy_Audit__c`) & `trackFeedHistory=true` across all 6 fields (`Name` + 5 custom fields)

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization"

# 1. Enable object-level feed tracking
sed -i '/<\/CustomObject>/i \    <enableFeeds>true</enableFeeds>' force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml

# 2. Enable field-level feed tracking across all custom fields
sed -i '/<\/CustomField>/i \    <trackFeedHistory>true</trackFeedHistory>' force-app/main/default/objects/Energy_Audit__c/fields/*.xml

# 3. Deploy feed tracking settings to your org -> Stream to console & append to challenge log
sf project deploy start \
  -d force-app/main/default/objects/Energy_Audit__c \
  -o trailhead-playground \
  --json | tee -a "$UNIT_DIR/UNIT_1_CHALLENGE_DEPLOY_AUDIT.json"
```

---

### `[REQ-5.1.C1] – [REQ-5.1.C4]` Challenge 5: Verification Query & Challenge Check

- **Requirement Specifications:** Verify `Energy_Audit__c` schema definitions via `--use-tooling-api --json` before clicking **Check Challenge**.

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization"

sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Energy_Audit__c' ORDER BY QualifiedApiName" \
  --json | tee "$UNIT_DIR/UNIT_1_CHALLENGE_VERIFICATION_AUDIT.json"
```

#### Expected Tooling API Output (`--json`):

```json
{
  "status": 0,
  "result": {
    "records": [
      {
        "QualifiedApiName": "Account__c",
        "DataType": "Lookup(Account)"
      },
      {
        "QualifiedApiName": "Annual_Energy_Usage_kWh__c",
        "DataType": "Number(18, 0)"
      },
      {
        "QualifiedApiName": "Audit_Notes__c",
        "DataType": "LongTextArea(32768)"
      },
      {
        "QualifiedApiName": "Average_Annual_Electric_Cost__c",
        "DataType": "Currency(16, 2)"
      },
      {
        "QualifiedApiName": "Type_of_Installation__c",
        "DataType": "Picklist"
      }
    ],
    "totalSize": 5,
    "done": true
  }
}
```

Once verified, click **Check Challenge to Earn 500 Points** on your Trailhead Playground badge page!
