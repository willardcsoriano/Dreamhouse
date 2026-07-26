# Trailhead Unit: Set Up Your Org

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 1:** Set Up Your Org  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_custom_objects?trail_id=force_com_dev_beginner)

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
  - [Meet Ursa Major Solar](#meet-ursa-major-solar)
- [Create a Custom Object](#create-a-custom-object)
- [Create a Custom Object Tab](#create-a-custom-object-tab)
- [Create Custom Fields](#create-custom-fields)
- [Create Energy Audit Records](#create-energy-audit-records)
- [Enable Feed Tracking](#enable-feed-tracking)
- [Resources](#resources)
- [Hands-on Challenge (+500 points)](#hands-on-challenge-500-points)
  - [Get Ready](#get-ready)
  - [Your Challenge: Create a Custom Object and Custom Fields](#your-challenge-create-a-custom-object-and-custom-fields)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem--engineering-learnings)

---

## Learning Objectives

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

## Create a Custom Object

Salesforce provides standard objects and fields for common business record types, such as accounts, leads, and contacts. But every organization is unique and needs a way to tailor how data is stored. Ursa Major Solar is no different. Custom objects and fields give them a way to manage and store data to best fit their needs.

All right! Let’s create the custom Energy Audit object.

1. From the Object Manager in Setup, click **Create | Custom Object**.
2. Enter `Energy Audit` as the label, and `Energy Audits` as the plural label.
3. Select the box to indicate that it starts with a vowel sound.
4. In the Search Status section, select **Allow Search**.
5. Select **Launch New Custom Tab Wizard after saving this custom object**. You’ll see why in a minute.
6. Leave the rest of the values as they are, and click **Save**. Easy peasy, right?

```bash
# Scaffolds the Energy_Audit__c custom object metadata definition file.
mkdir -p force-app/main/default/objects/Energy_Audit__c/fields # Creates target directory structure for Energy_Audit__c object and field definitions

cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Energy Audit</label> <!-- Object display label shown in UI navigation -->
    <pluralLabel>Energy Audits</pluralLabel> <!-- Plural display label for lists and navigation tabs -->
    <nameField> <!-- Defines standard record name field -->
        <label>Energy Audit Name</label> <!-- Display label for the standard record name field -->
        <type>Text</type> <!-- Data type for standard name field -->
        <trackFeedHistory>true</trackFeedHistory> <!-- Enables Chatter feed tracking on standard name field -->
    </nameField>
    <sharingModel>ReadWrite</sharingModel> <!-- Sets organization-wide default sharing model to Read/Write -->
    <deploymentStatus>Deployed</deploymentStatus> <!-- Makes object active and visible to authorized users -->
    <enableSearch>true</enableSearch> <!-- Allows records of this object to be found via Global Search -->
</CustomObject>
EOF
```

**Deploy and verification deferred — folded into the _Create Custom Fields_ step below, because the fields and tab are deployed atomically.**

---

## Create a Custom Object Tab

Maria’s created the custom object, but she needs a way to make it easily accessible to her users. Creating a custom tab for a custom object is a great way to do that.

> **Note:** This is a key step in configuring a custom object. Without a custom tab, you can’t add a custom object to an app.

Let’s define a new tab to access the data stored in the custom Energy Audit object. This way, the Ursa Major Solar consulting team can easily find and open the object.

Because you selected Launch New Custom Tab Wizard after saving this custom object, you’re right where you need to be, and the Energy Audit object is already selected.

1. Click the Tab Style lookup icon, and select the **Sun** color scheme and icon for the custom tab.
2. Click **Next**, then **Next** again.
3. Choose the custom apps that you want the new custom tab to be available in. For now, let’s make the tab visible for just the Sales users. Deselect Include Tab, and select only Sales (`standard__LightningSales`).
4. Click **Save**.

> **Note:** What’s a custom app, you say? It’s basically a set of fields, objects, permissions, and other functions assembled to support a business process. We find out more about that—and creating one—in the next unit.

```bash
# Scaffolds the Energy_Audit__c custom tab metadata definition with the Custom3: Sun motif.
mkdir -p force-app/main/default/tabs # Creates directory for custom tab metadata files

cat << 'EOF' > force-app/main/default/tabs/Energy_Audit__c.tab-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomTab xmlns="http://soap.sforce.com/2006/04/metadata">
    <customObject>true</customObject> <!-- Indicates this tab is associated with a custom object -->
    <motif>Custom3: Sun</motif> <!-- Sets tab style icon and color theme to Custom3: Sun -->
</CustomTab>
EOF
```

**Deploy and verification deferred — folded into the _Create Custom Fields_ step below, because the fields and tab are deployed atomically.**

---

## Create Custom Fields

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

| Field Type              | Label                        | Parameters                                                                                                               |
| :---------------------- | :--------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **Lookup Relationship** | Account                      | Related To: `Account` \| Always require a value in this field                                                            |
| **Currency**            | Average Annual Electric Cost | Length: `16` \| Decimal Places: `2` \| Help Text: `Annual cost per square foot.` \| Always require a value in this field |
| **Number**              | Annual Energy Usage (kWh)    | Help Text: `Usage per square foot.` \| Always require a value in this field                                              |
| **Text Area (Long)**    | Audit Notes                  | Visible Lines: `5`                                                                                                       |

Now the custom object is really taking shape. Nice work! And don’t forget that it’s easy to modify an existing custom field to fit your needs at any time. Let’s say you want to sort your data even more granularly. Or you want to change a text-entry field to a picklist to clean up data for reports. You can always come back and get things just right for your business needs.

```bash
# Scaffolds all 5 custom fields for Energy_Audit__c, grants FLS to Admin profile, and deploys object, tab, fields, and profiles atomically.
mkdir -p force-app/main/default/objects/Energy_Audit__c/fields # Ensures target directory exists for field metadata

# 1. Type_of_Installation__c
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Type_of_Installation__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Type_of_Installation__c</fullName> <!-- Custom field API name -->
    <label>Type of Installation</label> <!-- UI field label -->
    <type>Picklist</type> <!-- Data type set to Picklist -->
    <trackFeedHistory>true</trackFeedHistory> <!-- Enables Chatter feed tracking on field changes -->
    <valueSet>
        <restricted>true</restricted> <!-- Enforces picklist value restriction to defined list -->
        <valueSetDefinition>
            <sorted>false</sorted> <!-- Retains manual order of values rather than alphabetical -->
            <value>
                <fullName>Rooftop</fullName> <!-- Picklist option value -->
                <default>true</default> <!-- Sets Rooftop as default selection -->
                <label>Rooftop</label> <!-- UI label for picklist option -->
            </value>
            <value>
                <fullName>Carport</fullName> <!-- Picklist option value -->
                <default>false</default> <!-- Non-default picklist option -->
                <label>Carport</label> <!-- UI label for picklist option -->
            </value>
            <value>
                <fullName>Ground mounted</fullName> <!-- Picklist option value (case-insensitive in Metadata API) -->
                <default>false</default> <!-- Non-default picklist option -->
                <label>Ground mounted</label> <!-- UI label for picklist option -->
            </value>
        </valueSetDefinition>
    </valueSet>
</CustomField>
EOF

# 2. Account__c
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Account__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Account__c</fullName> <!-- Custom field API name -->
    <label>Account</label> <!-- UI field label -->
    <referenceTo>Account</referenceTo> <!-- Defines foreign key target object as Account -->
    <relationshipName>Energy_Audits</relationshipName> <!-- Child relationship name on Account -->
    <relationshipLabel>Energy Audits</relationshipLabel> <!-- UI label for related list on Account page layout -->
    <deleteConstraint>Restrict</deleteConstraint> <!-- Prevents parent Account deletion if child Energy Audits exist -->
    <type>Lookup</type> <!-- Data type set to Lookup Relationship -->
    <required>true</required> <!-- Makes field mandatory on all record creates/updates -->
    <trackFeedHistory>true</trackFeedHistory> <!-- Enables Chatter feed tracking on field changes -->
</CustomField>
EOF

# 3. Average_Annual_Electric_Cost__c
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Average_Annual_Electric_Cost__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Average_Annual_Electric_Cost__c</fullName> <!-- Custom field API name -->
    <label>Average Annual Electric Cost</label> <!-- UI field label -->
    <type>Currency</type> <!-- Data type set to Currency -->
    <precision>16</precision> <!-- Total number of digits allowed including decimals -->
    <scale>2</scale> <!-- Number of decimal places (2 for currency cents) -->
    <inlineHelpText>Annual cost per square foot.</inlineHelpText> <!-- Help text displayed beside field in UI -->
    <required>true</required> <!-- Makes field mandatory on record save -->
    <trackFeedHistory>true</trackFeedHistory> <!-- Enables Chatter feed tracking on field changes -->
</CustomField>
EOF

# 4. Annual_Energy_Usage_kWh__c
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Annual_Energy_Usage_kWh__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Annual_Energy_Usage_kWh__c</fullName> <!-- Custom field API name -->
    <label>Annual Energy Usage (kWh)</label> <!-- UI field label -->
    <type>Number</type> <!-- Data type set to Number -->
    <precision>18</precision> <!-- Total number of integer digits allowed -->
    <scale>0</scale> <!-- 0 decimal places for integer count -->
    <inlineHelpText>Usage per square foot.</inlineHelpText> <!-- Help text displayed beside field in UI -->
    <required>true</required> <!-- Makes field mandatory on record save -->
    <trackFeedHistory>true</trackFeedHistory> <!-- Enables Chatter feed tracking on field changes -->
</CustomField>
EOF

# 5. Audit_Notes__c
cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/fields/Audit_Notes__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Audit_Notes__c</fullName> <!-- Custom field API name -->
    <label>Audit Notes</label> <!-- UI field label -->
    <type>LongTextArea</type> <!-- Data type set to Long Text Area -->
    <length>32768</length> <!-- Maximum character capacity -->
    <visibleLines>5</visibleLines> <!-- Display height in UI layout -->
    <trackFeedHistory>true</trackFeedHistory> <!-- Enables Chatter feed tracking on field changes -->
</CustomField>
EOF

# Grant FLS permissions for Admin profile on non-required custom fields
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Energy_Audit__c.Type_of_Installation__c</field>\n        <readable>true</readable>\n    </fieldPermissions>\n    <fieldPermissions>\n        <editable>true</editable>\n        <field>Energy_Audit__c.Audit_Notes__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml # Inserts FLS grants into Admin profile XML before closing tag

# Deploy object, tab, fields, and profile metadata atomically to org
CMD="sf project deploy start -d force-app/main/default/objects/Energy_Audit__c -d force-app/main/default/tabs -d force-app/main/default/profiles -o trailhead-playground --json" # Assigns deploy command string to variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_1_GUIDED_DEPLOY_AUDIT.json # Logs command JSON and executes deployment, outputting to audit file
```

```bash
# Verifies that the Energy_Audit__c custom object and all 5 custom fields were created in the org.
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Energy_Audit__c' ORDER BY QualifiedApiName\" --json" # Tooling API query for Energy_Audit__c field metadata
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_1_GUIDED_VERIFICATION_AUDIT.json # Logs query command and executes Tooling API check to audit log
```

---

## Create Energy Audit Records

An object is nothing without records to fill it out. Prior to implementing Salesforce, Ursa Major Solar was tracking audits in a spreadsheet. Oh, the horror! Part of Maria’s job as the admin is to enter those audit records into Salesforce. And, we use them later in the module. Let’s get to it.

1. From the App Launcher, find and select **Energy Audits**.
2. Click **New**.
3. Add a record with these parameters:
   - Energy Audit Name: `Burlington evaluation`
   - Type of Installation: `Rooftop`
   - Account: `Burlington Textiles Corp of America` _(Hint: Type `Burlington` into the Account field to see all accounts that match what you entered)_
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

**No CLI equivalent — do this in the browser.** _(Optional CLI alternative provided below for automated data seeding.)_

```bash
# Inserts the 4 Energy Audit sample records using sf data create record CLI commands with dynamic Account ID resolution.
mkdir -p badges/05_lightning_experience_customization/logs # Ensures logs folder exists for audit logging

BURLINGTON_ID=$(sf data query -o trailhead-playground -q "SELECT Id FROM Account WHERE Name LIKE '%Burlington%' LIMIT 1" --json | jq -r '.result.records[0].Id') # Queries Account ID for Burlington
UNIV_ID=$(sf data query -o trailhead-playground -q "SELECT Id FROM Account WHERE Name LIKE '%University%' LIMIT 1" --json | jq -r '.result.records[0].Id') # Queries Account ID for University of Arizona
GENEPOINT_ID=$(sf data query -o trailhead-playground -q "SELECT Id FROM Account WHERE Name LIKE '%GenePoint%' LIMIT 1" --json | jq -r '.result.records[0].Id') # Queries Account ID for GenePoint
SFORCE_ID=$(sf data query -o trailhead-playground -q "SELECT Id FROM Account WHERE Name LIKE '%sForce%' LIMIT 1" --json | jq -r '.result.records[0].Id') # Queries Account ID for sForce

CMD="sf data create record -s Energy_Audit__c -v \"Name='Burlington evaluation' Type_of_Installation__c='Rooftop' Account__c='$BURLINGTON_ID' Average_Annual_Electric_Cost__c=1.86 Annual_Energy_Usage_kWh__c=23\" -o trailhead-playground --json" # Insert record 1
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_1_GUIDED_RECORDS_AUDIT.json # Execute and log

CMD="sf data create record -s Energy_Audit__c -v \"Name='UA Spring assessment' Type_of_Installation__c='Carport' Account__c='$UNIV_ID' Average_Annual_Electric_Cost__c=2.19 Annual_Energy_Usage_kWh__c=30\" -o trailhead-playground --json" # Insert record 2
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee -a badges/05_lightning_experience_customization/logs/UNIT_1_GUIDED_RECORDS_AUDIT.json # Execute and append log

CMD="sf data create record -s Energy_Audit__c -v \"Name='GenePoint 5-year review' Type_of_Installation__c='Rooftop' Account__c='$GENEPOINT_ID' Average_Annual_Electric_Cost__c=1.56 Annual_Energy_Usage_kWh__c=21\" -o trailhead-playground --json" # Insert record 3
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee -a badges/05_lightning_experience_customization/logs/UNIT_1_GUIDED_RECORDS_AUDIT.json # Execute and append log

CMD="sf data create record -s Energy_Audit__c -v \"Name='sForce Los Altos Hills campus' Type_of_Installation__c='Ground mounted' Account__c='$SFORCE_ID' Average_Annual_Electric_Cost__c=1.77 Annual_Energy_Usage_kWh__c=25\" -o trailhead-playground --json" # Insert record 4
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee -a badges/05_lightning_experience_customization/logs/UNIT_1_GUIDED_RECORDS_AUDIT.json # Execute and append log
```

---

## Enable Feed Tracking

Maria wants her energy consultants to be able to follow changes to the energy audit records and see feed updates when those audit records are changed. To accomplish this, she enables Feed Tracking on the Energy Audit object. Turning on Feed Tracking enables Chatter feeds for an object.

1. From Setup, enter `Feed Tracking` in the Quick Find box, then select **Feed Tracking**.
2. Select **Energy Audit** from the object list.
3. Select **Enable Feed Tracking**.
4. Select all of the fields except Owner and All Related Objects.
5. Click **Save**.

```bash
# Enables Feed Tracking on Energy_Audit__c object and field metadata definitions and deploys configuration to org.
sed -i '/<nameField>/,/<\/nameField>/ { /<\/nameField>/i \        <trackFeedHistory>true</trackFeedHistory>' -e '}' force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml # Enables feed tracking on standard name field
sed -i '/<\/CustomObject>/i \    <enableFeeds>true</enableFeeds>' force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml # Enables Chatter feed tracking at object level

CMD="sf project deploy start -d force-app/main/default/objects/Energy_Audit__c -o trailhead-playground --json" # Deploys updated feed tracking configuration
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee -a badges/05_lightning_experience_customization/logs/UNIT_1_GUIDED_DEPLOY_AUDIT.json # Logs deploy command and appends output to log
```

---

## Resources

- [Salesforce Help: Custom Field Attributes](https://help.salesforce.com/articleView?id=sf.custom_field_attributes.htm)
- [Salesforce Help: Custom Field Limits](https://help.salesforce.com/articleView?id=sf.custom_field_limits.htm)
- [Salesforce Help: Feed Tracking](https://help.salesforce.com/articleView?id=sf.collab_feed_tracking.htm)

---

## Hands-on Challenge (+500 points)

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
     - Select Enter values, with each value separated by a new line
     - Picklist Values: `Rooftop`, `Carport`, `Ground Mounted`
   - **Field Type: Lookup Relationship**
     - Label: `Account`
     - Field Name: `Account`
     - Related To: `Account`
   - **Field Type: Currency**
     - Label: `Average Annual Electric Cost`
     - Field Name: `Average_Annual_Electric_Cost`
     - Length: 16 | Decimal Places: 2 | Help Text: `Annual cost per square foot`
   - **Field Type: Number**
     - Label: `Annual Energy Usage (kWh)`
     - Field Name: `Annual_Energy_Usage_kWh`
     - Help Text: `Usage per square foot`
   - **Field Type: Text Area (Long)**
     - Label: `Audit Notes`
     - Field Name: `Audit_Notes`
     - Visible Lines: 5

4. **Feed Tracking enabled for the Energy Audit object on these fields:** `Account`, `Audit Notes`, `Energy Audit Name`, `Type of Installation`, `Annual Energy Usage (kWh)`, and `Average Annual Electric Cost`.

Already deployed — see the Guided Activity's payload above.

```bash
# Verifies that the Energy_Audit__c custom fields match the Challenge specifications via the Tooling API.
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Energy_Audit__c' ORDER BY QualifiedApiName\" --json" # Executes Tooling API query for FieldDefinition records
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_1_CHALLENGE_VERIFICATION_AUDIT.json # Captures command and output into JSON log file
```

---

## Technical Post-Mortem & Engineering Learnings

- **Trail:** Developer Beginner
- **Badge 05:** Lightning Experience Customization
- **Unit 1:** Set Up Your Org

### Key Engineering Hiccups & Solutions Encountered During Unit 1

1. **Picklist Value Case Sensitivity (`Duplicate picklist value ground mounted`):**
   - **Hiccup:** Guided activity specified `Ground mounted` (lowercase `m`), whereas the Challenge specified `Ground Mounted` (capital `M`). Including both in `Type_of_Installation__c.field-meta.xml` caused deployment to fail with `Duplicate picklist value ground mounted`.
   - **Resolution:** Salesforce picklist Metadata API definitions are case-insensitive. Standardized value sets to eliminate case-insensitive collisions.

2. **Standard Field Feed Tracking Metadata Schema (`<nameField>`):**
   - **Hiccup:** Feed tracking was enabled on custom fields (`<trackFeedHistory>true</trackFeedHistory>`) and object level (`<enableFeeds>true</enableFeeds>`), but Trailhead challenge check failed on field `Energy Audit Name`.
   - **Resolution:** Standard object name fields are defined inside `<nameField>` in `object-meta.xml`. Placed `<trackFeedHistory>true</trackFeedHistory>` explicitly inside the `<nameField>` block to enable Chatter Feed Tracking on `Name`.

3. **Lookup Foreign Key Binds & CLI Data Command Placeholders (`MALFORMED_ID`):**
   - **Hiccup:** Running `sf data create record -v "Account__c='<Burlington-Account-Id>'"` failed with `MALFORMED_ID` because text placeholders are invalid Salesforce IDs.
   - **Resolution:** Automated CLI scripts by binding Live Account IDs dynamically into bash variables via SOQL + `jq` (`BURLINGTON_ID=$(sf data query ... --json | jq -r '.result.records[0].Id')`).

4. **Terminal Input Buffer Overflows (Paste Truncation):**
   - **Hiccup:** Copy-pasting a 105-line monolithic bash code block into terminal caused line truncation (`ERROR_HTTP_404`), cutting off `cat << 'EOF'` mid-line.
   - **Resolution:** Modularized long CLI code blocks in documentation into paste-safe steps (`Challenge 3.1` and `Challenge 3.2`).

5. **Developer vs. AI Agent Responsibility Boundaries (Rule 4.4):**
   - **Hiccup:** Auto-committing and auto-executing CLI fixes created friction with hands-on learning retention.
   - **Resolution:** Established **Rule 4.4** in `docs/reference/SALESFORCE_DEVELOPMENT_RULES.md`, strictly separating file authoring (AI assistant permitted) from terminal execution and Git shipping (reserved exclusively for developer).
