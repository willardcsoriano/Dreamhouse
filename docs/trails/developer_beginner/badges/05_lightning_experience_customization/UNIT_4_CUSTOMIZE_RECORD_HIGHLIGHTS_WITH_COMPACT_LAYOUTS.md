# Trailhead Unit: Customize Record Highlights with Compact Layouts

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 4:** Customize Record Highlights with Compact Layouts  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_compact_layouts?trail_id=force_com_dev_beginner)

---

## Learning Objectives

After completing this unit, you’ll be able to:

- Describe how compact layouts help your users.
- Create a custom compact layout.

---

## What Do Compact Layouts Do?

Compact layouts control which fields your users see in the highlights panel at the top of a record. They also control the fields that appear in the expanded lookup card you see when you hover over a link in record details, and in the details section when you expand an activity in the activity timeline.

Compact layouts help make your team more productive by presenting them with the key record information so they can easily manage their work. For example, show phone numbers and regions on an account. Or, show stages, amounts, and ownership fields on an opportunity. With compact layouts, you can highlight whatever your users need to see at a glance when they look at a record.

As with page layouts, there are separate compact layouts for each object. Here’s an example of an opportunity record page. The first several fields you assign to an object’s compact layout appear in the object’s record highlights panel and in the expanded lookup card you see when you hover over a link in record details. The field you put first displays at the top in bold.

In this case, the highlights panel reflects the fields on the opportunity compact layout, and the expanded lookup card reflects the fields from the account compact layout.

> **Note:** Compact layouts also control how records display in the Salesforce mobile app. If your company uses the Salesforce mobile app, you can help your users see what they need on mobile screens, where space is limited and quick recognition of records is important.

### Example

Here’s a sample compact layout edit page for the Account object. It shows the name of the layout and a list of fields to display.

Here’s a record page for the same account object in Lightning Experience. You can see the account’s name, phone number, type, industry, rating, and account owner at the top of the page.

And here’s what that same account record looks like in the mobile app.

---

## Create a Compact Layout

When you create a custom object, it’s automatically assigned to a system default compact layout, which has only one field on it: the object name. Maria wants to call attention to the most important fields on the object when her users view the audit records. Let’s make that happen by creating a custom compact layout for the Energy Audit custom object.

1. First, find and open the compact layouts node in Setup for Energy Audit.
   - From Setup, click **Object Manager**.
   - Click **Energy Audit** to open the object and then click **Compact Layouts**.
2. You can see that the System Default compact layout is assigned as the primary compact layout right now. We’re going to change that.
3. Click **New**.
4. Give the compact layout a label: **Energy Audit Compact Layout**.
5. Add these fields to the compact layout, in this order:
   - **Energy Audit Name**
   - **Account**
   - **Annual Energy Usage (kWh)**
   - **Average Annual Electric Cost**
   - **Type of Installation**
6. Click **Save**.
7. Now let’s set the compact layout that you created as the primary compact layout for the object. This step makes the compact layout the new default for the Energy Audit custom object.
8. Click **Compact Layout Assignment** and then **Edit Assignment**.
9. Select **Energy Audit Compact Layout** and click **Save**.

Great job! Now, when users view an Energy Audit record, they see the most important information where they need it most—at the top of the record page.

> **Note:** Changes to compact layouts can sometimes take time to appear. If refreshing the page doesn’t help, try changing your display density to a different setting to force the page to reload.

```bash
# Deploys Energy_Audit_Compact_Layout and assigns it as the primary compact layout for Energy_Audit__c using Metadata API
mkdir -p force-app/main/default/objects/Energy_Audit__c/compactLayouts # Creates target directories for Energy_Audit__c compact layout metadata

cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/compactLayouts/Energy_Audit_Compact_Layout.compactLayout-meta.xml # Authors compact layout XML definition
<?xml version="1.0" encoding="UTF-8"?> <!-- Standard XML declaration -->
<!-- Salesforce Compact Layout Definition for Energy_Audit__c Custom Object --> <!-- Informational header comment -->
<CompactLayout xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Root element for CompactLayout metadata -->
    <fullName>Energy_Audit_Compact_Layout</fullName> <!-- Compact layout DeveloperName identifier -->
    <fields>Name</fields> <!-- 1. Energy Audit Name (primary bold header field) -->
    <fields>Account__c</fields> <!-- 2. Parent Account Lookup -->
    <fields>Annual_Energy_Usage_kWh__c</fields> <!-- 3. Custom numeric usage field -->
    <fields>Average_Annual_Electric_Cost__c</fields> <!-- 4. Custom currency cost field -->
    <fields>Type_of_Installation__c</fields> <!-- 5. Custom picklist installation type -->
    <label>Energy Audit Compact Layout</label> <!-- MasterLabel displayed in Setup UI -->
</CompactLayout>
EOF

cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/Energy_Audit__c.object-meta.xml # Authors CustomObject metadata assigning primary compact layout
<?xml version="1.0" encoding="UTF-8"?> <!-- Standard XML declaration -->
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Root element for CustomObject metadata -->
    <label>Energy Audit</label> <!-- Singular object label -->
    <pluralLabel>Energy Audits</pluralLabel> <!-- Plural object label -->
    <compactLayoutAssignment>Energy_Audit_Compact_Layout</compactLayoutAssignment> <!-- Primary compact layout default assignment -->
    <nameField> <!-- Standard Name field definition -->
        <label>Energy Audit Name</label> <!-- Name field label -->
        <type>Text</type> <!-- Name field data type -->
        <trackFeedHistory>true</trackFeedHistory> <!-- Enables Chatter feed tracking on Name -->
    </nameField>
    <sharingModel>ReadWrite</sharingModel> <!-- Object sharing model -->
    <deploymentStatus>Deployed</deploymentStatus> <!-- Object deployment status -->
    <enableSearch>true</enableSearch> <!-- Enables global search indexing -->
    <enableFeeds>true</enableFeeds> <!-- Enables Chatter feed tracking on object -->
</CustomObject>
EOF

CMD="sf project deploy start -d force-app/main/default/objects/Energy_Audit__c -o trailhead-playground --json" # Assigns deployment command string to variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_4_GUIDED_DEPLOY_AUDIT.json # Logs command JSON and executes deployment with output tee'd to log file
```

```bash
# Verifies Energy_Audit_Compact_Layout deployment and sObject assignment via Tooling API query
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT Id, DeveloperName, MasterLabel, SobjectType FROM CompactLayout WHERE DeveloperName='Energy_Audit_Compact_Layout'\" --json" # Assigns Tooling API SOQL query command string to variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_4_GUIDED_VERIFICATION_AUDIT.json # Logs command JSON and executes query with output tee'd to log file
```

---

## Resources

- [Salesforce Help: Compact Layouts](https://help.salesforce.com/s/articleView?id=sf.compact_layouts_overview.htm&type=5)
- [Salesforce Help: Notes on Compact Layouts](https://help.salesforce.com/s/articleView?id=sf.compact_layouts_notes.htm&type=5)
- [Salesforce Help: Assign Compact Layouts to Record Types](https://help.salesforce.com/s/articleView?id=sf.compact_layouts_assign.htm&type=5)

---

## Hands-On Challenge

### Get Ready

You’ll be completing this unit in your own hands-on org. Click **Launch** to get started, or click the name of your org to choose a different one.

### Your Challenge

#### Create a Custom Opportunity Compact Layout

When the Ursa Major Solar salespeople are on site with a customer, there are a few key fields they need to see right at the top of an opportunity record when they access Salesforce. Create a compact layout that will help them do that.

1. Create a compact layout for the Opportunity object:
   - **Label:** `New Oppty Compact Layout`
   - **Name:** `New_Oppty_Compact_Layout`
2. Include these fields, in this order: **Opportunity Name**, **Probability (%)**, **Close Date**, **Stage**, **Amount**, **Opportunity Owner**
3. Make it the primary compact layout

```bash
# Deploys New_Oppty_Compact_Layout and assigns it as primary compact layout on Opportunity using Metadata API
mkdir -p force-app/main/default/objects/Opportunity/compactLayouts # Creates target directories for Opportunity compact layout metadata

cat << 'EOF' > force-app/main/default/objects/Opportunity/compactLayouts/New_Oppty_Compact_Layout.compactLayout-meta.xml # Authors Opportunity compact layout XML definition
<?xml version="1.0" encoding="UTF-8"?> <!-- Standard XML declaration -->
<!-- Salesforce Compact Layout Definition for Opportunity Standard Object --> <!-- Informational header comment -->
<CompactLayout xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Root element for CompactLayout metadata -->
    <fullName>New_Oppty_Compact_Layout</fullName> <!-- Compact layout DeveloperName identifier -->
    <fields>Name</fields> <!-- 1. Opportunity Name (primary bold header field) -->
    <fields>Probability</fields> <!-- 2. Win Probability (%) -->
    <fields>CloseDate</fields> <!-- 3. Expected Close Date -->
    <fields>StageName</fields> <!-- 4. Sales Opportunity Stage -->
    <fields>Amount</fields> <!-- 5. Revenue / Deal Amount -->
    <fields>OwnerId</fields> <!-- 6. Opportunity Record Owner -->
    <label>New Oppty Compact Layout</label> <!-- MasterLabel displayed in Setup UI -->
</CompactLayout>
EOF

cat << 'EOF' > force-app/main/default/objects/Opportunity/Opportunity.object-meta.xml # Authors Opportunity CustomObject metadata with primary compact layout assignment
<?xml version="1.0" encoding="UTF-8"?> <!-- Standard XML declaration -->
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Root element for CustomObject metadata -->
    <compactLayoutAssignment>New_Oppty_Compact_Layout</compactLayoutAssignment> <!-- Sets primary compact layout default assignment -->
</CustomObject>
EOF

CMD="sf project deploy start -d force-app/main/default/objects/Opportunity -o trailhead-playground --json" # Assigns deployment command string to variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_4_CHALLENGE_DEPLOY_AUDIT.json # Logs command JSON and executes deployment with output tee'd to log file
```

```bash
# Verifies New_Oppty_Compact_Layout deployment and Opportunity sObject assignment via Tooling API query
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT Id, DeveloperName, MasterLabel, SobjectType FROM CompactLayout WHERE DeveloperName='New_Oppty_Compact_Layout'\" --json" # Assigns Tooling API SOQL query command string to variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_4_CHALLENGE_VERIFICATION_AUDIT.json # Logs command JSON and executes query with output tee'd to log file
```

---

## Technical Post-Mortem & Engineering Learnings

1. **Tooling API SOQL Field Name Discrepancy:**
   - **Hiccup:** Attempting to query `TargetEntity` on `CompactLayout` via Tooling API threw `INVALID_FIELD: No such column 'TargetEntity' on entity 'CompactLayout'`.
   - **Resolution:** In Tooling API for `CompactLayout`, the target sObject entity field is named `SobjectType`. Querying `SobjectType` returned `Energy_Audit__c` and `Opportunity` cleanly.
