# Trailhead Unit: Customize Record Page Components and Fields

## Table of Contents

- [Why This Unit Breaks the Unit 1/4 Pattern](#why-this-unit-breaks-the-unit-14-pattern)
- [Requirement to CLI Command Mapping Matrix](#requirement-to-cli-command-mapping-matrix)
- [Introduction & Learning Objectives](#introduction-learning-objectives)
- [Part 1: Guided Activity (`Energy_Audit__c`)](#part-1-guided-activity-energy_audit__c)
  - [1. `[REQ-5.5.G1.1]`–`[REQ-5.5.G1.5]` Build the Page in Lightning App Builder — `[GUI]`](#1-req-55g11req-55g15-build-the-page-in-lightning-app-builder-gui)
  - [2. `[REQ-5.5.G1.RET]` Retrieve, Then Deploy as a Redeployable Payload — `[CLI]`](#2-req-55g1ret-retrieve-then-deploy-as-a-redeployable-payload-cli)
  - [3. `[REQ-5.5.G2.RETRIEVE]`–`[REQ-5.5.G2.DEP]` Add the Files Related List — `[CLI]`](#3-req-55g2retrievereq-55g2dep-add-the-files-related-list-cli)
  - [4. `[REQ-5.5.G3.1]`–`[REQ-5.5.G3.RET]` Activate for the Sales Profile — `[GUI]` + `[CLI]`](#4-req-55g31req-55g3ret-activate-for-the-sales-profile-gui-cli)
- [Part 2: Hands-On Challenge (`Contact`)](#part-2-hands-on-challenge-contact)
  - [1. `[REQ-5.5.C1.1]`–`[REQ-5.5.C1.3]` Build the Contact Page — `[GUI]`](#1-req-55c11req-55c13-build-the-contact-page-gui)
  - [2. `[REQ-5.5.C1.RET]` Retrieve, Then Deploy as a Redeployable Payload — `[CLI]`](#2-req-55c1ret-retrieve-then-deploy-as-a-redeployable-payload-cli)
  - [3. `[REQ-5.5.C2.RETRIEVE]`–`[REQ-5.5.C2.DEP]` Swap the Related List — `[CLI]`](#3-req-55c2retrievereq-55c2dep-swap-the-related-list-cli)
  - [4. `[REQ-5.5.C3.1]`–`[REQ-5.5.C3.RET]` Activate as Org Default — `[GUI]` + `[CLI]`](#4-req-55c31req-55c3ret-activate-as-org-default-gui-cli)
- [Resources & Reference Documentation](#resources-reference-documentation)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem-engineering-learnings)

## Why This Unit Breaks the Unit 1/4 Pattern

Units 1 and 4 map cleanly onto declarative metadata you can hand-author with confidence: custom fields, objects, and compact layouts all have a small, stable XML schema. This unit is different — most of it is driven by the **Lightning App Builder's Dynamic Forms migration wizard** and the **Activation wizard**, both of which generate `FlexiPage` XML with builder-assigned region UUIDs, nested facets, and wizard-specific structure that isn't practical to hand-author from memory (verified against the current Metadata API docs — see `[REQ-5.5.G1]` below). Faking a `cat << EOF` block for that would look like CLI-first documentation but would actually be untested, unverifiable XML.

So this doc tags every requirement `[CLI]` or `[GUI]` per the classification rule in `docs/PIPELINE.md`:

- `[CLI]` — hand-authored (or retrieved-then-patched) metadata: the two page-layout related-list swaps.
- `[GUI]` — built once in the Lightning App Builder / Activation wizard per the Trailhead click-path, then closed out with a **retrieve → deploy** round trip: `sf project retrieve start` pulls the builder-generated result into source, and `sf project deploy start` on that exact retrieved file is the reproducible, auditable payload from then on — the thing you'd actually re-run against a fresh sandbox instead of re-clicking the wizard.

**Execution order, at a glance:**

- **`G1`, `G3`, `C1`, `C3` (`[GUI]`):** do the browser click-path first — nothing to run until that's done. Only after saving/activating do you switch to the terminal and run retrieve → deploy.
- **`G2`, `C2` (`[CLI]` only):** no browser steps at all. Run retrieve → hand-edit → deploy directly from the terminal.

---

## Requirement to CLI Command Mapping Matrix

| Activity Type | Requirement ID | Access | Summary | Target Component | Solved By |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Guided Activity | `[REQ-5.5.G1.1]` | `[GUI]` | Open Edit Page from the Burlington evaluation Energy Audit record | `Energy_Audit__c` FlexiPage | Lightning App Builder |
| Guided Activity | `[REQ-5.5.G1.2]` | `[GUI]` | Set page Label/API Name | `Energy_Audit_Record_Page_for_Sales` | App Builder page properties |
| Guided Activity | `[REQ-5.5.G1.3]` | `[GUI]` | Upgrade to Dynamic Forms from Energy Audit Layout | FlexiPage Details region | Dynamic Forms migration wizard |
| Guided Activity | `[REQ-5.5.G1.4]` | `[GUI]` | Reorder fields (Audit Notes, Type of Installation, Account) | FlexiPage field instances | Drag-and-drop in App Builder |
| Guided Activity | `[REQ-5.5.G1.5]` | `[GUI]` | Save without activating | FlexiPage | App Builder Save → Not Yet |
| Guided Activity | `[REQ-5.5.G1.RET]` | `[CLI]` | Capture the built page as a redeployable payload | `Energy_Audit_Record_Page_for_Sales.flexipage-meta.xml` | `sf project retrieve start -m "FlexiPage:Energy_Audit_Record_Page_for_Sales"` → `sf project deploy start -m "FlexiPage:Energy_Audit_Record_Page_for_Sales" --json` |
| Guided Activity | `[REQ-5.5.G2.RETRIEVE]` | `[CLI]` | Pull the org-default layout as an edit baseline | `Energy_Audit__c-Energy Audit Layout` | `sf project retrieve start -m "Layout:Energy_Audit__c-Energy Audit Layout"` |
| Guided Activity | `[REQ-5.5.G2.EDIT]` | `[CLI]` | Add the Files related list | `relatedLists` block | Hand-edit the retrieved `Layout` XML |
| Guided Activity | `[REQ-5.5.G2.DEP]` | `[CLI]` | Deploy the patched layout | `Energy_Audit__c-Energy Audit Layout` | `sf project deploy start -m "Layout:Energy_Audit__c-Energy Audit Layout" --json` |
| Guided Activity | `[REQ-5.5.G3.1]` | `[GUI]` | Assign the page to App + Record Type + Profile + Form Factor | `Energy_Consultations` app | Activation wizard |
| Guided Activity | `[REQ-5.5.G3.RET]` | `[CLI]` | Capture the resulting assignment as a redeployable payload | `Energy_Consultations.app-meta.xml` | `sf project retrieve start -m "CustomApplication:Energy_Consultations"` → `sf project deploy start -m "CustomApplication:Energy_Consultations" --json` |
| Hands-On Challenge | `[REQ-5.5.C1.1]` | `[GUI]` | Edit Page from a Contact record | Contact FlexiPage | Lightning App Builder |
| Hands-On Challenge | `[REQ-5.5.C1.2]` | `[GUI]` | Upgrade to Dynamic Forms from Contact Layout | FlexiPage Details region | Dynamic Forms migration wizard |
| Hands-On Challenge | `[REQ-5.5.C1.3]` | `[GUI]` | Remove Fax, Other Phone, Home Phone | FlexiPage field instances | Remove in App Builder |
| Hands-On Challenge | `[REQ-5.5.C1.RET]` | `[CLI]` | Capture the built page as a redeployable payload | `<generated-name>.flexipage-meta.xml` | `sf project retrieve start -m "FlexiPage:<confirm actual API name>"` → `sf project deploy start -m "FlexiPage:<confirm actual API name>" --json` |
| Hands-On Challenge | `[REQ-5.5.C2.RETRIEVE]` | `[CLI]` | Pull Contact's layout as an edit baseline | `Contact-Contact Layout` | `sf project retrieve start -m "Layout:Contact-Contact Layout"` |
| Hands-On Challenge | `[REQ-5.5.C2.EDIT]` | `[CLI]` | Remove Notes & Attachments, add Files | `relatedLists` block | Hand-edit the retrieved `Layout` XML |
| Hands-On Challenge | `[REQ-5.5.C2.DEP]` | `[CLI]` | Deploy the patched layout | `Contact-Contact Layout` | `sf project deploy start -m "Layout:Contact-Contact Layout" --json` |
| Hands-On Challenge | `[REQ-5.5.C3.1]` | `[GUI]` | Save, activate as org default, both form factors | Contact FlexiPage | Activation wizard |
| Hands-On Challenge | `[REQ-5.5.C3.RET]` | `[CLI]` | Capture the final page/assignment as a redeployable payload | `<generated-name>.flexipage-meta.xml` | `sf project retrieve start -m "FlexiPage:<confirm actual API name>"` → `sf project deploy start -m "FlexiPage:<confirm actual API name>" --json` |

---

## Introduction & Learning Objectives

Record pages in Lightning Experience are built from two layers: the **Lightning App Builder**, which controls page structure, component placement, and (via Dynamic Forms) individual field placement; and the **page layout editor**, which controls related lists, buttons, links, and quick actions. This unit works both tools to give a sales-specific view of Energy Audit records and a trimmed-down Contact record page.

After completing this unit, you'll be able to:

- Create, customize, and manage Lightning pages.
- Use the Lightning App Builder.
- Assign a Lightning page to a profile.

---

## Part 1: Guided Activity (`Energy_Audit__c`)

Maria wants a sales-specific Energy Audit record page: reordered fields via Dynamic Forms, a Files related list, and activation scoped to the Sales profile.

### 1. `[REQ-5.5.G1.1]`–`[REQ-5.5.G1.5]` Build the Page in Lightning App Builder — `[GUI]`

**Browser first — nothing to run in the terminal until this is done.**

1. App Launcher → **Energy Consultations** → **Energy Audits** tab → **All** list view → open **Burlington evaluation**.
2. Setup menu (gear icon) → **Edit Page**.
3. Page properties: set **Label** = `Energy Audit Record Page for Sales`, **API Name** = `Energy_Audit_Record_Page_for_Sales`.
4. Click the **Details** tab on the canvas → click the **Record Detail** component → **Upgrade Now** → step through the Dynamic Forms migration wizard, selecting **Energy Audit Layout** as the source → **Finish**.
5. Reorder fields in the right-hand column: drag **Audit Notes** above **Owner**, then drag **Type of Installation** above **Audit Notes**; confirm **Account** sits below **Energy Audit Name**.
6. **Save** → **Not Yet** (don't activate yet).

### 2. `[REQ-5.5.G1.RET]` Retrieve, Then Deploy as a Redeployable Payload — `[CLI]`

**Terminal only — run this after the browser steps above, not instead of them.**

```bash
# 1. Pull the builder-generated page into source (one-time, GUI-authored artifact)
sf project retrieve start \
  -m "FlexiPage:Energy_Audit_Record_Page_for_Sales" \
  -o trailhead-playground \
  --json

# 2. Redeploy that exact file — this is the reproducible, auditable command going forward
sf project deploy start \
  -m "FlexiPage:Energy_Audit_Record_Page_for_Sales" \
  -o trailhead-playground \
  --json
```

---

### 3. `[REQ-5.5.G2.RETRIEVE]`–`[REQ-5.5.G2.DEP]` Add the Files Related List — `[CLI]`

**No browser needed — run these commands directly.**

Salesforce auto-generated a default page layout for `Energy_Audit__c` when the object was first deployed (Unit 1) — that layout was never pulled into local source, so retrieve it first rather than hand-authoring a `Layout` file blind and risking silently dropping fields or sections it already has.

```bash
# 1. Pull the current org-default layout as an edit baseline
sf project retrieve start \
  -m "Layout:Energy_Audit__c-Energy Audit Layout" \
  -o trailhead-playground \
  --json
```

Open the retrieved `Energy_Audit__c-Energy Audit Layout.layout-meta.xml` and add a `relatedLists` entry for Files immediately before `</Layout>`:

```xml
<relatedLists>
    <relatedList>AttachedContentDocuments</relatedList>
</relatedLists>
```

```bash
# 2. Deploy the patched layout
sf project deploy start \
  -m "Layout:Energy_Audit__c-Energy Audit Layout" \
  -o trailhead-playground \
  --json
```

---

### 4. `[REQ-5.5.G3.1]`–`[REQ-5.5.G3.RET]` Activate for the Sales Profile — `[GUI]` + `[CLI]`

**Browser first, then terminal.**

1. Setup → Home tab → Quick Find **App Builder** → **Lightning App Builder** → **Edit** next to **Energy Audit Record Page for Sales**.
2. **Activation** → **App, Record Type, and Profile** tab → **Assign to Apps, Record Types, and Profiles**.
3. Step through the wizard: assign to the **Energy Consultations** app, **Desktop and phone** form factor, **Master** record type, and both **Custom: Sales Profile** and **System Administrator** (System Administrator only so the assignment is visible while logged in as admin — Maria's real users only need Sales Profile).
4. Review assignments → **Save**.

```bash
# 1. Pull the resulting App/Record-Type/Profile assignment into source
sf project retrieve start \
  -m "CustomApplication:Energy_Consultations" \
  -o trailhead-playground \
  --json

# 2. Redeploy that exact file — the reproducible, auditable command going forward
sf project deploy start \
  -m "CustomApplication:Energy_Consultations" \
  -o trailhead-playground \
  --json
```

---

## Part 2: Hands-On Challenge (`Contact`)

Give Contact records a trimmed field set and swap Notes & Attachments for Files.

### 1. `[REQ-5.5.C1.1]`–`[REQ-5.5.C1.3]` Build the Contact Page — `[GUI]`

**Browser first — nothing to run in the terminal until this is done.**

1. Open a Contact record → Setup menu → **Edit Page**.
2. Upgrade to Dynamic Forms, using **Contact Layout** as the source.
3. Remove these fields from the page: **Fax**, **Other Phone**, **Home Phone**.

### 2. `[REQ-5.5.C1.RET]` Retrieve, Then Deploy as a Redeployable Payload — `[CLI]`

**Terminal only — run this after the browser steps above, not instead of them.**

Confirm the FlexiPage's actual API name in App Builder's page properties before retrieving — Lightning App Builder auto-generates a name when cloning the org-default Contact page, and it isn't specified by the challenge text.

```bash
# 1. Pull the builder-generated page into source
sf project retrieve start \
  -m "FlexiPage:<confirm actual API name>" \
  -o trailhead-playground \
  --json

# 2. Redeploy that exact file — the reproducible, auditable command going forward
sf project deploy start \
  -m "FlexiPage:<confirm actual API name>" \
  -o trailhead-playground \
  --json
```

---

### 3. `[REQ-5.5.C2.RETRIEVE]`–`[REQ-5.5.C2.DEP]` Swap the Related List — `[CLI]`

**No browser needed — run these commands directly.**

```bash
# 1. Pull Contact Layout as an edit baseline
sf project retrieve start \
  -m "Layout:Contact-Contact Layout" \
  -o trailhead-playground \
  --json
```

Open the retrieved `Contact-Contact Layout.layout-meta.xml`:
- Remove the existing Notes & Attachments `relatedLists` entry — confirm its exact `<relatedList>` value against the retrieved file (commonly `CombinedAttachments`, but Contact's default layout should be checked rather than assumed).
- Add:

```xml
<relatedLists>
    <relatedList>AttachedContentDocuments</relatedList>
</relatedLists>
```

```bash
# 2. Deploy the patched layout
sf project deploy start \
  -m "Layout:Contact-Contact Layout" \
  -o trailhead-playground \
  --json
```

---

### 4. `[REQ-5.5.C3.1]`–`[REQ-5.5.C3.RET]` Activate as Org Default — `[GUI]` + `[CLI]`

**Browser first, then terminal.**

1. **Save** the Contact page.
2. **Activation** → **Org Default** → assign both **Desktop** and **Phone** form factors → **Save**.

```bash
# 1. Pull the final page/assignment into source
sf project retrieve start \
  -m "FlexiPage:<confirm actual API name>" \
  -o trailhead-playground \
  --json

# 2. Redeploy that exact file — the reproducible, auditable command going forward
sf project deploy start \
  -m "FlexiPage:<confirm actual API name>" \
  -o trailhead-playground \
  --json
```

---

## Resources & Reference Documentation

- [Salesforce Help: Create and Configure Lightning Experience Record Pages](https://help.salesforce.com/s/articleView?id=sf.lightning_page_create.htm&type=5)
- [Salesforce Help: Activate Lightning Experience Record Pages](https://help.salesforce.com/s/articleView?id=sf.lightning_page_activate.htm&type=5)
- [Metadata API Reference: FlexiPage](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flexipage.htm)
- [Metadata API Reference: Layout](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_layouts.htm)

---

## Technical Post-Mortem & Engineering Learnings

1. **FlexiPage / Dynamic Forms Hand-Authoring Infeasibility:**
   - **Finding:** Unlike `CompactLayout` or `CustomObject`, `FlexiPage` XML generated by the Dynamic Forms migration wizard and the Activation wizard includes builder-assigned region UUIDs and nested facet structures that Salesforce's own docs steer you away from hand-authoring.
   - **Resolution:** Built via GUI per the Trailhead click-path, then closed out with a retrieve → deploy round trip — the redeployed file, not a hand-written-from-scratch XML block, is the reproducible payload for these requirements.
2. **Missing Local Baseline for Page Layouts:**
   - **Finding:** `Energy_Audit__c`'s default page layout was auto-created by Salesforce when the object was deployed (Unit 1) but was never retrieved into local source, so its full field/section content wasn't known locally.
   - **Resolution:** Retrieve the current layout first, patch only the `relatedLists` block, then redeploy — avoids blindly reconstructing (and potentially corrupting) a layout whose existing content wasn't fully known.
