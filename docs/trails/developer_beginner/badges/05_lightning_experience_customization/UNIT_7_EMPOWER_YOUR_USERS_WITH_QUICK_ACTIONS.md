# Trailhead Unit: Empower Your Users with Quick Actions

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 7:** Empower Your Users with Quick Actions  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_actions?trail_id=force_com_dev_beginner)

---

## Learning Objectives

After completing this unit, you’ll be able to:

- Describe how actions help your users.
- Describe the difference between object-specific and global actions.
- Create an action and add it to a page layout.

> **Note:**
> **Accessibility**
>
> This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click the link below:
>
> [Open Trailhead screen reader instructions.](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_actions?trail_id=force_com_dev_beginner#)

---

## Quick Actions

You know the saying that you should judge someone only by their actions? That’s true in Salesforce, and your users will judge you favorably when you give them access to awesome customized actions.

Actions let your users quickly do tasks, such as create records, log calls, send emails, and more. With custom actions, you can make your users’ navigation and workflow as smooth as possible by giving them quick access to information that’s most important.

> **Note:**
> When thinking about what actions you might want to create, ask your users what they really wish they could do. For example, you might create an Emergency Order action for your food service company that allows delivery drivers to immediately order extra or missing food items. Creating actions that your users need can drive adoption in your organization and make you a hero to your users!

In previous units, we glossed over the actions sections of the object page layout. This unit is where we explore those areas of the page layout and give you a taste of how actions can enhance your users’ Salesforce experience.

Quick actions come in two different flavors.

### Object-specific Actions

Object-specific actions have automatic relationships to other records and let users quickly create or update records, log calls, send emails, and more, in the context of a particular object. For example, you add an object-specific action on the Account object that creates contacts. If a user creates a contact with that action on the detail page for the Acme account, that new contact is associated with Acme. Object-specific actions live on the page layout for the object.

There are several types of object-specific actions.

- **"Create" actions** create records that are automatically associated with related records.
- **"Update a Record" actions** make it easy for users to edit records. You can define the fields that are available for update.
- **"Log a Call" actions** let users enter notes about calls, meetings, or other interactions that are related to a specific record.
- **Custom actions** invoke Lightning components, flows, Visualforce pages, or canvas apps that let users interact with or create records that have a relationship to an object record. If you’re new to Visualforce, don’t worry. You can learn all about it in another module. For now, remember that Visualforce pages allow you to do really cool customizations in your actions.
- **"Send Email" actions**, available only on cases, give users access to a simplified version of the Case Feed Email action in the Salesforce mobile app. You can use the case-specific Send Email action in Salesforce Classic, Lightning Experience, and the Salesforce mobile app.

### Global Actions

You create global actions in a different place in Setup than you create object-specific actions. They’re called global actions because they can be put anywhere actions are supported. Use global actions to let users log call details, create records, or send email, all without leaving the page they’re on.

Global actions live on a special layout of their own, known as the global publisher layout. It isn’t associated with an object, and it populates the global actions menu in Lightning Experience. Users can access the global actions menu by clicking Global Actions menu icon in the Salesforce header.

If an object page layout isn’t customized with actions, then the actions on those object record pages are inherited from the global publisher layout.

There are more types of actions than just these two, but some of them aren’t customizable. We’re going to explore only object-specific and global actions in this unit.

> **Note:**
> You might see actions referred to as “quick actions” in Salesforce. It’s true, they’re quick and your users will love them. The quick part is just a category and means that the action is either object-specific or global and not some other kind of Salesforce action.

---

## Create an Object-Specific Action

Maria wants to give her users an easy way to create energy audit records. She’s going to create an object-specific action that lets her users create energy audits right from account records. Because it’s an object-specific action, the new audit records will be directly tied to the accounts they’re created from.

There are already some actions in the highlights panel on energy audit records. Those are default actions, inherited from the default global publisher layout. Maria’s going to create her new object-specific action, add it to the Account page layout, and then customize the actions that users see on account records.

1. From Setup, click **Object Manager**, then click **Account**.
2. Click **Buttons, Links, and Actions**, then click **New Action**.
3. Maria wants this action to create audit records, so select the **Create a Record** action type.
4. Select **Energy Audit** as the target object. This is the type of record that the action creates.
5. Enter the action label as `New Energy Audit`. This is the text users see for the action.
6. Click **Save**.

After you create the action, you can customize its layout using the action layout editor. It’s like the page layout editor but for actions. With the action layout editor, you can customize the fields the users must populate to complete the action.

Just like the page layout editor, the upper part of the action layout editor contains a palette, and below it is the action layout. The palette contains fields from the action’s target object that you can add to the action layout.

### Action Layout Editor

Each field on this action layout has a red asterisk, indicating that it’s a required field. Required fields are added to an action layout by default when you create the action. If you remove a required field from an action layout, then users can’t successfully complete the action. In this case, that means that users wouldn’t be able to create the energy audit record.

Audit Notes and Type of Installation are fields that could be populated after the audit record is created. So let’s leave this as-is and move on to the next step: making the action available to users.

---

## Add an Object-Specific Action to a Page Layout

To make the New Energy Audit action available to users from an account record, Maria must add the action to the Account page layout.

1. Click **Page Layouts**.
2. Click **Account Layout**.
   There are two action sections on a page layout. The “Quick Actions in the Salesforce Classic Publisher” section controls which actions appear on record pages in the Salesforce Classic UI. The “Salesforce Mobile and Lightning Experience Actions” section controls which actions appear on record pages in both Lightning Experience and in the Salesforce mobile app. If you don’t customize the action sections of a page layout, then the actions you see in the Salesforce app and in Lightning Experience come from a set of default actions defined by Salesforce.
3. In the “Salesforce Mobile and Lightning Experience Actions” section, click **override global publisher layout** to override the defaults.
   The actions you see when you override the defaults are a combination of the default actions for the object, plus any custom and standard buttons on the page layout. When the “Salesforce Mobile and Lightning Experience Actions” section isn’t customized, the Lightning page for the object takes the custom and standard buttons from their respective button sections on the layout to display on the page. However, once you override the defaults, any standard and custom buttons you want to appear on your Lightning page must be included in the “Salesforce Mobile and Lightning Experience Actions” section as actions.
4. Select **Mobile & Lightning Actions** in the palette and then drag the **New Energy Audit** action to the “Salesforce Mobile and Lightning Experience Actions” section.

### Adding an Action

You can adjust the order of the actions by dragging them around.

5. Let’s do a bit of cleanup. Drag these actions off the layout and back to the palette.
   - Thanks
   - Question
   - Sharing
   - Change Record Type
   - Get Contacts
   - Check for New Data
   - View Partner Scorecard
6. Click **Save**.

```bash
# Deploys the object-specific QuickAction New_Energy_Audit on Account object and updates Account-Account Layout to surface the action
mkdir -p force-app/main/default/objects/Account/quickActions # Creates directory for Account object-specific quick actions

cat << 'EOF' > force-app/main/default/objects/Account/quickActions/New_Energy_Audit.quickAction-meta.xml # Writes QuickAction XML metadata definition
<?xml version="1.0" encoding="UTF-8"?>
<!-- Object-specific Quick Action metadata definition for Account -->
<QuickAction xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>New Energy Audit</label> <!-- UI label for action displayed to users -->
    <optionsCreateFeedItem>true</optionsCreateFeedItem> <!-- Option to create a feed item upon record creation -->
    <quickActionLayout> <!-- Layout configuration for the Quick Action modal dialog -->
        <quickActionLayoutColumns> <!-- Column layout container for quick action fields -->
            <quickActionLayoutItems> <!-- First layout field item -->
                <emptySpace>false</emptySpace> <!-- Indicates field slot is populated -->
                <field>Name</field> <!-- Energy Audit Name input field -->
                <uiBehavior>Required</uiBehavior> <!-- Marks Name field as required in modal -->
            </quickActionLayoutItems>
            <quickActionLayoutItems> <!-- Second layout field item -->
                <emptySpace>false</emptySpace> <!-- Indicates field slot is populated -->
                <field>Account__c</field> <!-- Parent Account lookup field -->
                <uiBehavior>Required</uiBehavior> <!-- Marks Account lookup as required in modal -->
            </quickActionLayoutItems>
        </quickActionLayoutColumns>
    </quickActionLayout>
    <targetObject>Energy_Audit__c</targetObject> <!-- Target sObject type created by this quick action -->
    <targetFieldName>Account__c</targetFieldName> <!-- Field linking new Energy Audit to current Account record -->
    <type>Create</type> <!-- Action type set to Create record -->
</QuickAction>
EOF

CMD="sf project deploy start -d force-app/main/default/objects/Account/quickActions -d force-app/main/default/layouts/Account-Account\ Layout.layout-meta.xml -o trailhead-playground --json" # Sets CLI deployment command
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_7_GUIDED_DEPLOY_AUDIT_1.json # Executes deployment and logs command and output to JSON audit log
```

```bash
# Verifies the New_Energy_Audit quick action deployment on Account via Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, DeveloperName, MasterLabel, TargetSobjectType, Type FROM QuickActionDefinition WHERE DeveloperName = 'Account.New_Energy_Audit' OR DeveloperName = 'New_Energy_Audit'\" -o trailhead-playground --json" # Sets Tooling API query command for QuickActionDefinition
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_7_GUIDED_VERIFICATION_AUDIT_1.json # Executes Tooling API verification query and logs output to JSON log
```

Excellent! Now Maria’s users can easily create an energy audit record that’s automatically associated with an account. Her users will see the new action on the page-level action menu. Let’s take a look.

The actions in the action menu are shown in the order that they’re listed on the page layout. For example, this page layout with the New Energy Audit action …

### Action List

Looks like this on the account record …

### Actions

> **Note:**
> Although they’re actions, Email, Log a Call, New Event, and New Task don’t show up here. Because they’re associated with activities, they appear under the Activity tab. Standard Chatter actions like Post and Poll show up under the Chatter tab.

---

## Create a Global Action

The Sales team has asked Maria to create an action that lets users create a campaign no matter where they are in Salesforce. A global action is an ideal way to do this, because the global actions menu appears at the top of every page.

Creating a global action looks a lot like creating an object-specific action except you start on a different page in Setup.

1. From Setup, click the **Home** tab.
2. Enter `Global Actions` in the Quick Find box and click **Global Actions**.
3. Click **New Action**.
4. Select **Create a Record** for the action type.
5. Select **Campaign** for the target object.
6. Enter `New Campaign` as the label for the action.

### Create a New Campaign action

7. Click **Save**.
8. On the action layout, remove the Parent Campaign field and add the Expected Revenue in Campaign and Campaign Owner fields.

### New Campaign action layout

9. Click **Save**.

---

## Add a Global Action to the Global Actions Menu

As we mentioned earlier in the unit, global actions live on a special layout of their own, known as the global publisher layout. The global publisher layout populates the global actions menu.

Adding an action to the global actions menu is a lot like adding an action to a record page. You simply drag an action from the palette onto the global publisher layout.

1. From Setup, click the **Home** tab.
2. Enter `Publisher` in the Quick Find box and click **Publisher Layouts**.
3. Click **Edit** next to Global Layout.
4. If the “Salesforce Mobile and Lightning Experience Actions” section isn’t customized, click **override global publisher layout** to override it.
5. Click the **Mobile & Lightning Actions** category in the palette.
6. Drag **New Campaign** from the palette into the Salesforce Mobile and Lightning Experience Actions section.
7. Save the layout.

```bash
# Deploys global QuickAction New_Campaign and updates Global Publisher Layout to make action accessible across org
mkdir -p force-app/main/default/quickActions # Creates directory for global quick action metadata definitions

cat << 'EOF' > force-app/main/default/quickActions/New_Campaign.quickAction-meta.xml # Writes global QuickAction XML metadata file
<?xml version="1.0" encoding="UTF-8"?>
<!-- Global Quick Action metadata definition for creating Campaign records -->
<QuickAction xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>New Campaign</label> <!-- UI label for action displayed in global actions header menu -->
    <optionsCreateFeedItem>true</optionsCreateFeedItem> <!-- Option to post feed item when campaign is created -->
    <quickActionLayout> <!-- Layout configuration for the global action modal dialog -->
        <quickActionLayoutColumns> <!-- First layout column containing key campaign fields -->
            <quickActionLayoutItems> <!-- Campaign Name layout item -->
                <emptySpace>false</emptySpace> <!-- Indicates field slot is populated -->
                <field>Name</field> <!-- Campaign Name input field -->
                <uiBehavior>Required</uiBehavior> <!-- Marks Campaign Name as required in modal dialog -->
            </quickActionLayoutItems>
            <quickActionLayoutItems> <!-- Campaign Owner layout item -->
                <emptySpace>false</emptySpace> <!-- Indicates field slot is populated -->
                <field>OwnerId</field> <!-- Campaign Owner lookup field -->
                <uiBehavior>Edit</uiBehavior> <!-- Allows editing Campaign Owner -->
            </quickActionLayoutItems>
        </quickActionLayoutColumns>
        <quickActionLayoutColumns> <!-- Second layout column for financial metric fields -->
            <quickActionLayoutItems> <!-- Expected Revenue layout item -->
                <emptySpace>false</emptySpace> <!-- Indicates field slot is populated -->
                <field>ExpectedRevenue</field> <!-- Expected Revenue currency input field -->
                <uiBehavior>Edit</uiBehavior> <!-- Allows editing Expected Revenue -->
            </quickActionLayoutItems>
        </quickActionLayoutColumns>
    </quickActionLayout>
    <targetObject>Campaign</targetObject> <!-- Target sObject type created by this global action -->
    <type>Create</type> <!-- Action type set to Create record -->
</QuickAction>
EOF

CMD="sf project deploy start -d force-app/main/default/quickActions -d force-app/main/default/layouts/Global-Global\ Layout.layout-meta.xml -o trailhead-playground --json" # Sets CLI deployment command for global quick action and global layout
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_7_GUIDED_DEPLOY_AUDIT_2.json # Executes deployment and logs command and JSON result
```

```bash
# Verifies the global New_Campaign quick action deployment via Tooling API query
CMD="sf data query --use-tooling-api -q \"SELECT Id, DeveloperName, MasterLabel, TargetSobjectType, Type FROM QuickActionDefinition WHERE DeveloperName = 'New_Campaign'\" -o trailhead-playground --json" # Sets Tooling API query command for global quick action
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/05_lightning_experience_customization/logs/UNIT_7_GUIDED_VERIFICATION_AUDIT_2.json # Executes query and writes output to JSON log file
```

8. Refresh the browser, then click global actions menu icon to check out the global actions menu.

### Global actions menu

There’s the New Campaign action. Nice work! Now anyone at Ursa Major Solar can create a new campaign from anywhere in Salesforce.

---

## Resources

- [Salesforce Help: Quick Actions](https://help.salesforce.com/articleView?id=sf.actions_overview.htm)
- [Salesforce Help: Action Types](https://help.salesforce.com/articleView?id=sf.action_types.htm)
- [Salesforce Help: Actions in Lightning Experience](https://help.salesforce.com/articleView?id=sf.actions_in_lex.htm)
- [Salesforce Help: How Actions Are Ordered in Lightning Experience](https://help.salesforce.com/articleView?id=sf.actions_order_in_lex.htm)

---

## Quiz

To complete this unit, you need to answer all the quiz questions correctly.

**+100 Points**

### 1. How do custom actions help your users?

- **A.** By allowing them to create custom objects
- **B.** By giving them more ways to view and edit records
- **C.** By making it fast and easy to interact with information in your org
- **D.** A and B
- **E.** B and C

### 2. What’s the main difference between object-specific actions and global actions?

- **A.** Object-specific actions have automatic relationships to other records, and global actions don't.
- **B.** Global actions perform actions outside of Salesforce, and object-specific actions only perform actions inside Salesforce.
- **C.** Object-specific actions perform actions only on specific objects.
- **D.** You can use object-specific actions wherever actions are supported in Salesforce.

---

## Technical Post-Mortem & Engineering Learnings

1. **Object-Specific vs Global Quick Action Metadata Packaging:**
   - **Hiccup:** Object-specific quick actions reside within the `objects/<ObjectName>/quickActions/` subfolder (e.g., `force-app/main/default/objects/Account/quickActions/New_Energy_Audit.quickAction-meta.xml`), whereas global quick actions are stored directly under the top-level `quickActions/` directory (e.g., `force-app/main/default/quickActions/New_Campaign.quickAction-meta.xml`).
   - **Resolution:** Ensured proper directory structure separation for object-specific vs. global metadata boundaries before invoking `sf project deploy start`.

2. **Tooling API QuickActionDefinition Query Namespace:**
   - **Hiccup:** Querying `QuickActionDefinition` for object-specific quick actions requires qualification via `<ObjectName>.<ActionName>` (e.g., `Account.New_Energy_Audit`) in SOQL `DeveloperName` filters, while global actions use the unqualified `DeveloperName` (`New_Campaign`).
   - **Resolution:** Formulated the Tooling API SOQL query with `DeveloperName IN ('Account.New_Energy_Audit', 'New_Energy_Audit')` to ensure robust verification across both namespace formats.
