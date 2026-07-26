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

DreamHouse wants a way to track users who mark particular properties as favorites on their website. To start, create a custom object called Favorite and add a field to the object.

1. Click the **Object Manager** tab.
2. Click **Create | Custom Object** in the top-right corner.
3. For Label, enter `Favorite`.
4. For Plural Label, enter `Favorites`.
5. Check the box for **Launch New Custom Tab Wizard** after saving this custom object.
6. Leave the rest of the values as default and click **Save**.
7. On the New Custom Object Tab page, click the **Tab Style** field and select a style you like.
8. Click **Next**, **Next**, and **Save**.

```bash
# Favorite__c custom object — Text name field, ControlledByParent sharing (required for the Master-Detail detail side)
cat << 'EOF' > force-app/main/default/objects/Favorite__c/Favorite__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Favorite</label>                          <!-- "Label" field from the New Custom Object form -->
    <pluralLabel>Favorites</pluralLabel>              <!-- "Plural Label" field -->
    <nameField>
        <label>Favorite Name</label>                  <!-- Name shown on every Favorite record -->
        <type>Text</type>                             <!-- Plain text name (Trailhead left this as the default) -->
    </nameField>
    <sharingModel>ControlledByParent</sharingModel>          <!-- Who can see a Favorite record: same access as its parent Property, once the Master-Detail field below is added -->
    <externalSharingModel>ControlledByParent</externalSharingModel>
    <deploymentStatus>Deployed</deploymentStatus>     <!-- Object is live, not "In Development" -->
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
    <motif>Custom19: Heart</motif>   <!-- The "Tab Style" icon/color you'd pick in the wizard -->
</CustomTab>
EOF

# Grant tab visibility for the new Favorite tab
sed -i '/<\/Profile>/i \    <tabVisibilities>\n        <tab>Favorite__c</tab>\n        <visibility>DefaultOn</visibility>\n    </tabVisibilities>' force-app/main/default/profiles/Admin.profile-meta.xml
```

## Create a Lookup Relationship

Next, create two custom relationship fields on the Favorite object. First, create a lookup relationship that lists the users who select Favorite for a property.

1. From Setup, go to **Object Manager | Favorite**.
2. On the sidebar, click **Fields & Relationships**.
3. Click **New**.
4. Choose **Lookup Relationship** and click **Next**.
5. For Related To, choose **Contact**. For the purposes of DreamHouse, contacts represent potential home buyers.
6. Click **Next**.
7. For Field Name, enter `Contact`, then click **Next**.
8. Click **Next**, **Next**, and **Save**.

```bash
# Contact__c Lookup field on Favorite__c — links to Contact, SetNull on delete; relationshipName deploys as Favorites1 (Salesforce auto-suffixed it, plain "Favorites" was already taken)
cat << 'EOF' > force-app/main/default/objects/Favorite__c/fields/Contact__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Contact__c</fullName>                    <!-- "Field Name" you typed in the wizard -->
    <label>Contact</label>                              <!-- Field Label shown on the page -->
    <type>Lookup</type>                                 <!-- "Lookup Relationship" field type -->
    <referenceTo>Contact</referenceTo>                  <!-- "Related To" — which object this looks up to -->
    <relationshipName>Favorites1</relationshipName>     <!-- Deploys as Favorites1, not Favorites — Salesforce auto-suffixed it because the plain name "Favorites" was already taken elsewhere in the org -->
    <relationshipLabel>Favorites</relationshipLabel>    <!-- What shows on the Related tab of a Contact record -->
    <deleteConstraint>SetNull</deleteConstraint>        <!-- If the Contact is deleted, clear this field instead of blocking the delete or cascading it -->
    <required>false</required>                          <!-- Not a required field, so it needs its own visibility grant below -->
    <trackTrending>false</trackTrending>
</CustomField>
EOF

# Provision Field-Level Security (FLS) so the field isn't invisible by default — required because Contact__c isn't a required field (Rule above)
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Favorite__c.Contact__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

## Create a Master-Detail Relationship

Now, create a second relationship field. You want a master-detail relationship where Property is the master and Favorite is the detail.

1. On the Object Manager page for the custom object, click **Fields & Relationships**.
2. Click **New**.
3. Select **Master-Detail Relationship** and click **Next**.
4. For Related To, choose **Property**.
5. Click **Next**.
6. For Field Name, enter `Property` and click **Next**.
7. Click **Next**, **Next**, and **Save**.

```bash
# Property__c Master-Detail field on Favorite__c — links to Property__c, no fieldPermissions block (Master-Detail inherits security from the parent)
cat << 'EOF' > force-app/main/default/objects/Favorite__c/fields/Property__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Property__c</fullName>                    <!-- "Field Name" you typed in the wizard -->
    <label>Property</label>                              <!-- Field Label shown on the page -->
    <type>MasterDetail</type>                            <!-- "Master-Detail Relationship" field type -->
    <referenceTo>Property__c</referenceTo>               <!-- "Related To" — Property is the master, Favorite is the detail -->
    <relationshipName>Favorites1</relationshipName>      <!-- Deploys as Favorites1, same auto-suffix as the Contact lookup above -->
    <relationshipLabel>Favorites</relationshipLabel>     <!-- What shows on the Related tab of a Property record -->
    <relationshipOrder>0</relationshipOrder>
    <reparentableMasterDetail>false</reparentableMasterDetail>
    <writeRequiresMasterRead>false</writeRequiresMasterRead>
    <trackTrending>false</trackTrending>
</CustomField>
EOF

# No fieldPermissions block for this field: Master-Detail fields always inherit security from their parent object, and the Metadata API rejects an explicit fieldPermissions entry here
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

The challenge applies the same lookup + master-detail pattern from above to the `Offer__c` object built in Unit 1:

- Master-Detail relationship to `Property__c`
- Lookup relationship to `Contact`

```bash
# Property__c Master-Detail field on Offer__c — links to Property__c, Offers relationship name, no fieldPermissions block
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Property__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Property__c</fullName>                    <!-- "Field Name" you'd type in the wizard -->
    <label>Property</label>                              <!-- Field Label shown on the page -->
    <type>MasterDetail</type>                            <!-- "Master-Detail Relationship" field type -->
    <referenceTo>Property__c</referenceTo>               <!-- "Related To" — Property is the master, Offer is the detail -->
    <relationshipName>Offers</relationshipName>          <!-- What shows on the Related tab of a Property record -->
    <relationshipLabel>Offers</relationshipLabel>
    <reparentableMasterDetail>false</reparentableMasterDetail>
    <writeRequiresMasterRead>false</writeRequiresMasterRead>
</CustomField>
EOF

# No fieldPermissions block for Property__c: Master-Detail fields always inherit security from their parent object

# Contact__c Lookup field on Offer__c — links to Contact, SetNull on delete, Offers relationship name
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Contact__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Contact__c</fullName>                    <!-- "Field Name" you'd type in the wizard -->
    <label>Contact</label>                              <!-- Field Label shown on the page -->
    <type>Lookup</type>                                 <!-- "Lookup Relationship" field type -->
    <referenceTo>Contact</referenceTo>                  <!-- "Related To" — which object this looks up to -->
    <relationshipName>Offers</relationshipName>         <!-- What shows on the Related tab of a Contact record -->
    <relationshipLabel>Offers</relationshipLabel>
    <deleteConstraint>SetNull</deleteConstraint>        <!-- If the Contact is deleted, clear this field instead of blocking the delete or cascading it -->
    <required>false</required>                          <!-- Not a required field, so it needs its own visibility grant below -->
</CustomField>
EOF

# Provision Field-Level Security (FLS) so the field isn't invisible by default — required because Contact__c isn't a required field
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
