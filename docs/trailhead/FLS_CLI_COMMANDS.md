# CLI Command Log: Diagnosing & Fixing the Offer FLS Trailhead Failure

## Overview

This is a copy-paste-ready command log of the exact `sf` CLI sequence that diagnosed and resolved the Trailhead field-level-security (FLS) failure described in `TRAILHEAD_TROUBLESHOOTING.md`. Where that file explains _why_ the error happened, this one is a terse runbook of _what was actually typed_, in order, so the same sequence can be replayed quickly the next time a Trailhead challenge falsely reports a field as missing or wrong-typed. Replace `Offer__c`/field names/`<org>` with the object, fields, and org alias relevant at the time. Commands are grouped into three phases: confirm the org connection, diagnose schema vs. access, then fix and reverify.

---

## Table of Contents

- [Overview](#overview)
- [1. Confirm You're Connected to the Right Org](#1-confirm-youre-connected-to-the-right-org)
- [2. Diagnose: Does the Field Exist, and Is It Accessible?](#2-diagnose-does-the-field-exist-and-is-it-accessible)
- [3. Confirm Who You're Checking As](#3-confirm-who-youre-checking-as)
- [4. Fix: Grant FLS via a Profile Metadata Deploy](#4-fix-grant-fls-via-a-profile-metadata-deploy)
- [5. Reverify](#5-reverify)
- [Related Commands Used Along the Way (Useful, But Not Part of the Fix)](#related-commands-used-along-the-way-useful-but-not-part-of-the-fix)

## 1. Confirm You're Connected to the Right Org

Trailhead validates whatever org/username its challenge page shows as your connected Hands-on Org — confirm the CLI is authenticated to that same org before diagnosing anything else.

```bash
sf org list --json
sf org display -o <org-alias> --json
```

## 2. Diagnose: Does the Field Exist, and Is It Accessible?

Run these three in order. Tooling API queries bypass the CLI's own describe cache, which can otherwise show stale results right after a deploy.

```bash
# Schema-level existence + real type (bypasses describe caching)
sf data query -o <org-alias> --use-tooling-api -q \
  "SELECT QualifiedApiName, DataType FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName = '<Object__c>'"

# Object-level permissions (Read/Create/Edit) for every profile/permission set
sf data query -o <org-alias> -q \
  "SELECT SobjectType, PermissionsRead, PermissionsCreate, PermissionsEdit, Parent.Profile.Name
   FROM ObjectPermissions WHERE SobjectType='<Object__c>'"

# Field-level permissions (Read/Edit) for every profile/permission set — the one that was empty
sf data query -o <org-alias> -q \
  "SELECT Field, PermissionsRead, PermissionsEdit, Parent.Profile.Name
   FROM FieldPermissions WHERE SobjectType='<Object__c>'"
```

**Read the result:** field shows up in `FieldDefinition` with the right `DataType`, but `FieldPermissions` returns zero rows (or `PermissionsRead: false`) for the profile you're checking as → it's an FLS gap, not a missing/mistyped field.

## 3. Confirm Who You're Checking As

```bash
sf data query -o <org-alias> -q \
  "SELECT Username, Profile.Name FROM User WHERE Username='<your-playground-username>'"
```

## 4. Fix: Grant FLS via a Profile Metadata Deploy

Create (or extend) `force-app/main/default/profiles/Admin.profile-meta.xml` — `Admin` is the file/API name for the "System Administrator" profile — with a `fieldPermissions` block per field:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Profile xmlns="http://soap.sforce.com/2006/04/metadata">
    <fieldPermissions>
        <editable>true</editable>
        <field><Object__c>.<Field__c></field>
        <readable>true</readable>
    </fieldPermissions>
</Profile>
```

Deploy just the profile directory (a partial deploy — only listed `fieldPermissions` entries are added/updated, nothing else in the profile is touched):

```bash
sf project deploy start -d force-app/main/default/profiles -o <org-alias>
```

## 5. Reverify

Rerun the `FieldPermissions` query from step 2 — it should now show `PermissionsRead: true, PermissionsEdit: true` for the profile. Then retry the Trailhead **Check Challenge** button.

```bash
sf data query -o <org-alias> -q \
  "SELECT Field, PermissionsRead, PermissionsEdit, Parent.Profile.Name
   FROM FieldPermissions WHERE SobjectType='<Object__c>'"
```

## Related Commands Used Along the Way (Useful, But Not Part of the Fix)

These confirmed the deploy itself succeeded and ruled out a stale-cache false negative — worth knowing about, but they weren't what actually solved the problem:

```bash
# Deploy a field/object change
sf project deploy start -d force-app/main/default/objects/<Object__c> -o <org-alias>

# CLI's own describe — can lag behind a fresh deploy, don't trust it alone
sf sobject describe -s <Object__c> -o <org-alias> --json

# Retrieve the live metadata as currently deployed in the org (must target a dir inside the project)
sf project retrieve start -m CustomObject:<Object__c> -o <org-alias> -r <project-relative-dir>
```
