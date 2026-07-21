# Trailhead Unit: Optimize Customer Data with Standard and Custom Objects

**Trail:** Developer Beginner
**Badge 04:** Data Modeling
**Unit 1:** Optimize Customer Data with Standard and Custom Objects
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/data_modeling/objects_intro?trail_id=force_com_dev_beginner)

---

## Table of Contents

- [Execution Order, At a Glance](#execution-order-at-a-glance)
- [Introduction & Learning Objectives](#introduction-learning-objectives)
- [Part 1: Guided Activity (`Property`)](#part-1-guided-activity-property)
  - [1. `[REQ-4.1.G1.1]` & `[REQ-4.1.G1.2]` Create the Property Custom Object and Price Field — `[CLI]`](#1-req-41g11-req-41g12-create-the-property-custom-object-and-price-field-cli)
  - [2. `[REQ-4.1.G1.DEP]` Deploy Property Schema — `[CLI]`](#2-req-41g1dep-deploy-property-schema-cli)
  - [3. `[REQ-4.1.G1.AUD]` Audit Property Schema via Tooling API — `[CLI]`](#3-req-41g1aud-audit-property-schema-via-tooling-api-cli)
  - [4. `[REQ-4.1.G2.1]` Create a Sample Property Record — Informational, No CLI Artifact](#4-req-41g21-create-a-sample-property-record-informational-no-cli-artifact)
- [Part 2: Hands-On Challenge (`Offer`)](#part-2-hands-on-challenge-offer)
  - [1. `[REQ-4.1.C1.1]` Create the Offer Custom Object — `[CLI]`](#1-req-41c11-create-the-offer-custom-object-cli)
  - [2. `[REQ-4.1.C1.2]` & `[REQ-4.1.C1.3]` Create Offer Amount and Provision FLS — `[CLI]`](#2-req-41c12-req-41c13-create-offer-amount-and-provision-fls-cli)
  - [3. `[REQ-4.1.C1.4]` & `[REQ-4.1.C1.5]` Create Target Close Date and Provision FLS — `[CLI]`](#3-req-41c14-req-41c15-create-target-close-date-and-provision-fls-cli)
  - [4. `[REQ-4.1.C1.DEP]` Atomic Deploy of Offer Schema and FLS — `[CLI]`](#4-req-41c1dep-atomic-deploy-of-offer-schema-and-fls-cli)
  - [5. `[REQ-4.1.C1.AUD]` Audit Offer Schema via Tooling API — `[CLI]`](#5-req-41c1aud-audit-offer-schema-via-tooling-api-cli)
- [Resources & Reference Documentation](#resources-reference-documentation)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem-engineering-learnings)

## Execution Order, At a Glance

Every metadata-bearing requirement in this unit is `[CLI]` per the classification rule in `docs/reference/CLI_GUI_BOUNDARIES.md`: `CustomObject`, `CustomField`, and `fieldPermissions` are all small, stable, well-documented schema types with worked Metadata API examples — there's no builder-generated structure here to fake, so everything is hand-authored XML deployed straight from the terminal. **No browser needed for any schema/security requirement below.**

The one exception is `[REQ-4.1.G2.1]` (creating a sample `Property` record) — that's a one-off UI data-entry action with no fixed schema for a CLI payload to reproduce, so it carries no `[CLI]` tag and no deploy command. See its section for why.

---

## Introduction & Learning Objectives

DreamHouse is a realty company that helps customers shop for homes and contact agents online. Its brokers already lean on standard Salesforce CRM objects — `Contact` and `Lead` — to manage buyer data, but Salesforce has no standard object for tracking properties for sale. That's the gap this unit closes: modeling DreamHouse's data with **standard objects** (built into Salesforce — `Account`, `Contact`, `Lead`, `Opportunity`) and **custom objects** (objects you define yourself to store company- or industry-specific data — here, `Property`).

Every object, standard or custom, carries four broad field categories: **Identity** (the auto-generated 18-character record ID), **System** (read-only audit fields like `CreatedDate`), **Name** (the field that distinguishes one record from another — text or auto-number), and **Custom** (fields you add yourself, always suffixed `__c`). This unit exercises object creation, then layers a required Currency custom field onto it — reinforcing why "required fields when necessary" (Trailhead's own closing best practice) matters for data quality.

After completing this unit, you'll be able to:

- Describe the perks of using objects on the Salesforce CRM platform.
- Explain the difference between standard objects and custom objects.
- List the types of custom fields an object can have.

---

## Part 1: Guided Activity (`Property`)

D'Angelo, the DreamHouse admin, needs a place to track the homes the company has for sale — Salesforce has no standard object for that, so this walks through building a custom `Property` object with a required `Price` field.

### 1. `[REQ-4.1.G1.1]` & `[REQ-4.1.G1.2]` Create the Property Custom Object and Price Field — `[CLI]`

**No browser needed — run these commands directly.**

Trailhead's click-path creates the object via **Object Manager → Create → Custom Object**, setting Label `Property` (Object Name and Record Name auto-fill) and Plural Label `Properties`, leaving the rest default (Text name field, `ReadWrite` sharing, no description). It then adds the `Price` field via **Fields & Relationships → New → Currency**, with Field Label `Price`, Description "The listed sale price of the home.", and the **Required** checkbox checked.

```bash
mkdir -p force-app/main/default/objects/Property__c/fields

# 1. Property custom object
cat << 'EOF' > force-app/main/default/objects/Property__c/Property__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Property</label>
    <pluralLabel>Properties</pluralLabel>
    <nameField>
        <label>Property Name</label>
        <type>Text</type>
    </nameField>
    <sharingModel>ReadWrite</sharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
</CustomObject>
EOF

# 2. Price__c Currency field
cat << 'EOF' > force-app/main/default/objects/Property__c/fields/Price__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Price__c</fullName>
    <description>The listed sale price of the home.</description>
    <label>Price</label>
    <precision>18</precision>
    <required>true</required>
    <scale>0</scale>
    <type>Currency</type>
</CustomField>
EOF
```

**No `fieldPermissions` step here.** `Price__c` is `<required>true</required>`, which per Rule 2.3 auto-grants universal FLS visibility — appending explicit `fieldPermissions` for it would actually cause the deploy to be rejected (`You cannot deploy to a required field`). Confirmed against the live org: `Admin.profile-meta.xml` has no `fieldPermissions` entry for `Property__c.Price__c` at all.

**Scope note on the Custom Tab wizard:** Trailhead's click-path also checks "Launch New Custom Tab Wizard after saving this custom object" and steps through picking a tab icon/style, so the `Property` object gets a navigable tab in the **Sales** app. That tab and app assignment were never retrieved into this repo's source — there's no `Property__c.tab-meta.xml` under `force-app/main/default/tabs/` and no `Sales.app-meta.xml` under `force-app/main/default/applications/` (compare `Energy_Audit__c.tab-meta.xml`, which _was_ retrieved in Badge 05). This doc reproduces the object/field schema only; see the Technical Post-Mortem section below for why the tab/app artifacts aren't hand-authored here.

### 2. `[REQ-4.1.G1.DEP]` Deploy Property Schema — `[CLI]`

**No browser needed — run this command directly.**

```bash
# Deploy the Property__c object and Price__c field to the Trailhead Playground
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -o trailhead-playground \
  --json
```

### 3. `[REQ-4.1.G1.AUD]` Audit Property Schema via Tooling API — `[CLI]`

**No browser needed — run this command directly.**

```bash
# Verify Property__c's fields and their data types via the Tooling API
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  --json \
  -q "SELECT QualifiedApiName, DataType, IsRequired FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'"
```

### 4. `[REQ-4.1.G2.1]` Create a Sample Property Record — Informational, No CLI Artifact

Trailhead closes the Guided Activity by having you create one `Property` record by hand: **App Launcher → Sales → Properties tab → New**, entering any name and price, then **Save**.

This step is deliberately left without a CLI command. Trailhead doesn't grade the specific values entered — any name/price combination satisfies the check — so unlike the object and field schema above, there's no fixed identifier or structure for a deploy payload to reproduce. A record's field _values_ aren't a version-controlled metadata artifact the way a `CustomObject` or `CustomField` definition is. (A generic `sf data create record --sobject Property__c --values "..."` command could technically insert _a_ row, but there's no canonical value set to hand-author against, so it's omitted rather than presented as if it were.) This Requirement ID exists only so the ID list for this unit stays complete for tracking purposes.

---

## Part 2: Hands-On Challenge (`Offer`)

DreamHouse also needs to track offers buyers make on properties. This challenge creates the `Offer__c` custom object with an `Auto Number` name field and two custom fields: `Offer_Amount__c` (Currency) and `Target_Close_Date__c` (Date).

### 1. `[REQ-4.1.C1.1]` Create the Offer Custom Object — `[CLI]`

**No browser needed — run this command directly.**

```bash
mkdir -p force-app/main/default/objects/Offer__c/fields

# Offer custom object — AutoNumber name field, format OF-{0000}
cat << 'EOF' > force-app/main/default/objects/Offer__c/Offer__c.object-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>Offer</label>
    <pluralLabel>Offers</pluralLabel>
    <nameField>
        <displayFormat>OF-{0000}</displayFormat>
        <label>Offer Name</label>
        <type>AutoNumber</type>
    </nameField>
    <sharingModel>ReadWrite</sharingModel>
    <deploymentStatus>Deployed</deploymentStatus>
</CustomObject>
EOF
```

**Specification:** Label `Offer`, Plural Label `Offers`, Record Name `Offer Name`, Data Type Auto Number, Display Format `OF-{0000}`, Starting Number 1 (`AutoNumber` fields start at 1 by default, so no explicit `<startingNumber>` element is required for the deploy to match).

### 2. `[REQ-4.1.C1.2]` & `[REQ-4.1.C1.3]` Create Offer Amount and Provision FLS — `[CLI]`

**No browser needed — run these commands directly.**

**Specification:** Data Type Currency, Field Label `Offer Amount`, Field Name `Offer_Amount__c`, Precision 18, Scale 2.

```bash
# Offer_Amount__c Currency field — not required, so it needs explicit FLS below
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Offer_Amount__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Offer_Amount__c</fullName>
    <label>Offer Amount</label>
    <precision>18</precision>
    <required>false</required>
    <scale>2</scale>
    <type>Currency</type>
</CustomField>
EOF

# Not required — needs explicit FLS to avoid the Ghost Field anti-pattern (Rule 2.1)
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Offer_Amount__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

### 3. `[REQ-4.1.C1.4]` & `[REQ-4.1.C1.5]` Create Target Close Date and Provision FLS — `[CLI]`

**No browser needed — run these commands directly.**

**Specification:** Data Type Date, Field Label `Target Close Date`, Field Name `Target_Close_Date__c`.

```bash
# Target_Close_Date__c Date field — not required, so it needs explicit FLS below
cat << 'EOF' > force-app/main/default/objects/Offer__c/fields/Target_Close_Date__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Target_Close_Date__c</fullName>
    <label>Target Close Date</label>
    <required>false</required>
    <type>Date</type>
</CustomField>
EOF

# Not required — needs explicit FLS to avoid the Ghost Field anti-pattern (Rule 2.1)
sed -i '/<\/Profile>/i \    <fieldPermissions>\n        <editable>true</editable>\n        <field>Offer__c.Target_Close_Date__c</field>\n        <readable>true</readable>\n    </fieldPermissions>' force-app/main/default/profiles/Admin.profile-meta.xml
```

### 4. `[REQ-4.1.C1.DEP]` Atomic Deploy of Offer Schema and FLS — `[CLI]`

**No browser needed — run this command directly.**

Per Rule 1.2, object schema and profile security deploy together, atomically, in one command — never as two separate deploys that could land out of order.

```bash
# Deploy Offer__c's schema and its Admin profile FLS grants atomically (Rule 1.2)
sf project deploy start \
  -d force-app/main/default/objects/Offer__c \
  -d force-app/main/default/profiles \
  -o trailhead-playground \
  --json
```

### 5. `[REQ-4.1.C1.AUD]` Audit Offer Schema via Tooling API — `[CLI]`

**No browser needed — run this command directly.**

```bash
# Verify Offer__c's fields and their data types via the Tooling API
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  --json \
  -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'"
```

---

## Resources & Reference Documentation

No additional Trailhead Help links were included in this unit's raw scrape (`docs/trails/developer_beginner/badges/04_data_modeling/raw/UNIT_1_RAW_GUIDED_ACTIVITY.md`) — the unit's only linked source is the Trailhead unit page itself, already captured in the header above.

---

## Technical Post-Mortem & Engineering Learnings

1. **The "Ghost Field" Anti-Pattern (Hiccup → Resolution):**
   - **Hiccup:** Deploying a `CustomField` XML file alone physically instantiates the column, but Salesforce sets Field-Level Security to invisible/non-editable for every profile by default. Without a paired `fieldPermissions` deploy, the field is 100% invisible in the GUI, SOQL queries referencing it fail with `No such column`, and Trailhead's verification check fails.
   - **Resolution:** Schema (`CustomField`) and security (`fieldPermissions`) deploy as a single atomic unit (Rule 2.1), using non-interactive `sed -i '/<\/Profile>/i ...'` stream editing as the CLI equivalent of checking the GUI wizard's visibility boxes (Rule 3.2). Confirmed live: `Offer__c.Offer_Amount__c` and `Offer__c.Target_Close_Date__c` both carry `<editable>true</editable>` / `<readable>true</readable>` entries in `Admin.profile-meta.xml`.

2. **Required-Field FLS Exception (Rule 2.3) Confirmed Against Ground Truth:**
   - **Finding:** `Property__c.Price__c` is `<required>true</required>` in the deployed org. Salesforce auto-grants universal FLS to required fields so users can populate them on record creation — appending explicit `fieldPermissions` for a required field causes the deploy to be _rejected_ outright (`You cannot deploy to a required field`), not merely redundant. Confirmed: `Admin.profile-meta.xml` has zero `fieldPermissions` entries referencing `Property__c.Price__c`. This is the inverse case of Finding 1 above, and both fields being handled correctly (one with FLS, one without) is what an atomic-and-correct deploy looks like.

3. **`precision` Is a Total Digit Count, Not the Wizard's "Length" Field (Hiccup → Resolution):**
   - **Hiccup:** An earlier draft of this doc's `Offer_Amount__c` payload used `<precision>16</precision>` — reading the field spec's "Precision: 16" as the Currency field's total metadata precision. Verified against the deployed `Offer_Amount__c.field-meta.xml`, the actual value is `<precision>18</precision>`.
   - **Resolution:** In `CustomField` metadata, `precision` is the _total_ digit count (integer digits plus `scale`), not just the integer-side "Length" shown in the Setup wizard. A GUI entry of Length 16 / Decimal Places 2 serializes to `<precision>18</precision>` (16 + 2), `<scale>2</scale>`. This doc's payload now uses `precision=18` to match production exactly — a deploy with the old `precision=16` would create a field with a _different_ schema than what's actually live, silently breaking reproducibility even though it would deploy without error.

4. **Custom Tab / App Assignment Never Retrieved Into Source (Known Gap, Not Fabricated):**
   - **Finding:** Trailhead's Guided Activity walks through the Custom Tab wizard (picking a tab icon/style for `Property__c`) and later references a "Properties" tab inside a "Sales" app. Neither `force-app/main/default/tabs/Property__c.tab-meta.xml` nor `force-app/main/default/applications/Sales.app-meta.xml` exists anywhere in this repo — that GUI-authored artifact was apparently never pulled back into source via `sf project retrieve start` (violating Rule 1.1's SSOT directive as a historical fact, not something this doc can fix after the fact).
   - **Resolution/Status:** Left undocumented here rather than guessed. Hand-authoring a `CustomTab` XML with an invented icon/color identifier would repeat exactly the mistake `CLI_GUI_BOUNDARIES.md` warns against (builder-assigned identifiers you wouldn't know without the picker) — with no retrieved file to verify a guess against, it's not safe to fake. If this gets closed later, the correct fix is a one-time `sf project retrieve start -m "CustomTab:Property__c" -m "CustomApplication:Sales"` against the live org, per the `[GUI]` retrieve → deploy pattern in `docs/reference/PIPELINE.md`.

5. **`sharingModel` Drift Is Expected, Not a Bug:**
   - **Finding:** The live `Offer__c.object-meta.xml` shows `<sharingModel>ControlledByParent</sharingModel>`, but this unit's hand-authored payload (and the org's actual state immediately after this unit) used `ReadWrite`. This isn't a discrepancy in _this_ unit's work — `ControlledByParent` is what Salesforce auto-switches an object to once it gains a Master-Detail relationship, which happens in Badge 04 Unit 2 (Object Relationships) when `Offer__c.Property__c` is added. This doc's payload intentionally reflects `Offer__c`'s schema as of _this_ unit, not its current state.

6. **Source-Driven Metadata Tracking:** Defining object names, auto-number formats (`OF-{0000}`), and field types directly in source files (rather than only in the GUI) keeps this repo's `force-app` tree in parity with standard SFDX source-tracking conventions, and is what makes the audit queries in this doc meaningful — they're checking a deploy that came from version control, not an undocumented click-path.
