# Unit 6: Create Custom Buttons and Links

**Badge:** Lightning Experience Customization  
**Trail:** Developer Beginner  
**File Link (Absolute):** [UNIT_6_CREATE_AND_CUSTOMIZE_BUTTONS_AND_LINKS.md](file:///home/willard/repos/Dreamhouse/docs/trails/developer_beginner/badges/05_lightning_experience_customization/UNIT_6_CREATE_AND_CUSTOMIZE_BUTTONS_AND_LINKS.md)

---

## Overview

In this unit, custom buttons and links are created to integrate Salesforce data with external URLs and applications directly from record details and related lists.

### Objectives & Key Concepts

1. **Custom List Button:** Appears on a related list on an object record page (e.g., `Audit Guidelines` custom button on the `Energy_Audit__c` related list on `Account`).
2. **Custom Detail Page Link:** Appears in the Custom Links section of a record detail page (e.g., `Google This Account` on `Account`).
3. **Custom Detail Page Button:** Appears in the action menu / highlights panel of a record page (e.g., `Map Location` on `Account`).
4. **Hands-on Challenge:** Create a custom button `Google Info` (`Google_Info`) on the `Contact` object pointing to `https://www.google.com/search?q={!Contact.Name}` and add it to the `Contact Layout`.

---

## Troubleshooting & Verification Notes

### Troubleshooting Note: GUI Record Visibility & List View Filtering

- **Observed Behavior:** The `GenePoint` Account record and its related `GenePoint 5-year review` Energy Audit record appeared missing when attempting to access the Accounts tab in the Salesforce Lightning GUI (`filterName=__Recent`).
- **Root Cause Diagnosis:**
  1. Records created or queried programmatically via the Salesforce CLI (`sf data create` / `sf data query`) exist in the org database but do not automatically register in the browser-specific **Recently Viewed** (`__Recent`) list view until accessed directly in the GUI.
  2. `GenePoint` is an **Account** record, whereas `GenePoint 5-year review` is a child **Energy Audit** (`Energy_Audit__c`) record linked to `GenePoint` via a lookup relationship (`Account__c`).
- **Empirical CLI Verification:**
  ```bash
  sf data query -q "SELECT Id, Name, Type, Phone, Industry FROM Account WHERE Name LIKE '%GenePoint%'"
  ```
  _Result:_ Returned 1 record (`Id: 001dL00002LjoYOQAZ`), confirming database presence.
- **GUI Resolution Procedure:**
  1. Open the **Accounts** tab in Lightning Experience.
  2. Switch the list view filter from **Recently Viewed** to **All Accounts**.
  3. Open the **GenePoint** account record, select the **Related** tab, and scroll down to the **Energy Audits** related list to locate **GenePoint 5-year review**.

---

## Hands-on Challenge Specifications

- **Target Object:** `Contact`
- **Button Label:** `Google Info`
- **Button Name:** `Google_Info`
- **Display Type:** Detail Page Button
- **Content Source:** URL (`https://www.google.com/search?q={!Contact.Name}`)
- **Page Layout Assignment:** `Contact Layout` (`Contact-Contact Layout`)
