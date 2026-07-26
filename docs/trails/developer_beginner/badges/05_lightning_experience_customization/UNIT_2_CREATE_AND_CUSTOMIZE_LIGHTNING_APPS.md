# Trailhead Unit: Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 2:** Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_apps?trail_id=force_com_dev_beginner)

---

## Learning Objectives

After completing this unit, you’ll be able to:

- Describe the benefits of Lightning apps.
- Create a Lightning app with custom branding.
- List two best practices for planning Lightning apps for your org.

> **Note:**  
> **Accessibility**  
> This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click the link below:  
> [Open Trailhead screen reader instructions.](https://trailhead.salesforce.com)

---

## What Is a Lightning App?

An app is a collection of items that work together to serve a particular function. In Lightning Experience, Lightning apps give your users access to sets of objects, tabs, and other items all in one convenient bundle in the navigation bar.

Lightning apps let you brand your apps with a custom color and logo. You can even include a utility bar and Lightning page tabs in your Lightning app. Members of your org can work more efficiently by easily switching between apps. What’s most important to sales reps? Accounts, events, and organizations. How about sales managers? Reports and dashboards make the top of the list.

Let’s jump into the details.

Each Lightning app has a navigation bar at the top of the page, letting your users:

- Find what they need using item names for easy recognition
- Complete actions and access recent records and lists with a single click
- Personalize the navigation bar to suit the unique way they work

Think of the navigation bar as a container for a set of items and functionality. It’s always there, but the items within it change based on the app you’re using.

### Lightning Navigation

- The app name (1) displays on the left side of the navigation bar and custom colors and branding make each app unique and easy to identify.
- Your users can access other items and apps by clicking the App Launcher icon (2).
- Your users can create records and access recent records and lists directly from the navigation bar (3) for items like Opportunities.

So what things can you put in a Lightning app?

- Most standard objects, including Home, the main Chatter feed, Groups, and People
- Your org’s custom objects
- Visualforce tabs
- Lightning component tabs
- Canvas apps via Visualforce tabs
- Web tabs

You can even include Lightning page tabs and utilities like Lightning Voice. If your org uses utility features, you can enable a utility bar in your app that allows instant access to productivity tools, like integrated voice, in the Lightning Experience footer.

You can also build your own on-demand apps by grouping items into new custom apps.

To switch between apps, users can use the App Launcher icon. This makes it easy for users to switch contexts and still have access to the items, objects, and pages they need most.

---

## Meet the Lightning Experience App Manager

The App Manager in Setup is your go-to place for managing apps for Lightning Experience. It shows all your connected apps and Salesforce apps.

Use the App Manager in Lightning Experience to:

- View all your Salesforce apps.
- Create Lightning apps or connected apps.
- See which apps are visible in Lightning Experience.
- Easily manage apps.

> **Note:** Click a column header to sort the list based on that column.

---

## What’s the Visible in Lightning Column About?

You can see in the App Manager that there are two types of apps: Classic and Lightning. A checkmark in the Visible in Lightning Experience column means that the app is accessible in Lightning Experience via the App Launcher and is fully functional.

Classic apps that don’t have a check mark in the Visible in Lightning column are enabled only for our Salesforce Classic UI. Because you’re working in Lightning Experience, you won’t find those Classic-only apps in the App Launcher. Classic apps marked as visible in Lightning Experience are fully usable in Lightning Experience, but they don’t take advantage of the app enhancements that Lightning Experience offers.

---

## Create a Lightning App

Creating and editing a Lightning app is easy. As Ursa Major Solar’s admin, Maria needs an app that puts everything about customer energy assessments at her consultants’ fingertips. Let’s dive right in and try it out. In a few simple steps, you can give an app a name, set its primary color, upload a logo, specify which items appear in the app’s navigation bar, and assign the app to user profiles.

1. From the Home tab in Setup, enter `App` in the Quick Find box, then select **App Manager**.
2. Click **New Lightning App**. Walk through the Lightning App Wizard, creating an app with these parameters.
   - App Name: `Energy Consultations`
   - Description: `Track energy audits and product recommendations.`
   - Image: Your choice! Use a JPG, PNG, BMP, or GIF image that’s smaller than 5 MB. For best results, upload an image that’s 128 by 128 pixels. Images larger than the maximum display of 128 by 128 pixels are automatically resized.
   - Primary Hex Color Value: `#FA8B05`
   - Org Theme Options: Select the checkbox.
   - App Options and Utility Items: Leave as is.
   - Navigation Items: Add these items in this order: `Home`, `Chatter`, `Groups`, `Energy Audits`, `Accounts`, `Contacts`, `Products`, `Tasks`
   - If there are multiple Home tabs in the Available Items list, choose the one with the red icon.
   - Assigned to user profile: `System Administrator`. Maria would assign it to her consultants’ user profile, but for our purposes, it’s easier to test if we set it to System Administrator.
3. Click **Save and Finish** to exit the wizard.
4. From the App Launcher icon, find and select **Energy Consultations**.
5. Check out the new app! It’s got all the custom branding you gave it: a custom icon in the upper left and the custom color you assigned to it. Because Home is first in the navigation bar, it becomes the first page your users see when they open the app.

```bash
# Deploys the Energy_Consultations CustomApplication metadata, custom tab, and profile application visibility atomically to trailhead-playground org
mkdir -p force-app/main/default/applications # Creates destination directory for CustomApplication metadata files

cat << 'EOF' > force-app/main/default/applications/Energy_Consultations.app-meta.xml # Generates application metadata XML file
<?xml version="1.0" encoding="UTF-8"?> <!-- XML declaration specifies UTF-8 encoding -->
<CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata"> <!-- Metadata API root element for custom applications -->
    <brand> <!-- Container for custom app branding configurations -->
        <headerColor>#FA8B05</headerColor> <!-- Primary brand hex color value (Warm Orange) -->
        <shouldOverrideOrgTheme>false</shouldOverrideOrgTheme> <!-- Flag indicating whether to override org theme -->
    </brand> <!-- End of branding container -->
    <description>Track energy audits and product recommendations.</description> <!-- Descriptive summary of app purpose -->
    <formFactors>Small</formFactors> <!-- Enables app accessibility on mobile form factor -->
    <formFactors>Large</formFactors> <!-- Enables app accessibility on desktop form factor -->
    <isNavAutoTempTabsDisabled>false</isNavAutoTempTabsDisabled> <!-- Allows temporary tabs during user navigation -->
    <isNavPersonalizationDisabled>false</isNavPersonalizationDisabled> <!-- Allows end users to personalize navigation bar -->
    <isNavTabPersistenceDisabled>false</isNavTabPersistenceDisabled> <!-- Retains tab navigation persistence across sessions -->
    <label>Energy Consultations</label> <!-- User-facing application label in App Launcher -->
    <navType>Standard</navType> <!-- Specifies standard navigation mode instead of console mode -->
    <tabs>standard-home</tabs> <!-- Navigation item 1: Standard Home tab -->
    <tabs>standard-Feed</tabs> <!-- Navigation item 2: Standard Chatter Feed tab (standard-Feed in Metadata API) -->
    <tabs>standard-CollaborationGroup</tabs> <!-- Navigation item 3: Standard Groups tab -->
    <tabs>Energy_Audit__c</tabs> <!-- Navigation item 4: Custom Energy Audit object tab -->
    <tabs>standard-Account</tabs> <!-- Navigation item 5: Standard Accounts object tab -->
    <tabs>standard-Contact</tabs> <!-- Navigation item 6: Standard Contacts object tab -->
    <tabs>standard-Product2</tabs> <!-- Navigation item 7: Standard Products object tab -->
    <tabs>standard-Task</tabs> <!-- Navigation item 8: Standard Tasks object tab -->
    <uiType>Lightning</uiType> <!-- Configures application natively for Lightning Experience -->
</CustomApplication> <!-- End of CustomApplication definition -->
EOF <!-- End of heredoc content -->

sed -i '/<\/Profile>/i \    <applicationVisibilities>\n        <application>Energy_Consultations</application>\n        <default>false</default>\n        <visible>true</visible>\n    </applicationVisibilities>' force-app/main/default/profiles/Admin.profile-meta.xml # Appends application visibility grant to System Administrator profile

CMD="sf project deploy start -d force-app/main/default/applications/Energy_Consultations.app-meta.xml -d force-app/main/default/tabs -d force-app/main/default/profiles/Admin.profile-meta.xml -o trailhead-playground --json" # Assigns deployment command to CMD variable for structured log recording
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_2_GUIDED_DEPLOY_APP.json # Executes deployment and logs JSON command output
```

```bash
# Queries Tooling API for CustomApplication metadata to verify Energy_Consultations app attributes landed in the target org
CMD="sf data query -o trailhead-playground --use-tooling-api -q \"SELECT DeveloperName, Label, Description, UiType, NavType FROM CustomApplication WHERE DeveloperName = 'Energy_Consultations'\" --json" # Assigns SOQL query command targeting Tooling API CustomApplication entity to CMD variable
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_2_VERIFICATION_AUDIT.json # Executes Tooling API verification query and logs output to JSON file
```

#### Expected Tooling API Output (`--json`):

```json
{
  "status": 0,
  "result": {
    "records": [
      {
        "DeveloperName": "Energy_Consultations",
        "Label": "Energy Consultations",
        "Description": "Track energy audits and product recommendations.",
        "UiType": "Lightning",
        "NavType": "Standard"
      }
    ],
    "totalSize": 1,
    "done": true
  }
}
```

Nice work! Now you’re ready to create your own custom Lightning apps.

> **Note:** Did you know that app images for Lightning apps can be animated GIFs? Oh yes, they can. You're welcome.

---

## Tips for Creating Apps in Lightning Experience

It’s time for the fun part: deciding how to set up Lightning apps for your users. Here are some tips for planning Lightning apps for your org.

Talk to your users. Ask them what their priorities are. Customizing tabs in apps gives you a unique opportunity to engage with your users. Each group of users has its own priorities. Find out which objects and items represent their highest priorities.

- Ask users to post feedback to a Chatter group.
- Publish polls.
- Schedule lunch sessions. Everyone likes a free lunch, and nearly everybody is happy to express their opinion.

Create a master list of objects that everyone in your org wants. Then trim down the list for each group—sales reps, sales managers, execs, and so on. The menus for every user group share some common objects, like Home, Tasks, and Feed. Keep the high-priority items for each group at the top. Put low-priority items at the bottom, or remove them altogether. Users can always go to the App Launcher to get the items they use less often.

---

## Resources

- [Salesforce Help: Salesforce App Considerations](https://help.salesforce.com/s/articleView?id=sf.apps_lex_considerations.htm&type=5)
- [Salesforce Help: Personalized Navigation Considerations](https://help.salesforce.com/s/articleView?id=sf.user_user_nav_considerations.htm&type=5)
- [Metadata API Reference: CustomApplication](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_customapplication.htm)

---

## Hands-On Challenge

### Retake Quiz

This round is just for practice—you won’t earn more points or change your completion date. Now test your knowledge!

#### 1. What's a key benefit (or benefits) of Lightning apps for your users?

- [ ] A. Users can create records and access recent records and lists directly from the navigation bar.
- [ ] B. It's easy to switch contexts with the App Launcher.
- [ ] C. Lightning apps give users access to the items, objects, and pages they need most.
- [x] D. All of the above

#### 2. What can you include in a Lightning app?

- [ ] A. Unique scents that get released when a user clicks a button
- [ ] B. Custom sound effects and flashing text
- [x] C. Web tabs, standard and custom objects, and utility features like Lightning Voice
- [ ] D. All of the above

#### 3. What's a good way to optimize an app for your users?

- [ ] A. Brand the app with an animated GIF and neon colors to get their attention.
- [x] B. Put the highest priority objects and tabs first in the navigation menu.
- [ ] C. Have a developer code in a sad trombone sound effect that plays for every error message.
- [ ] D. Add every object in the org to the navigation menu.

---

## Technical Post-Mortem & Engineering Learnings

- **Trail:** Developer Beginner
- **Badge 05:** Lightning Experience Customization
- **Unit 2:** Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)

### Key Engineering Hiccups & Solutions Encountered

1. **Lightning App Navigation Tab Identifier Discrepancy (`standard-Chatter` vs `standard-Feed`):**
   - **Hiccup:** Trailhead instructions specify adding `Chatter` to navigation tabs. Using `<tabs>standard-Chatter</tabs>` in `CustomApplication` XML metadata caused deployment to fail with `Tab standard-Chatter can't be added to Lightning app Energy_Consultations because it's not supported in Lightning apps`.
   - **Resolution:** In Salesforce Metadata API for `uiType: Lightning`, the standard Chatter feed tab identifier is `<tabs>standard-Feed</tabs>`, whereas `standard-Chatter` refers to the legacy Salesforce Classic Chatter tab. Updated metadata schema to `<tabs>standard-Feed</tabs>`, resolving deployment error `0AfdL00000durUbSAI`.
