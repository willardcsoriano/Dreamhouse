badge5unit4

https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_compact_layouts?trail_id=force_com_dev_beginner

Customize Record Highlights with Compact Layouts
Learning Objectives

After completing this unit, you’ll be able to:

    Describe how compact layouts help your users.
    Create a custom compact layout.

What Do Compact Layouts Do?

Compact layouts control which fields your users see in the highlights panel at the top of a record. They also control the fields that appear in the expanded lookup card you see when you hover over a link in record details, and in the details section when you expand an activity in the activity timeline.

Compact layouts help make your team more productive by presenting them with the key record information so they can easily manage their work. For example, show phone numbers and regions on an account. Or, show stages, amounts, and ownership fields on an opportunity. With compact layouts, you can highlight whatever your users need to see at a glance when they look at a record.

As with page layouts, there are separate compact layouts for each object. Here’s an example of an opportunity record page. The first several fields you assign to an object’s compact layout appear in the object’s record highlights panel and in the expanded lookup card you see when you hover over a link in record details. The field you put first displays at the top in bold.

In this case, the highlights panel reflects the fields on the opportunity compact layout, and the expanded lookup card reflects the fields from the account compact layout.

Compact layouts in Lightning Experience
Note

Compact layouts also control how records display in the Salesforce mobile app. If your company uses the Salesforce mobile app, you can help your users see what they need on mobile screens, where space is limited and quick recognition of records is important.
Example

Here’s a sample compact layout edit page for the Account object. It shows the name of the layout and a list of fields to display.

Sample Compact Layout

Here’s a record page for the same account object in Lightning Experience. You can see the account’s name, phone number, type, industry, rating, and account owner at the top of the page.

Sample Layout

And here’s what that same account record looks like in the mobile app.

The newly created compact layout in the mobile app.
Create a Compact Layout

When you create a custom object, it’s automatically assigned to a system default compact layout, which has only one field on it: the object name. Maria wants to call attention to the most important fields on the object when her users view the audit records. Let’s make that happen by creating a custom compact layout for the Energy Audit custom object.

    First, find and open the compact layouts node in Setup for Energy Audit.

        From Setup, click Object Manager.
        Click Energy Audit to open the object and then click Compact Layouts.

    You can see that the System Default compact layout is assigned as the primary compact layout right now. We’re going to change that.
    Click New.
    Give the compact layout a label: Energy Audit Compact Layout

    .
    Add these fields to the compact layout, in this order:

        Energy Audit Name
        Account
        Annual Energy Usage (kWh)
        Average Annual Electric Cost
        Type of Installation

    Click Save.
    Now let’s set the compact layout that you created as the primary compact layout for the object. This step makes the compact layout the new default for the Energy Audit custom object.
    Click Compact Layout Assignment and then Edit Assignment.
    Select Energy Audit Compact Layout and click Save.

Great job! Now, when users view an Energy Audit record, they see the most important information where they need it most—at the top of the record page.

Energy audit record
Note

Changes to compact layouts can sometimes take time to appear. If refreshing the page doesn’t help, try changing your display density to a different setting to force the page to reload.
Resources

    Salesforce Help: Compact Layouts
    Salesforce Help: Notes on Compact Layouts
    Salesforce Help: Assign Compact Layouts to Record Types

Hands-on Challenge
+500 points
Get Ready

You’ll be completing this unit in your own hands-on org. Click Launch to get started, or click the name of your org to choose a different one.
Your Challenge
Create a Custom Opportunity Compact Layout
When the Ursa Major Solar salespeople are on site with a customer, there are a few key fields they need to see right at the top of an opportunity record when they access Salesforce. Create a compact layout that will help them do that.

    Create a compact layout for the Opportunity object:
        Label: New Oppty Compact Layout
        Name: New_Oppty_Compact_Layout
    Include these fields, in this order: Opportunity Name, Probability (%), Close Date, Stage, Amount, Opportunity Owner
    Make it the primary compact layout
