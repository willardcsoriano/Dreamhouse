# Trailhead Unit: Create Custom Buttons and Links

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 6:** Create Custom Buttons and Links  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_buttons_links?trail_id=force_com_dev_beginner)

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Custom Buttons and Links](#custom-buttons-and-links)
- [What Can Custom Buttons and Links Do?](#what-can-custom-buttons-and-links-do)
- [Create a Custom List Button](#create-a-custom-list-button)
- [Create a Custom Detail Page Link](#create-a-custom-detail-page-link)
- [Create a Custom Detail Page Button](#create-a-custom-detail-page-button)
- [Resources](#resources)
- [Hands-On Challenge](#hands-on-challenge)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem-engineering-learnings)
  - [Technical Learnings & Observations](#technical-learnings-observations)
  - [Hiccup → Resolution: GUI Record Visibility & List View Filtering](#hiccup-resolution-gui-record-visibility-list-view-filtering)

## Learning Objectives

After completing this unit, you'll be able to:

- Create custom buttons and links.
- Add them to a page layout.
- Explain the difference between a custom button and a custom link.

> **Note:**  
> **Accessibility**
>
> This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click the link below:
>
> Open Trailhead screen reader instructions.

---

## Custom Buttons and Links

Every org has a unique set of business needs. If your users frequently need to access other pages in or outside your org, you can add custom buttons and links directly to object and record detail pages.

Custom buttons and links help you integrate Salesforce data with external URLs, applications, your company’s intranet, or other back-end office systems.

When your users have all the information they need on hand, they can be even more productive with Salesforce.

---

## What Can Custom Buttons and Links Do?

Custom links can link to an external URL, such as www.google.com, a Visualforce page, or your company’s intranet. Custom buttons can connect users to external applications, such as web pages, and launch custom links.

You can choose the display window properties that determine how the target of a link or button is displayed to your users. Custom links can include Salesforce fields as tokens within the URL. For example, you can include an account name in a URL that searches Yahoo: `https://search.yahoo.com/bin/search?p={!Account_Name}`.

> **Note:**  
> If you want the button or link to launch a custom page or other code, consider a Visualforce page. If you don’t know how to use Visualforce pages yet, don’t worry. We don’t address them here, but you can learn about them in a different module.

In Lightning Experience, custom buttons and links live on your page layouts and appear in different areas of a Lightning page.

There are three primary types of custom buttons and links that you can create.

- **List button**—Appears on a related list on an object record page.
- **Detail page link**—Appears in the Links section of the record details on an object record page.
- **Detail page button**—Appears in the action menu in the highlights panel of a record page.

We’ll explore all three of these options.

---

## Create a Custom List Button

You’ve read what they can do, now find out how to create one. For each type, you must define the action that occurs when a user clicks it. First, the custom list button.

A custom list button is a button that you can add to a related list. When you create a list button for an object, you can add that button to that object’s related list when the related list appears on other objects. Because Energy Audits are tied to accounts with a lookup relationship field, an Energy Audits related list automatically appears on account records.

For example, earlier in the module you entered audit information for “GenePoint 5-year review.” When you view the GenePoint account record, then click the Related tab and scroll to the end of the record page, you see an Energy Audits related list displaying that audit.

Maria wants to add a custom button to that Energy Audits related list to let users navigate directly to the Ursa Major Solar energy audit guidelines PDF. She’s already uploaded the PDF as a file, but she needs its URL in order to have the custom button point to it. Here’s how that works.

1. From the App Launcher, find and select the **Sales** app.
2. Click the **Files** tab.

Here, Maria can see the guidelines PDF she uploaded.

3. Upload a file of your own so you can follow along with the rest of these steps.
4. Click Action dropdown for the file you just uploaded and select **Share**.
5. Click the carat next to **Who Can Access** to expand that section.
6. In the Create Public Link area, set the Password toggle button to **Off**.
7. Click **Create Link**, then click **Create**.  
   This generates a public URL for the file that you can share with others, or in this case, add as a URL to a custom button or link. In this example, Maria's URL is `https://ursamajorsolar.salesforce.com/sfc/p/R00000008nD1/a/R000000007LK/8Z8auAJBSeSCzqQ8Kv9ofolIWi_jP13oR3LUUYuXc3A`.
8. Click **Copy Link**, then click **Done**.

**No CLI equivalent for file upload and share link generation — do this in the browser to obtain the URL.**

9. From Setup, click **Object Manager**, then click **Energy Audit**.
10. Click **Buttons, Links, and Actions**, then **New Button or Link**.
11. Name the button **Audit Guidelines**.
12. Select **List Button**.
13. Paste the file URL into the large text box.  
    Because the file is local to your org, use everything after the domain portion of the URL to create the custom link. Using this example, Maria's link points to `/sfc/p/R00000008nD1/a/R000000007LK/8Z8auAJBSeSCzqQ8Kv9ofolIWi_jP13oR3LUUYuXc3A`.

You might be thinking to yourself: “OK, whoa! What’s all that formula-looking stuff? What do I do with that?” That’s a version of Salesforce’s formula editor, and you can use it to define the properties of the button or link. For example, if your content source is URL as in this case, this section is where you put the URL you want the button or link to point to. And, you can add merge fields and operators to enhance the behavior of the button or link by including data from Salesforce. For more information on merge fields and operators, check out the Salesforce Help.

14. Click **Save**, then **OK**.  
    The button won’t appear on the Energy Audits related list for any object until Maria adds it. That’s next.
15. Click **Object Manager**, then click **Account**.
16. Click **Page Layouts**, then click **Account Layout**.
17. Scroll all the way down the end of the layout, to the Energy Audits related list.
18. Click the wrench icon to edit it.
19. Click the plus icon to expand the Buttons section header.
20. Add the **Audit Guidelines** button to the Selected Buttons list, then click **OK**.
21. Click **Save**.
22. Navigate back to the Sales app, click **Accounts** and select the **GenePoint** account.
23. Click the **Related** tab, scroll to the bottom, and you see the new **Audit Guidelines** button on the Energy Audits related list.

```bash
# Deploys the Audit_Guidelines list button on Energy_Audit__c and updates Account Layout to include it on the Energy Audits related list.
mkdir -p force-app/main/default/objects/Energy_Audit__c/webLinks # Creates directory for Energy_Audit__c WebLink metadata

cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/webLinks/Audit_Guidelines.webLink-meta.xml # Writes WebLink XML payload file
<?xml version="1.0" encoding="UTF-8"?> <!-- XML declaration -->
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Metadata API namespace for WebLink definition -->
    <fullName>Audit_Guidelines</fullName> <!-- Unique API name for the custom button -->
    <availability>online</availability> <!-- Makes the button active and available to users -->
    <displayType>massActionButton</displayType> <!-- Specifies list button type for related lists -->
    <encodingKey>UTF-8</encodingKey> <!-- Sets character encoding to UTF-8 -->
    <height>600</height> <!-- Display window height in pixels -->
    <linkType>url</linkType> <!-- Target content type is a URL -->
    <masterLabel>Audit Guidelines</masterLabel> <!-- UI label visible on the button -->
    <openType>sidebar</openType> <!-- Display window setting: open with sidebar -->
    <protected>false</protected> <!-- Component is public and unprotected -->
    <requireRowSelection>true</requireRowSelection> <!-- Shows multi-select checkboxes on related list -->
    <url>/sfc/p/R00000008nD1/a/R000000007LK/8Z8auAJBSeSCzqQ8Kv9ofolIWi_jP13oR3LUUYuXc3A</url> <!-- Relative URL path to public file share -->
</WebLink> <!-- End of WebLink metadata definition -->
EOF <!-- End of XML heredoc creation -->

CMD="sf project deploy start -d force-app/main/default/objects/Energy_Audit__c/webLinks -m Layout:Account-Account\ Layout -o trailhead-playground --json" # Sets deploy CLI command for Audit_Guidelines button and Account layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_GUIDED_LIST_BUTTON_DEPLOY_AUDIT.json # Executes deployment and logs JSON output
```

```bash
# Verifies that the Audit_Guidelines WebLink exists in the org via Tooling API query.
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT Id, MasterLabel, LinkType, DisplayType, Url FROM WebLink WHERE MasterLabel='Audit Guidelines'\"" # Sets Tooling API query command
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_GUIDED_LIST_BUTTON_VERIFICATION_AUDIT.json # Executes query and logs JSON output
```

---

## Create a Custom Detail Page Link

Maria, our Ursa Major Solar admin, wants to add a custom link that lets her users do a quick Google search on the accounts they’re viewing.

Let’s get started.

1. From Setup, click **Object Manager**, then click **Account**.
2. Click **Buttons, Links, and Actions**, then **New Button or Link**.
3. Name the link **Google This Account**.
4. Make sure that **Detail Page Link** is selected for the display type, and leave the next two fields as-is.

Now it’s time to add the URL we want this link to point to.

5. In the formula editor, enter `https://www.google.com/search?q={!Account.Name}`.
6. Click **Save**, then click **OK**.

You can also use Quick Save to save and continue editing. Saving validates the URL you defined if you set the content source to URL. Before you can use your custom buttons and links, you must add them to an object’s page layout. You can then see and use the button or link on a record detail page. Let’s do that next.

7. Click **Page Layouts**, then **Account Layout**.
8. From the Custom Links category in the palette, drag **Google This Account** into the Custom Links section of the layout.
9. Hover over the Custom Links section and click the wrench icon that appears.
10. In the Section Properties window, select **Detail Page**, then click **OK**.
11. Save the page layout.

Let’s go check out the results.

12. From the App Launcher, find and select **Accounts**.
13. Open an account record.
14. Click the **Details** tab and scroll to the bottom to find the custom link.

> **Note:**  
> Custom detail page links are only supported on record pages that don’t use Dynamic Forms. See the Lightning App Builder module for more information on Dynamic Forms.

```bash
# Deploys the Google_This_Account detail page link on Account and updates Account Layout to include it in Custom Links.
mkdir -p force-app/main/default/objects/Account/webLinks # Creates directory for Account WebLink metadata

cat << 'EOF' > force-app/main/default/objects/Account/webLinks/Google_This_Account.webLink-meta.xml # Writes WebLink XML payload file
<?xml version="1.0" encoding="UTF-8"?> <!-- XML declaration -->
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Metadata API namespace for WebLink definition -->
    <fullName>Google_This_Account</fullName> <!-- Unique API name for the custom link -->
    <availability>online</availability> <!-- Makes the link active and available to users -->
    <displayType>link</displayType> <!-- Specifies display type: Detail Page Link -->
    <encodingKey>UTF-8</encodingKey> <!-- Sets character encoding to UTF-8 -->
    <hasMenubar>false</hasMenubar> <!-- Hides browser menu bar when opened -->
    <hasScrollbars>true</hasScrollbars> <!-- Enables browser scrollbars -->
    <hasToolbar>false</hasToolbar> <!-- Hides browser toolbar -->
    <height>600</height> <!-- Display window height in pixels -->
    <isResizable>true</isResizable> <!-- Allows browser window resizing -->
    <linkType>url</linkType> <!-- Target content type is a URL -->
    <masterLabel>Google This Account</masterLabel> <!-- UI label visible in Custom Links section -->
    <openType>newWindow</openType> <!-- Opens target URL in a new browser window -->
    <position>none</position> <!-- Default window position -->
    <protected>false</protected> <!-- Component is public and unprotected -->
    <showsLocation>false</showsLocation> <!-- Hides URL location bar in browser window -->
    <showsStatus>false</showsStatus> <!-- Hides browser status bar -->
    <url>https://www.google.com/search?q={!Account.Name}</url> <!-- Dynamic Google search URL with Account Name merge field -->
</WebLink> <!-- End of WebLink metadata definition -->
EOF <!-- End of XML heredoc creation -->

CMD="sf project deploy start -d force-app/main/default/objects/Account/webLinks/Google_This_Account.webLink-meta.xml -m Layout:Account-Account\ Layout -o trailhead-playground --json" # Sets deploy CLI command for Google_This_Account link and Account layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_GUIDED_DETAIL_LINK_DEPLOY_AUDIT.json # Executes deployment and logs JSON output
```

```bash
# Verifies that the Google_This_Account WebLink exists in the org via Tooling API query.
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT Id, MasterLabel, LinkType, DisplayType, Url FROM WebLink WHERE MasterLabel='Google This Account'\"" # Sets Tooling API query command
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_GUIDED_DETAIL_LINK_VERIFICATION_AUDIT.json # Executes query and logs JSON output
```

---

## Create a Custom Detail Page Button

Maria wants to add a custom button to account pages that shows the account’s location on Google Maps.

1. From Setup, click **Object Manager**, then click **Account**.
2. Click **Buttons, Links, and Actions**, then click **New Button or Link**.
3. Name the button **Map Location**.
4. Select **Detail Page Button**.
5. Paste this URL into the formula editor: `http://maps.google.com/maps?q={!Account_BillingStreet}%20{!Account_BillingCity}%20{!Account_BillingState}%20{!Account_BillingPostalCode}`.

This URL uses merge fields (`{!Account_BillingStreet}`) and passes the field information from the account record that the button is clicked from into the URL.

6. Click **Save**, then click **OK**.
7. Now add it to the Account page layout.
8. Click **Page Layouts**, then click **Account Layout**.
9. From the Buttons category in the palette, drag **Map Location** into the Custom Buttons area on the page layout.
10. Click **Save**.
11. OK! Now let’s test it.
12. From the App Launcher, find and select **Sales**, then click the **Accounts** tab.
13. Open an account record.
14. In the highlights panel, not only do you see the fields from the object’s compact layout, but you also see an actions menu. The actions menu is a combination of the standard buttons, custom buttons, and actions from the page layout. (We’ll go over actions in the next unit.)
15. Expand the actions menu, and select **Map Location**.
16. The browser opens a new window or tab that shows you the account’s address in Google Maps.

Is Map Location not showing up in the actions menu even though you added the custom button to the page layout? This happens sometimes if you override the default settings of the "Salesforce Mobile and Lightning Experience Actions" section of a page layout. To fix it, add any missing buttons to the page layout as actions by dragging them from the "Mobile & Lightning Actions" category in the palette into the "Salesforce Mobile and Lightning Experience Actions" section.

> **Note:**  
> Custom detail page buttons and links can do the same things. Consider where and how you want them to appear on your page, and that can help you decide which type to choose.

```bash
# Deploys the Map_Location detail page button on Account and updates Account Layout to include it in Custom Buttons.
mkdir -p force-app/main/default/objects/Account/webLinks # Creates directory for Account WebLink metadata

cat << 'EOF' > force-app/main/default/objects/Account/webLinks/Map_Location.webLink-meta.xml # Writes WebLink XML payload file
<?xml version="1.0" encoding="UTF-8"?> <!-- XML declaration -->
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Metadata API namespace for WebLink definition -->
    <fullName>Map_Location</fullName> <!-- Unique API name for the custom button -->
    <availability>online</availability> <!-- Makes the button active and available to users -->
    <displayType>button</displayType> <!-- Specifies display type: Detail Page Button -->
    <encodingKey>UTF-8</encodingKey> <!-- Sets character encoding to UTF-8 -->
    <hasMenubar>false</hasMenubar> <!-- Hides browser menu bar when opened -->
    <hasScrollbars>true</hasScrollbars> <!-- Enables browser scrollbars -->
    <hasToolbar>false</hasToolbar> <!-- Hides browser toolbar -->
    <height>600</height> <!-- Display window height in pixels -->
    <isResizable>true</isResizable> <!-- Allows browser window resizing -->
    <linkType>url</linkType> <!-- Target content type is a URL -->
    <masterLabel>Map Location</masterLabel> <!-- UI label visible on the detail page button -->
    <openType>newWindow</openType> <!-- Opens target URL in a new browser window -->
    <position>none</position> <!-- Default window position -->
    <protected>false</protected> <!-- Component is public and unprotected -->
    <showsLocation>false</showsLocation> <!-- Hides URL location bar in browser window -->
    <showsStatus>false</showsStatus> <!-- Hides browser status bar -->
    <url>http://maps.google.com/maps?q={!Account.BillingStreet}%20{!Account.BillingCity}%20{!Account.BillingState}%20{!Account.BillingPostalCode}</url> <!-- Google Maps URL with Account Billing address merge fields -->
</WebLink> <!-- End of WebLink metadata definition -->
EOF <!-- End of XML heredoc creation -->

CMD="sf project deploy start -d force-app/main/default/objects/Account/webLinks/Map_Location.webLink-meta.xml -m Layout:Account-Account\ Layout -o trailhead-playground --json" # Sets deploy CLI command for Map_Location button and Account layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_GUIDED_DETAIL_BUTTON_DEPLOY_AUDIT.json # Executes deployment and logs JSON output
```

```bash
# Verifies that the Map_Location WebLink exists in the org via Tooling API query.
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT Id, MasterLabel, LinkType, DisplayType, Url FROM WebLink WHERE MasterLabel='Map Location'\"" # Sets Tooling API query command
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_GUIDED_DETAIL_BUTTON_VERIFICATION_AUDIT.json # Executes query and logs JSON output
```

---

## Resources

- [Salesforce Help: Define Custom Buttons and Links](https://help.salesforce.com/s/articleView?id=sf.customize_customlinktext.htm&type=5)
- [Salesforce Help: Custom Button and Link Samples](https://help.salesforce.com/s/articleView?id=sf.customlink_examples.htm&type=5)
- [Salesforce Help: Constructing Effective Custom URL Buttons and Links](https://help.salesforce.com/s/articleView?id=sf.customlink_urls.htm&type=5)
- [Salesforce Help: Custom Button Considerations](https://help.salesforce.com/s/articleView?id=sf.customlink_considerations.htm&type=5)

---

## Hands-On Challenge

Get Ready

You’ll be completing this unit in your own hands-on org. Click Launch to get started, or click the name of your org to choose a different one.

Your Challenge
Add a Custom Button to a Contact

Ursa Major Solar wants to be able to look at their contacts’ internet footprints. Create a custom button so users can do this right from a contact record.

- Create a custom button for the Contact object:
  - Label: **Google Info**
  - Name: **Google_Info**
  - The custom button opens a link to `https://www.google.com/search?q={!Contact.Name}` (where `{!Contact.Name}` is the current contact's name)
  - Add the custom button to the **Contact Layout** page layout

```bash
# Deploys the Google_Info detail page button on Contact and updates Contact Layout to include it in Custom Buttons.
mkdir -p force-app/main/default/objects/Contact/webLinks # Creates directory for Contact WebLink metadata

cat << 'EOF' > force-app/main/default/objects/Contact/webLinks/Google_Info.webLink-meta.xml # Writes WebLink XML payload file
<?xml version="1.0" encoding="UTF-8"?> <!-- XML declaration -->
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Metadata API namespace for WebLink definition -->
    <fullName>Google_Info</fullName> <!-- Unique API name for the custom button -->
    <availability>online</availability> <!-- Makes the button active and available to users -->
    <displayType>button</displayType> <!-- Specifies display type: Detail Page Button -->
    <encodingKey>UTF-8</encodingKey> <!-- Sets character encoding to UTF-8 -->
    <hasMenubar>false</hasMenubar> <!-- Hides browser menu bar when opened -->
    <hasScrollbars>true</hasScrollbars> <!-- Enables browser scrollbars -->
    <hasToolbar>false</hasToolbar> <!-- Hides browser toolbar -->
    <height>600</height> <!-- Display window height in pixels -->
    <isResizable>true</isResizable> <!-- Allows browser window resizing -->
    <linkType>url</linkType> <!-- Target content type is a URL -->
    <masterLabel>Google Info</masterLabel> <!-- UI label visible on the Contact detail page button -->
    <openType>newWindow</openType> <!-- Opens target URL in a new browser window -->
    <position>none</position> <!-- Default window position -->
    <protected>false</protected> <!-- Component is public and unprotected -->
    <showsLocation>false</showsLocation> <!-- Hides URL location bar in browser window -->
    <showsStatus>false</showsStatus> <!-- Hides browser status bar -->
    <url>https://www.google.com/search?q={!Contact.Name}</url> <!-- Google search URL with Contact Name merge field -->
</WebLink> <!-- End of WebLink metadata definition -->
EOF <!-- End of XML heredoc creation -->

CMD="sf project deploy start -d force-app/main/default/objects/Contact/webLinks/Google_Info.webLink-meta.xml -m Layout:Contact-Contact\ Layout -o trailhead-playground --json" # Sets deploy CLI command for Google_Info button and Contact layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_CHALLENGE_DEPLOY_AUDIT.json # Executes deployment and logs JSON output
```

```bash
# Verifies that the Google_Info WebLink exists in the org via Tooling API query.
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT Id, MasterLabel, LinkType, DisplayType, Url FROM WebLink WHERE MasterLabel='Google Info'\"" # Sets Tooling API query command
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_6_CHALLENGE_VERIFICATION_AUDIT.json # Executes query and logs JSON output
```

---

## Technical Post-Mortem & Engineering Learnings

### Technical Learnings & Observations

1. **`WebLink` Metadata Structure & Field Mappings:**
   - Custom list buttons, detail page links, and detail page buttons are all represented by the `WebLink` Metadata API type.
   - `displayType` differentiates the button/link behavior: `massActionButton` for related list buttons (or `button` with `requireRowSelection`), `link` for detail page links, and `button` for detail page buttons.
   - URL merge fields must use standard API field path dot-notation (e.g. `{!Account.BillingStreet}` or `{!Contact.Name}`).

2. **Page Layout Declarative Placement:**
   - WebLinks are assigned to page layouts via XML tags in `Layout` metadata: `<customButtons>` for detail page buttons, `<customLink>` inside `<layoutItems>` for detail page links, and `<customButtons>` inside `<relatedLists>` for related list buttons.

3. **Logging & Verification Standards:**
   - Command logging uses structured JSON wrapper syntax (`CMD="..."` and `{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee ...`) to record both command string and CLI JSON result.
   - Tooling API queries verify `WebLink` existence, label, display type, and URL endpoints directly from org metadata.

### Hiccup → Resolution: GUI Record Visibility & List View Filtering

- **Hiccup:** The `GenePoint` Account record and its related `GenePoint 5-year review` Energy Audit record appeared missing when accessing the Accounts tab in the Salesforce Lightning GUI (default `Recently Viewed` list view filter, `filterName=__Recent`).
- **Root Cause:** Records created or queried programmatically via the Salesforce CLI (`sf data create` / `sf data query`) exist in the org database but don't automatically register in the browser-specific **Recently Viewed** list view until accessed directly through the GUI. `GenePoint` is an **Account** record; `GenePoint 5-year review` is a child **Energy Audit** (`Energy_Audit__c`) record linked to it via a lookup relationship (`Account__c`).
- **Verification:** `sf data query -q "SELECT Id, Name, Type, Phone, Industry FROM Account WHERE Name LIKE '%GenePoint%'"` returned 1 record (`Id: 001dL00002LjoYOQAZ`), confirming the record existed in the org database the whole time — this was a list-view filter issue, not a deploy or data problem.
- **Resolution:** In the Accounts tab, switch the list view filter from **Recently Viewed** to **All Accounts**, open the **GenePoint** account record, select the **Related** tab, and scroll to the **Energy Audits** related list to find **GenePoint 5-year review**.
