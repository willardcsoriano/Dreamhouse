# Work with Schema Builder

**Source:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/data_modeling/schema_builder?trail_id=force_com_dev_beginner)

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [See Your Data Model in Action](#see-your-data-model-in-action)
- [Create an Object with Schema Builder](#create-an-object-with-schema-builder)
- [Create Fields with Schema Builder](#create-fields-with-schema-builder)
- [Sum It Up](#sum-it-up)
- [Resources](#resources)
- [Hands-On Challenge](#hands-on-challenge)
  - [Your Challenge — Use Schema Builder to create a custom field for the Property object](#your-challenge-use-schema-builder-to-create-a-custom-field-for-the-property-object)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem-engineering-learnings)

## Learning Objectives

After completing this unit, you'll be able to:

- Describe the advantages of using Schema Builder for data modeling.
- Use Schema Builder to create a schema for a given object model.
- Use Schema Builder to add a custom object to your schema.
- Use Schema Builder to add a custom field to your schema.

> **Accessibility:** This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click this link: Open Trailhead screen reader instructions.

## See Your Data Model in Action

By now, you and D'Angelo have created a handful of custom objects, fields, and relationships. Your app's data model is starting to get a little more complicated.

Schema Builder is a tool that lets you visualize and edit your data model. It's useful for designing and understanding complex data models like the one D'Angelo is building. Take a look at how it's done.

1. From Setup, search for and click **Schema Builder** in the Quick Find box.

   _Quick Find box location._

2. In the left panel, click **Clear All**.
3. Check **Contact**, **Favorite**, **Offer**, and **Property**. You should have the Favorite object from the previous unit, and the Offer and Property objects from the previous challenges.
4. Click **Auto-Layout**.

You'll see something like this:

_The user interface for the Schema Builder._

Notice that you can drag these objects around the canvas. This doesn't change your objects or relationships, but it can help you visualize your data model in a useful way. Schema Builder is a handy tool for introducing your Salesforce customizations to a co-worker or explaining the way data flows throughout your system.

_D'Angelo explaining the DreamHouse app schema to Michelle._

No CLI equivalent — Schema Builder's Auto-Layout canvas is a read-only visualization of objects and relationships that already exist. It doesn't create, verify, or change anything a deploy or query could confirm; do this in the browser.

## Create an Object with Schema Builder

You can also create objects using Schema Builder. If you prefer, you can create objects in this visual interface if you're designing your system and want to be able to revise all your customizations on the spot. Here's how it's done.

1. In the left sidebar, click the **Elements** tab.
2. Click **Object** and drag it onto the canvas.
3. Enter information about your object. You can make it whatever you want!
4. Click **Save**.

Your new object appears in the Schema Builder. That was quick! Next, add some fields.

No CLI equivalent — Trailhead deliberately leaves this object's label and fields up to you ("make it whatever you want"), so there's no fixed schema to hand-author a payload against. Do this in the browser.

## Create Fields with Schema Builder

Creating fields with Schema Builder is just like creating objects.

1. From the Elements tab, choose a field type and drag it onto the object you just created. Notice that you can create relationship fields, formula fields, and normal fields in Schema Builder.
2. Fill out the details about your new field.
3. Click **Save**.

Cool! If you go back through Object Manager, you'll see your new object shows up the same way your Property, Offer, and Favorite objects do.

_A comparison of an object in Object Manager and Schema Builder._

No CLI equivalent, for the same reason as the object above — this field's type and label are an open-ended choice, not a fixed requirement. Do this in the browser.

## Sum It Up

We've learned a lot in this module. First, you learned about the data model and the database including objects, fields, and records and created some of each for our DreamHouse app. Then you learned about relationships between objects and how you can visualize your data model using Schema Builder.

As you start to dive into more advanced content, you'll see custom objects and fields everywhere. Before you know it, you'll be a data modeling pro. Happy building!

## Resources

- Salesforce Help: Design Your Own Data Model With Schema Builder
- Salesforce Help: Schema Builder Custom Object Definition

---

## Hands-On Challenge

+500 points

**Get Ready:** You'll be completing this unit in your own hands-on org. Click Launch to get started, or click the name of your org to choose a different one.

### Your Challenge — Use Schema Builder to create a custom field for the Property object

DreamHouse brokers often visit properties with their clients. They want to see on the property record where the property is located. Use Schema Builder to add a street address field to the Property object.

- Data Type: Text Area
- Field Label: `Street Address`
- Field Name: `Street_Address`
- Always require a value in this field in order to save a record: Selected

The challenge asks you to build this through Schema Builder's canvas, but a required `TextArea` field has a small, stable, fully-documented Metadata API shape — it passes all three CLI-payload checks, so it's worth hand-authoring here rather than treated as GUI-only:

```bash
mkdir -p force-app/main/default/objects/Property__c/fields
mkdir -p docs/trails/developer_beginner/badges/04_data_modeling/logs

# Street_Address__c Text Area field — required, so it auto-grants universal FLS and skips fieldPermissions entirely
cat << 'EOF' > force-app/main/default/objects/Property__c/fields/Street_Address__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Street_Address__c</fullName>       <!-- "Field Name" you'd type in the wizard -->
    <label>Street Address</label>                 <!-- "Field Label" you typed -->
    <type>TextArea</type>                         <!-- "Data Type: Text Area" -->
    <required>true</required>                     <!-- The "Required" checkbox — auto-grants universal FLS, so no fieldPermissions step is needed below -->
</CustomField>
EOF

# Deploy Property__c schema to the Trailhead Playground
CMD="sf project deploy start -d force-app/main/default/objects/Property__c -o trailhead-playground --json"
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } \
  | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_3_CHALLENGE_DEPLOY_AUDIT.json

# Verify Street_Address__c's data type and required-ness via the Tooling API
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT QualifiedApiName, DataType, IsRequired FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c' AND QualifiedApiName = 'Street_Address__c'\" --json"
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } \
  | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_3_CHALLENGE_VERIFICATION_AUDIT.json
```

## Technical Post-Mortem & Engineering Learnings

_No hiccups logged yet — append Hiccup → Resolution pairs here after running Stage 4 against the target org._
