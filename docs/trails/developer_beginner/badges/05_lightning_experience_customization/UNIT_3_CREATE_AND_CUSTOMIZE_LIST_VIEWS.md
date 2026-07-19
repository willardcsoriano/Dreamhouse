# Trailhead Unit: Create and Customize List Views

**Trail:** Developer Beginner  
**Badge 05:** Lightning Experience Customization  
**Unit 3:** Create and Customize List Views  
**Source URL:** [trailhead.salesforce.com](https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_list?trail_id=force_com_dev_beginner)

---

## Introduction & Learning Objectives

List views are a key productivity tool in Salesforce Lightning Experience, enabling users to sort, filter, customize, visual-chart, and inline-edit record lists without requiring system administrator intervention.

After completing this unit, you’ll be able to:

- Create a custom list view for standard or custom objects.
- Create and configure a custom list view chart.
- Edit, filter, and sort list views for streamlined record management.

---

## Conceptual Overview: What Are List Views?

In Salesforce Lightning Experience, list views present data in tabular format for any standard or custom object. Users can customize filters, displayed columns, field sorting, inline editing, and visual summary charts tailored to their daily workflow.

### Key Capabilities of List Views

1. **Custom List Views & Sharing Settings:** Users can build tailored list views filtered by specific criteria (e.g., Accounts of a specific type or location) and define visibility (`Only I can see`, `All users can see`, or `Share with group of users`).
2. **Column Customization & Inline Editing:** Select which fields to display in columns, reorder display order, and edit record fields directly inline via the pencil icon (editable fields) without needing to navigate to individual record detail pages.
3. **Sorting & Multi-Criteria Filtering:** Sort list records alphanumerically or chronologically by clicking column headers. Apply complex filter logic using standard and custom object fields.
4. **List View Charts:** Visualize list view metrics directly alongside records using Donut, Vertical Bar, or Horizontal Bar charts aggregated by `Sum`, `Count`, or `Average`. List view charts are tied to the underlying object and remain accessible across all list views for that object (except `Recently Viewed`).

---

## Guided Activities (Step-by-Step Instructions)

### Activity 1: Create and Filter a Custom List View (Accounts)

- **Scenario:** Erin Donaghue (Sales Rep at Ursa Major Solar) needs a dedicated list view to monitor US West Coast channel customers.
- **Steps:**
  1. Open the **App Launcher** (9-dot grid icon), search for and select **Sales**.
  2. Click the **Accounts** tab.
  3. Click **List View Controls** (gear icon in upper right) and select **New**.
  4. Enter **List Name:** `Channel Customers` (API Name auto-populates as `Channel_Customers`).
  5. Under **Who sees this list view**, select `All users can see this list view`. Click **Save**.
  6. In the **Filters** pane on the right side:
     - Click **Add Filter**.
     - Set **Field:** `Type`, **Operator:** `equals`, **Value:** `Customer - Channel`. Click **Done**.
     - Click **Add Filter**.
     - Set **Field:** `Billing State/Province`, **Operator:** `equals`, **Value:** `WA,OR,CA`. Click **Done**.
  7. Click **Save** in the filter panel to apply changes.

### Activity 2: Customize Display Fields & Record Sorting

- **Steps:**
  1. Click **List View Controls** (gear icon) -> **Select Fields to Display**.
  2. Move `Account Site`, `Account Owner Alias`, and `Phone` out of the **Visible Fields** column.
  3. Move `Industry` and `Customer Priority` into the **Visible Fields** column.
  4. Click **Save**.
  5. Click the **Account Name** column header to toggle ascending/descending sorting.

### Activity 3: Create a List View Chart (Opportunities)

- **Scenario:** Erin wants to visualize total pipeline value by Account for all opportunities.
- **Steps:**
  1. In the **Sales** app, click the **Opportunities** tab.
  2. Select the **All Opportunities** list view from the dropdown menu.
  3. Click the **Charts** icon (bar graph icon in the upper right toolbar).
  4. In the Charts panel, click the gear icon and select **New Chart**.
  5. Configure chart parameters:
     - **Chart Name:** `Pipeline Total Value`
     - **Chart Type:** `Donut Chart`
     - **Aggregate Type:** `Sum`
     - **Aggregate Field:** `Amount`
     - **Grouping Field:** `Account Name`
  6. Click **Save**.

---

## Hands-on Challenge Requirements & Solution Details

### Challenge Goal

Create a custom Opportunity list view for sales rep Lance Park to isolate opportunities that are in late-stage negotiations or have a high probability of closing (>= 50%).

### Specifications & Requirements

| Property                   | Value / Requirement                                         |
| :------------------------- | :---------------------------------------------------------- |
| **Target Object**          | Opportunity (`Opportunity`)                                 |
| **List Name**              | `High Probability Opportunities`                            |
| **List API Name**          | `High_Probability_Opportunities`                            |
| **Sharing Setting**        | `All users can see this list view`                          |
| **Filter 1 (Stage)**       | `Stage` equals `Proposal/Price Quote`, `Negotiation/Review` |
| **Filter 2 (Probability)** | `Probability (%)` greater than or equal to `50`             |

### Declarative Setup (Salesforce UI Step-by-Step)

1. Open **App Launcher** -> select **Sales**.
2. Click the **Opportunities** tab.
3. Click **List View Controls** (gear icon) -> select **New**.
4. Enter **List Name:** `High Probability Opportunities` and **List API Name:** `High_Probability_Opportunities`.
5. Select **All users can see this list view** and click **Save**.
6. Open the **Filters** pane:
   - Click **Add Filter**:
     - **Field:** `Stage`
     - **Operator:** `equals`
     - **Value:** `Proposal/Price Quote`, `Negotiation/Review`
     - Click **Done**.
   - Click **Add Filter**:
     - **Field:** `Probability (%)`
     - **Operator:** `greater or equal`
     - **Value:** `50`
     - Click **Done**.
7. Verify both filters are active (`1 AND 2`).
8. Click **Save** on the filter panel.

---

## Verification Query & SFDX CLI Commands

Verify the `ListView` record creation in your Trailhead Playground org via SOQL using `sf data query`:

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

sf data query \
  -o trailhead-playground \
  -q "SELECT Id, Name, DeveloperName, SobjectType, FilterScope FROM ListView WHERE SobjectType = 'Opportunity' AND DeveloperName = 'High_Probability_Opportunities'" \
  --json | tee "$UNIT_DIR/UNIT_3_VERIFICATION_AUDIT.json"
```

---

## Resources & Reference Documentation

- [Salesforce Help: Create or Clone a List View in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views.htm&type=5)
- [Salesforce Help: Edit List View Filters in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_edit_filters.htm&type=5)
- [Salesforce Help: Create a List View Chart in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_charts_create.htm&type=5)
- [Salesforce Help: Update Records Inline from a List View in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_inline_editing.htm&type=5)
