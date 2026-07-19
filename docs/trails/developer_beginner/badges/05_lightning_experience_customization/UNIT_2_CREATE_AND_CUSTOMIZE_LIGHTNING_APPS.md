# Trailhead Unit: Create and Customize Lightning Apps (Agentforce 360 Platform Apps)

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 2:** Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_apps?trail_id=force_com_dev_beginner)

---

## Introduction & Learning Objectives

An app is a collection of items that work together to serve a particular function. In Lightning Experience, Lightning apps give users access to sets of objects, tabs, and other items all in one convenient bundle accessible from the top navigation bar and App Launcher.

After completing this unit, you’ll be able to:

- Describe the benefits of Lightning apps and custom navigation.
- Create and configure a Lightning app with custom branding and ordered navigation items.
- List two best practices for planning and organizing Lightning apps across different user groups in your org.

---

## Conceptual Architecture: What Is a Lightning App?

Each Lightning app features a **Navigation Bar** at the top of the page that acts as a container for items and functionality. While the navigation bar container is always present, the items within it change dynamically based on the active app.

### Key Capabilities of the Navigation Bar

1. **App Identity & Branding:** Displays the custom app name, logo, and primary brand color on the far left of the navigation bar (`headerColor`).
2. **App Launcher Access:** Users can discover and switch between connected apps, Lightning apps, and Classic apps with a single click on the 9-dot **App Launcher** icon (`App Launcher`).
3. **Item Navigation & Action Menus:** Provides instant access to standard objects (Home, Chatter, Groups), custom objects (`Energy_Audit__c`), Visualforce tabs, Lightning component tabs, and web tabs. Users can create records and access recent lists directly from item dropdown menus.
4. **Utility Bar Integration:** If enabled, the utility bar provides persistent footer access to common productivity tools across all app pages (e.g., integrated voice, notes, flow runners).

---

## Meet the Lightning Experience App Manager

The **App Manager** in Setup (`Setup | App Manager`) is the centralized console for managing all connected and Salesforce apps within the org.

### Visible in Lightning Column Explained

- **Lightning Apps (`UiType: Lightning`):** Designed natively for Lightning Experience with custom branding, utility bars, and enhanced navigation. Always checked in the _Visible in Lightning_ column.
- **Classic Apps Marked Visible:** Classic apps (`UiType: SalesforceClassic`) that have a checkmark in the _Visible in Lightning_ column are accessible and usable via the App Launcher in Lightning Experience, but they do not support advanced features like utility bars or custom branding colors.
- **Classic-Only Apps:** Classic apps without a checkmark are restricted to the legacy Salesforce Classic UI and are hidden from the Lightning App Launcher.

---

## Best Practices for Planning Lightning Apps

When designing custom apps for different business units across your org, follow these core planning principles:

1. **Conduct User Priority Assessments:** Engage directly with end users through Chatter feedback groups, polls, and discovery sessions to identify high-priority objects for each job role (e.g., Sales Reps prioritize Accounts and Opportunities, while Sales Managers prioritize Reports and Dashboards).
2. **Create and Prune a Master Object List:** Assemble a comprehensive list of all required objects org-wide, then tailor and prune the navigation items for each specific user profile:
   - Keep shared essentials (`Home`, `Tasks`, `Chatter`) across all apps.
   - Position high-priority items at the top/front of the navigation bar.
   - Remove low-priority items entirely (users can still access secondary items on-demand via the App Launcher).

---

## Guided Activities (Consolidated Requirements & Solutions)

### `[REQ-5.2.G1]` Create a Custom Lightning App (`Energy_Consultations`)

As Ursa Major Solar's administrator, Maria Jimenez needs an app that consolidates customer energy assessments and audit tools into a single navigation bundle for her energy consultants.

#### Requirement Specifications

- **Target Application Developer Name:** `Energy_Consultations`
- **Application Label:** `Energy Consultations`
- **Description:** `Track energy audits and product recommendations.`
- **Brand Primary Hex Color:** `#FA8B05` (Warm Orange)
- **Org Theme Options:** Override / use org theme (`shouldOverrideOrgTheme: false`)
- **Navigation Items (Exact Order):**
  1. `standard-home` (Home tab)
  2. `standard-Chatter` (Chatter feed)
  3. `standard-CollaborationGroup` (Groups)
  4. `Energy_Audit__c` (Custom Energy Audit object tab created in Unit 1)
  5. `standard-Account` (Accounts)
  6. `standard-Contact` (Contacts)
  7. `standard-Product2` (Products)
  8. `standard-Task` (Tasks)
- **Assigned Profile Visibility:** `System Administrator` (`Admin`)

---

### Step 1: Generate `CustomApplication` Metadata XML

Instead of manually clicking through the Lightning App Wizard in Setup, we generate the exact declarative `CustomApplication` schema metadata on our local feature branch:

```bash
mkdir -p force-app/main/default/applications

cat << 'EOF' > force-app/main/default/applications/Energy_Consultations.app-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">
    <brand>
        <headerColor>#FA8B05</headerColor>
        <shouldOverrideOrgTheme>false</shouldOverrideOrgTheme>
    </brand>
    <description>Track energy audits and product recommendations.</description>
    <formFactors>Small</formFactors>
    <formFactors>Large</formFactors>
    <isNavAutoTempTabsDisabled>false</isNavAutoTempTabsDisabled>
    <isNavPersonalizationDisabled>false</isNavPersonalizationDisabled>
    <isNavTabPersistenceDisabled>false</isNavTabPersistenceDisabled>
    <label>Energy Consultations</label>
    <navType>Standard</navType>
    <tabs>standard-home</tabs>
    <tabs>standard-Chatter</tabs>
    <tabs>standard-CollaborationGroup</tabs>
    <tabs>Energy_Audit__c</tabs>
    <tabs>standard-Account</tabs>
    <tabs>standard-Contact</tabs>
    <tabs>standard-Product2</tabs>
    <tabs>standard-Task</tabs>
    <uiType>Lightning</uiType>
</CustomApplication>
EOF
```

---

### Step 2: Provision Profile Application Visibility (`Admin`)

In accordance with **Rule 1.2 (Atomic Schema & Security Deployments)**, applications deployed without explicit profile visibility remain hidden from the App Launcher. We use non-interactive stream editing (`sed`) to append application visibility directly into `Admin.profile-meta.xml`:

```bash
sed -i '/<\/Profile>/i \    <applicationVisibilities>\n        <application>Energy_Consultations</application>\n        <default>false</default>\n        <visible>true</visible>\n    </applicationVisibilities>' force-app/main/default/profiles/Admin.profile-meta.xml
```

---

### Step 3: Atomic Deployment to Salesforce Cloud

Deploy the application definitions, custom tabs, and profile permissions atomically using the SFDX CLI `--json` protocol:

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

sf project deploy start \
  -d force-app/main/default/applications/Energy_Consultations.app-meta.xml \
  -d force-app/main/default/tabs \
  -d force-app/main/default/profiles/Admin.profile-meta.xml \
  -o trailhead-playground \
  --json | tee "$UNIT_DIR/UNIT_2_GUIDED_DEPLOY_APP.json"
```

---

## Verification Query & Challenge Check

Verify the `CustomApplication` schema definition across the org via the **Tooling API** (`--use-tooling-api`) before testing in the App Launcher:

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT DeveloperName, Label, Description, UiType, NavType FROM CustomApplication WHERE DeveloperName = 'Energy_Consultations'" \
  --json | tee "$UNIT_DIR/UNIT_2_VERIFICATION_AUDIT.json"
```

### Expected Tooling API Output (`--json`):

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

Once verified, open the App Launcher in your Trailhead Playground (`App Launcher | Energy Consultations`) to verify the `#FA8B05` branding and ordered navigation items!

---

## Resources & Reference Documentation

- [Salesforce Help: Salesforce App Considerations](https://help.salesforce.com/s/articleView?id=sf.apps_lex_considerations.htm&type=5)
- [Salesforce Help: Personalized Navigation Considerations](https://help.salesforce.com/s/articleView?id=sf.user_user_nav_considerations.htm&type=5)
- [Metadata API Reference: CustomApplication](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_customapplication.htm)
