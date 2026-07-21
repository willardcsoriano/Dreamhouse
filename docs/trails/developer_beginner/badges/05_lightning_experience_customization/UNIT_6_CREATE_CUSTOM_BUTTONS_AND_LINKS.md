# Trailhead Unit: Create Custom Buttons and Links

**Trail:** Developer Beginner
**Badge 05:** Lightning Experience Customization
**Unit 6:** Create Custom Buttons and Links
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_buttons_links)

---

## Table of Contents

- [Why This Unit Is Mixed `[CLI]` / `[GUI]`](#why-this-unit-is-mixed-cli-gui)
- [Requirement to CLI Command Mapping Matrix](#requirement-to-cli-command-mapping-matrix)
- [Introduction & Learning Objectives](#introduction-learning-objectives)
- [Part 1: Guided Activity (`Energy_Audit__c` / `Account`)](#part-1-guided-activity-energy_audit__c-account)
  - [1. `[REQ-5.6.G1.PRE]` Upload a File & Generate a Public Share Link — `[GUI]`](#1-req-56g1pre-upload-a-file-generate-a-public-share-link-gui)
  - [2. `[REQ-5.6.G1.1]` & `[REQ-5.6.G1.2]` Create the List Button & Add It to the Related List — `[CLI]`](#2-req-56g11-req-56g12-create-the-list-button-add-it-to-the-related-list-cli)
  - [3. `[REQ-5.6.G2.1]` & `[REQ-5.6.G2.2]` Create the Detail Page Link & Add It to Custom Links — `[CLI]`](#3-req-56g21-req-56g22-create-the-detail-page-link-add-it-to-custom-links-cli)
  - [4. `[REQ-5.6.G1.DEP]` & `[REQ-5.6.G2.DEP]` Deploy the List Button and Detail Link — `[CLI]`](#4-req-56g1dep-req-56g2dep-deploy-the-list-button-and-detail-link-cli)
  - [5. `[REQ-5.6.G1.AUD]` & `[REQ-5.6.G2.AUD]` Audit the List Button and Detail Link — `[CLI]`](#5-req-56g1aud-req-56g2aud-audit-the-list-button-and-detail-link-cli)
  - [6. `[REQ-5.6.G3.1]` Create the Detail Page Button — `[CLI]`](#6-req-56g31-create-the-detail-page-button-cli)
  - [7. `[REQ-5.6.G3.DEP]` Deploy the Detail Page Button — `[CLI]`](#7-req-56g3dep-deploy-the-detail-page-button-cli)
  - [8. `[REQ-5.6.G3.AUD]` Audit the Detail Page Button — `[CLI]`](#8-req-56g3aud-audit-the-detail-page-button-cli)
  - [9. `[REQ-5.6.G3.2]` Add Map Location to the Actions Menu — `[GUI]`](#9-req-56g32-add-map-location-to-the-actions-menu-gui)
  - [10. `[REQ-5.6.G3.RET]` Capture the Actions-Menu Placement as a Redeployable Payload — `[CLI]`](#10-req-56g3ret-capture-the-actions-menu-placement-as-a-redeployable-payload-cli)
- [Part 2: Hands-On Challenge (`Contact`)](#part-2-hands-on-challenge-contact)
  - [1. `[REQ-5.6.C1.1]` Create the Custom Button — `[CLI]`](#1-req-56c11-create-the-custom-button-cli)
  - [2. `[REQ-5.6.C1.DEP]` Deploy the Custom Button — `[CLI]`](#2-req-56c1dep-deploy-the-custom-button-cli)
  - [3. `[REQ-5.6.C1.AUD]` Audit the Custom Button — `[CLI]`](#3-req-56c1aud-audit-the-custom-button-cli)
  - [4. `[REQ-5.6.C1.2]` Add the Button to the Contact Layout — `[GUI]`](#4-req-56c12-add-the-button-to-the-contact-layout-gui)
  - [5. `[REQ-5.6.C1.RET]` Capture the Result as a Redeployable Payload — `[CLI]`](#5-req-56c1ret-capture-the-result-as-a-redeployable-payload-cli)
- [Resources & Reference Documentation](#resources-reference-documentation)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem-engineering-learnings)

## Why This Unit Is Mixed `[CLI]` / `[GUI]`

The `WebLink` metadata type itself — the button or link definition — passes all three tests in `docs/reference/CLI_GUI_BOUNDARIES.md`: the Metadata API reference has worked examples of exactly this structure (list button, detail page link, detail page button), every identifier (`fullName`, `masterLabel`, `url`) is one the developer chooses rather than one a wizard assigns, and a structurally valid deploy is exactly equivalent to what the click-path produces. So every `WebLink` in this unit is `[CLI]`.

*Placement* is where it splits:

- Adding a button to a **related list** (`relatedLists.customButtons`) and adding a link to the **Custom Links** section (`layoutItems.customLink`) are both flat, semantic, already-precedented in this repo's own `Account-Account Layout.layout-meta.xml` (it already carries a working `<customLink>Billing</customLink>` entry) — `[CLI]`.
- Adding a button to the **Highlights Panel actions menu** ("Salesforce Mobile and Lightning Experience Actions") is the one place the raw Trailhead content itself flags as unreliable: *"Is Map Location not showing up in the actions menu even though you added the custom button to the page layout? This happens sometimes..."* That's the project's own signal that this specific placement is builder/state-dependent, not a stable declarative write — Rule 3 fails. So the actions-menu placement is `[GUI]`: build it once in the Page Layout editor, then retrieve → deploy the resulting `Layout` file as the reproducible payload, same pattern Unit 5 used for `FlexiPage`.

**Execution order, at a glance:**

- **`G1`, `G2` (`[CLI]` only):** no browser needed for the button/link definition or its page-layout placement — hand-author and deploy directly. `G1` does need one manual browser prerequisite (`G1.PRE`) to generate a file-sharing URL, since that's live org data, not metadata.
- **`G3`, `C1` (`[CLI]` + `[GUI]`):** create and deploy the `WebLink` from the terminal first, *then* switch to the browser to place it on the actions menu, then close out with retrieve → deploy.

---

## Requirement to CLI Command Mapping Matrix

| Activity Type       | Requirement ID         | Access  | Summary                                                    | Target Component                          | Solved By CLI Command / GUI Steps                                                                                                          |
| :------------------- | :---------------------- | :------ | :----------------------------------------------------------- | :------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| Guided Activity      | `[REQ-5.6.G1.PRE]`      | `[GUI]` | Upload a file, generate a public share link                | Salesforce Files (org data, not metadata) | Files tab → Share → Create Public Link                                                                                                     |
| Guided Activity      | `[REQ-5.6.G1.1]`        | `[CLI]` | Create the `Audit_Guidelines` list button                  | `Energy_Audit__c` `WebLink`               | `cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/webLinks/Audit_Guidelines.webLink-meta.xml`                                 |
| Guided Activity      | `[REQ-5.6.G1.2]`        | `[CLI]` | Add the button to Account's Energy Audits related list     | `Account-Account Layout` `relatedLists`   | Hand-edit `Account-Account Layout.layout-meta.xml`                                                                                          |
| Guided Activity      | `[REQ-5.6.G2.1]`        | `[CLI]` | Create the `Google_This_Account` detail page link           | `Account` `WebLink`                       | `cat << 'EOF' > force-app/main/default/objects/Account/webLinks/Google_This_Account.webLink-meta.xml`                                       |
| Guided Activity      | `[REQ-5.6.G2.2]`        | `[CLI]` | Add the link to Account's Custom Links section              | `Account-Account Layout` `layoutItems`    | Hand-edit `Account-Account Layout.layout-meta.xml`                                                                                          |
| Guided Activity      | `[REQ-5.6.G1.DEP]` / `[REQ-5.6.G2.DEP]` | `[CLI]` | Deploy both WebLinks + patched Account layout | `Energy_Audit__c`, `Account`, layouts     | `sf project deploy start -d force-app/main/default/objects/Energy_Audit__c/webLinks -d force-app/main/default/objects/Account/webLinks -m "Layout:Account-Account Layout" -o trailhead-playground --json` |
| Guided Activity      | `[REQ-5.6.G1.AUD]` / `[REQ-5.6.G2.AUD]` | `[CLI]` | Audit both WebLinks via Tooling API | Tooling API `WebLink`                     | `sf data query -o trailhead-playground --use-tooling-api -q "SELECT Id, MasterLabel, LinkType, DisplayType, Url FROM WebLink WHERE MasterLabel IN ('Audit Guidelines','Google This Account')"` |
| Guided Activity      | `[REQ-5.6.G3.1]`        | `[CLI]` | Create the `Map_Location` detail page button                | `Account` `WebLink`                       | `cat << 'EOF' > force-app/main/default/objects/Account/webLinks/Map_Location.webLink-meta.xml`                                             |
| Guided Activity      | `[REQ-5.6.G3.DEP]`      | `[CLI]` | Deploy the `Map_Location` WebLink                           | `Account`                                 | `sf project deploy start -d force-app/main/default/objects/Account/webLinks -o trailhead-playground --json`                                |
| Guided Activity      | `[REQ-5.6.G3.AUD]`      | `[CLI]` | Audit `Map_Location` via Tooling API                        | Tooling API `WebLink`                     | `sf data query -o trailhead-playground --use-tooling-api -q "SELECT Id, MasterLabel, Url FROM WebLink WHERE MasterLabel='Map Location'"`   |
| Guided Activity      | `[REQ-5.6.G3.2]`        | `[GUI]` | Add Map Location to the Account page's actions menu         | Account Layout actions menu               | Page Layout editor → Mobile & Lightning Actions → drag into Salesforce Mobile and Lightning Experience Actions                             |
| Guided Activity      | `[REQ-5.6.G3.RET]`      | `[CLI]` | Capture the resulting layout as a redeployable payload      | `Account-Account Layout.layout-meta.xml`  | `sf project retrieve start -m "Layout:Account-Account Layout" -o trailhead-playground --json` → `sf project deploy start -m "Layout:Account-Account Layout" -o trailhead-playground --json` |
| Hands-On Challenge  | `[REQ-5.6.C1.1]`        | `[CLI]` | Create the `Google_Info` custom button                      | `Contact` `WebLink`                       | `cat << 'EOF' > force-app/main/default/objects/Contact/webLinks/Google_Info.webLink-meta.xml`                                              |
| Hands-On Challenge  | `[REQ-5.6.C1.DEP]`      | `[CLI]` | Deploy the `Google_Info` WebLink                             | `Contact`                                 | `sf project deploy start -d force-app/main/default/objects/Contact/webLinks -o trailhead-playground --json`                                |
| Hands-On Challenge  | `[REQ-5.6.C1.AUD]`      | `[CLI]` | Audit `Google_Info` via Tooling API                          | Tooling API `WebLink`                     | `sf data query -o trailhead-playground --use-tooling-api -q "SELECT Id, MasterLabel, Url FROM WebLink WHERE MasterLabel='Google Info'"`    |
| Hands-On Challenge  | `[REQ-5.6.C1.2]`        | `[GUI]` | Add the button to the Contact Layout page layout             | Contact Layout                            | Page Layout editor → drag `Google Info` onto the layout (Trailhead's Challenge doesn't pin down which zone)                                |
| Hands-On Challenge  | `[REQ-5.6.C1.RET]`      | `[CLI]` | Capture the resulting layout as a redeployable payload       | `Contact-Contact Layout.layout-meta.xml`  | `sf project retrieve start -m "Layout:Contact-Contact Layout" -o trailhead-playground --json` → `sf project deploy start -m "Layout:Contact-Contact Layout" -o trailhead-playground --json` |

---

## Introduction & Learning Objectives

Custom buttons and links extend Salesforce records out to external URLs, Visualforce pages, or other back-end systems. They come in three flavors — a **list button** on a related list, a **detail page link** in the Links section, and a **detail page button** in the highlights-panel actions menu — all backed by the same `WebLink` metadata type, differentiated by `displayType` and where they're placed on the page layout.

After completing this unit, you'll be able to:

- Create custom buttons and links.
- Add them to a page layout.
- Explain the difference between a custom button and a custom link.

---

## Part 1: Guided Activity (`Energy_Audit__c` / `Account`)

Maria Jimenez wants three things off the Ursa Major Solar Account and Energy Audit pages: a list button that jumps straight to an audit guidelines PDF, a detail link that Googles the account, and a detail button that maps the account's billing address.

### 1. `[REQ-5.6.G1.PRE]` Upload a File & Generate a Public Share Link — `[GUI]`

**Browser first — nothing to run in the terminal until this is done.**

This step produces org-specific, session-specific data (a public file URL) — not metadata, so there's nothing to hand-author or check into source. Substitute your own generated path into `G1.1` below.

1. App Launcher → **Sales** app → **Files** tab.
2. Upload a file (e.g. a PDF of your own audit guidelines).
3. Action dropdown on that file → **Share**.
4. Expand **Who Can Access** → set **Password** toggle to **Off** → **Create Link** → **Create**.
5. **Copy Link**, then **Done**. Keep everything after the domain (e.g. `/sfc/p/R00000008nD1/a/R000000007LK/8Z8auAJBSeSCzqQ8Kv9ofolIWi_jP13oR3LUUYuXc3A`) — that's the value for the `<url>` element in `G1.1`.

---

### 2. `[REQ-5.6.G1.1]` & `[REQ-5.6.G1.2]` Create the List Button & Add It to the Related List — `[CLI]`

**No browser needed — run these commands directly.**

```bash
mkdir -p force-app/main/default/objects/Energy_Audit__c/webLinks

cat << 'EOF' > force-app/main/default/objects/Energy_Audit__c/webLinks/Audit_Guidelines.webLink-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Audit_Guidelines</fullName>
    <availability>online</availability>
    <displayType>button</displayType>
    <linkType>url</linkType>
    <masterLabel>Audit Guidelines</masterLabel>
    <openType>noSidebar</openType>
    <protected>false</protected>
    <!-- Replace with the path captured in G1.PRE, e.g. /sfc/p/<...>/a/<...>/<...> -->
    <url>/sfc/p/REPLACE_WITH_YOUR_FILE_SHARE_PATH</url>
</WebLink>
EOF
```

Open `force-app/main/default/layouts/Account-Account Layout.layout-meta.xml` and add a new `relatedLists` block immediately before `</Layout>` — `Energy_Audit__c` is the child object, `Account__c` is its lookup to Account (established in Badge 04), so the related list identifier follows this repo's existing `<ChildObject>.<LookupField>` convention (see the `Favorite__c.Contact__c` entry already in `Contact-Contact Layout.layout-meta.xml`):

```xml
<relatedLists>
    <customButtons>Audit_Guidelines</customButtons>
    <fields>NAME</fields>
    <relatedList>Energy_Audit__c.Account__c</relatedList>
</relatedLists>
```

---

### 3. `[REQ-5.6.G2.1]` & `[REQ-5.6.G2.2]` Create the Detail Page Link & Add It to Custom Links — `[CLI]`

**No browser needed — run these commands directly.**

```bash
mkdir -p force-app/main/default/objects/Account/webLinks

cat << 'EOF' > force-app/main/default/objects/Account/webLinks/Google_This_Account.webLink-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Google_This_Account</fullName>
    <availability>online</availability>
    <displayType>link</displayType>
    <linkType>url</linkType>
    <masterLabel>Google This Account</masterLabel>
    <openType>noSidebar</openType>
    <protected>false</protected>
    <url>https://www.google.com/search?q={!Account.Name}</url>
</WebLink>
EOF
```

`Account-Account Layout.layout-meta.xml` already has a `CustomLinks`-style `layoutSections` block (it carries the existing `Billing` link). Add a second `layoutItems` entry to its first `layoutColumns`:

```xml
<layoutColumns>
    <layoutItems>
        <customLink>Billing</customLink>
    </layoutItems>
    <layoutItems>
        <customLink>Google_This_Account</customLink>
    </layoutItems>
</layoutColumns>
```

---

### 4. `[REQ-5.6.G1.DEP]` & `[REQ-5.6.G2.DEP]` Deploy the List Button and Detail Link — `[CLI]`

```bash
sf project deploy start \
  -d force-app/main/default/objects/Energy_Audit__c/webLinks \
  -d force-app/main/default/objects/Account/webLinks \
  -m "Layout:Account-Account Layout" \
  -o trailhead-playground \
  --json
```

---

### 5. `[REQ-5.6.G1.AUD]` & `[REQ-5.6.G2.AUD]` Audit the List Button and Detail Link — `[CLI]`

```bash
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT Id, MasterLabel, LinkType, DisplayType, Url FROM WebLink WHERE MasterLabel IN ('Audit Guidelines', 'Google This Account')"
```

---

### 6. `[REQ-5.6.G3.1]` Create the Detail Page Button — `[CLI]`

**No browser needed — run these commands directly.**

The raw scrape's URL used underscore-joined merge-field names (`{!Account_BillingStreet}`), which isn't valid Salesforce formula syntax — corrected to dot notation (`{!Account.BillingStreet}`) below.

```bash
cat << 'EOF' > force-app/main/default/objects/Account/webLinks/Map_Location.webLink-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Map_Location</fullName>
    <availability>online</availability>
    <displayType>button</displayType>
    <linkType>url</linkType>
    <masterLabel>Map Location</masterLabel>
    <openType>newWindow</openType>
    <protected>false</protected>
    <url>http://maps.google.com/maps?q={!Account.BillingStreet}%20{!Account.BillingCity}%20{!Account.BillingState}%20{!Account.BillingPostalCode}</url>
</WebLink>
EOF
```

---

### 7. `[REQ-5.6.G3.DEP]` Deploy the Detail Page Button — `[CLI]`

```bash
sf project deploy start \
  -d force-app/main/default/objects/Account/webLinks \
  -o trailhead-playground \
  --json
```

---

### 8. `[REQ-5.6.G3.AUD]` Audit the Detail Page Button — `[CLI]`

```bash
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT Id, MasterLabel, Url FROM WebLink WHERE MasterLabel='Map Location'"
```

---

### 9. `[REQ-5.6.G3.2]` Add Map Location to the Actions Menu — `[GUI]`

**Browser first — nothing to run in the terminal until this is done.**

1. Object Manager → **Account** → **Page Layouts** → **Account Layout**.
2. From the **Buttons** category in the palette, drag **Map Location** into the **Custom Buttons** area on the page layout → **Save**.
3. Open an Account record → expand the actions menu (highlights panel) → confirm **Map Location** appears.
4. If it doesn't (the raw content flags this as a known intermittent wizard quirk), go back to the layout editor and drag **Map Location** from the **Mobile & Lightning Actions** category directly into the **Salesforce Mobile and Lightning Experience Actions** section → **Save**.

---

### 10. `[REQ-5.6.G3.RET]` Capture the Actions-Menu Placement as a Redeployable Payload — `[CLI]`

**Terminal only — run this after the browser steps above, not instead of them.**

```bash
sf project retrieve start \
  -m "Layout:Account-Account Layout" \
  -o trailhead-playground \
  --json

sf project deploy start \
  -m "Layout:Account-Account Layout" \
  -o trailhead-playground \
  --json
```

---

## Part 2: Hands-On Challenge (`Contact`)

**Your Challenge:** Ursa Major Solar wants to look up a contact's internet footprint straight from the contact record.

- Create a custom button for the Contact object: **Label** `Google Info`, **Name** `Google_Info`, opening `https://www.google.com/search?q={!Contact.Name}`.
- Add the custom button to the Contact Layout page layout.

### 1. `[REQ-5.6.C1.1]` Create the Custom Button — `[CLI]`

**No browser needed — run this command directly.**

```bash
mkdir -p force-app/main/default/objects/Contact/webLinks

cat << 'EOF' > force-app/main/default/objects/Contact/webLinks/Google_Info.webLink-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<WebLink xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Google_Info</fullName>
    <availability>online</availability>
    <displayType>button</displayType>
    <linkType>url</linkType>
    <masterLabel>Google Info</masterLabel>
    <openType>noSidebar</openType>
    <protected>false</protected>
    <url>https://www.google.com/search?q={!Contact.Name}</url>
</WebLink>
EOF
```

---

### 2. `[REQ-5.6.C1.DEP]` Deploy the Custom Button — `[CLI]`

```bash
sf project deploy start \
  -d force-app/main/default/objects/Contact/webLinks \
  -o trailhead-playground \
  --json
```

---

### 3. `[REQ-5.6.C1.AUD]` Audit the Custom Button — `[CLI]`

```bash
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT Id, MasterLabel, Url FROM WebLink WHERE MasterLabel='Google Info'"
```

---

### 4. `[REQ-5.6.C1.2]` Add the Button to the Contact Layout — `[GUI]`

**Browser first — nothing to run in the terminal until this is done.**

The Challenge text doesn't specify which zone of the layout the button belongs in, and — per `G3.2` above — button placement on this layout is the one step this unit's own content flags as builder/state-dependent. Place it in the **Custom Buttons** area, consistent with `Map Location` in the Guided Activity, and confirm it renders somewhere reachable from the record (actions menu or custom buttons row) before moving on.

1. Object Manager → **Contact** → **Page Layouts** → **Contact Layout**.
2. From the **Buttons** category in the palette, drag **Google Info** onto the layout → **Save**.
3. Open a Contact record and confirm the button appears; if not, repeat via the **Mobile & Lightning Actions** category into the actions section, same as `G3.2`.

---

### 5. `[REQ-5.6.C1.RET]` Capture the Result as a Redeployable Payload — `[CLI]`

**Terminal only — run this after the browser steps above, not instead of them.**

```bash
sf project retrieve start \
  -m "Layout:Contact-Contact Layout" \
  -o trailhead-playground \
  --json

sf project deploy start \
  -m "Layout:Contact-Contact Layout" \
  -o trailhead-playground \
  --json
```

---

## Resources & Reference Documentation

- [Salesforce Help: Define Custom Buttons and Links](https://help.salesforce.com/s/articleView?id=sf.customize_customlinktext.htm&type=5)
- [Salesforce Help: Custom Button and Link Samples](https://help.salesforce.com/s/articleView?id=sf.customlink_examples.htm&type=5)
- [Salesforce Help: Constructing Effective Custom URL Buttons and Links](https://help.salesforce.com/s/articleView?id=sf.customlink_urls.htm&type=5)
- [Metadata API Reference: WebLink](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_weblink.htm)
- [Metadata API Reference: Layout](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_layouts.htm)

---

## Technical Post-Mortem & Engineering Learnings

This unit hasn't gone through Stage 4 (human execution against the live org) yet — the items below are flagged risks and corrections made during Stage 2/3 authoring, not confirmed post-execution hiccups. Update this section with real outcomes once `trailhead-playground` deploy/audit output comes back.

1. **Merge field syntax correction (raw scrape artifact).**
   - **Issue:** The raw Trailhead text renders the Map Location URL with underscore-joined tokens — `{!Account_BillingStreet}` — which is not valid Salesforce formula/merge-field syntax.
   - **Resolution:** Corrected to dot notation, `{!Account.BillingStreet}`, consistent with the `{!Account.Name}` merge field used elsewhere in the same raw content and with every other formula field in this codebase.

2. **`G1.PRE` produces data, not metadata.**
   - The file-upload-and-share step generates an org-specific, session-specific public URL. There's nothing here to hand-author or check into source control — `G1.1`'s `<url>` element carries a placeholder the developer must replace with their own captured path.

3. **Actions-menu placement is the one genuinely `[GUI]` step in this unit.**
   - The raw Trailhead content itself documents that a custom button added to a page layout doesn't reliably show up in the actions menu without an extra manual drag from the **Mobile & Lightning Actions** palette category — the exact "wizard/builder-state-dependent" failure mode `docs/reference/CLI_GUI_BOUNDARIES.md` Rule 3 describes. `G3.2` and `C1.2` are written as `[GUI]` for that reason, closed out with retrieve → deploy rather than a hand-authored `platformActionList`/`quickActionList` guess.

4. **Tooling API `WebLink` field names are unverified against a live org.**
   - The audit queries above (`MasterLabel`, `LinkType`, `DisplayType`, `Url`) are drafted from the Metadata API's `WebLink` schema, not confirmed against a live Tooling API response. If any field throws `INVALID_FIELD`, treat it the same way Unit 4 handled `CompactLayout`'s `SobjectType` — capture the corrected field name here.
