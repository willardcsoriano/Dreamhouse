badge5unit1

https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_custom_objects?trail_id=force_com_dev_beginner

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
    Create the Energy Audit custom tage

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
