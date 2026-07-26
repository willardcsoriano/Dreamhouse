# Trailhead Unit: Create and Customize List Views

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 3:** Create and Customize List Views  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_list?trail_id=force_com_dev_beginner)

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Create a List View](#create-a-list-view)
- [Customize a List View](#customize-a-list-view)
- [Create a List View Chart](#create-a-list-view-chart)
- [Resources](#resources)
- [Hands-On Challenge](#hands-on-challenge)
  - [Get Ready](#get-ready)
  - [Your Challenge](#your-challenge)
    - [Create a Custom List View](#create-a-custom-list-view)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem-engineering-learnings)
  - [Technical Learnings & Architecture](#technical-learnings-architecture)

## Learning Objectives

After completing this unit, you'll be able to:

- Create a custom list view.
- Create a custom list view chart.
- Edit and sort list views.

> **Note:**  
> **Accessibility**
>
> This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click the link below:
>
> Open Trailhead screen reader instructions.

---

## Create a List View

Since users don’t need an admin to create list views for them, Maria’s going to go get some coffee, and we’ll step into the shoes of one of her coworkers, Erin Donaghue. Erin’s a new sales rep for Ursa Major Solar, focusing on channel customers in the United States. She wants to set up a custom list view so she can see only those types of accounts. Here we go.

1. From the App Launcher, find and select the **Sales** app and select the **Accounts** tab.
2. From the list view controls **List View Controls**, select **New**.
3. Name the list `Channel Customers`.
4. Select **All users can see this list view**.
5. Click **Save**.

So far, the list view is showing us all of Maria's accounts, regardless of their type or location. Also, the Filters panel is now available.

Let’s set up some filters.

First, Erin wants to see only channel customers.

1. Click **Add Filter**.
2. From the Field dropdown menu, select **Type**.
3. Select the **equals** operator.
4. For Value, select **Customer - Channel**, then click **Save**, and then click **Save** again.

Great! The list has been pared down to only channel customers.

But let’s say Erin not only wants to see channel customers, but also only those on the West coast of the United States.

1. Add another filter where **Billing State/Province** equals `WA,OR,CA`.

Wow, that filtered the list down to only a few items. But you get the idea. The new view appears in the list view dropdown list so you can access it later.

You can collapse and expand the filter pane by clicking list view filters icon. You can change who can see the list view by clicking **List View Controls** and selecting **Sharing Settings**.

```bash
# Deploys initial Channel_Customers Account ListView metadata containing Type and Billing State filter criteria
mkdir -p force-app/main/default/objects/Account/listViews # Scaffolds directory structure for Account ListView metadata

cat << 'EOF' > force-app/main/default/objects/Account/listViews/Channel_Customers.listView-meta.xml # Generates initial ListView metadata definition file
<?xml version="1.0" encoding="UTF-8"?> <!-- Metadata API XML declaration -->
<ListView xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- ListView metadata root element -->
    <fullName>Channel_Customers</fullName> <!-- API name for the Account list view -->
    <columns>ACCOUNT.NAME</columns> <!-- Displays Account Name column -->
    <columns>ACCOUNT.SITE</columns> <!-- Displays Account Site column -->
    <columns>ACCOUNT.PHONE1</columns> <!-- Displays Phone column -->
    <columns>ACCOUNT.TYPE</columns> <!-- Displays Account Type column -->
    <columns>CORE.USERS.ALIAS</columns> <!-- Displays Account Owner Alias column -->
    <filterScope>Everything</filterScope> <!-- Shares list view visibility with all users -->
    <filters> <!-- Begins first filter definition -->
        <field>ACCOUNT.TYPE</field> <!-- Filter field for Account Type -->
        <operation>equals</operation> <!-- Filter comparison operator -->
        <value>Customer - Channel</value> <!-- Restricts results to Customer - Channel -->
    </filters> <!-- Ends first filter definition -->
    <filters> <!-- Begins second filter definition -->
        <field>ACCOUNT.ADDRESS1_STATE</field> <!-- Filter field for Billing State/Province -->
        <operation>equals</operation> <!-- Filter comparison operator -->
        <value>WA,OR,CA</value> <!-- Restricts results to WA, OR, or CA -->
    </filters> <!-- Ends second filter definition -->
    <label>Channel Customers</label> <!-- UI label displayed in Salesforce navigation -->
</ListView> <!-- Ends ListView metadata container -->
EOF <!-- End of XML heredoc payload -->

CMD="sf project deploy start -d force-app/main/default/objects/Account/listViews/Channel_Customers.listView-meta.xml -o trailhead-playground --json" # Assigns deployment command to CMD variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_3_GUIDED_LISTVIEW_DEPLOY.json # Deploys metadata and writes command log
```

**Deploy and verification deferred — folded into the _Customize a List View_ step below, because field selection for this list view occurs in the subsequent section.**

---

## Customize a List View

You’ve created a custom list view and added filters, but there’s even more you can do. Erin doesn’t want to see certain columns, and wants to add others. Let’s start there.

1. From the list view controls **List View Controls**, select **Select Fields to Display**.
2. Move **Account Site**, **Account Owner Alias**, and **Phone** out of the **Visible Fields** area, and add **Industry** and **Customer Priority** instead.
3. Click **Save**.

See the little arrow in the **Account Name** column header? That indicates which direction the contents of that column are sorted. Click the header to sort that column. The arrow indicates how the list is sorted: from the column’s first record Up Sort (alphanumerically) or its last Down Sort.

You can edit record fields directly from within a list view. Editable cells display a pencil icon Editable Field when you hover over the cell, while non-editable cells display a lock icon Uneditable Field.

```bash
# Updates Channel_Customers Account ListView metadata to display Industry and Customer Priority columns while removing Site, Alias, and Phone
cat << 'EOF' > force-app/main/default/objects/Account/listViews/Channel_Customers.listView-meta.xml # Overwrites ListView XML file with updated display columns
<?xml version="1.0" encoding="UTF-8"?> <!-- Metadata API XML declaration -->
<ListView xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- ListView metadata root element -->
    <fullName>Channel_Customers</fullName> <!-- API name for the Account list view -->
    <columns>ACCOUNT.NAME</columns> <!-- Displays Account Name column -->
    <columns>ACCOUNT.INDUSTRY</columns> <!-- Displays Industry column -->
    <columns>CustomerPriority__c</columns> <!-- Displays Customer Priority custom field column -->
    <filterScope>Everything</filterScope> <!-- Shares list view visibility with all users -->
    <filters> <!-- Begins first filter definition -->
        <field>ACCOUNT.TYPE</field> <!-- Filter field for Account Type -->
        <operation>equals</operation> <!-- Filter comparison operator -->
        <value>Customer - Channel</value> <!-- Restricts results to Customer - Channel -->
    </filters> <!-- Ends first filter definition -->
    <filters> <!-- Begins second filter definition -->
        <field>ACCOUNT.ADDRESS1_STATE</field> <!-- Filter field for Billing State/Province -->
        <operation>equals</operation> <!-- Filter comparison operator -->
        <value>WA,OR,CA</value> <!-- Restricts results to WA, OR, or CA -->
    </filters> <!-- Ends second filter definition -->
    <label>Channel Customers</label> <!-- UI label displayed in Salesforce navigation -->
</ListView> <!-- Ends ListView metadata container -->
EOF <!-- End of XML heredoc payload -->

CMD="sf project deploy start -d force-app/main/default/objects/Account/listViews/Channel_Customers.listView-meta.xml -o trailhead-playground --json" # Assigns deployment command to CMD variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_3_GUIDED_LISTVIEW_UPDATE.json # Deploys updated metadata and logs output
```

```bash
# Queries Tooling API to verify Channel_Customers ListView exists on Account object with total record size confirmation
CMD="sf data query -o trailhead-playground -q \"SELECT Id, Name, DeveloperName, SobjectType FROM ListView WHERE SobjectType = 'Account' AND DeveloperName = 'Channel_Customers'\" --use-tooling-api --json" # Assigns SOQL query to CMD variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_3_GUIDED_LISTVIEW_AUDIT.json # Executes Tooling API query and writes audit log
```

---

## Create a List View Chart

List view charts help you visualize your list view data. Erin wants to see which accounts represent the most overall pipeline value, so she’s going to add a chart to the All Opportunities list view. Let’s follow along.

1. From the Sales app, click the **Opportunities** tab.
2. Use the dropdown menu () to select the **All Opportunities** list view.
3. Click list view charts icon.
4. In the Charts panel that appears, click list view charts gear icon and select **New Chart**.
5. Name the chart `Pipeline Total Value` and give it these parameters.
   - **Chart Type:** Donut Chart
   - **Aggregate Type:** Sum
   - **Aggregate Field:** Amount
   - **Grouping Field:** Account Name
     The aggregate type specifies how the field data is calculated: by sum, count, or average. The aggregate field specifies the type of data to calculate. The grouping field labels the chart segments.
6. Click **Save**.

> **Note:**  
> When you create a list view chart for an object, such as Opportunities or Leads, the chart is associated with the object. The chart is available for any list view that you have permission to see for that object, except the Recently Viewed list.

**No CLI equivalent — do this in the browser.**

---

## Resources

- [Salesforce Help: Create or Clone a List View in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views.htm&type=5)
- [Salesforce Help: Edit List View Filters in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_edit_filters.htm&type=5)
- [Salesforce Help: Create a List View Chart in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_charts_create.htm&type=5)
- [Salesforce Help: Update Records Inline from a List View in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_inline_editing.htm&type=5)

---

## Hands-On Challenge

### Get Ready

You’ll be completing this unit in your own hands-on org. Click **Launch** to get started, or click the name of your org to choose a different one.

### Your Challenge

#### Create a Custom List View

Lance Park, one of Ursa Major Solar’s sales reps, wants to see a list of opportunities that are in the late stages of negotiation or have high probability to close, or both. Step into Lance’s shoes and make that happen.

1. Use the App Launcher to open the **Sales** app
2. Create an Opportunity list view:
   - **List Name:** `High Probability Opportunities`
   - **List API Name:** `High_Probability_Opportunities`
   - **Who sees this list view:** `All users can see this list view`
   - Show only opportunities whose stage is `Proposal/Price Quote` or `Negotiation/Review` and whose probability is greater than or equal to `50%`

```bash
# Deploys High_Probability_Opportunities Opportunity ListView metadata with stage and probability filters
mkdir -p force-app/main/default/objects/Opportunity/listViews # Scaffolds directory structure for Opportunity ListView metadata

cat << 'EOF' > force-app/main/default/objects/Opportunity/listViews/High_Probability_Opportunities.listView-meta.xml # Generates ListView metadata definition file
<?xml version="1.0" encoding="UTF-8"?> <!-- Metadata API XML declaration -->
<ListView xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- ListView metadata root element -->
    <fullName>High_Probability_Opportunities</fullName> <!-- API name for the Opportunity list view -->
    <filterScope>Everything</filterScope> <!-- Shares list view visibility with all users -->
    <filters> <!-- Begins Stage filter block -->
        <field>OPPORTUNITY.STAGE_NAME</field> <!-- Filter field targeting Opportunity Stage -->
        <operation>equals</operation> <!-- Comparison operator matching picklist values -->
        <value>Proposal/Price Quote,Negotiation/Review</value> <!-- Target stage values for late-stage opportunities -->
    </filters> <!-- Ends Stage filter block -->
    <filters> <!-- Begins Probability filter block -->
        <field>OPPORTUNITY.PROBABILITY</field> <!-- Filter field targeting Probability percentage -->
        <operation>greaterOrEqual</operation> <!-- Comparison operator for numerical threshold -->
        <value>50</value> <!-- Minimum probability percentage required -->
    </filters> <!-- Ends Probability filter block -->
    <label>High Probability Opportunities</label> <!-- UI label displayed in Salesforce navigation -->
</ListView> <!-- Ends ListView metadata container -->
EOF <!-- End of XML heredoc payload -->

CMD="sf project deploy start -d force-app/main/default/objects/Opportunity/listViews/High_Probability_Opportunities.listView-meta.xml -o trailhead-playground --json" # Assigns deployment command to CMD variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_3_CHALLENGE_DEPLOY.json # Deploys metadata and writes command log
```

```bash
# Queries Tooling API to verify High_Probability_Opportunities ListView exists on Opportunity object
CMD="sf data query -o trailhead-playground -q \"SELECT Id, Name, DeveloperName, SobjectType FROM ListView WHERE SobjectType = 'Opportunity' AND DeveloperName = 'High_Probability_Opportunities'\" --use-tooling-api --json" # Assigns SOQL query to CMD variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_3_CHALLENGE_VERIFICATION_AUDIT.json # Executes Tooling API query and writes audit log
```

---

## Technical Post-Mortem & Engineering Learnings

### Technical Learnings & Architecture

1. **ListView Metadata API Schema:**
   - Salesforce list views are represented in the Metadata API as XML files in `objects/<Object>/listViews/<DeveloperName>.listView-meta.xml`.
   - `ACCOUNT.TYPE` and `ACCOUNT.ADDRESS1_STATE` are standard field names used within filter definitions for the `Account` object, while `OPPORTUNITY.STAGE_NAME` and `OPPORTUNITY.PROBABILITY` are standard field names for `Opportunity`.
   - Multi-value picklist filter values are comma-separated strings inside `<value>` (e.g. `<value>WA,OR,CA</value>` or `<value>Proposal/Price Quote,Negotiation/Review</value>`).

2. **Lightning Experience List View Charts:**
   - List view charts (`ListViewChart`) in Lightning Experience are client-side UI configurations tied to the object level. They do not have a dedicated Metadata API CLI deployment surface separate from user UI state, making browser configuration the primary deployment mechanism for custom charts.

3. **Tooling API Querying:**
   - The `ListView` object in Salesforce can be queried via SOQL with `--use-tooling-api` to programmatically verify that custom list views (`Channel_Customers` and `High_Probability_Opportunities`) exist on target objects.
