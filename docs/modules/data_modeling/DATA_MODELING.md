# Trailhead Module: Data Modeling

**Trail:** Developer Beginner  
**Module:** Data Modeling  
**Date:** July 18, 2026

---

## Unit 1: Optimize Customer Data with Standard and Custom Objects

### Challenge Requirements

When a homebuyer makes an offer to buy a property, the brokers at DreamHouse Realty need to track the details in Salesforce. Create a custom object they can use to record the offer amount and target close date for the sale. Use auto numbering to generate the name of each offer record.

1. **Create a Custom Object:**
   - **Label:** Offer
   - **Object Name:** `Offer` (`Offer__c`)
   - **Record Name:** Offer Name
   - **Data Type:** Auto Number
   - **Display Format:** `OF-{0000}`
   - **Starting Number:** 1

2. **Create a Custom Currency Field:**
   - **Data Type:** Currency
   - **Field Label:** Offer Amount
   - **Field Name:** `Offer_Amount` (`Offer_Amount__c`)

3. **Create a Custom Date Field:**
   - **Data Type:** Date
   - **Field Label:** Target Close Date
   - **Field Name:** `Target_Close_Date` (`Target_Close_Date__c`)

---

### Solution Source Metadata & Commands

#### 1. Custom Object (`force-app/main/default/objects/Offer__c/Offer__c.object-meta.xml`)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Offer</label>
    <pluralLabel>Offers</pluralLabel>
    <nameField>
        <displayFormat>OF-{0000}</displayFormat>
        <label>Offer Name</label>
        <type>AutoNumber</type>
    </nameField>
    <sharingModel>ReadWrite</sharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
</CustomObject>
```

#### 2. Currency Field (`force-app/main/default/objects/Offer__c/fields/Offer_Amount__c.field-meta.xml`)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Offer_Amount__c</fullName>
    <label>Offer Amount</label>
    <type>Currency</type>
    <precision>16</precision>
    <scale>2</scale>
</CustomField>
```

#### 3. Date Field (`force-app/main/default/objects/Offer__c/fields/Target_Close_Date__c.field-meta.xml`)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Target_Close_Date__c</fullName>
    <label>Target Close Date</label>
    <type>Date</type>
</CustomField>
```

#### 4. Field-Level Security Profile Grant (`force-app/main/default/profiles/Admin.profile-meta.xml`)

```xml
<fieldPermissions>
    <editable>true</editable>
    <field>Offer__c.Offer_Amount__c</field>
    <readable>true</readable>
</fieldPermissions>
<fieldPermissions>
    <editable>true</editable>
    <field>Offer__c.Target_Close_Date__c</field>
    <readable>true</readable>
</fieldPermissions>
```

#### 5. Deployment Command

```bash
sf project deploy start -d force-app/main/default/objects/Offer__c -d force-app/main/default/profiles -o trailhead-playground
```
