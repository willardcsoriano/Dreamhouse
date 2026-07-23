badge5unit5

https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_page_layouts?trail_id=force_com_dev_beginner

Customize Record Page Components and Fields

Learning Objectives

After completing this unit, you’ll be able to:

    Create, customize, and manage Lightning pages.
    Use the Lightning App Builder.
    Assign a Lightning page to a profile.

Note
Accessibility

This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click the link below:

Open Trailhead screen reader instructions.
Record Pages

What you see when you log in to Salesforce for the first time is just the start. You can customize and personalize many things on object record pages using a combination of the Lightning App Builder and page layouts.

Most of the pages you see in Lightning Experience, such as the Home page and record pages, are Lightning pages. Lightning pages are a collection of components arranged in regions on the page. You can customize the structure of the page, the position of its components, and the record detail fields it displays with the Lightning App Builder. (Learn more in the Lightning App Builder module right here on Trailhead)

Other page contents, such as the buttons, links, actions, and related lists that appear on the page, are controlled with a different tool called the page layout editor.

We work with both the Lightning App Builder and the page layout editor in this unit to review how to customize your Lightning record pages.

The Lightning App Builder lets you:

    Control which components appear on Lightning pages
    Create custom Lightning pages for different apps and users
    Control which fields appear on record pages

The page layout editor lets you:

    Control which lists of related records and custom links users see
    Control which standard and custom buttons appear on records and related lists
    Control which quick actions appear on the page

You’re probably thinking, "Buttons, lists, record details? What is all this stuff?" Let’s tour the record page by looking at an example contact record, and then we’ll dive in and customize a page.

These are the parts of a record page that you can customize to create a personalized view for different teams and processes in your org.

    In the previous unit, you learned about record highlights (1) and how to customize the fields it shows using compact layouts. The record highlights area also contains a set of buttons and actions (2), which you’ll learn how to customize in a later unit.
    The Related tab (3) contains related lists, which are lists of other records that are associated with the record you’re viewing. For example, an account can have related products, contacts, opportunities, and other custom records.
    The Details tab (4) shows information about a record. By default, fields and links appear here. For example, a contact record detail page shows the name, address, owner, account, and other fields that are used to store information about the contact and other related records.

Related List Page

We’ve mentioned buttons, links, and actions. We’ll go over those in more detail and how to modify them on Lightning pages in later units. In this unit, we focus on customizing the page structure, components, record detail fields, and related lists.
Create a Custom Lightning Record Page

Maria wants to create an Energy Audit record page just for her sales team so they can have the necessary field and related list information at their fingertips when they view the Energy Audit records.

When the Energy Audit custom object was created, a system default Energy Audit record page was created too. Right now, everyone in the org who views an Energy Audit record sees the information from that default layout. Maria is going to create a customized record page just for the sales people.

Let’s follow along.

    From the App Launcher , find and select Energy Consultations, then click the Energy Audits tab.
    Open the All list view.
    Select Burlington evaluation.
    From the Setup menu Setup, select Edit Page.
    The page opens in the Lightning App Builder.
    In the page properties, change the Label to Energy Audit Record Page for Sales

.
Change the API Name to Energy_Audit_Record_Page_for_Sales

    .
    Click the Details tab on the canvas, then click the Record Detail component (where the fields are).
    There are all the fields for the Energy Audit object. But they’re all in one non-customizable block. With the click of one button, we can change that.
    In the properties pane, click Upgrade Now to start the Dynamic Forms migration wizard.

Upgrade to Dynamic Forms message with Upgrade Now button

With Dynamic Forms, you can migrate the fields and sections from your existing record pages into individual components. Then you can configure them just like the rest of the components on the page—adding more, removing some, or moving them around–giving your users only the fields and sections that they need.

    Step through the wizard, select Energy Audit Layout, then click Finish.
    The right-hand column of the Details section is almost empty, and the fields could be in a better order. Let’s fix that.
    Click the Audit Notes field and drag it to the right column, above Owner.
    Drag the Type of Installation field above Audit Notes.
    If it's not already there, move Account below Energy Audit Name.
    Click Save, then Not Yet.
    Activating the page makes it available to your users. This page isn’t quite ready for users, however. Maria wants to add a related list.

Customize Related Lists

Because Energy Audit is a custom object, it doesn’t have any related lists…yet. Let’s add one. We can do that in the page layout editor.

    Click Back Back in the App Builder header.
    From the Setup menu Setup, select Setup.
    Setup opens in a new browser tab.
    Click Object Manager, then find and click Energy Audit in the list of objects.
    Click Page Layouts, then Energy Audit Layout.
    Scroll down to the Related Lists section.
    In the palette at the top of the page, click Related Lists, and drag the Files element down to the Related Lists section.
    With the Files related list, Ursa Major Solar sales reps can add files to a record and see a list of files associated with the record.
    Click Quick Save, then click Yes.

Activate the Page

Maria’s done with customizing the page for now, but no one can see it. It’s time to activate the Lightning page and make it live for her Sales users.

    From Setup, click the Home tab.
    Enter App Builder

    in the Quick Find box, then select Lightning App Builder.
    Click Edit next to the Energy Audit Record Page for Sales page.
    Click Activation.

The Activation: energy Audit Record Page for Sales has three options: Org Default, App Default, and App, Record, Type and Profile.

There are four options for activation.

    Make the page the org default for the object.
    Make the page the default object record page for specific Lightning apps.
    Assign the page to a combination of Lightning apps, record types, and profiles.
    Assign the page to a form factor, such as a desktop or phone.

Maria wants Ursa Major Solar’s salespeople to see this new record page. She’s going to assign it to her sales team’s user profile so that when they view Energy Audit records, they’ll see the revised view of the fields and the new related list. She’s also going to make sure it’s assigned to both the desktop and phone form factors, so her users can view it when working on their desktops and when on the road from their mobile devices. Let’s get started.

    Click the App, Record Type, and Profile tab.
    Click Assign to Apps, Record Types, and Profiles.
    Step through the wizard and assign the page to the Energy Consultations app, the Desktop and phone form factor, the Master record type, and both the Custom: Sales Profile and the System Administrator profile.

Normally, Maria would select only Custom: Sales Profile, but since you’re logged in as a System Administrator, we select that too so that you can see how the new page layout looks.

    Review the page assignments.
    The New Page column is populated with the name of the page we’re activating: Energy Audit Record Page for Sales.
    Click Save.

Maria’s customized record page is now live. Let’s go check it out.
View the Customized Page

    Click Back Back in the App Builder header.
    From the App Launcher App Launcher, find and select Energy Audits, then open an audit record.
    You might have to refresh the page to see the changes.
    Look at the Details tab. It’s more condensed and efficient now.

Before

Details tab with original organization of fields
After

Details tab with new organization of fields

    Click the Related tab.

Now you can see the Files related list there, just waiting for someone to upload something.

Great job! Now that you’re more familiar with Lightning page customization, you can start creating pages that give your users just what they need. By arranging components and fields in logical sections, you can make it even easier for your users to store and manage the data that’s important to your business.
Resources

    Salesforce Help: Create and Configure Lightning Experience Record Pages
    Salesforce Help: Activate Lightning Experience Record Pages
    Salesforce Help: Lightning App Builder Considerations

Hands-on Challenge
+500 points
Get Ready

You’ll be completing this unit in your own hands-on org. Click Launch to get started, or click the name of your org to choose a different one.
Your Challenge
Customize a contact record page
Give users a customized set of fields on their contact record pages.

    Select Edit Page from a contact record
    Upgrade the page to use Dynamic Forms
    Use the Contact Layout as the source for the fields
    Remove these fields from the page:
        Fax
        Other Phone
        Home Phone
    Remove the Notes & Attachments related list from the Contact Layout page layout and replace it with the Files related list.
    Save and activate the page as the org default, and make it available to both desktop and phone users
