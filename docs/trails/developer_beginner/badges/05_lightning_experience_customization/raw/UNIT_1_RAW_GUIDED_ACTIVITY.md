badge5unit1

https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_custom_objects?trail_id=force_com_dev_beginner

Set Up Your Org

Learning Objectives

After completing this unit, you’ll be able to:

    Describe the business value of custom objects and fields.
    Create and edit custom objects and fields.
    Create a custom tab for a custom object.

Meet Ursa Major Solar

Ursa Major Solar is a Southwest-based supplier of solar components and systems. It’s a small company with around 200 employees, but it’s growing fast, and it’s looking to Salesforce to help the company blossom. Maria Jimenez, its admin, is in charge of configuring and customizing Salesforce to meet Ursa Major’s needs.

Maria

Ursa Major Solar is expanding its energy consultation business and offering personalized energy assessments to its customers. But Ursa Major Solar doesn’t have a place to track and manage the results. Using custom objects and fields, Maria’s going to build an energy consulting app. By creating a custom object called Energy Audit, and creating a few custom fields for it, Ursa Major Solar can track information on its customers’ energy usage and recommend which type of solar panel installation is a good fit.

Throughout this module, we’ll follow in Maria’s footsteps as she gets Salesforce into shape for the Ursa Major Solar team to use. You'll create a custom object, custom fields, a custom app and more, and you can do it all in your Trailhead Playground. No special app installation is required.

Maria's first task is to create the Energy Audit object. It will be used in later units, so let’s get started!
Create a Custom Object

Salesforce provides standard objects and fields for common business record types, such as accounts, leads, and contacts. But every organization is unique and needs a way to tailor how data is stored. Ursa Major Solar is no different. Custom objects and fields give them a way to manage and store data to best fit their needs.

All right! Let’s create the custom Energy Audit object.

    From the Object Manager in Setup, click Create | Custom Object.
    Enter Energy Audit

as the label, and Energy Audits

    as the plural label.

Energy Audit Custom Object

    Select the box to indicate that it starts with a vowel sound.
    In the Search Status section, select Allow Search.
    Select Launch New Custom Tab Wizard after saving this custom object. You’ll see why in a minute.
    Leave the rest of the values as they are, and click Save. Easy peasy, right?

Create a Custom Object Tab

Maria’s created the custom object, but she needs a way to make it easily accessible to her users. Creating a custom tab for a custom object is a great way to do that.
Note

This is a key step in configuring a custom object. Without a custom tab, you can’t add a custom object to an app.

Let’s define a new tab to access the data stored in the custom Energy Audit object. This way, the Ursa Major Solar consulting team can easily find and open the object.

Because you selected Launch New Custom Tab Wizard after saving this custom object, you’re right where you need to be, and the Energy Audit object is already selected.

    Click the Tab Style lookup icon, and select the Sun color scheme and icon for the custom tab.

Custom Tab Creation Screen

    Click Next, then Next again.
    Choose the custom apps that you want the new custom tab to be available in. For now, let’s make the tab visible for just the Sales users. Deselect Include Tab, and select only Sales (standard__LightningSales).
    Click Save.

Note

What’s a custom app, you say? It’s basically a set of fields, objects, permissions, and other functions assembled to support a business process. We find out more about that—and creating one—in the next unit.

Now you see the details of the Energy Audit custom object.

Energy Audit object details
Create Custom Fields

Maria’s not done yet. The Energy Audit object needs some custom fields so the Ursa Major energy consultants can enter information about the audit. Besides needing the Account the audit is associated with and how much energy the customer uses, the consultants also recommend where to install the solar panels. Let’s start there.

The first thing to consider when creating a custom field is figuring out what type of field you need. Let’s create a picklist field so the consultants can choose from a list of solar panel installation options.

    Click Fields & Relationships, then click New.
    Choose Picklist as the field type and click Next.
    Give it a label: Type of Installation

    .
    Select Enter values, with each value separated by a new line.
    Enter the picklist values, making sure to enter each one on a new line.

        Rooftop
        Carport
        Ground mounted

    Select Use first value as default value, and then click Next.

Custom Field

    Leave the field-level security settings as they are, and click Next.
    Leave Energy Audit Layout selected, and click Save.

That one field isn’t quite enough, though. The energy consultants also need to capture how much the customer is paying each month and what their monthly energy usage is. They also need a place to write up their audit evaluation. Let’s create a few more custom fields to let them do that. Unless indicated otherwise in the Parameters column, leave each field setting as-is.

Field Type

Label

Parameters

Lookup Relationship

Account

Related To: Account

Always require a value in this field.

Currency

Average Annual Electric Cost

Length: 16
Decimal Places: 2 Help Text: Annual cost per square foot.

Always require a value in this field.

Number

Annual Energy Usage (kWh)

Help Text: Usage per square foot.

Always require a value in this field.

Text Area (Long)

Audit Notes

# Visible Lines: 5

Now the custom object is really taking shape. Nice work! And don’t forget that it’s easy to modify an existing custom field to fit your needs at any time. Let’s say you want to sort your data even more granularly. Or you want to change a text-entry field to a picklist to clean up data for reports. You can always come back and get things just right for your business needs.
Create Energy Audit Records

An object is nothing without records to fill it out. Prior to implementing Salesforce, Ursa Major Solar was tracking audits in a spreadsheet. Oh, the horror! Part of Maria’s job as the admin is to enter those audit records into Salesforce. And, we use them later in the module. Let’s get to it.

    From the App Launcher App Launcher icon, find and select Energy Audits.
    Click New.
    Add a record with these parameters.

        Energy Audit Name: Burlington evaluation

Type of Installation: Rooftop
Account: Burlington Textiles Corp of America
Hint: Type Burlington
into the Account field to see all accounts that match what you entered.
Average Annual Electric Cost: 1.86
Annual Energy Usage (kWh): 23

        These numbers seem small, but they’re cost and usage per square foot. For buildings with many thousands of square feet, that adds up to a lot of energy use and a big bill!

    Click Save & New.
    Let’s add a few more records to flesh things out.

Energy Audit Name

Type of Installation

Account

Average Annual Electric Cost

Annual Energy Usage (kWh)

UA Spring assessment

Carport

University of Arizona

2.19

30

GenePoint 5-year review

Rooftop

GenePoint

1.56

21

sForce Los Altos Hills campus

Ground mounted

sForce

1.77

25

Nice job! We’ll put those into use shortly.
Enable Feed Tracking

Maria wants her energy consultants to be able to follow changes to the energy audit records and see feed updates when those audit records are changed. To accomplish this, she enables Feed Tracking on the Energy Audit object. Turning on Feed Tracking enables Chatter feeds for an object.

    From Setup, enter Feed Tracking

    in the Quick Find box, then select Feed Tracking.
    Select Energy Audit from the object list.
    Select Enable Feed Tracking.
    Select all of the fields except Owner and All Related Objects.
    Click Save.

Resources

    Salesforce Help: Custom Field Attributes
    Salesforce Help: Custom Field Limits
    Salesforce Help: Feed Tracking

Hands-on Challenge
+500 points
Get Ready

You’ll be completing this unit in your own hands-on org. Click Launch to get started, or click the name of your org to choose a different one.
Your Challenge
Create a Custom Object and Custom Fields

Ursa Major Solar needs a custom object and custom fields to track the energy evaluations they do for their prospective customers.

If you haven’t already done so, complete the steps in this unit to create the Energy Audit custom object in your org. We’ll be building on it as we go through this module. If you followed along in the unit and already created the object, fields, and records, you can go ahead and check the challenge.

    Create the Energy Audit custom object:
        Label: Energy Audit
        Plural Label: Energy Audits
        Object Name: Energy_Audit
        Search Status: Allow Search
    Create the Energy Audit custom tab

    Create five custom fields on the Energy Audit object:
        Field Type: Picklist
            Label: Type of Installation
            Field Name: Type_of_Installation
            Select Enter values, with each value separated by a new line
            Picklist Values: Rooftop, Carport, Ground Mounted
        Field Type: Lookup Relationship
            Label: Account
            Field Name: Account
            Related To: Account
        Field Type: Currency
            Label: Average Annual Electric Cost
            Field Name: Average_Annual_Electric_Cost
            Length: 16
            Decimal Places: 2
            Help Text: Annual cost per square foot
        Field Type: Number
            Label: Annual Energy Usage (kWh)
            Field Name: Annual_Energy_Usage_kWh
            Help Text: Usage per square foot
        Field Type: Text Area (Long)
            Label: Audit Notes
            Field Name: Audit_Notes
            # Visible Lines:5
    Feed Tracking enabled for the Energy Audit object on these fields: Account, Audit Notes, Energy Audit Name, Type of Installation, Annual Energy Usage (kWh), and Average Annual Electric Cost
