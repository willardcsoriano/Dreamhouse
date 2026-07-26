# Trailhead Unit: Optimize Customer Data with Standard and Custom Objects

**Trail:** Developer Beginner  
**Badge 04:** Data Modeling  
**Unit 1:** Optimize Customer Data with Standard and Custom Objects  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/data_modeling/objects_intro?trail_id=force_com_dev_beginner)

---

## Table of Contents

- [Introduction & Learning Objectives](#introduction--learning-objectives)
- [Guided Activities (Consolidated Requirements & Solutions)](#guided-activities-consolidated-requirements-solutions)
  - [Overview of Objects](#overview-of-objects)
  - [Get to Know Objects](#get-to-know-objects)
  - [Create a Custom Object](#create-a-custom-object)
    - [`[REQ-4.1.G1.1]` Create Custom Object (`Property__c`)](#req-41g11-create-custom-object-property__c)
  - [Get to Know Fields](#get-to-know-fields)
  - [Create a Custom Field](#create-a-custom-field)
    - [`[REQ-4.1.G2.1]` Create Custom Field (`Price__c`)](#req-41g21-create-custom-field-price__c)
  - [Create a Record](#create-a-record)
  - [Customize Responsibly](#customize-responsibly)
  - [Resources](#resources)
- [Hands-On Challenge (+500 points)](#hands-on-challenge-500-points)
  - [Get Ready](#get-ready)
  - [Your Challenge: Build a custom Offer object](#your-challenge-build-a-custom-offer-object)
    - [`[REQ-4.1.C1.1]` Create Custom Object (`Offer__c`)](#req-41c11-create-custom-object-offer__c)
    - [`[REQ-4.1.C1.2]` Create Custom Field (`Offer_Amount__c`)](#req-41c12-create-custom-field-offer_amount__c)
    - [`[REQ-4.1.C1.3]` Create Custom Field (`Target_Close_Date__c`)](#req-41c13-create-custom-field-target_close_date__c)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem--engineering-learnings)

---

## Introduction & Learning Objectives

After completing this unit, you'll be able to:

- Describe the perks of using objects on the Salesforce CRM platform.
- Explain the difference between standard objects and custom objects.
- List the types of custom fields an object can have.

> **Accessibility Note:** This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click this link: Open Trailhead screen reader instructions.

---

## Guided Activities (Consolidated Requirements & Solutions)

### Overview of Objects

DreamHouse is a realty company that provides a way for customers to shop for homes and contact real estate agents online. DreamHouse brokers use some of the standard Salesforce CRM functionality, like contacts and leads, to manage customer data of home buyers.

But when it comes to selling houses, there are a lot more things they want to track. For example, Salesforce doesn't include a standard way to track properties. How is DreamHouse supposed to know which homes they have for sale or how much each home costs?

Luckily, the Salesforce admin, D'Angelo, knows that the Salesforce platform offers a solution. And you can work with D'Angelo to see what he's building.

Start with the data model. A data model is more or less what it sounds like. It's a way to model what database tables look like in a way that makes sense to humans. If you're not familiar with databases, think about storing data in a spreadsheet. For example, D'Angelo can use a spreadsheet to track all DreamHouse's properties. Columns can store the address, cost, and other important attributes. Rows can store this information for each property that DreamHouse is selling. Database tables are set up in a similar way.

_A spreadsheet that stores property information._

But looking at data in tables isn't ideal for humans. That's where the data model comes in.

In Salesforce CRM, we think about database tables as objects, we think about columns as fields, and rows as records. So instead of an account spreadsheet or table, we have an Account object with fields and a bunch of identically structured records.

_A property record with the same information as the table._

When we talk about the data model, we're talking about the collection of objects and fields in an app. Learn more about objects and fields so you can start building your own data model.

---

### Get to Know Objects

Salesforce supports several different types of objects. There are standard objects, custom objects, external objects, platform events, and BigObjects. In this module, we focus on the two most common types of objects: standard and custom.

Standard objects are objects that are included with Salesforce. Common business objects like Account, Contact, Lead, and Opportunity are all standard objects.

Custom objects are objects that you create to store information that's specific to your company or industry. For DreamHouse, D'Angelo wants to build a custom Property object that stores information about the homes his company is selling.

Objects are containers for your information, but they also give you special functionality. For example, when you create a custom object, the platform automatically builds things like the page layout for the user interface.

---

### Create a Custom Object

Follow along as D'Angelo to see how he builds the Property object. You need this object later, so don't skip these steps!

1. Scroll to the bottom of this page and create a Trailhead Playground. Don't skip this step! You need to use a fresh and clean Trailhead Playground for this module.

   > **Note:** Even if you're completing this module as part of the Admin Beginner trail, be sure and create a new Trailhead Playground to complete these steps. You don't need to reinstall the Dreamhouse app in the new playground org.

2. Once your playground is created (it takes a minute!), press **Launch**.
3. Click the gear icon at the top of the page and launch setup.
4. Click the **Object Manager** tab.
5. Click **Create | Custom Object** in the top-right corner.
6. For Label, enter `Property`. Notice that the Object Name and Record Name fields auto-fill.
7. For Plural Label, enter `Properties`.
8. Prior to saving the custom object, scroll to the bottom of the page and select the checkbox **Launch New Custom Tab Wizard** after saving this custom object.
9. Leave the rest of the values as default and click **Save**.
10. On the New Custom Object Tab page, click the **Tab Style** field and select a style you like. The style sets the icon to display in the UI for the object.
11. Click **Next**, **Next**, and **Save**.

Steps 1–3 (playground creation, launch, Setup) have no CLI equivalent — do this in the browser. Steps 4–11 create the object itself, which does have a Metadata API surface.

#### `[REQ-4.1.G1.1]` Create Custom Object (`Property__c`)

- **Requirement Specifications:** Target: `Property__c` | Label: `Property` | Plural: `Properties` | Record Name: `Property Name` (Text) | Sharing: `ReadWrite` | Status: `Deployed`

```bash
mkdir -p force-app/main/default/objects/Property__c/fields

# Property custom object — Text name field, ReadWrite sharing (default)
cat << 'EOF' > force-app/main/default/objects/Property__c/Property__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Property</label>                          <!-- "Label" field from the New Custom Object form -->
    <pluralLabel>Properties</pluralLabel>             <!-- "Plural Label" field -->
    <nameField>
        <label>Property Name</label>                  <!-- Name shown on every Property record -->
        <type>Text</type>                             <!-- Plain text name (Trailhead left this as the default, not Auto Number) -->
    </nameField>
    <sharingModel>ReadWrite</sharingModel>            <!-- Default sharing: every user can view/edit any Property record -->
    <deploymentStatus>Deployed</deploymentStatus>     <!-- Object is live, not "In Development" -->
</CustomObject>
EOF
```

Great job! You just created your first custom object. Now, learn about adding fields to this object. The deploy and verification for `Property__c` are folded into the **Create a Custom Field** section below, since Trailhead has you add the `Price__c` field before ever saving the object metadata to source.

---

### Get to Know Fields

Every standard and custom object has fields attached to it. Get familiar with the different types of fields.

| Field Type   | What is it?                                                                                                                                                                                                                                         | Can I get an example?                                                                  |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| **Identity** | An 18-character, case-insensitive value that's automatically generated for every record. You can find a record's ID in its URL. Note: Records also have a 15-character case-sensitive version of its ID that can be used for specific applications. | An account ID looks like `0015000000Gv7qJAAN`.                                         |
| **System**   | Read-only fields that provide information about a record from the system, like when the record was created or when it was last changed.                                                                                                             | `CreatedDate`, `LastModifiedById`, and `LastModifiedDate`.                             |
| **Name**     | All records need names so you can distinguish between them. You can use text names or auto-numbered names that automatically increment every time you create a record.                                                                              | A contact's name can be Julie Bean. A support case's name can be CA-1024.              |
| **Custom**   | Fields you create on standard or custom objects are called custom fields.                                                                                                                                                                           | You can create a custom field on the Contact object to store your contacts' birthdays. |

Identity, system, and name fields are standard on every object in Salesforce. Each standard object also comes with a set of prebuilt, standard fields. You can customize standard objects by adding custom fields, and you can add custom fields to your custom objects.

Every field has a data type. A data type indicates what kind of information the field stores.

Salesforce supports a bunch of different data types, but here are a few you'll run into.

- **Checkbox** — for fields that are a simple "yes" or "no," a checkbox field is what you want.
- **Date or DateTime** — these field types represent dates or date/time combinations, like birthdays or sales milestones.
- **Formula** — this special field type holds a value that's automatically calculated based on a formula that you write. For example, D'Angelo can write a formula field that automatically calculates a real estate agent's commission on a home sale.

Again, there are quite a few field types, but most of them are fairly self-explanatory. The important takeaway here is that you want to think about what kind of data you're trying to store when you create a custom field.

---

### Create a Custom Field

The Property object you just created is pretty bare-bones. Add some custom fields to it. Head back to your Trailhead Playground.

1. From Setup, go to **Object Manager | Property**.
2. In the sidebar, click **Fields & Relationships**. Notice that there are already some fields there. There's a name field and some of the system fields you learned about earlier.
3. Click **New** in the top right.
4. For data type, select **Currency**.
5. Click **Next**.
6. Fill out the following:
   - Field Label: `Price`
   - Description: "The listed sale price of the home."
7. Check the **Required** box.
8. Click **Next**, **Next** again, and then **Save**.

#### `[REQ-4.1.G2.1]` Create Custom Field (`Price__c`)

- **Requirement Specifications:** Target: `Property__c.Price__c` | Label: `Price` | Type: `Currency` | Description: `The listed sale price of the home.` | Required: `true`

```bash
# Price__c Currency field — required, so it auto-grants universal FLS and skips fieldPermissions entirely
cat << 'EOF' > force-app/main/default/objects/Property__c/fields/Price__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Price__c</fullName>                                       <!-- "Field Name" you'd see auto-generated in the wizard -->
    <description>The listed sale price of the home.</description>      <!-- "Description" you typed -->
    <label>Price</label>                                                <!-- "Field Label" you typed -->
    <precision>18</precision>                                           <!-- Total digits allowed, integer + decimal combined -->
    <required>true</required>                                           <!-- The "Required" checkbox you ticked -->
    <scale>0</scale>                                                    <!-- Decimal places: 0, whole-dollar amounts only -->
    <type>Currency</type>                                               <!-- "Data type: Currency" you selected -->
</CustomField>
EOF

mkdir -p docs/trails/developer_beginner/badges/04_data_modeling/logs

# Deploy the Property__c object and Price__c field to the Trailhead Playground
CMD="sf project deploy start -d force-app/main/default/objects/Property__c -o trailhead-playground --json"
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } \
  | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_1_GUIDED_DEPLOY_AUDIT.json

# Verify Property__c's fields, their data types, and required-ness via the Tooling API
CMD="sf data query -o trailhead-playground --use-tooling-api --json -q \"SELECT QualifiedApiName, DataType, IsRequired FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'\""
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } \
  | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_1_GUIDED_VERIFICATION_AUDIT.json
```

You'll see your new Price field in the list of Property fields. In the Field Name column, notice that it says `Price__c` — the "__c" is an easy way to tell that a particular field is a custom field.

---

### Create a Record

Now, create a property record to see what you did.

1. From the App Launcher, find and select **Sales**.
2. Click the **Properties** tab in the navigation bar. If you don't see it, look under the **More** dropdown.
3. Click **New** in the top corner.
4. Enter a name and price for the property and click **Save**.

Awesome! You'll see something like the following.

_The record you just created._

No CLI equivalent — creating a demo record through the UI is the point of this step, not something to script.

---

### Customize Responsibly

While it can seem easy to add and customize objects, remember that what's going on under the hood is technically complicated. Here are some best practices to keep in mind as you start customizing your own org.

**Be thoughtful about names.** Once you start creating a bunch of objects, it can be tempting to give them "lazy" names. For example, if D'Angelo created another custom object to track condominiums, he might be tempted to name it Property2 instead of Condominium. That's a recipe for confusion in your org. Give your objects and fields descriptive, unique names to improve clarity.

**Help out your users.** Even with careful naming, your users might not always be clear about the purpose of a particular object or field. Include descriptions for your custom objects and fields. For specialized or complicated customizations, use help text to give more details.

**Require fields when necessary.** Sometimes, you'll want to force your users to fill out a field when they're creating a record on a certain object. Every property needs a price, right? Make important fields required to avoid incomplete data.

---

### Resources

- Salesforce Help: Customize Your Salesforce Org
- Salesforce Help: Store Information That's Unique to Your Organization
- Trailblazer Community: Customer Success Community

---

## Hands-On Challenge (+500 points)

### Get Ready

You'll be completing this unit in your own hands-on org. Click Launch to get started, or click the name of your org to choose a different one.

### Your Challenge: Build a custom Offer object

When a homebuyer makes an offer to buy a property, the brokers at DreamHouse Realty need to track the details in Salesforce. Create a custom object they can use to record the offer amount and target close date for the sale. Use auto numbering to generate the name of each offer record.

1. Create a custom object
   - Label: `Offer`
   - Object Name: `Offer`
   - Record Name: `Offer Name`
   - Data Type: Auto Number
   - Display Format: `OF-{0000}`
   - Starting Number: `1`
2. Create a custom currency field on the Offer object
   - Data Type: Currency
   - Field Label: `Offer Amount`
   - Field Name: `Offer_Amount`
3. Create a custom date field on the Offer object
   - Data Type: Date
   - Field Label: `Target Close Date`
   - Field Name: `Target_Close_Date`

#### `[REQ-4.1.C1.1]` Create Custom Object (`Offer__c`)

- **Requirement Specifications:** Target: `Offer__c` | Label: `Offer` | Plural: `Offers` | Name: `Offer Name` | Type: `AutoNumber` (`OF-{0000}`)

#### `[REQ-4.1.C1.2]` Create Custom Field (`Offer_Amount__c`)

- **Requirement Specifications:** Target: `Offer__c.Offer_Amount__c` | Label: `Offer Amount` | Type: `Currency` | Precision: `18` | Scale: `2`

#### `[REQ-4.1.C1.3]` Create Custom Field (`Target_Close_Date__c`)

- **Requirement Specifications:** Target: `Offer__c.Target_Close_Date__c` | Label: `Target Close Date` | Type: `Date`

```bash
mkdir -p force-app/main/default/objects/Offer__c/fields
mkdir -p docs/trails/developer_beginner/badges/04_data_modeling/logs

# Offer custom object — AutoNumber name field, format OF-{0000}, starts at 1 by default
cat << 'EOF' > force-app/main/default/objects/Offer__c/Offer__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Offer</label>                                     <!-- Object Label -->
    <pluralLabel>Offers</pluralLabel>                        <!-- Plural Label -->
    <nameField>
        <displayFormat>OF-{0000}</displayFormat>              <!-- Naming pattern: OF-0001, OF-0002, ... -->
        <label>Offer Name</label>                             <!-- Name shown on every Offer record -->
        <type>AutoNumber</type>                               <!-- "Data Type: Auto Number" — auto-increments, starts at 1 by default -->
    </nameField>
    <sharingModel>ReadWrite</sharingModel>                   <!-- Default sharing: every user can view/edit any Offer record -->
    <deploymentStatus>Deployed</deploymentStatus>            <!-- Object is live, not "In Development" -->
</CustomObject>
EOF

# Offer_Amount__c Currency field — precision is total digit count (integer + scale), not just the wizard's "Length"; not required, so it needs explicit FLS below
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Offer_Amount__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Offer_Amount__c</fullName>                    <!-- Field Name -->
    <label>Offer Amount</label>                              <!-- Field Label -->
    <precision>18</precision>                                <!-- Total digits allowed (16 before the decimal + 2 after) -->
    <required>false</required>                               <!-- Not required, so it needs its own visibility grant below -->
    <scale>2</scale>                                          <!-- Decimal places: 2, i.e. cents -->
    <type>Currency</type>                                    <!-- "Data type: Currency" -->
</CustomField>
EOF

# Not required — needs explicit FLS to avoid the Ghost Field anti-pattern (field exists but is invisible/non-editable by default)
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Offer_Amount__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml

# Target_Close_Date__c Date field — not required, so it needs explicit FLS below
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Target_Close_Date__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Target_Close_Date__c</fullName>               <!-- Field Name -->
    <label>Target Close Date</label>                         <!-- Field Label -->
    <required>false</required>                               <!-- Not required, so it needs its own visibility grant below -->
    <type>Date</type>                                        <!-- "Data type: Date" -->
</CustomField>
EOF

# Not required — needs explicit FLS to avoid the Ghost Field anti-pattern
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Target_Close_Date__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml

# Deploy Offer__c's schema and its Admin profile FLS grants atomically — never as two separate deploys that could land out of order
CMD="sf project deploy start -d force-app/main/default/objects/Offer__c -d force-app/main/default/profiles -o trailhead-playground --json"
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } \
  | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_1_CHALLENGE_DEPLOY_AUDIT.json

# Verify Offer__c's fields and their data types via the Tooling API
CMD="sf data query -o trailhead-playground --use-tooling-api --json -q \"SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'\""
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } \
  | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_1_CHALLENGE_VERIFICATION_AUDIT_SCHEMA.json

# Verify the sed-based FLS grants actually landed on the Admin profile — confirms Offer_Amount__c and Target_Close_Date__c aren't Ghost Fields
CMD="sf data query -o trailhead-playground --use-tooling-api --json -q \"SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE SobjectType='Offer__c'\""
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } \
  | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_1_CHALLENGE_VERIFICATION_AUDIT_FIELDPERMISSIONS.json
```

---

## Technical Post-Mortem & Engineering Learnings

_No hiccups logged yet — append Hiccup → Resolution pairs here after running Stage 4 against the target org._
