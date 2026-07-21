# Trailhead Challenge Troubleshooting

## Overview

This is a standalone, quick-lookup reference for Trailhead challenge check failures on this project — kept separate from the broader `DEVELOPER_REFERENCE.md` and `DEVELOPMENT_SETUP.md` docs so it's fast to find the next time a challenge check fails for a non-obvious reason (e.g., after Trailhead re-links the Playground to VS Code/the CLI, or after any future org re-authentication). Each entry below documents a specific misleading Trailhead error message, its real root cause, the exact diagnostic commands used to confirm it, the fix, and any dead-end hypotheses that were tried and ruled out along the way so they aren't retried. Covers four incidents so far: a "field does not exist / wrong type" error that was actually a missing field-level security grant, a wrong-org authentication mismatch that made every challenge check fail regardless of what was deployed, a Files related-list value that isn't in Salesforce's own documentation, and a record-page activation mode that turns out not to be deployable via any API at all.

---

## Table of Contents

- [Overview](#overview)
- [Field-Level Security Not Granted by Metadata API Deploys](#field-level-security-not-granted-by-metadata-api-deploys)
  - [Symptom](#symptom)
  - [Root Cause](#root-cause)
  - [Diagnostic Method](#diagnostic-method)
  - [Fix](#fix)
  - [Ruled-Out Hypothesis: Currency Precision/Scale](#ruled-out-hypothesis-currency-precisionscale)
  - [Prevention Rule](#prevention-rule)
- [Wrong Org Authorized](#wrong-org-authorized)
  - [Symptom](#symptom-1)
  - [Root Cause](#root-cause-1)
  - [Fix](#fix-1)
- [Files Related List Value Not in Salesforce's Own Documentation](#files-related-list-value-not-in-salesforces-own-documentation)
  - [Symptom](#symptom-2)
  - [Root Cause](#root-cause-2)
  - [Diagnostic Method](#diagnostic-method-1)
  - [Fix](#fix-2)
  - [Ruled-Out Values](#ruled-out-values)
  - [Prevention Rule](#prevention-rule-1)
- [Org-Default Record Page Activation Isn't Deployable via Any API](#org-default-record-page-activation-isnt-deployable-via-any-api)
  - [Symptom](#symptom-3)
  - [Root Cause](#root-cause-3)
  - [Diagnostic Method](#diagnostic-method-2)
  - [Fix](#fix-3)
  - [Prevention Rule](#prevention-rule-2)

## Field-Level Security Not Granted by Metadata API Deploys

### Symptom

A custom field is deployed successfully via `sf project deploy start` — the CLI reports `Succeeded`, the field shows up correctly typed in `Schema` describe calls, Tooling API `FieldDefinition` queries, and Object Manager. Yet a downstream consumer that respects field-level security (FLS) — a Trailhead challenge validator, a Lightning page, a report, an integration user — behaves as if the field doesn't exist. For this project specifically, deploying `Offer__c.Offer_Amount__c` (Currency) and `Offer__c.Target_Close_Date__c` (Date) produced this exact Trailhead error on every retry:

```
Challenge not yet complete
The field 'Offer_Amount__c' either does not exist on the Offer__c object or it is not of type currency.
```

...despite the field genuinely existing with the correct type, on the correct org, immediately after a clean deploy.

### Root Cause

**Existence in the schema and visibility to a user are two different layers, and the Metadata API only guarantees the first one.**

- Creating a custom field through the **Setup UI wizard** prompts "Which profiles will have access?" and defaults to granting the current profile (almost always System Administrator) both Read and Edit — this step is easy to miss because it's automatic and silent.
- Creating the exact same field through the **Metadata API** (i.e., `sf project deploy start` against a bare `CustomField` `.field-meta.xml`) does **not** perform this step. No profile — not even System Administrator — gets FLS granted unless a `Profile` or `PermissionSet` metadata component explicitly says so. The field is real, typed correctly, and fully queryable via Tooling API, but every profile's `FieldPermissions` for it are simply absent (not "denied" — _absent_, which resolves to no access).
- Trailhead's challenge validator (and most well-behaved Salesforce client code) checks field access from the perspective of the logged-in user, so an inaccessible-but-existing field surfaces as an "existence" or "type" failure. The error message is misleading — it's really an FLS problem, not a schema problem.
- Object-level permissions (`ObjectPermissions` — Read/Create/Edit on `Offer__c` itself) can be perfectly fine while field-level permissions are still completely missing; they're deployed and checked independently, so a working object with a "missing" field is a strong signal to check FLS next.

### Diagnostic Method

Standard `describe` calls and the CLI's own `sf sobject describe` can be misleading here because of client-side caching layers, so the reliable way to separate "field doesn't exist" from "field exists but is inaccessible" is to query the org directly via SOQL against Tooling/setup entities, bypassing any CLI describe cache:

```bash
# 1. Confirm the field exists in the schema at all, with its real type/precision
sf data query -o <org> --use-tooling-api -q \
  "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = 'Offer__c'"

# 2. Confirm object-level access (Read/Create/Edit) for the running profile
sf data query -o <org> -q \
  "SELECT SobjectType, PermissionsRead, PermissionsCreate, PermissionsEdit, Parent.Profile.Name
   FROM ObjectPermissions WHERE SobjectType='Offer__c'"

# 3. Confirm field-level access (Read/Edit) for the running profile — this is the one that was empty
sf data query -o <org> -q \
  "SELECT Field, PermissionsRead, PermissionsEdit, Parent.Profile.Name
   FROM FieldPermissions WHERE SobjectType='Offer__c'"
```

If step 1 returns the field with the right `DataType` but step 3 returns zero rows (or rows with `PermissionsRead: false`) for the profile the checker/user runs as, FLS is the culprit, not the field definition.

### Fix

Deploy a `Profile` metadata component granting explicit `fieldPermissions` for the field(s) to the relevant profile. The System Administrator profile's metadata file is named `Admin.profile-meta.xml` (a long-standing Salesforce naming quirk — the label is "System Administrator" but the API/file name is `Admin`):

```xml
<!-- force-app/main/default/profiles/Admin.profile-meta.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<Profile xmlns="http://soap.sforce.com/2006/04/metadata">
    <fieldPermissions>
        <editable>true</editable>
        <field>Offer__c.Offer_Amount__c</field>
        <readable>true</readable>
    </fieldPermissions>
    <fieldPermissions>
        <editable>true</editable>
        <field>Offer__c.Target_Close_Date__c</field>
        <readable>true</readable>
    </fieldPermissions>
</Profile>
```

```bash
sf project deploy start -d force-app/main/default/profiles -o <org>
```

This is a partial profile deploy — only the listed `fieldPermissions` entries are added/updated; the rest of the profile's existing configuration is left untouched. Re-running the step 3 query afterward should show `PermissionsRead: true, PermissionsEdit: true` for the profile.

### Ruled-Out Hypothesis: Currency Precision/Scale

While this was being diagnosed, a second, concurrent debugging session (a separate agent instance run in parallel) hypothesized a different cause: the deployed `Offer_Amount__c` field had `precision=18, scale=0`, whereas fields created via the Setup UI default to `precision=16, scale=2`. That session changed and redeployed the field to match the GUI default (`Currency(16, 2)` — confirmed live in the org), reasoning that the mismatched scale might be why the checker considered it "not of type currency."

**This did not fix the issue.** The Trailhead error was identical before and after the scale change, which on its own rules out precision/scale as a cause of an "existence or type" validation error — that class of check reads `DisplayType`/`DataType` (`Currency`), not the numeric precision/scale sub-parameters. The scale change is harmless and now matches conventional GUI-created defaults, so it was kept, but it was not the actual fix. The FLS grant (above) is what resolved the check. If this error resurfaces on a future field, don't spend time adjusting precision/scale — go straight to the `FieldPermissions` query in the Diagnostic Method above.

### Prevention Rule

**Every new custom field deployed via the Metadata API (source-driven / CLI workflow, not the Setup UI) needs an accompanying FLS grant, every time — not just when a checker or user complains.** When adding a `CustomField` to this repo going forward:

1. Create the `.field-meta.xml` under `objects/<Object>/fields/` as usual.
2. In the same change, add or update `fieldPermissions` entries for that field in `force-app/main/default/profiles/Admin.profile-meta.xml` (or the relevant permission set, if this project moves to permission-set-based access later).
3. Deploy both together. Don't treat the profile/permission-set grant as an optional follow-up — a field with no FLS grant is, for practical purposes, a field that doesn't exist to anyone using it through normal UI, Apex-with-sharing, or API access checks.

---

## Wrong Org Authorized

### Symptom

Every Trailhead challenge check fails, regardless of what's actually been built or deployed — including challenges that were previously passing, or metadata that's demonstrably correct in whatever org the CLI is talking to.

### Root Cause

The Salesforce CLI was authenticated to a personal Salesforce Developer org rather than the specific Trailhead Playground the challenge page is checking. Trailhead validates whatever org/username its challenge page shows as your connected Hands-on Org — a browser-side connection that has no relationship to which org `sf` happens to have as its default locally. A deploy can succeed perfectly and still never be seen by the checker if it landed in the wrong org.

### Fix

1. Confirm which org Trailhead expects: open the challenge page and check the username/org shown near **Check Challenge** (or `trailhead.salesforce.com/myplayground`).
2. Compare against the CLI's connected org: `sf org list --json` / `sf org display -o <alias> --json`.
3. If they don't match, authenticate to the correct Playground. If the Playground's auto-generated password is unknown, reset it via the **Playground Starter** app's credentials tab, then re-authenticate:
   ```bash
   sf org login web -a <alias> -s -d
   ```
4. Set it as the default target org so subsequent deploys go to the right place without needing `-o` every time:
   ```bash
   sf config set target-org <alias>
   ```
5. Re-deploy (or simply re-check, if the metadata was already correct) once the CLI and the challenge page agree on the org.

---

## Files Related List Value Not in Salesforce's Own Documentation

### Symptom

Adding a "Files" related list to a page layout via Metadata API — trying documented-sounding values like `AttachedContentDocuments` or `RelatedContentDocumentList` in a `<relatedLists><relatedList>` block — fails deployment every time:

```
Cannot find related list:AttachedContentDocuments
```

or

```
Cannot find related list:RelatedContentDocumentList
```

...even though both names look plausible and follow Salesforce's usual naming conventions for other related lists (`RelatedContactList`, `RelatedOpportunityList`, etc.).

### Root Cause

The Metadata API's `Layout.relatedLists.relatedList` field has no comprehensive published list of valid values — Salesforce's own Metadata API reference just says "the name of the related list," without enumerating them. Multiple plausible-sounding names circulate in blog posts and community answers, but the actual value Salesforce assigns for a Files-type related list is `RelatedFileList` — not either of the more "modern-sounding" ContentDocument-based names that show up in searches.

### Diagnostic Method

No SOQL/Tooling API query reliably returns valid `relatedList` values ahead of time, and checking other already-deployed layouts in the same org for a working example isn't guaranteed to help — Files may not already be present anywhere. The only reliable method: add the Files related list through the classic Page Layout editor's GUI (drag **Files** from the Related Lists palette onto the layout, **Save**), then retrieve that exact layout and read the resulting `<relatedList>` value directly:

```bash
sf project retrieve start -m "Layout:<Object>-<Layout Name>" -o <org> --json
grep -A2 "relatedList" "force-app/main/default/layouts/<Object>-<Layout Name>.layout-meta.xml"
```

### Fix

Use the confirmed value directly — no GUI trip needed on subsequent objects, since this value isn't object-specific:

```xml
<relatedLists>
    <relatedList>RelatedFileList</relatedList>
</relatedLists>
```

### Ruled-Out Values

- `AttachedContentDocuments` — fails with `Cannot find related list:AttachedContentDocuments`
- `RelatedContentDocumentList` — fails with `Cannot find related list:RelatedContentDocumentList`

### Prevention Rule

For any related list type without a confirmed value on file, don't guess from naming convention or blog posts — add it via the GUI once on any layout, retrieve, and read the real value before hand-authoring it elsewhere. `RelatedFileList` is now confirmed for this org/API version; reuse it directly.

---

## Org-Default Record Page Activation Isn't Deployable via Any API

### Symptom

Wanting to assign a Lightning Record Page (`FlexiPage`) as the **Org Default** for an object entirely via CLI/Metadata API, with no metadata type found — `FlexiPage`, `Layout`, `CustomApplication`, nor any Tooling API object — that represents this assignment.

### Root Cause

"Assign as Org Default" record page activation is genuinely not represented in any Salesforce metadata type. Confirmed by checking three separate sources: the `FlexiPage` Metadata API reference (documents `type`, `sobjectType`, and region/component structure, but nothing for default-activation state), the general Metadata API developer guide, and the Tooling API object list. This is a permanent platform limitation, not a documentation gap that better searching would close.

### Diagnostic Method

Retrieve the `FlexiPage` after performing the Org Default activation via the browser, and compare it against the pre-activation version — there is no diff. The activation state genuinely lives outside anything retrievable via source.

### Fix

This one action must be done via browser click every time: Lightning App Builder → **Activation** → **Org Default** → assign form factors (Desktop/Phone) → **Save**. Everything else about a record page — its structure, and its **App, Record Type, and Profile** assignment (a _different_ activation mode) via `profileActionOverrides` on the owning `CustomApplication` — can be deployed via CLI. Only Org Default activation specifically cannot.

### Prevention Rule

Don't spend time searching for a CLI path to Org Default record page activation — it doesn't exist, confirmed. Budget for one browser click per object needing this, and use the retrieve/deploy round trip afterward only to confirm state (it will correctly show `Unchanged`), not to try to capture the assignment itself.
