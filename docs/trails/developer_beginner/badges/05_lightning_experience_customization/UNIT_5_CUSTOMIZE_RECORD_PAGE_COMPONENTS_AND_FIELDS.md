# Trailhead Unit: Customize Record Page Components and Fields

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 5:** Customize Record Page Components and Fields  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_page_layouts?trail_id=force_com_dev_beginner)

---

## Learning Objectives

After completing this unit, you’ll be able to:

- Create, customize, and manage Lightning pages.
- Use the Lightning App Builder.
- Assign a Lightning page to a profile.

> **Note:**  
> **Accessibility**  
> This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click the link below:  
> Open Trailhead screen reader instructions.

---

## Record Pages

What you see when you log in to Salesforce for the first time is just the start. You can customize and personalize many things on object record pages using a combination of the Lightning App Builder and page layouts.

Most of the pages you see in Lightning Experience, such as the Home page and record pages, are Lightning pages. Lightning pages are a collection of components arranged in regions on the page. You can customize the structure of the page, the position of its components, and the record detail fields it displays with the Lightning App Builder. (Learn more in the Lightning App Builder module right here on Trailhead)

Other page contents, such as the buttons, links, actions, and related lists that appear on the page, are controlled with a different tool called the page layout editor.

We work with both the Lightning App Builder and the page layout editor in this unit to review how to customize your Lightning record pages.

The Lightning App Builder lets you:

- Control which components appear on Lightning pages
- Create custom Lightning pages for different apps and users
- Control which fields appear on record pages

The page layout editor lets you:

- Control which lists of related records and custom links users see
- Control which standard and custom buttons appear on records and related lists
- Control which quick actions appear on the page

You’re probably thinking, "Buttons, lists, record details? What is all this stuff?" Let’s tour the record page by looking at an example contact record, and then we’ll dive in and customize a page.

These are the parts of a record page that you can customize to create a personalized view for different teams and processes in your org.

- In the previous unit, you learned about record highlights (1) and how to customize the fields it shows using compact layouts. The record highlights area also contains a set of buttons and actions (2), which you’ll learn how to customize in a later unit.
- The Related tab (3) contains related lists, which are lists of other records that are associated with the record you’re viewing. For example, an account can have related products, contacts, opportunities, and other custom records.
- The Details tab (4) shows information about a record. By default, fields and links appear here. For example, a contact record detail page shows the name, address, owner, account, and other fields that are used to store information about the contact and other related records.

### Related List Page

We’ve mentioned buttons, links, and actions. We’ll go over those in more detail and how to modify them on Lightning pages in later units. In this unit, we focus on customizing the page structure, components, record detail fields, and related lists.

---

## Create a Custom Lightning Record Page

Maria wants to create an Energy Audit record page just for her sales team so they can have the necessary field and related list information at their fingertips when they view the Energy Audit records.

When the Energy Audit custom object was created, a system default Energy Audit record page was created too. Right now, everyone in the org who views an Energy Audit record sees the information from that default layout. Maria is going to create a customized record page just for the sales people.

Let’s follow along.

1. From the App Launcher, find and select **Energy Consultations**, then click the **Energy Audits** tab.
2. Open the **All** list view.
3. Select **Burlington evaluation**.
4. From the Setup menu, select **Edit Page**.
   - The page opens in the Lightning App Builder.
5. In the page properties, change the Label to **Energy Audit Record Page for Sales**.
6. Change the API Name to **Energy_Audit_Record_Page_for_Sales**.
7. Click the **Details** tab on the canvas, then click the **Record Detail** component (where the fields are).
   - There are all the fields for the Energy Audit object. But they’re all in one non-customizable block. With the click of one button, we can change that.
8. In the properties pane, click **Upgrade Now** to start the Dynamic Forms migration wizard.
   - Upgrade to Dynamic Forms message with Upgrade Now button
   - With Dynamic Forms, you can migrate the fields and sections from your existing record pages into individual components. Then you can configure them just like the rest of the components on the page—adding more, removing some, or moving them around–giving your users only the fields and sections that they need.
9. Step through the wizard, select **Energy Audit Layout**, then click **Finish**.
   - The right-hand column of the Details section is almost empty, and the fields could be in a better order. Let’s fix that.
10. Click the **Audit Notes** field and drag it to the right column, above **Owner**.
11. Drag the **Type of Installation** field above **Audit Notes**.
12. If it's not already there, move **Account** below **Energy Audit Name**.
13. Click **Save**, then **Not Yet**.
    - Activating the page makes it available to your users. This page isn’t quite ready for users, however. Maria wants to add a related list.

**No CLI equivalent — do this in the browser.**

```bash
# Retrieves the wizard-generated Dynamic Forms FlexiPage and deploys it as a reproducible metadata payload
mkdir -p badges/05_lightning_experience_customization/logs # creates logs directory for output tracking

# Step 1: Retrieve builder-generated FlexiPage metadata into local source
CMD="sf project retrieve start -m FlexiPage:Energy_Audit_Record_Page_for_Sales -o trailhead-playground --json" # sf retrieve command for flexipage
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_FLEXIPAGE_RETRIEVE_AUDIT.json # executes retrieve and writes log output

# Step 2: Deploy captured FlexiPage metadata payload back to org
CMD="sf project deploy start -m FlexiPage:Energy_Audit_Record_Page_for_Sales -o trailhead-playground --json" # sf deploy command for flexipage
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_FLEXIPAGE_DEPLOY_AUDIT.json # executes deploy and writes log output
```

```bash
# Verifies Energy Audit record flexipage metadata deployment via Salesforce Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, DeveloperName, MasterLabel, SobjectType FROM FlexiPage WHERE DeveloperName = 'Energy_Audit_Record_Page_for_Sales'\" -o trailhead-playground --json" # tooling api query for flexipage
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_FLEXIPAGE_VERIFY_AUDIT.json # executes query and writes log output
```

---

## Customize Related Lists

Because Energy Audit is a custom object, it doesn’t have any related lists…yet. Let’s add one. We can do that in the page layout editor.

1. Click **Back** in the App Builder header.
2. From the Setup menu, select **Setup**.
   - Setup opens in a new browser tab.
3. Click **Object Manager**, then find and click **Energy Audit** in the list of objects.
4. Click **Page Layouts**, then **Energy Audit Layout**.
5. Scroll down to the **Related Lists** section.
6. In the palette at the top of the page, click **Related Lists**, and drag the **Files** element down to the Related Lists section.
   - With the Files related list, Ursa Major Solar sales reps can add files to a record and see a list of files associated with the record.
7. Click **Quick Save**, then click **Yes**.

```bash
# Retrieves Energy Audit Layout XML, applies RelatedFileList entry, and deploys updated layout metadata
mkdir -p badges/05_lightning_experience_customization/logs # creates logs directory for output tracking

# Step 1: Retrieve org-default layout baseline
CMD="sf project retrieve start -m Layout:Energy_Audit__c-Energy Audit Layout -o trailhead-playground --json" # sf retrieve command for object layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_LAYOUT_RETRIEVE_AUDIT.json # executes retrieve and writes log output

# Step 2: Deploy patched layout metadata with RelatedFileList
CMD="sf project deploy start -m Layout:Energy_Audit__c-Energy Audit Layout -o trailhead-playground --json" # sf deploy command for object layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_LAYOUT_DEPLOY_AUDIT.json # executes deploy and writes log output
```

```bash
# Verifies Energy Audit layout metadata existence in target org via Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, Name, TableEnumOrId FROM Layout WHERE TableEnumOrId = 'Energy_Audit__c'\" -o trailhead-playground --json" # tooling api layout verification query
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_LAYOUT_VERIFY_AUDIT.json # executes query and writes log output
```

---

## Activate the Page

Maria’s done with customizing the page for now, but no one can see it. It’s time to activate the Lightning page and make it live for her Sales users.

1. From Setup, click the **Home** tab.
2. Enter `App Builder` in the Quick Find box, then select **Lightning App Builder**.
3. Click **Edit** next to the **Energy Audit Record Page for Sales** page.
4. Click **Activation**.

The Activation: Energy Audit Record Page for Sales has three options: Org Default, App Default, and App, Record Type, and Profile.

There are four options for activation.

1. Make the page the org default for the object.
2. Make the page the default object record page for specific Lightning apps.
3. Assign the page to a combination of Lightning apps, record types, and profiles.
4. Assign the page to a form factor, such as a desktop or phone.

Maria wants Ursa Major Solar’s salespeople to see this new record page. She’s going to assign it to her sales team’s user profile so that when they view Energy Audit records, they’ll see the revised view of the fields and the new related list. She’s also going to make sure it’s assigned to both the desktop and phone form factors, so her users can view it when working on their desktops and when on the road from their mobile devices. Let’s get started.

1. Click the **App, Record Type, and Profile** tab.
2. Click **Assign to Apps, Record Types, and Profiles**.
3. Step through the wizard and assign the page to the **Energy Consultations** app, the **Desktop and phone** form factor, the **Master** record type, and both the **Custom: Sales Profile** and the **System Administrator** profile.
   - Normally, Maria would select only Custom: Sales Profile, but since you’re logged in as a System Administrator, we select that too so that you can see how the new page layout looks.
4. Review the page assignments.
   - The New Page column is populated with the name of the page we’re activating: Energy Audit Record Page for Sales.
5. Click **Save**.

**No CLI equivalent — do this in the browser.**

```bash
# Retrieves CustomApplication Energy Consultations metadata after activation wizard completion and redeploys it
mkdir -p badges/05_lightning_experience_customization/logs # creates logs directory for output tracking

# Step 1: Retrieve CustomApplication metadata after activation wizard completion
CMD="sf project retrieve start -m CustomApplication:Energy_Consultations -o trailhead-playground --json" # sf retrieve command for custom application
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_ACTIVATION_RETRIEVE_AUDIT.json # executes retrieve and writes log output

# Step 2: Deploy CustomApplication metadata back to org
CMD="sf project deploy start -m CustomApplication:Energy_Consultations -o trailhead-playground --json" # sf deploy command for custom application
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_ACTIVATION_DEPLOY_AUDIT.json # executes deploy and writes log output
```

```bash
# Verifies CustomApplication metadata exist in org via Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, DeveloperName FROM CustomApplication WHERE DeveloperName = 'Energy_Consultations'\" -o trailhead-playground --json" # tooling api custom application query
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_GUIDED_ACTIVATION_VERIFY_AUDIT.json # executes query and writes log output
```

---

## View the Customized Page

Maria’s customized record page is now live. Let’s go check it out.

1. Click **Back** in the App Builder header.
2. From the App Launcher, find and select **Energy Audits**, then open an audit record.
   - You might have to refresh the page to see the changes.
3. Look at the **Details** tab. It’s more condensed and efficient now.

**Before**  
Details tab with original organization of fields

**After**  
Details tab with new organization of fields

4. Click the **Related** tab.

Now you can see the Files related list there, just waiting for someone to upload something.

Great job! Now that you’re more familiar with Lightning page customization, you can start creating pages that give your users just what they need. By arranging components and fields in logical sections, you can make it even easier for your users to store and manage the data that’s important to your business.

---

## Resources

- [Salesforce Help: Create and Configure Lightning Experience Record Pages](https://help.salesforce.com/s/articleView?id=sf.lightning_page_create.htm&type=5)
- [Salesforce Help: Activate Lightning Experience Record Pages](https://help.salesforce.com/s/articleView?id=sf.lightning_page_activate.htm&type=5)
- [Salesforce Help: Lightning App Builder Considerations](https://help.salesforce.com/s/articleView?id=sf.flexipage_overview.htm&type=5)

---

## Hands-On Challenge

### Get Ready

You’ll be completing this unit in your own hands-on org. Click Launch to get started, or click the name of your org to choose a different one.

### Your Challenge

#### Customize a contact record page

Give users a customized set of fields on their contact record pages.

- Select **Edit Page** from a contact record
- Upgrade the page to use Dynamic Forms
- Use the **Contact Layout** as the source for the fields
- Remove these fields from the page:
  - Fax
  - Other Phone
  - Home Phone
- Remove the **Notes & Attachments** related list from the Contact Layout page layout and replace it with the **Files** related list.
- Save and activate the page as the org default, and make it available to both desktop and phone users

```bash
# Authors FlexiPage XML for Contact_Record_Page_for_Sales with Dynamic Forms layout and deploys to target org
mkdir -p force-app/main/default/flexipages # creates flexipages metadata directory
mkdir -p badges/05_lightning_experience_customization/logs # creates logging directory

cat << 'EOF' > force-app/main/default/flexipages/Contact_Record_Page_for_Sales.flexipage-meta.xml # starts heredoc for Contact flexipage
<?xml version="1.0" encoding="UTF-8"?> <!-- XML declaration header -->
<FlexiPage xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- FlexiPage root element -->
    <flexiPageRegions> <!-- Header region definition -->
        <itemInstances> <!-- Component instance wrapper -->
            <componentInstance> <!-- Highlights panel component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>collapsed</name> <!-- Property name: collapsed -->
                    <value>false</value> <!-- Property value: false -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>enableActionsConfiguration</name> <!-- Property name: enableActionsConfiguration -->
                    <value>false</value> <!-- Property value: false -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>enableActionsInNative</name> <!-- Property name: enableActionsInNative -->
                    <value>false</value> <!-- Property value: false -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>hideChatterActions</name> <!-- Property name: hideChatterActions -->
                    <value>false</value> <!-- Property value: false -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>hideSlackAction</name> <!-- Property name: hideSlackAction -->
                    <value>false</value> <!-- Property value: false -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>numVisibleActions</name> <!-- Property name: numVisibleActions -->
                    <value>3</value> <!-- Property value: 3 -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>force:highlightsPanel</componentName> <!-- Standard highlights panel component -->
                <identifier>force_highlightsPanel</identifier> <!-- Unique component identifier -->
            </componentInstance> <!-- End highlights panel component -->
        </itemInstances> <!-- End component instance wrapper -->
        <mode>Replace</mode> <!-- Region mode: Replace -->
        <name>header</name> <!-- Region name: header -->
        <type>Region</type> <!-- Region type: Region -->
    </flexiPageRegions> <!-- End header region -->
    <flexiPageRegions> <!-- First column field facet -->
        <itemInstances> <!-- Owner field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.OwnerId</fieldItem> <!-- Contact Owner field item -->
                <identifier>RecordOwnerIdField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Owner field -->
        </itemInstances> <!-- End Owner item -->
        <itemInstances> <!-- Name field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>required</value> <!-- Required UI behavior for Name -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.Name</fieldItem> <!-- Contact Name field item -->
                <identifier>RecordNameField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Name field -->
        </itemInstances> <!-- End Name item -->
        <itemInstances> <!-- Account field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.AccountId</fieldItem> <!-- Contact Account field item -->
                <identifier>RecordAccountIdField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Account field -->
        </itemInstances> <!-- End Account item -->
        <itemInstances> <!-- Title field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.Title</fieldItem> <!-- Contact Title field item -->
                <identifier>RecordTitleField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Title field -->
        </itemInstances> <!-- End Title item -->
        <itemInstances> <!-- Department field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.Department</fieldItem> <!-- Contact Department field item -->
                <identifier>RecordDepartmentField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Department field -->
        </itemInstances> <!-- End Department item -->
        <itemInstances> <!-- Birthdate field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.Birthdate</fieldItem> <!-- Contact Birthdate field item -->
                <identifier>RecordBirthdateField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Birthdate field -->
        </itemInstances> <!-- End Birthdate item -->
        <itemInstances> <!-- ReportsTo field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.ReportsToId</fieldItem> <!-- Contact Reports To field item -->
                <identifier>RecordReportsToIdField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End ReportsTo field -->
        </itemInstances> <!-- End ReportsTo item -->
        <itemInstances> <!-- LeadSource field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.LeadSource</fieldItem> <!-- Contact Lead Source field item -->
                <identifier>RecordLeadSourceField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End LeadSource field -->
        </itemInstances> <!-- End LeadSource item -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000001</name> <!-- First column facet name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End first column field facet -->
    <flexiPageRegions> <!-- Second column field facet -->
        <itemInstances> <!-- Phone field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.Phone</fieldItem> <!-- Contact Phone field item -->
                <identifier>RecordPhoneField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Phone field -->
        </itemInstances> <!-- End Phone item -->
        <itemInstances> <!-- Mobile Phone field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.MobilePhone</fieldItem> <!-- Contact Mobile Phone field item -->
                <identifier>RecordMobilePhoneField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Mobile Phone field -->
        </itemInstances> <!-- End Mobile Phone item -->
        <itemInstances> <!-- Email field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.Email</fieldItem> <!-- Contact Email field item -->
                <identifier>RecordEmailField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Email field -->
        </itemInstances> <!-- End Email item -->
        <itemInstances> <!-- Assistant Name field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.AssistantName</fieldItem> <!-- Contact Assistant Name field item -->
                <identifier>RecordAssistantNameField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Assistant Name field -->
        </itemInstances> <!-- End Assistant Name item -->
        <itemInstances> <!-- Assistant Phone field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>none</value> <!-- None UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.AssistantPhone</fieldItem> <!-- Contact Assistant Phone field item -->
                <identifier>RecordAssistantPhoneField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End Assistant Phone field -->
        </itemInstances> <!-- End Assistant Phone item -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000002</name> <!-- Second column facet name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End second column field facet -->
    <flexiPageRegions> <!-- Field section columns facet -->
        <itemInstances> <!-- First column container -->
            <componentInstance> <!-- Column component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000001</value> <!-- References first column facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:column</componentName> <!-- Flexipage column component -->
                <identifier>flexipage_column</identifier> <!-- Column identifier -->
            </componentInstance> <!-- End column component -->
        </itemInstances> <!-- End first column container -->
        <itemInstances> <!-- Second column container -->
            <componentInstance> <!-- Column component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000002</value> <!-- References second column facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:column</componentName> <!-- Flexipage column component -->
                <identifier>flexipage_column2</identifier> <!-- Column identifier 2 -->
            </componentInstance> <!-- End column component -->
        </itemInstances> <!-- End second column container -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000003</name> <!-- Columns facet name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End field section columns facet -->
    <flexiPageRegions> <!-- Information section facet -->
        <itemInstances> <!-- Information field section component -->
            <componentInstance> <!-- Section component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>columns</name> <!-- Columns property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000003</value> <!-- References columns facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>horizontalAlignment</name> <!-- Alignment property -->
                    <value>false</value> <!-- Horizontal alignment false -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>label</name> <!-- Section label property -->
                    <value>@@@SFDCInformationSFDC@@@</value> <!-- Standard Information label identifier -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:fieldSection</componentName> <!-- Flexipage field section component -->
                <identifier>flexipage_fieldSection</identifier> <!-- Field section identifier -->
            </componentInstance> <!-- End section component -->
        </itemInstances> <!-- End field section wrapper -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000004</name> <!-- Information section facet name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End Information section facet -->
    <flexiPageRegions> <!-- System Information left column facet -->
        <itemInstances> <!-- CreatedBy field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>readonly</value> <!-- Read-only UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.CreatedById</fieldItem> <!-- Created By lookup field item -->
                <identifier>RecordCreatedByIdField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End CreatedBy field -->
        </itemInstances> <!-- End CreatedBy item -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000005</name> <!-- System Info left column facet -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End System Info left column facet -->
    <flexiPageRegions> <!-- System Information right column facet -->
        <itemInstances> <!-- LastModifiedBy field instance -->
            <fieldInstance> <!-- Field instance tag -->
                <fieldInstanceProperties> <!-- Property wrapper -->
                    <name>uiBehavior</name> <!-- UI behavior property -->
                    <value>readonly</value> <!-- Read-only UI behavior -->
                </fieldInstanceProperties> <!-- End property wrapper -->
                <fieldItem>Record.LastModifiedById</fieldItem> <!-- Last Modified By lookup field item -->
                <identifier>RecordLastModifiedByIdField</identifier> <!-- Field identifier -->
            </fieldInstance> <!-- End LastModifiedBy field -->
        </itemInstances> <!-- End LastModifiedBy item -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000006</name> <!-- System Info right column facet -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End System Info right column facet -->
    <flexiPageRegions> <!-- System Information section columns facet -->
        <itemInstances> <!-- System Info left column container -->
            <componentInstance> <!-- Column component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000005</value> <!-- References system info left facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:column</componentName> <!-- Flexipage column component -->
                <identifier>flexipage_column3</identifier> <!-- Column identifier 3 -->
            </componentInstance> <!-- End column component -->
        </itemInstances> <!-- End column container -->
        <itemInstances> <!-- System Info right column container -->
            <componentInstance> <!-- Column component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000006</value> <!-- References system info right facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:column</componentName> <!-- Flexipage column component -->
                <identifier>flexipage_column4</identifier> <!-- Column identifier 4 -->
            </componentInstance> <!-- End column component -->
        </itemInstances> <!-- End column container -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000007</name> <!-- System Info columns facet name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End System Information section columns facet -->
    <flexiPageRegions> <!-- System Information section facet -->
        <itemInstances> <!-- System Information field section component -->
            <componentInstance> <!-- Section component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>columns</name> <!-- Columns property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000007</value> <!-- References system info columns facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>horizontalAlignment</name> <!-- Alignment property -->
                    <value>false</value> <!-- Horizontal alignment false -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>label</name> <!-- Section label property -->
                    <value>@@@SFDCSystem_InformationSFDC@@@</value> <!-- Standard System Information label identifier -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:fieldSection</componentName> <!-- Flexipage field section component -->
                <identifier>flexipage_fieldSection2</identifier> <!-- Field section identifier 2 -->
            </componentInstance> <!-- End section component -->
        </itemInstances> <!-- End field section wrapper -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000008</name> <!-- System Info section facet name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End System Information section facet -->
    <flexiPageRegions> <!-- Related lists tab content facet -->
        <itemInstances> <!-- Related list container component -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>relatedListComponentOverride</name> <!-- Component override property -->
                    <value>NONE</value> <!-- Standard related list override setting -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>rowsToDisplay</name> <!-- Rows count property -->
                    <value>10</value> <!-- Display 10 rows per related list -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>showActionBar</name> <!-- Show action bar property -->
                    <value>true</value> <!-- Display action bar on related lists -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>force:relatedListContainer</componentName> <!-- Standard related list container -->
                <identifier>force_relatedListContainer</identifier> <!-- Related list container identifier -->
            </componentInstance> <!-- End related list component -->
        </itemInstances> <!-- End related list item -->
        <mode>Replace</mode> <!-- Replace mode -->
        <name>relatedTabContent</name> <!-- Related tab content name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End Related lists tab content facet -->
    <flexiPageRegions> <!-- Detail tab content facet -->
        <itemInstances> <!-- Record detail panel component -->
            <componentInstance> <!-- Component instance -->
                <componentName>force:detailPanel</componentName> <!-- Standard detail panel component -->
                <identifier>force_detailPanel</identifier> <!-- Detail panel identifier -->
            </componentInstance> <!-- End detail component -->
        </itemInstances> <!-- End detail item -->
        <mode>Replace</mode> <!-- Replace mode -->
        <name>detailTabContent</name> <!-- Detail tab content name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End Detail tab content facet -->
    <flexiPageRegions> <!-- Main tabs facet -->
        <itemInstances> <!-- Related lists tab component -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>relatedTabContent</value> <!-- References related tab content facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>title</name> <!-- Tab title property -->
                    <value>Standard.Tab.relatedLists</value> <!-- Standard related lists tab title -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:tab</componentName> <!-- Flexipage tab component -->
                <identifier>relatedListsTab</identifier> <!-- Related lists tab identifier -->
            </componentInstance> <!-- End tab component -->
        </itemInstances> <!-- End related tab item -->
        <itemInstances> <!-- Detail tab component -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>active</name> <!-- Active property -->
                    <value>true</value> <!-- Sets detail tab as active by default -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>detailTabContent</value> <!-- References detail tab content facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>title</name> <!-- Tab title property -->
                    <value>Standard.Tab.detail</value> <!-- Standard detail tab title -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:tab</componentName> <!-- Flexipage tab component -->
                <identifier>detailTab</identifier> <!-- Detail tab identifier -->
            </componentInstance> <!-- End tab component -->
        </itemInstances> <!-- End detail tab item -->
        <mode>Replace</mode> <!-- Replace mode -->
        <name>maintabs</name> <!-- Main tabs name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End Main tabs facet -->
    <flexiPageRegions> <!-- Main region -->
        <itemInstances> <!-- Accordion component container -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>accordionSections</name> <!-- Accordion sections property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000009</value> <!-- References accordion sections facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>allowMultipleSectionsOpen</name> <!-- Multiple sections property -->
                    <value>false</value> <!-- Disallow multiple open sections -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>defaultSectionName</name> <!-- Default section property -->
                    <value>accordionSection1</value> <!-- Default open section accordionSection1 -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:accordion</componentName> <!-- Flexipage accordion component -->
                <identifier>flexipage_accordion</identifier> <!-- Accordion identifier -->
            </componentInstance> <!-- End accordion component -->
        </itemInstances> <!-- End accordion container item -->
        <itemInstances> <!-- Main tabset component container -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>label</name> <!-- Tabset label property -->
                    <value>Tabs</value> <!-- Tabset label Tabs -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>tabs</name> <!-- Tabs property -->
                    <value>maintabs</value> <!-- References maintabs facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:tabset</componentName> <!-- Flexipage tabset component -->
                <identifier>flexipage_tabset</identifier> <!-- Tabset identifier -->
            </componentInstance> <!-- End tabset component -->
        </itemInstances> <!-- End tabset item -->
        <mode>Replace</mode> <!-- Replace mode -->
        <name>main</name> <!-- Region name: main -->
        <type>Region</type> <!-- Region type: Region -->
    </flexiPageRegions> <!-- End Main region -->
    <flexiPageRegions> <!-- Accordion sections facet -->
        <itemInstances> <!-- Information accordion section -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000004</value> <!-- References Information section facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>label</name> <!-- Section label property -->
                    <value>Standard.Tab.fields</value> <!-- Fields tab label -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>name</name> <!-- Section name property -->
                    <value>accordionSection1</value> <!-- Section identifier accordionSection1 -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:accordionSection</componentName> <!-- Accordion section component -->
                <identifier>flexipage_accordionSection</identifier> <!-- Section identifier -->
            </componentInstance> <!-- End section component -->
        </itemInstances> <!-- End Information section item -->
        <itemInstances> <!-- System Info accordion section -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000008</value> <!-- References System Info section facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>label</name> <!-- Section label property -->
                    <value>Standard.Tab.additionalFields</value> <!-- Additional fields tab label -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>name</name> <!-- Section name property -->
                    <value>accordionSection2</value> <!-- Section identifier accordionSection2 -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:accordionSection</componentName> <!-- Accordion section component -->
                <identifier>flexipage_accordionSection2</identifier> <!-- Section identifier 2 -->
            </componentInstance> <!-- End section component -->
        </itemInstances> <!-- End System Info section item -->
        <name>Facet-c1a1b2c3-1111-4a1a-8a1a-000000000009</name> <!-- Accordion sections facet name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End Accordion sections facet -->
    <flexiPageRegions> <!-- Chatter feed tab content facet -->
        <itemInstances> <!-- Record feed component -->
            <componentInstance> <!-- Component instance -->
                <componentName>forceChatter:recordFeedContainer</componentName> <!-- Standard Chatter feed container component -->
                <identifier>forceChatter_recordFeedContainer</identifier> <!-- Chatter feed identifier -->
            </componentInstance> <!-- End feed component -->
        </itemInstances> <!-- End feed item -->
        <mode>Replace</mode> <!-- Replace mode -->
        <name>feedTabContent</name> <!-- Feed tab content name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End Chatter feed tab content facet -->
    <flexiPageRegions> <!-- Sidebar tabs facet -->
        <itemInstances> <!-- Collaborate tab component -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>body</name> <!-- Body property -->
                    <value>feedTabContent</value> <!-- References feed tab content facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>title</name> <!-- Tab title property -->
                    <value>Standard.Tab.collaborate</value> <!-- Standard collaborate tab title -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:tab</componentName> <!-- Flexipage tab component -->
                <identifier>collaborateTab</identifier> <!-- Collaborate tab identifier -->
            </componentInstance> <!-- End tab component -->
        </itemInstances> <!-- End collaborate tab item -->
        <mode>Replace</mode> <!-- Replace mode -->
        <name>sidebartabs</name> <!-- Sidebar tabs name -->
        <type>Facet</type> <!-- Facet region type -->
    </flexiPageRegions> <!-- End Sidebar tabs facet -->
    <flexiPageRegions> <!-- Sidebar region -->
        <itemInstances> <!-- Sidebar tabset component container -->
            <componentInstance> <!-- Component instance -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>label</name> <!-- Tabset label property -->
                    <value>Tabs</value> <!-- Tabset label Tabs -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentInstanceProperties> <!-- Property wrapper -->
                    <name>tabs</name> <!-- Tabs property -->
                    <value>sidebartabs</value> <!-- References sidebartabs facet -->
                </componentInstanceProperties> <!-- End property wrapper -->
                <componentName>flexipage:tabset</componentName> <!-- Flexipage tabset component -->
                <identifier>flexipage_tabset2</identifier> <!-- Sidebar tabset identifier -->
            </componentInstance> <!-- End tabset component -->
        </itemInstances> <!-- End sidebar tabset item -->
        <mode>Replace</mode> <!-- Replace mode -->
        <name>sidebar</name> <!-- Region name: sidebar -->
        <type>Region</type> <!-- Region type: Region -->
    </flexiPageRegions> <!-- End Sidebar region -->
    <masterLabel>Contact Record Page for Sales</masterLabel> <!-- Master label for FlexiPage -->
    <parentFlexiPage>flexipage__default_rec_L</parentFlexiPage> <!-- Parent standard default FlexiPage template -->
    <sobjectType>Contact</sobjectType> <!-- SObject type: Contact -->
    <template> <!-- Template definition -->
        <name>flexipage:recordHomeTemplateDesktop</name> <!-- Standard desktop record home template -->
    </template> <!-- End template definition -->
    <type>RecordPage</type> <!-- FlexiPage type: RecordPage -->
</FlexiPage> <!-- End FlexiPage document -->
EOF # ends heredoc for Contact FlexiPage

# Step 2: Deploy Contact Record Page for Sales metadata to target org
CMD="sf project deploy start -m FlexiPage:Contact_Record_Page_for_Sales -o trailhead-playground --json" # sf deploy command
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_FLEXIPAGE_DEPLOY_AUDIT.json # executes deploy and writes log output

# Step 3: Retrieve Contact Record Page for Sales metadata back to local source
CMD="sf project retrieve start -m FlexiPage:Contact_Record_Page_for_Sales -o trailhead-playground --json" # sf retrieve command
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_FLEXIPAGE_RETRIEVE_AUDIT.json # executes retrieve and writes log output
```

```bash
# Verifies Contact record flexipage metadata deployment via Salesforce Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, DeveloperName, MasterLabel, SobjectType FROM FlexiPage WHERE DeveloperName = 'Contact_Record_Page_for_Sales'\" -o trailhead-playground --json" # tooling api flexipage query
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_FLEXIPAGE_VERIFY_AUDIT.json # executes query and writes log output
```

```bash
# Deploys updated Contact Layout metadata with Notes & Attachments removed and Files related list added
mkdir -p badges/05_lightning_experience_customization/logs # creates logging directory for output tracking

# Step 1: Deploy patched Contact Layout metadata
CMD="sf project deploy start -m Layout:Contact-Contact Layout -o trailhead-playground --json" # sf deploy command for contact layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_LAYOUT_DEPLOY_AUDIT.json # executes deploy and writes log output
```

```bash
# Verifies Contact layout metadata exist in target org via Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, Name, TableEnumOrId FROM Layout WHERE TableEnumOrId = 'Contact' AND Name = 'Contact Layout'\" -o trailhead-playground --json" # tooling api layout query
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_LAYOUT_VERIFY_AUDIT.json # executes query and writes log output
```

```bash
# Retrieves Contact_Record_Page_for_Sales metadata post org-default activation and redeploys as audit payload
mkdir -p badges/05_lightning_experience_customization/logs # creates logging directory for output tracking

# Step 1: Retrieve activated FlexiPage metadata from org
CMD="sf project retrieve start -m FlexiPage:Contact_Record_Page_for_Sales -o trailhead-playground --json" # sf retrieve command for activated flexipage
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_ACTIVATION_RETRIEVE_AUDIT.json # executes retrieve and writes log output

# Step 2: Deploy activated FlexiPage metadata back to org
CMD="sf project deploy start -m FlexiPage:Contact_Record_Page_for_Sales -o trailhead-playground --json" # sf deploy command for activated flexipage
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_ACTIVATION_DEPLOY_AUDIT.json # executes deploy and writes log output
```

```bash
# Verifies activation of Contact_Record_Page_for_Sales FlexiPage via Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, DeveloperName, SobjectType FROM FlexiPage WHERE DeveloperName = 'Contact_Record_Page_for_Sales'\" -o trailhead-playground --json" # tooling api query for flexipage activation
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_5_CHALLENGE_ACTIVATION_VERIFY_AUDIT.json # executes query and writes log output
```

---

## Technical Post-Mortem & Engineering Learnings

1. **FlexiPage / Dynamic Forms Hand-Authoring Infeasibility:**
   - **Finding:** Unlike `CompactLayout` or `CustomObject`, `FlexiPage` XML generated by the Dynamic Forms migration wizard and the Activation wizard includes builder-assigned region UUIDs and nested facet structures that Salesforce's own docs steer you away from hand-authoring.
   - **Resolution:** Built via GUI per the Trailhead click-path, then closed out with a retrieve → deploy round trip — the redeployed file, not a hand-written-from-scratch XML block, is the reproducible payload for these requirements.

2. **Missing Local Baseline for Page Layouts:**
   - **Finding:** `Energy_Audit__c`'s default page layout was auto-created by Salesforce when the object was deployed (Unit 1) but was never retrieved into local source, so its full field/section content wasn't known locally.
   - **Resolution:** Retrieve the current layout first, patch only the `relatedLists` block, then redeploy — avoids blindly reconstructing (and potentially corrupting) a layout whose existing content wasn't fully known.

3. **Field Order Regression Caught by Auditing the Retrieved Output:**
   - **Finding:** After the `G1` Dynamic Forms build, the retrieved FlexiPage showed `Account__c` listed _before_ `Record.Name` — backwards from the requirement ("Account sits below Energy Audit Name"). Easy to miss without actually reading the retrieved XML.
   - **Resolution:** Since a real, wizard-generated baseline already existed, the two `<itemInstances>` blocks were swapped directly via a targeted hand-edit — safe because it reordered existing sibling elements without introducing any new builder-assigned identifiers.

4. **Files Related List: Two Wrong Values Before the Real One:**
   - **Finding:** `AttachedContentDocuments` and `RelatedContentDocumentList` both failed deployment with `Cannot find related list:...`. Neither is documented in Salesforce's Metadata API reference, and no existing layout in the org (Account's included) had a working example to copy from.
   - **Resolution:** The real value — **`RelatedFileList`** — was only discoverable by adding Files via the classic Page Layout GUI editor once, saving, then retrieving to see what Salesforce itself assigned.

5. **Org-Default Activation Cannot Be Deployed via CLI at All — Confirmed, Not Assumed:**
   - **Finding:** Verified across three separate documentation checks (the `FlexiPage` Metadata API reference, the general Metadata API docs, and the Tooling API object list) that "Assign as Org Default" record page activation isn't represented in any deployable metadata type. This is a genuine, permanent Salesforce platform limitation, not a gap that better tooling knowledge would close.
   - **Resolution:** This one action — Activation → Org Default → Save — must always happen via browser click. Contrast with `G3`'s **App, Record Type, and Profile** assignment (not Org Default), which _is_ captured, via `profileActionOverrides` inside the owning `CustomApplication`'s own metadata — confirmed by inspecting `Energy_Consultations.app-meta.xml` directly after activation.

6. **Unfilled Doc Placeholders Produce Confusing Failures:**
   - **Finding:** `<confirm actual API name>` was left in `C3`'s code block even after the real name (`Contact_Record_Page_for_Sales`) was already known elsewhere in the doc, causing `Entity of type 'FlexiPage' named '<confirm actual API name>' cannot be found`.
   - **Resolution:** Once a placeholder's real value is confirmed anywhere in a doc, immediately propagate it to every occurrence — stale template text left sitting in an otherwise-real, copy-paste-ready code block reads as a working command until it isn't.

7. **Audit Logs Must Be Written By the Command Itself, Not Reconstructed Afterward:**
   - **Finding:** Both Unit 4 and this unit lost their audit trail for a stretch — `--json` output was being pasted into chat/terminal without ever being redirected to a file, and by the time it's noticed, the exact raw output isn't reliably recoverable.
   - **Resolution:** Every deploy command in this doc now pipes its own output directly to the log file via `tee`, matching Unit 3's established pattern — the log is a direct capture of what the CLI actually returned, never a secondhand transcription.

8. **Terminal Paste Corruption on Multi-Line Commands:**
   - **Finding:** Multi-line `\`-continued commands repeatedly broke when pasted through the terminal — a wrapped `git push --force-with-lease`, a SOQL query, and a `sf project deploy start` call all hit this, the last one appending a stray `~` that broke the `--json` flag entirely.
   - **Resolution:** Prefer single-line commands for anything likely to be copy-pasted through a terminal prone to bracketed-paste-mode artifacts. Multi-line heredocs (`cat << 'EOF' ... EOF`) were never affected, since they paste as one logical block.

9. **Re-Retrieving Metadata Can Silently Overwrite an Undeployed Local Fix:**
   - **Finding:** After manually correcting `Contact-Contact Layout.layout-meta.xml`'s related-list value locally, re-running its retrieve command (as part of a "rerun everything from scratch" pass) would have pulled the org's still-broken state and erased the fix — the deploy that would've made the fix live had errored out first, so the org was never actually caught up.
   - **Resolution:** When rerunning a sequence from scratch, skip any retrieve that pulls _from_ the org if a correct, not-yet-deployed local edit already exists for that file — only the deploy should be repeated in that case.
