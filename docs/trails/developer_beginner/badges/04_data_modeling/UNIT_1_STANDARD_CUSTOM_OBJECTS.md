# Optimize Customer Data with Standard and Custom Objects

**Source:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/data_modeling/objects_intro?trail_id=force_com_dev_beginner)

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Overview of Objects](#overview-of-objects)
- [Get to Know Objects](#get-to-know-objects)
- [Create a Custom Object](#create-a-custom-object)
- [Get to Know Fields](#get-to-know-fields)
- [Create a Custom Field](#create-a-custom-field)
- [Create a Record](#create-a-record)
- [Customize Responsibly](#customize-responsibly)
- [Hands-On Challenge](#hands-on-challenge)

## Learning Objectives

After completing this unit, you'll be able to:

- Describe the perks of using objects on the Salesforce CRM platform.
- Explain the difference between standard objects and custom objects.
- List the types of custom fields an object can have.

## Overview of Objects

DreamHouse is a realty company that provides a way for customers to shop for homes and contact real estate agents online. DreamHouse brokers use some of the standard Salesforce CRM functionality, like contacts and leads, to manage customer data of home buyers.

But when it comes to selling houses, there are a lot more things they want to track. For example, Salesforce doesn't include a standard way to track properties. How is DreamHouse supposed to know which homes they have for sale or how much each home costs?

Start with the data model. A data model is a way to model what database tables look like in a way that makes sense to humans — think of a spreadsheet, where columns store attributes like address and cost, and rows store that information for each property being sold.

In Salesforce CRM, we think about database tables as objects, columns as fields, and rows as records. So instead of an account spreadsheet or table, we have an Account object with fields and a bunch of identically structured records.

## Get to Know Objects

Salesforce supports several different types of objects — standard objects, custom objects, external objects, platform events, and BigObjects. This module focuses on the two most common types: standard and custom.

Standard objects are objects that are included with Salesforce. Common business objects like Account, Contact, Lead, and Opportunity are all standard objects.

Custom objects are objects that you create to store information that's specific to your company or industry. For DreamHouse, that means a custom `Property` object that stores information about the homes the company is selling.

Objects are containers for your information, but they also give you special functionality — when you create a custom object, the platform automatically builds things like the page layout for the user interface.

## Create a Custom Object

You need this object later, so don't skip these steps.

1. Scroll to the bottom of this page and create a Trailhead Playground. Even if you're completing this module as part of the Admin Beginner trail, be sure to create a new Trailhead Playground — you don't need to reinstall the DreamHouse app in the new playground org.
2. Once your playground is created, press **Launch**.
3. Click the gear icon at the top of the page and launch Setup.
4. Click the **Object Manager** tab.
5. Click **Create | Custom Object** in the top-right corner.
6. For Label, enter `Property`. Notice that the Object Name and Record Name fields auto-fill.
7. For Plural Label, enter `Properties`.
8. Prior to saving the custom object, scroll to the bottom of the page and check the box for **Launch New Custom Tab Wizard** after saving this custom object.
9. Leave the rest of the values as default and click **Save**.
10. On the New Custom Object Tab page, click the **Tab Style** field and select a style you like.
11. Click **Next**, **Next**, and **Save**.

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

## Get to Know Fields

Every standard and custom object has fields attached to it.

- **Identity** — an 18-character, case-insensitive value automatically generated for every record. You can find a record's ID in its URL. (Records also have a 15-character case-sensitive version of their ID, used for specific applications.) An account ID looks like `0015000000Gv7qJAAN`.
- **System** — read-only fields that provide information about a record from the system, like when it was created or last changed: `CreatedDate`, `LastModifiedById`, `LastModifiedDate`.
- **Name** — every record needs a name so you can distinguish between them, either a text name or an auto-numbered name that increments with each new record. A contact's name can be Julie Bean; a support case's name can be CA-1024.
- **Custom** — fields you create on standard or custom objects, e.g. a custom field on Contact to store a birthday.

Identity, system, and name fields are standard on every object in Salesforce, and each standard object comes with its own set of prebuilt fields. You can customize standard objects by adding custom fields, and you can add custom fields to your custom objects.

Every field has a data type indicating what kind of information it stores. A few common ones:

- **Checkbox** — for fields that are a simple "yes" or "no."
- **Date or DateTime** — represents dates or date/time combinations, like birthdays or sales milestones.
- **Formula** — holds a value automatically calculated based on a formula you write, e.g. an agent's commission on a home sale.

## Create a Custom Field

The Property object you just created is pretty bare-bones. Add a custom field to it.

1. From Setup, go to **Object Manager | Property**.
2. In the sidebar, click **Fields & Relationships**. Notice there are already some fields there — a name field and some of the system fields covered above.
3. Click **New** in the top right.
4. For data type, select **Currency**.
5. Click **Next**.
6. Fill out the following: Field Label `Price`, Description "The listed sale price of the home."
7. Check the **Required** box.
8. Click **Next**, **Next** again, and then **Save**.

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

# Deploy the Property__c object and Price__c field to the Trailhead Playground
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -o trailhead-playground \
  --json

# Verify Property__c's fields and their data types via the Tooling API
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  --json \
  -q "SELECT QualifiedApiName, DataType, IsRequired FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'"
```

You'll see your new Price field in the list of Property fields. In the Field Name column, notice that it says `Price__c` — the "__c" is an easy way to tell that a particular field is a custom field.

## Create a Record

Now, create a property record to see what you did.

1. From the App Launcher, find and select **Sales**.
2. Click the **Properties** tab in the navigation bar. If you don't see it, look under the **More** dropdown.
3. Click **New** in the top corner.
4. Enter a name and price for the property and click **Save**.

## Customize Responsibly

While it can seem easy to add and customize objects, remember that what's going on under the hood is technically complicated. Some best practices to keep in mind as you start customizing your own org:

- **Be thoughtful about names.** It can be tempting to give objects "lazy" names — e.g. naming a condominium-tracking object `Property2` instead of `Condominium`. That's a recipe for confusion. Give objects and fields descriptive, unique names.
- **Help out your users.** Even with careful naming, users might not be clear about the purpose of a particular object or field — include descriptions, and use help text for specialized or complicated customizations.
- **Require fields when necessary.** Every property needs a price, right? Make important fields required to avoid incomplete data.

---

## Hands-On Challenge

The challenge adds an `Offer__c` custom object — Auto Number name field, format `OF-{0000}` — with two custom fields: `Offer_Amount__c` (Currency) and `Target_Close_Date__c` (Date), both requiring Field-Level Security since neither is required.

```bash
mkdir -p force-app/main/default/objects/Offer__c/fields

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
sf project deploy start \
  -d force-app/main/default/objects/Offer__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground \
  --json

# Verify Offer__c's fields and their data types via the Tooling API
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  --json \
  -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'"
```
