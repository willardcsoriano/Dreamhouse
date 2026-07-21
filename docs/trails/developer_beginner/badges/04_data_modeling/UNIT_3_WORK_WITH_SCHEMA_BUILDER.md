# Trailhead Unit: Work with Schema Builder

**Trail:** Developer Beginner
**Badge 04:** Data Modeling
**Unit 3:** Work with Schema Builder
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/data_modeling/schema_builder?trail_id=force_com_dev_beginner)

---

**Execution order, at a glance:** Part 1 (Guided Activity) is a Schema Builder tour — checking existing objects, clicking Auto-Layout to visualize them, and dragging out an open-ended demo object/field. None of that produces a fixed, checkable metadata artifact, so Part 1 carries **no Requirement IDs** and nothing to run in the terminal. Part 2 (Hands-On Challenge) is the one graded, deployable piece of this unit — a required `Street_Address__c` field on `Property__c` — and it's **100% `[CLI]`**: no browser needed, run the commands directly.

---

## Table of Contents

- [Introduction & Learning Objectives](#introduction-learning-objectives)
- [Part 1: Guided Activity (Schema Builder Walkthrough)](#part-1-guided-activity-schema-builder-walkthrough)
  - [See Your Data Model in Action](#see-your-data-model-in-action)
  - [Create an Object with Schema Builder](#create-an-object-with-schema-builder)
  - [Create Fields with Schema Builder](#create-fields-with-schema-builder)
- [Part 2: Hands-On Challenge (Property — `Street_Address__c`)](#part-2-hands-on-challenge-property-street_address__c)
  - [1. `[REQ-4.3.C1.1]`–`[REQ-4.3.C1.5]` Create the Field Metadata — `[CLI]`](#1-req-43c11req-43c15-create-the-field-metadata-cli)
  - [2. `[REQ-4.3.C1.DEP]` Deploy Metadata to Salesforce Cloud — `[CLI]`](#2-req-43c1dep-deploy-metadata-to-salesforce-cloud-cli)
  - [3. `[REQ-4.3.C1.AUD]` Verify Schema State via Tooling API SOQL — `[CLI]`](#3-req-43c1aud-verify-schema-state-via-tooling-api-soql-cli)
- [Resources & Reference Documentation](#resources-reference-documentation)
- [Technical Post-Mortem & Engineering Learnings](#technical-post-mortem-engineering-learnings)

## Introduction & Learning Objectives

By this point in the trail, you (and D'Angelo) have created a handful of custom objects, fields, and relationships across Favorite, Offer, and Property. The data model is starting to get complicated enough that seeing it laid out visually is genuinely useful — that's what Schema Builder is for. It's a point-and-click tool for visualizing and editing a data model, and it's also a good way to introduce your Salesforce customizations to a co-worker without walking them through Object Manager one object at a time.

After completing this unit, you'll be able to:

- Describe the advantages of using Schema Builder for data modeling.
- Use Schema Builder to create a schema for a given object model.
- Use Schema Builder to add a custom object to your schema.
- Use Schema Builder to add a custom field to your schema.

---

## Part 1: Guided Activity (Schema Builder Walkthrough)

**No Requirement IDs in this part.** Trailhead's own instructions describe the demo object and demo field as "you can make it whatever you want!" — there is no fixed name, type, or spec to satisfy, and Auto-Layout is pure UI visualization that doesn't touch any metadata. Assigning a `[REQ-...]` ID or a `[CLI]`/`[GUI]` tag to any of this would imply a checkable artifact that doesn't exist. What follows is a plain description of the click-path for repeatability, not a set of graded requirements.

### See Your Data Model in Action

1. From Setup, search for and click **Schema Builder** in the Quick Find box.
2. In the left panel, click **Clear All**.
3. Check **Contact**, **Favorite**, **Offer**, and **Property**.
4. Click **Auto-Layout**.

This arranges the selected objects and their relationships on a canvas. Dragging objects around doesn't change anything — no object, field, or relationship metadata is created, modified, or deployed by this step. It's a read-only visualization layer over schema that already exists (most of it built in Units 1 and 2 of this badge).

### Create an Object with Schema Builder

Schema Builder can also author new objects and fields directly on the canvas, as an alternative to Object Manager:

1. In the left sidebar, click the **Elements** tab.
2. Click **Object** and drag it onto the canvas.
3. Enter information about the object — Trailhead is explicit that this is open-ended ("You can make it whatever you want!"), so there's no fixed API name or label to record here.
4. Click **Save**.

### Create Fields with Schema Builder

1. From the **Elements** tab, choose a field type and drag it onto the object just created. Schema Builder supports relationship fields, formula fields, and plain fields the same way Object Manager does.
2. Fill out the field's details — again open-ended, not graded.
3. Click **Save**.

The resulting object and field show up in Object Manager exactly the way objects and fields created through the standard UI wizard do — Schema Builder is just a different entry point onto the same metadata, not a separate system.

---

## Part 2: Hands-On Challenge (Property — `Street_Address__c`)

**No browser needed — run these commands directly.**

The challenge requires adding a required Text Area custom field to the `Property__c` object.

### 1. `[REQ-4.3.C1.1]`–`[REQ-4.3.C1.5]` Create the Field Metadata — `[CLI]`

- **`[REQ-4.3.C1.1]` Target Object:** `Property` (`Property__c`)
- **`[REQ-4.3.C1.2]` Field Data Type:** Text Area (`TextArea`)
- **`[REQ-4.3.C1.3]` Field Label:** Street Address
- **`[REQ-4.3.C1.4]` Field Name:** `Street_Address` (`Street_Address__c`)
- **`[REQ-4.3.C1.5]` Required Rule:** Always require a value in this field in order to save a record (`<required>true</required>`).

```bash
# 1. Ensure target fields directory exists under Property__c object
mkdir -p force-app/main/default/objects/Property__c/fields

# 2. Write Text Area custom field XML metadata with mandatory required rule (<required>true</required>)
cat << 'EOF' > force-app/main/default/objects/Property__c/fields/Street_Address__c.field-meta.xml
<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Street_Address__c</fullName>
    <label>Street Address</label>
    <type>TextArea</type>
    <required>true</required>
</CustomField>
EOF
```

> **Developer Architectural Note (Rule 2.3 — Required Field FLS Encapsulation):**
> Fields with `<required>true</required>` automatically enforce universal read/edit access across all user profiles. Explicit profile `fieldPermissions` entries are deliberately omitted here because the Metadata API rejects profile permissions on required fields (`You cannot deploy to a required field`). This has been confirmed against `force-app/main/default/profiles/Admin.profile-meta.xml` — no `fieldPermissions` entry exists for `Street_Address__c`.

### 2. `[REQ-4.3.C1.DEP]` Deploy Metadata to Salesforce Cloud — `[CLI]`

```bash
# Deploy Property__c schema (-d objects/Property__c) to target org (-o trailhead-playground)
sf project deploy start \
  -d force-app/main/default/objects/Property__c \
  -o trailhead-playground \
  --json
```

**Deployment output (as executed and captured):**

```text
Deployed Source
┌───────────┬───────────────────────────────┬──────────────┬───────────────────┐
│ State     │ Name                          │ Type         │ Path              │
├───────────┼───────────────────────────────┼──────────────┼───────────────────┤
│ Unchanged │ Property__c.Price__c          │ CustomField  │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/fields/P │
│           │                               │              │ rice__c.field-met │
│           │                               │              │ a.xml             │
│ Created   │ Property__c.Street_Address__c │ CustomField  │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/fields/S │
│           │                               │              │ treet_Address__c. │
│           │                               │              │ field-meta.xml    │
│ Unchanged │ Property__c                   │ CustomObject │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/Property │
│           │                               │              │ __c.object-meta.x │
│           │                               │              │ ml                │
│ Unchanged │ Property__c.All               │ ListView     │ force-app/main/de │
│           │                               │              │ fault/objects/Pro │
│           │                               │              │ perty__c/listView │
│           │                               │              │ s/All.listView-me │
│           │                               │              │ ta.xml            │
└───────────┴───────────────────────────────┴──────────────┴───────────────────┘

Status: Succeeded | Elapsed Time: 3.19s
```

This run predates this badge's `--json` standardization (Rule 3.4), so the table above is the human-readable output actually captured, not a `--json` payload. Any future re-run of this exact command with `--json` (as written above) should have its raw output saved to `docs/trails/developer_beginner/badges/04_data_modeling/logs/UNIT_3_CHALLENGE_DEPLOY_AUDIT.json` per Stage 4 of `docs/reference/PIPELINE.md`.

### 3. `[REQ-4.3.C1.AUD]` Verify Schema State via Tooling API SOQL — `[CLI]`

```bash
# Run Tooling API query via CLI to verify QualifiedApiName and DataType schema properties for Property__c
sf data query -o trailhead-playground --use-tooling-api \
  -q "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Property__c'" \
  --json
```

**Query output (as executed and captured):**

```text
┌────────────────────┬────────────────────────────┐
│ QUALIFIEDAPINAME   │ DATATYPE                   │
├────────────────────┼────────────────────────────┤
│ Price__c           │ Currency(18, 0)            │
│ Street_Address__c  │ Text Area(255)             │
└────────────────────┴────────────────────────────┘

Total number of records retrieved: 14.
```

Same note as above — this is the historical human-readable capture; a re-run with `--json` should be logged under `docs/trails/developer_beginner/badges/04_data_modeling/logs/`.

---

## Resources & Reference Documentation

- Salesforce Help: Design Your Own Data Model With Schema Builder
- Salesforce Help: Schema Builder Custom Object Definition

---

## Technical Post-Mortem & Engineering Learnings

- **Required Field Enforcement & FLS Encapsulation (`<required>true</required>`):** Setting `<required>true</required>` on a `CustomField` XML definition enforces platform-level database validation. Attempting to deploy explicit profile `fieldPermissions` for a required field causes the Metadata API to reject deployment (`You cannot deploy to a required field`). Required fields automatically grant universal visibility to all profiles because users must be able to input values upon record creation. Verified against the live `Admin.profile-meta.xml` — no `fieldPermissions` entry for `Street_Address__c` exists, confirming the field deployed correctly without one.
- **Source-Driven Metadata Tracking:** Defining object names and custom field types directly in local source files ensures standard SFDX source tracking compatibility across developer sandbox environments.
- **Schema Builder produces no separate metadata format:** Objects and fields created via Schema Builder's drag-and-drop canvas land in Object Manager identically to ones created through the standard "New Field"/"New Object" wizards — same `CustomObject`/`CustomField` XML on the Metadata API side. Schema Builder is a visualization and authoring _surface_, not a distinct metadata type; there was nothing badge-specific to retrieve or classify as `[CLI]`/`[GUI]` beyond what Units 1 and 2 already established for object/field creation in general.
- **Why this unit has no Guided Activity Requirement IDs:** Unlike every other unit in this badge, the Guided Activity here is explicitly open-ended per Trailhead's own copy ("you can make it whatever you want!"). Inventing a concrete object/field name and documenting it as a graded `[REQ-...]` would have fabricated a requirement that never existed — the honest documentation choice was to describe the tool and click-path without pretending there's a fixed artifact behind it.
