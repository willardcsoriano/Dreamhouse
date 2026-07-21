# Create Object Relationships

**Source:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/data_modeling/object_relationships?trail_id=force_com_dev_beginner)

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [What Are Object Relationships?](#what-are-object-relationships)
- [The Wide World of Object Relationships](#the-wide-world-of-object-relationships)
  - [Lookup Relationships](#lookup-relationships)
  - [Master-Detail Relationships](#master-detail-relationships)
  - [More on Relationships](#more-on-relationships)
- [Create a Custom Object](#create-a-custom-object)
- [Create a Lookup Relationship](#create-a-lookup-relationship)
- [Create a Master-Detail Relationship](#create-a-master-detail-relationship)
- [Add a Favorite Property](#add-a-favorite-property)
- [Resources](#resources)
- [Hands-On Challenge](#hands-on-challenge)

## Learning Objectives

After completing this unit, you'll be able to:

- Define the different types of object relationships and their typical use cases.
- Create or modify a lookup relationship.
- Create or modify a master-detail relationship.

## What Are Object Relationships?

Now that you're comfortable with objects and fields, it's time to take things to the next level with object relationships. Object relationships are a special field type that connects two objects together.

Think about a standard object like Account. If a sales rep opens an account, they've probably been talking to a few people at that account's company. They've probably made contacts like executives or IT managers and stored those contacts' information in Salesforce.

It makes sense, then, that there should be a relationship between the Account object and the Contact object. And there is! When you look at an account record in Salesforce, you can see that there's a section for contacts on the Related tab, with a button that lets you quickly add a contact to an account.

The Account to Contact relationship is an example of a standard relationship in Salesforce. But just like objects and fields, you can build custom relationships as well. In the last unit, you created two objects: Property and Offer. Wouldn't it be great if all the offers made on a home showed up on its record in Salesforce?

## The Wide World of Object Relationships

There are two main types of object relationships: lookup and master-detail.

### Lookup Relationships

In our Account to Contact example above, the relationship between the two objects is a lookup relationship. A lookup relationship essentially links two objects together so that you can "look up" one object from the related items on another object.

Lookup relationships can be one-to-one or one-to-many. The Account to Contact relationship is one-to-many because a single account can have many related contacts.

### Master-Detail Relationships

While lookup relationships are fairly casual, master-detail relationships are a bit tighter. In this type of relationship, one object is the master and another is the detail. The master object controls certain behaviors of the detail object, like who can view the detail's data.

For example, say the owner of a property wanted to take their home off the market. DreamHouse wouldn't want to keep any offers made on that property. With a master-detail relationship between Property and Offer, you can delete the property and all its associated offers from your system.

### More on Relationships

Typically, you use lookup relationships when objects are only related in some cases. Objects in lookup relationships usually work as stand-alone objects and have their own tabs in the user interface.

In a master-detail relationship, the detail object doesn't work as a stand-alone — it's highly dependent on the master. If a record on the master object is deleted, all its related detail records are deleted as well. When you're creating master-detail relationships, you always create the relationship field on the detail object.

A third relationship type, hierarchical, is a special type of lookup only available on the User object — used for things like management chains between users.

## Create a Custom Object

DreamHouse wants a way to track users who mark particular properties as favorites on their website. To start, create a custom object called Favorite: Object Manager → Create → Custom Object → Label `Favorite`, Plural Label `Favorites`, check **Launch New Custom Tab Wizard** → Save → pick a tab style → Next, Next, Save.

```bash
# Favorite__c custom object — Text name field, ControlledByParent sharing (required for the Master-Detail detail side)
cat << 'EOF' > force-app/main/default/objects/Favorite__c/Favorite__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Favorite</label>
    <pluralLabel>Favorites</pluralLabel>
    <nameField>
        <label>Favorite Name</label>
        <type>Text</type>
    </nameField>
    <sharingModel>ControlledByParent</sharingModel>
    <externalSharingModel>ControlledByParent</externalSharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableActivities>false</enableActivities>
    <enableBulkApi>true</enableBulkApi>
    <enableFeeds>false</enableFeeds>
    <enableHistory>false</enableHistory>
    <enableReports>false</enableReports>
    <enableSearch>false</enableSearch>
    <enableSharing>true</enableSharing>
    <enableStreamingApi>true</enableStreamingApi>
</CustomObject>
EOF

# Favorite__c custom tab — Heart motif, makes the object navigable from the app menu
cat << 'EOF' > force-app/main/default/tabs/Favorite__c.tab-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomTab xmlns="http://soap.sforce.com/2006/04/metadata">
    <customObject>true</customObject>
    <motif>Custom19: Heart</motif>
</CustomTab>
EOF

# Grant tab visibility for the new Favorite tab
sed -i '/<\/Profile>/i \    <tabVisibilities>\n        <tab>Favorite__c</tab>\n        <visibility>DefaultOn</visibility>\n    </tabVisibilities>' force-app/main/default/profiles/Admin.profile-meta.xml
```

## Create a Lookup Relationship

Next, create two custom relationship fields on the Favorite object. First, create a lookup relationship that lists the users who select Favorite for a property: Object Manager | Favorite → Fields & Relationships → New → Lookup Relationship → Related To: **Contact** → Field Name `Contact` → Next, Next, Save.

```bash
# Contact__c Lookup field on Favorite__c — links to Contact, SetNull on delete
cat << 'EOF' > force-app/main/default/objects/Favorite__c/fields/Contact__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Contact__c</fullName>
    <label>Contact</label>
    <type>Lookup</type>
    <referenceTo>Contact</referenceTo>
    <relationshipName>Favorites1</relationshipName>
    <relationshipLabel>Favorites</relationshipLabel>
    <deleteConstraint>SetNull</deleteConstraint>
    <required>false</required>
    <trackTrending>false</trackTrending>
</CustomField>
EOF

# Provision Field-Level Security (FLS) for the Lookup field
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Favorite__c.Contact__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

> Deployed as `Favorites1`, not `Favorites` — Salesforce auto-suffixed it because the plain name was already taken elsewhere. Confirmed against the live org rather than guessed.

## Create a Master-Detail Relationship

Now, create a second relationship field. You want a master-detail relationship where Property is the master and Favorite is the detail: Object Manager | Favorite → Fields & Relationships → New → Master-Detail Relationship → Related To: **Property** → Field Name `Property` → Next, Next, Save.

```bash
# Property__c Master-Detail field on Favorite__c — links to Property__c, no fieldPermissions block (Master-Detail inherits security from the parent)
cat << 'EOF' > force-app/main/default/objects/Favorite__c/fields/Property__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Property__c</fullName>
    <label>Property</label>
    <type>MasterDetail</type>
    <referenceTo>Property__c</referenceTo>
    <relationshipName>Favorites1</relationshipName>
    <relationshipLabel>Favorites</relationshipLabel>
    <relationshipOrder>0</relationshipOrder>
    <reparentableMasterDetail>false</reparentableMasterDetail>
    <writeRequiresMasterRead>false</writeRequiresMasterRead>
    <trackTrending>false</trackTrending>
</CustomField>
EOF
```

Deploy everything for Favorite in one atomic push, then verify:

```bash
mkdir -p docs/trails/developer_beginner/badges/04_data_modeling/logs

# Deploy Favorite__c object, tab, fields, and profile FLS/tab-visibility grants atomically
sf project deploy start \
  -d force-app/main/default/objects/Favorite__c \
  -d force-app/main/default/tabs \
  -d force-app/main/default/profiles \
  -o trailhead-playground \
  --json | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_2_GUIDED_DEPLOY_AUDIT.json

# Verify Favorite__c field data types deployed correctly via Tooling API
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Favorite__c'" \
  --json | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_2_GUIDED_VERIFICATION_AUDIT.json
```

Now, if you look at a Property record, you'll see Favorites listed in the Related tab.

## Add a Favorite Property

Next, take a look at how to view favorite properties.

1. From the App Launcher, find and select **Sales**.
2. Click the **Properties** tab in the navigation bar. If you don't see it, look under the **More** dropdown.
3. Click the name of a Property record.
4. Click **Related**. You'll see Favorites (0) in the Related tab.
5. Click **New**.
6. Enter a name for Favorite Name, then click **Save**.

Great job! Our Favorite object is all set up.

## Resources

- Salesforce Help: Object Relationships Overview
- Salesforce Help: Considerations for Object Relationships

---

## Hands-On Challenge

The challenge applies the same lookup + master-detail pattern from above to the `Offer__c` object built in Unit 1, linking it to `Property__c` (Master-Detail) and `Contact` (Lookup).

```bash
# Property__c Master-Detail field on Offer__c — links to Property__c, Offers relationship name, no fieldPermissions block
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Property__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Property__c</fullName>
    <label>Property</label>
    <type>MasterDetail</type>
    <referenceTo>Property__c</referenceTo>
    <relationshipName>Offers</relationshipName>
    <relationshipLabel>Offers</relationshipLabel>
    <reparentableMasterDetail>false</reparentableMasterDetail>
    <writeRequiresMasterRead>false</writeRequiresMasterRead>
</CustomField>
EOF

# Contact__c Lookup field on Offer__c — links to Contact, SetNull on delete, Offers relationship name
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Contact__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Contact__c</fullName>
    <label>Contact</label>
    <type>Lookup</type>
    <referenceTo>Contact</referenceTo>
    <relationshipName>Offers</relationshipName>
    <relationshipLabel>Offers</relationshipLabel>
    <deleteConstraint>SetNull</deleteConstraint>
    <required>false</required>
</CustomField>
EOF

# Provision Field-Level Security (FLS) for the Lookup field
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Contact__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

```bash
mkdir -p docs/trails/developer_beginner/badges/04_data_modeling/logs

# Deploy Offer__c relationship fields and profile FLS grant atomically
sf project deploy start \
  -d force-app/main/default/objects/Offer__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground \
  --json | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_2_CHALLENGE_DEPLOY_AUDIT.json

# Verify Offer__c field data types deployed correctly via Tooling API
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'" \
  --json | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_2_CHALLENGE_VERIFICATION_AUDIT_SCHEMA.json

# Verify Admin profile FieldPermissions on Offer__c.Contact__c; Master-Detail Property__c has no row by design
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE SobjectType='Offer__c'" \
  --json | tee docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_2_CHALLENGE_VERIFICATION_AUDIT_FIELDPERMISSIONS.json
```
