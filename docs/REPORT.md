# Trailhead Progress Report

**Date:** July 20, 2026  
**Subject:** Developer Beginner Trailhead Progress & Learnings

---

## Table of Contents

- [Learnings](#learnings)
- [Supplemental Learnings](#supplemental-learnings)
- [Roadblocks](#roadblocks)
- [Unit-Level Engineering Hiccups & Resolutions](#unit-level-engineering-hiccups-resolutions)
  - [Trail: Developer Beginner](#trail-developer-beginner)
    - [Badge 04: Data Modeling](#badge-04-data-modeling)
      - [Unit 2 & 3: Create Custom Objects & Create Object Relationships](#unit-2-3-create-custom-objects-create-object-relationships)
    - [Badge 05: Lightning Experience Customization](#badge-05-lightning-experience-customization)
      - [Unit 1: Set Up Your Org](#unit-1-set-up-your-org)
      - [Unit 2: Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)](#unit-2-create-and-customize-agentforce-360-platform-apps-formerly-lightning-apps)
      - [Unit 3: Create and Customize List Views](#unit-3-create-and-customize-list-views)
      - [Unit 5: Customize Record Page Components and Fields](#unit-5-customize-record-page-components-and-fields)

## Learnings

1. **Enterprise Operations Tracking:** Salesforce is used extensively by businesses to track and manage end-to-end business operations seamlessly within a single unified platform.
2. **Salesforce Paradigm vs. Traditional RDBMS:** Salesforce abstracts standard database concepts into its own business-centric terminology:
   - **Objects & Fields:** Objects represent database tables, Fields represent columns, and Records represent rows.
   - **Primary Keys (`Id`):** Every record is automatically assigned a unique 18-character alphanumeric string (`Id`).
   - **Foreign Keys (Lookup vs. Master-Detail):** Both are Foreign Key columns storing the parent's `Id` under the hood. **Lookup** acts as an optional FK with independent record ownership, while **Master-Detail** acts as a strict `NOT NULL` FK with cascading deletes, parent-inherited security (`ControlledByParent`), and support for real-time **Roll-Up Summary fields** (`SUM`, `COUNT`, `MIN`, `MAX`).
3. **Two-Way Metadata Synchronization (Deploy vs. Retrieve):**
   - **Deploy (`sf project deploy start`):** Pushes local metadata files (Apex, XML, LWC) from VS Code to the Salesforce cloud org so the platform registers the changes.
   - **Retrieve (`sf project retrieve start`):** The Salesforce term for "pulling" GUI changes; downloads metadata created or modified in the web Setup UI back into local VS Code files for Git version control.

   ```text
          [ VS CODE / GIT REPO ]
            (Local Source Files)
             │              ▲
             │              │
       sf project      sf project
      deploy start    retrieve start
      (Push Code)     (Pull Metadata)
             │              │
             ▼              │
          [ SALESFORCE CLOUD ORG ]
            (Web GUI / Sandbox)
   ```

4. **Atomic Schema & FLS Provisioning (The "Ghost Field" Anti-Pattern):**
   - **Database Schema vs. Visibility Layer:** Creating a `CustomField` XML file physically instantiates the column in Salesforce, BUT Salesforce sets Field-Level Security (FLS) to `invisible/non-editable` by default for all user profiles.
   - **The "Ghost Field" Phenomenon:** Deploying schema without profile `fieldPermissions` produces "ghost fields"—fields that exist in the database but are completely hidden from the GUI, throw `No such column` errors in SOQL queries, and cause Trailhead verification checks to fail.
   - **GUI Parity & CLI Automation:** In the Salesforce Setup GUI, Step 3 of the field creation wizard displays a page of checkboxes that automatically grants FLS visibility to profiles. When working via CLI/source XML, non-interactive Stream Editing (`sed -i '/<\/Profile>/i ...'`) acts as the exact CLI equivalent of checking those GUI visibility boxes.
   - **Mandatory Pattern:** Schema creation (`CustomField`) and Security provisioning (`fieldPermissions`) MUST always be executed as a single atomic unit.
   - **Pattern Recurred as "Ghost Tabs" (Badge 05, Unit 1):** The same root cause — a Setup GUI wizard silently bundling a profile-level permission grant that a raw CLI metadata deploy skips — recurred for `tabVisibilities`, not just `fieldPermissions`. This was flagged as a known risk going into Badge 05 and still wasn't caught until Unit 5, days later, when navigating to the tab for the first time. **Generalized rule:** any component created via CLI that has a corresponding GUI wizard step for per-profile visibility (fields, tabs, record types, apps) needs its profile visibility grant checked explicitly — don't assume the field-specific mitigation covers the whole class of bug. See the Unit 1 hiccup below for the full trace.

5. **The Hybrid SFDX CLI + `--json` Execution Protocol:**
   - **The Sweet Spot:** Combining hands-on SFDX CLI execution with the `--json` output flag provides the ultimate developer hybrid: **100% hands-on CLI learning retention** (mastering flags like `-d`, `-o`, `-q`) paired with **100% deterministic JSON payload traceability** matching MCP protocol auditability standards.

6. **The Roll-Forward Deployment Strategy (No Destructive Rollbacks):**
   - **Enterprise Rule:** Destructive rollbacks in cloud org environments carry severe risks of data loss, foreign key corruption, and component breaking. When deployment errors or missing FLS permissions occur, engineers MUST NOT attempt destructive rollbacks. Always fix the issue in local source code and **roll forward** with a patch deployment.

---

## Supplemental Learnings

1. **Database Architecture & Evolution:** Salesforce patented their multi-tenant database approach in the 2000s (virtualized schemas using universal data tables, custom indexers, and dynamic sharing rules). However, as database technology rapidly advanced, modern relational databases easily handle these concerns natively today (e.g., PostgreSQL using `JSONB` schemas, GIN/Expression indexing, and native Row-Level Security / RLS). For a deeper breakdown, refer to [DEVELOPER_REFERENCE.md](../setup/DEVELOPER_REFERENCE.md).
2. **Cost & Investment:** Salesforce represents a heavy financial investment for organizations. Entry-level pricing starts at **$25 per user/month** for the Starter Suite (billed annually), scaling to **$80/user/month** for Pro Suite, and reaching **$165–$330+ per user/month** for Enterprise and Unlimited editions.

---

## Roadblocks

1. **Out-of-Order Badge Completion & Setup Friction:** Completed the first badge, then unknowingly jumped directly to Badge 3 inside the web Playground without VS Code. Discovering that Badge 2 was skipped (which covered the initial VS Code connection) caused significant confusion and consumed extra time connecting the Trailhead Playground org to VS Code. Additionally, navigating the Salesforce GUI initially presented a steep learning curve, though following the included tutorial videos helped clarify the navigation.
2. **Hardware Limitations & Remote VM Migration:** Local hardware constraints (8 GB RAM) were insufficient to run VS Code alongside developer tooling without performance degradation. To resolve this, development was migrated to a 16 GB Hetzner VM via Remote SSH, which required setting up the development stack from scratch and cost setup time.

---

## Unit-Level Engineering Hiccups & Resolutions

### Trail: Developer Beginner

#### Badge 04: Data Modeling

##### Unit 2 & 3: Create Custom Objects & Create Object Relationships

1. **CLI Deployment vs. GUI Challenge Verification ("Ghost Fields"):**
   - **Context:** `Developer Beginner > Badge 04: Data Modeling > Unit 3: Create Object Relationships`
   - **Hiccup:** Completing activities via the Salesforce CLI (`sf project deploy start`) instead of the point-and-click Setup GUI caused Trailhead challenge checks to fail with misleading "field does not exist" errors. Unlike the Setup UI wizard, CLI metadata deployments do not automatically grant Field-Level Security (FLS) access permissions to user profiles. This created "ghost fields" that existed in the database schema but remained completely invisible to SOQL and Trailhead.
   - **Resolution:** Diagnosed the missing access via Tooling API SOQL queries on `FieldPermissions` and appended explicit `fieldPermissions` into `Admin.profile-meta.xml` before deploying schema and profile metadata atomically:

```bash
# 1. Confirm field exists in the schema via Tooling API
$ sf data query -o trailhead-playground --use-tooling-api -q \
    "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'"

┌──────────────────────┬────────────────────────────┐
│ QUALIFIEDAPINAME     │ DATATYPE                   │
├──────────────────────┼────────────────────────────┤
│ Id                   │ Lookup()                   │
│ Offer_Amount__c      │ Currency(16, 2)            │
│ Target_Close_Date__c │ Date                       │
│ Contact__c           │ Lookup(Contact)            │
│ Property__c          │ Master-Detail(Property)    │
└──────────────────────┴────────────────────────────┘

# 2. Confirm field-level security permissions (Pre-fix: 0 records returned)
$ sf data query -o trailhead-playground -q \
    "SELECT Field, PermissionsRead, PermissionsEdit, Parent.Profile.Name FROM FieldPermissions WHERE SobjectType='Offer__c'"

Total number of records retrieved: 0.

# 3. Stream-edit Admin profile XML to append FLS visibility right before </Profile>
$ sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Offer_Amount__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml

# 4. Deploy object schema and profile metadata atomically
$ sf project deploy start \
    -d force-app/main/default/objects/Offer__c \
    -d force-app/main/default/profiles \
    -o trailhead-playground

Status: Succeeded | 2/2 Components Deployed

# 5. Re-verify permissions (Post-fix: Read/Edit granted to System Administrator)
$ sf data query -o trailhead-playground -q \
    "SELECT Field, PermissionsRead, PermissionsEdit, Parent.Profile.Name FROM FieldPermissions WHERE SobjectType='Offer__c'"

┌─────────────────────────────┬─────────────────┬─────────────────┬──────────────────────┐
│ FIELD                       │ PERMISSIONSREAD │ PERMISSIONSEDIT │ PARENT.PROFILE.NAME  │
├─────────────────────────────┼─────────────────┼─────────────────┼──────────────────────┤
│ Offer__c.Offer_Amount__c    │ true            │ true            │ System Administrator │
│ Offer__c.Target_Close_Date  │ true            │ true            │ System Administrator │
│ Offer__c.Contact__c         │ true            │ true            │ System Administrator │
└─────────────────────────────┴─────────────────┴─────────────────┴──────────────────────┘
```

---

#### Badge 05: Lightning Experience Customization

##### Unit 1: Set Up Your Org

1. **Picklist Value Case Sensitivity (`Duplicate picklist value ground mounted`):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 1: Set Up Your Org`
   - **Hiccup:** Guided activity specified `Ground mounted` (lowercase `m`), whereas the Challenge specified `Ground Mounted` (capital `M`). Including both in `Type_of_Installation__c.field-meta.xml` caused deployment to fail with `Duplicate picklist value ground mounted`.
   - **Resolution:** Salesforce picklist Metadata API definitions are case-insensitive. Standardized value sets to eliminate case-insensitive collisions.

2. **Standard Field Feed Tracking Metadata Schema (`<nameField>`):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 1: Set Up Your Org`
   - **Hiccup:** Feed tracking was enabled on custom fields (`<trackFeedHistory>true</trackFeedHistory>`) and object level (`<enableFeeds>true</enableFeeds>`), but Trailhead challenge check failed on field `Energy Audit Name`.
   - **Resolution:** Standard object name fields are defined inside `<nameField>` in `object-meta.xml`. Placed `<trackFeedHistory>true</trackFeedHistory>` explicitly inside the `<nameField>` block to enable Chatter Feed Tracking on `Name`.

3. **Lookup Foreign Key Binds & CLI Data Command Placeholders (`MALFORMED_ID`):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 1: Set Up Your Org`
   - **Hiccup:** Running `sf data create record -v "Account__c='<Burlington-Account-Id>'"` failed with `MALFORMED_ID` because text placeholders are invalid Salesforce IDs.
   - **Resolution:** Automated CLI scripts by binding Live Account IDs dynamically into bash variables via SOQL + `jq` (`BURLINGTON_ID=$(sf data query ... --json | jq -r '.result.records[0].Id')`).

4. **Terminal Input Buffer Overflows (Paste Truncation):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 1: Set Up Your Org`
   - **Hiccup:** Copy-pasting a 105-line monolithic bash code block into terminal caused line truncation (`ERROR_HTTP_404`), cutting off `cat << 'EOF'` mid-line.
   - **Resolution:** Modularized long CLI code blocks in documentation into paste-safe steps (`Challenge 3.1` and `Challenge 3.2`).

5. **Developer vs. AI Agent Responsibility Boundaries (Rule 4.4):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 1: Set Up Your Org`
   - **Hiccup:** Auto-committing and auto-executing CLI fixes created friction with hands-on learning retention.
   - **Resolution:** Established **Rule 4.4** in `docs/reference/SALESFORCE_DEVELOPMENT_RULES.md`, strictly separating file authoring (AI assistant permitted) from terminal execution and Git shipping (reserved exclusively for developer).

6. **CLI Tab Deployment Skips Profile Visibility Grant (The "Ghost Tab" Anti-Pattern):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 1: Set Up Your Org` (surfaced during Unit 5 execution, days later, while navigating to the tab for the first time)
   - **Hiccup:** The `Energy_Audit__c` custom tab was deployed via raw CLI metadata (`CustomTab.tab-meta.xml`) and correctly wired into the `Energy_Consultations` app's `<tabs>` list in Unit 2, but never appeared in the App Launcher or nav bar. Unlike the Setup GUI's "New Custom Tab" wizard — which has an explicit step granting per-profile tab visibility — the CLI-only deploy skipped that grant entirely, leaving `Admin.profile-meta.xml` with zero `<tabVisibilities>` entries. Same root cause as the Ghost Field anti-pattern (item 4 above), just for tab visibility instead of FLS — and notably, it recurred despite the Ghost Field precedent already being a known watch-item going into this badge.
   - **Resolution:** Added an explicit `tabVisibilities` grant to `Admin.profile-meta.xml` and deployed it in isolation:

```bash
# 1. Confirm zero tabVisibilities entries exist for the Admin profile
$ grep -c "<tabVisibilities>" force-app/main/default/profiles/Admin.profile-meta.xml
0

# 2. Add explicit tab visibility grant to Admin.profile-meta.xml
<tabVisibilities>
    <tab>Energy_Audit__c</tab>
    <visibility>DefaultOn</visibility>
</tabVisibilities>

# 3. Deploy the profile change in isolation
$ sf project deploy start -m "Profile:Admin" -o trailhead-playground --json

Status: Succeeded | 1/1 Components Deployed
```

     After deploying, the **Energy Audits** tab appeared correctly under the **Energy Consultations** app in the nav bar and App Launcher.

##### Unit 2: Create and Customize Agentforce 360 Platform Apps (formerly Lightning Apps)

1. **Lightning App Navigation Tab Identifier Discrepancy (`standard-Chatter` vs `standard-Feed`):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 2: Create and Customize Agentforce 360 Platform Apps`
   - **Hiccup:** Trailhead unit instructions specified adding the `Chatter` tab to navigation items. Defining `<tabs>standard-Chatter</tabs>` in `CustomApplication` XML metadata caused deployment to fail with `Tab standard-Chatter can't be added to Lightning app Energy_Consultations because it's not supported in Lightning apps`.
   - **Resolution:** In Salesforce Metadata API for `uiType: Lightning`, the standard Chatter feed tab identifier is `<tabs>standard-Feed</tabs>`, whereas `standard-Chatter` refers to the legacy Salesforce Classic Chatter tab. Updated metadata schema to `<tabs>standard-Feed</tabs>`, resolving deployment error `0AfdL00000durUbSAI`.

##### Unit 3: Create and Customize List Views

1. **Metadata API vs. Client UI Component Boundaries (List View Charts vs. List Views):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 3: Create and Customize List Views`
   - **Hiccup:** Attempting to query `ListViewChart` via SOQL returned `INVALID_TYPE: sObject type 'ListViewChart' is not supported`.
   - **Resolution:** Clarified component boundaries: Custom List Views (`ListView`) are deployable Metadata API XML files (`.listView-meta.xml`), whereas List View Charts (`Donut Chart`, `Bar Chart`) are interactive client UI widgets configured directly in the Lightning Experience browser toolbar (`📊` icon).

2. **ListView Column API Naming Conventions (`ACCOUNT.PHONE1` & `CustomerPriority__c`):**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 3: Create and Customize List Views`
   - **Hiccup:** Referencing `ACCOUNT.PHONE_NUMBER` or `ACCOUNT.CUSTOMER_PRIORITY` inside `<columns>` blocks in `ListView` metadata XML caused deployment failures (`Could not resolve list view column`).
   - **Resolution:** Standard phone field on Account in Metadata API is `<columns>ACCOUNT.PHONE1</columns>`, and custom fields on Account use exact custom API names (`<columns>CustomerPriority__c</columns>`).

3. **Request-Response Audit JSON Protocol Upgrade:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 3: Create and Customize List Views`
   - **Hiccup:** Raw CLI stdout redirects (`--json | tee`) saved only the Salesforce response payload, leaving no visibility into the original query or input command parameters in audit log files.
   - **Resolution:** Upgraded Unit 3 audit logging code blocks to use `jq` to wrap both `input` (command, targetOrg, query) and `output` (Salesforce response, totalSize, record ID) into unified Request-Response Audit JSON logs (`UNIT_3_GUIDED_LISTVIEW_AUDIT.json` and `UNIT_3_CHALLENGE_VERIFICATION_AUDIT.json`).

##### Unit 5: Customize Record Page Components and Fields

1. **FlexiPage / Dynamic Forms Hand-Authoring Infeasibility:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** Unlike `CompactLayout` or `CustomObject`, `FlexiPage` XML generated by the Dynamic Forms migration wizard and the Activation wizard includes builder-assigned region UUIDs and nested facet structures that Salesforce's own docs steer you away from hand-authoring.
   - **Resolution:** Built via GUI per the Trailhead click-path, then closed out with a retrieve → deploy round trip — the redeployed file, not a hand-written-from-scratch XML block, is the reproducible payload for these requirements.

2. **Missing Local Baseline for Page Layouts:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** `Energy_Audit__c`'s default page layout was auto-created by Salesforce when the object was deployed (Unit 1) but was never retrieved into local source, so its full field/section content wasn't known locally.
   - **Resolution:** Retrieve the current layout first, patch only the `relatedLists` block, then redeploy — avoids blindly reconstructing (and potentially corrupting) a layout whose existing content wasn't fully known.

3. **Field Order Regression Caught by Auditing the Retrieved Output:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** After the `G1` Dynamic Forms build, the retrieved FlexiPage showed `Account__c` listed _before_ `Record.Name` — backwards from the requirement ("Account sits below Energy Audit Name"). Easy to miss without actually reading the retrieved XML.
   - **Resolution:** Since a real, wizard-generated baseline already existed, the two `<itemInstances>` blocks were swapped directly via a targeted hand-edit — safe because it reordered existing sibling elements without introducing any new builder-assigned identifiers.

4. **Files Related List: Two Wrong Values Before the Real One:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** `AttachedContentDocuments` and `RelatedContentDocumentList` both failed deployment with `Cannot find related list:...`. Neither is documented in Salesforce's Metadata API reference, and no existing layout in the org (Account's included) had a working example to copy from.
   - **Resolution:** The real value — `RelatedFileList` — was only discoverable by adding Files via the classic Page Layout GUI editor once, saving, then retrieving to see what Salesforce itself assigned. Full diagnostic writeup: `docs/reference/TROUBLESHOOTING.md`.

5. **Org-Default Activation Cannot Be Deployed via CLI at All — Confirmed, Not Assumed:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** Repeated attempts to find a CLI/metadata path for "Assign as Org Default" record page activation, hoping to avoid the browser entirely.
   - **Resolution:** Verified across three independent Salesforce documentation checks that this is a genuine, permanent platform limitation, not a tooling gap — this one action must always be a browser click. By contrast, **App, Record Type, and Profile** assignment (a different activation mode) _is_ deployable, captured via `profileActionOverrides` inside the owning `CustomApplication`'s metadata. Full diagnostic writeup: `docs/reference/TROUBLESHOOTING.md`.

6. **Unfilled Doc Placeholders Produce Confusing Failures:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** `<confirm actual API name>` was left in a code block even after the real name (`Contact_Record_Page_for_Sales`) was already known elsewhere in the doc, causing `Entity of type 'FlexiPage' named '<confirm actual API name>' cannot be found`.
   - **Resolution:** Once a placeholder's real value is confirmed anywhere in a doc, immediately propagate it to every occurrence.

7. **Audit Logs Silently Stopped Being Recorded After Unit 3:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** Neither Unit 4 nor this unit had any files under `logs/` for a stretch — `--json` output was being pasted into chat/terminal without ever being redirected to a file.
   - **Resolution:** Every deploy command in the Unit 5 doc now pipes its own output directly to the log file via `tee` at the point of execution, rather than being reconstructed from a chat transcript afterward.

8. **Terminal Paste Corruption on Multi-Line Commands:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** Multi-line `\`-continued commands repeatedly broke when pasted through the terminal — a wrapped `git push --force-with-lease`, a SOQL query, and a `sf project deploy start` call all hit this, the last one appending a stray `~` that broke the `--json` flag entirely.
   - **Resolution:** Prefer single-line commands for anything likely to be copy-pasted through a terminal prone to bracketed-paste-mode artifacts. Multi-line heredocs (`cat << 'EOF' ... EOF`) were never affected.

9. **Re-Retrieving Metadata Can Silently Overwrite an Undeployed Local Fix:**
   - **Context:** `Developer Beginner > Badge 05: Lightning Experience Customization > Unit 5: Customize Record Page Components and Fields`
   - **Hiccup:** After manually correcting `Contact-Contact Layout.layout-meta.xml`'s related-list value locally, re-running its retrieve command (as part of a "rerun everything from scratch" pass) would have pulled the org's still-broken state and erased the fix, since the deploy that would've made the fix live had errored out first.
   - **Resolution:** When rerunning a sequence from scratch, skip any retrieve that pulls _from_ the org if a correct, not-yet-deployed local edit already exists for that file — only the deploy should be repeated in that case.
