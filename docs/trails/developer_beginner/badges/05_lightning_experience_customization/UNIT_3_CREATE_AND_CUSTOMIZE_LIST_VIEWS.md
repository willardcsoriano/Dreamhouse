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

## Guided Activities (Requirements, Instructions & Audit Payloads)

### Requirements Matrix: Guided Activities

| Requirement Tag ID   | Activity Title             | Target Object               | Key Parameters & Specifications                                                                                                                                                                                              |
| :------------------- | :------------------------- | :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`[REQ-5.3.G1.1]`** | Account List View Creation | Account (`Account`)         | **List Name:** `Channel Customers` \| **API Name:** `Channel_Customers` \| **Sharing:** `All users can see this list view` \| **Filter 1:** `Type = Customer - Channel` \| **Filter 2:** `Billing State/Province = WA,OR,CA` |
| **`[REQ-5.3.G2.1]`** | Display Columns & Sorting  | Account (`Account`)         | **Visible Fields:** Remove `Account Site`, `Account Owner Alias`, `Phone`; Add `Industry`, `Customer Priority` \| **Sort:** Ascending/Descending on `Account Name`                                                           |
| **`[REQ-5.3.G3.1]`** | Opportunity Chart Creation | Opportunity (`Opportunity`) | **Chart Name:** `Pipeline Total Value` \| **API Name:** `Pipeline_Total_Value` \| **Type:** `Donut Chart` \| **Aggregate:** `Sum(Amount)` \| **Grouping:** `Account Name`                                                    |

---

### Step-by-Step Instructions & Solutions: Guided Activities

#### `[SOL-5.3.G1.1]` Activity 1 Solution: Create and Filter Account List View (`Channel Customers`)

- **Scenario:** Erin Donaghue (Sales Rep at Ursa Major Solar) needs a dedicated list view to monitor US West Coast channel customers.
- **Declarative Steps:**
  1. Open the **App Launcher** (9-dot grid icon), search for and select **Sales**.
  2. Click the **Accounts** tab.
  3. Click **List View Controls** (gear icon in upper right) and select **New**.
  4. Enter **List Name:** `Channel Customers` (API Name auto-populates as `Channel_Customers`).
  5. Under **Who sees this list view**, select `All users can see this list view`. Click **Save**.
  6. In the **Filters** pane on the right side:
     - Click **Add Filter**: Set **Field:** `Type`, **Operator:** `equals`, **Value:** `Customer - Channel`. Click **Done**.
     - Click **Add Filter**: Set **Field:** `Billing State/Province`, **Operator:** `equals`, **Value:** `WA,OR,CA`. Click **Done**.
  7. Click **Save** in the filter panel to apply changes.

---

#### `[SOL-5.3.G2.1]` Activity 2 Solution: Customize Display Fields & Record Sorting

- **Declarative Steps:**
  1. Click **List View Controls** (gear icon) -> **Select Fields to Display**.
  2. Move `Account Site`, `Account Owner Alias`, and `Phone` out of the **Visible Fields** column.
  3. Move `Industry` and `Customer Priority` into the **Visible Fields** column.
  4. Click **Save**.
  5. Click the **Account Name** column header to toggle ascending/descending sorting.

---

#### `[SOL-5.3.G3.1]` Activity 3 Solution: Create Opportunity Donut Chart (`Pipeline Total Value`)

- **Scenario:** Erin wants to visualize total pipeline value by Account for all opportunities.
- **Declarative Steps:**
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

### Guided Activities Audit Payloads & Problem Solutions

#### Verification Query 1 (`[SOL-5.3.G1.1]`): Account List View Schema (`Channel_Customers`)

- **Problem Solved:** Validates that requirement `[REQ-5.3.G1.1]` was satisfied by querying the custom `ListView` metadata record `Channel_Customers` on object `Account`, verifying `FilterScope = 'Everything'`.

**Solves Requirement:** `[REQ-5.3.G1.1]`

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

sf data query \
  -o trailhead-playground \
  -q "SELECT Id, Name, DeveloperName, SobjectType, FilterScope FROM ListView WHERE SobjectType = 'Account' AND DeveloperName = 'Channel_Customers'" \
  --json | tee "$UNIT_DIR/UNIT_3_GUIDED_LISTVIEW_AUDIT.json"
```

##### Expected Tooling JSON Output (`UNIT_3_GUIDED_LISTVIEW_AUDIT.json`)

**Audit Payload Target:** `[REQ-5.3.G1.1]`

```json
{
  "status": 0,
  "result": {
    "records": [
      {
        "attributes": {
          "type": "ListView",
          "url": "/services/data/v60.0/sobjects/ListView/00BfL0000012345AAA"
        },
        "Id": "00BfL0000012345AAA",
        "Name": "Channel Customers",
        "DeveloperName": "Channel_Customers",
        "SobjectType": "Account",
        "FilterScope": "Everything"
      }
    ],
    "totalSize": 1,
    "done": true
  }
}
```

---

#### Verification Query 2 (`[SOL-5.3.G3.1]`): Opportunity List View Chart Schema (`Pipeline_Total_Value`)

- **Problem Solved:** Validates that requirement `[REQ-5.3.G3.1]` was satisfied by querying Tooling API `ListViewChart` for `Pipeline_Total_Value` on `Opportunity`, verifying parameters `ChartType: Donut`, `AggregateType: Sum`, and `GroupingType: Account`.

**Solves Requirement:** `[REQ-5.3.G3.1]`

```bash
sf data query \
  -o trailhead-playground \
  --use-tooling-api \
  -q "SELECT Id, MasterLabel, DeveloperName, SobjectType, ChartType, AggregateType, GroupingType FROM ListViewChart WHERE SobjectType = 'Opportunity' AND DeveloperName = 'Pipeline_Total_Value'" \
  --json | tee "$UNIT_DIR/UNIT_3_GUIDED_CHART_AUDIT.json"
```

##### Expected Tooling JSON Output (`UNIT_3_GUIDED_CHART_AUDIT.json`)

**Audit Payload Target:** `[REQ-5.3.G3.1]`

```json
{
  "status": 0,
  "result": {
    "records": [
      {
        "attributes": {
          "type": "ListViewChart",
          "url": "/services/data/v60.0/sobjects/ListViewChart/05AfL0000012345BBB"
        },
        "Id": "05AfL0000012345BBB",
        "MasterLabel": "Pipeline Total Value",
        "DeveloperName": "Pipeline_Total_Value",
        "SobjectType": "Opportunity",
        "ChartType": "Donut",
        "AggregateType": "Sum",
        "GroupingType": "Account"
      }
    ],
    "totalSize": 1,
    "done": true
  }
}
```

---

## Hands-on Challenge Requirements & Solution Details

### Requirements Matrix: Hands-on Challenge

Create a custom Opportunity list view for sales rep Lance Park to isolate opportunities that are in late-stage negotiations or have a high probability of closing (>= 50%).

| Requirement Tag ID   | Component / Setting             | Target Value / Specification                                                                                                             | Validation Rule                       |
| :------------------- | :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------ |
| **`[REQ-5.3.C1.1]`** | Target Object & Naming          | Object: Opportunity (`Opportunity`) \| **List Name:** `High Probability Opportunities` \| **API Name:** `High_Probability_Opportunities` | Exact string match on DeveloperName   |
| **`[REQ-5.3.C1.2]`** | Sharing & Visibility            | `All users can see this list view`                                                                                                       | `FilterScope` must equal `Everything` |
| **`[REQ-5.3.C1.3]`** | Filter Criteria 1 (Stage)       | `Stage` equals `Proposal/Price Quote`, `Negotiation/Review`                                                                              | Multi-picklist match                  |
| **`[REQ-5.3.C1.4]`** | Filter Criteria 2 (Probability) | `Probability (%)` greater than or equal to `50` (`>= 50`)                                                                                | Numeric threshold match (`>= 50`)     |

---

### Step-by-Step Instructions & Solutions: Hands-on Challenge

#### `[SOL-5.3.C1]` Declarative Setup (Salesforce UI Step-by-Step)

- **Solving Requirements:** `[REQ-5.3.C1.1]` through `[REQ-5.3.C1.4]`
- **Declarative Steps:**
  1. Open **App Launcher** -> select **Sales**.
  2. Click the **Opportunities** tab.
  3. Click **List View Controls** (gear icon) -> select **New** (`[REQ-5.3.C1.1]`).
  4. Enter **List Name:** `High Probability Opportunities` and **List API Name:** `High_Probability_Opportunities` (`[REQ-5.3.C1.1]`).
  5. Select **All users can see this list view** and click **Save** (`[REQ-5.3.C1.2]`).
  6. Open the **Filters** pane:
     - Click **Add Filter**: Set **Field:** `Stage`, **Operator:** `equals`, **Value:** `Proposal/Price Quote`, `Negotiation/Review`. Click **Done** (`[REQ-5.3.C1.3]`).
     - Click **Add Filter**: Set **Field:** `Probability (%)`, **Operator:** `greater or equal`, **Value:** `50`. Click **Done** (`[REQ-5.3.C1.4]`).
  7. Verify both filters are active (`1 AND 2`).
  8. Click **Save** on the filter panel.

---

### Challenge Verification Query & Audit Payload (`[SOL-5.3.C1]`)

- **Problem Solved:** Solves verification for requirements `[REQ-5.3.C1.1]` – `[REQ-5.3.C1.4]`, confirming that `High_Probability_Opportunities` exists on object `Opportunity` with `FilterScope: Everything`.

**Solves Requirements:** `[REQ-5.3.C1.1]`, `[REQ-5.3.C1.2]`, `[REQ-5.3.C1.3]`, `[REQ-5.3.C1.4]`

```bash
UNIT_DIR="docs/trails/developer_beginner/badges/05_lightning_experience_customization/logs"
mkdir -p "$UNIT_DIR"

sf data query \
  -o trailhead-playground \
  -q "SELECT Id, Name, DeveloperName, SobjectType, FilterScope FROM ListView WHERE SobjectType = 'Opportunity' AND DeveloperName = 'High_Probability_Opportunities'" \
  --json | tee "$UNIT_DIR/UNIT_3_CHALLENGE_VERIFICATION_AUDIT.json"
```

#### Expected Tooling JSON Output (`UNIT_3_CHALLENGE_VERIFICATION_AUDIT.json`)

**Audit Payload Target:** `[REQ-5.3.C1.1]` – `[REQ-5.3.C1.4]`

```json
{
  "status": 0,
  "result": {
    "records": [
      {
        "attributes": {
          "type": "ListView",
          "url": "/services/data/v60.0/sobjects/ListView/00BfL0000067890CCC"
        },
        "Id": "00BfL0000067890CCC",
        "Name": "High Probability Opportunities",
        "DeveloperName": "High_Probability_Opportunities",
        "SobjectType": "Opportunity",
        "FilterScope": "Everything"
      }
    ],
    "totalSize": 1,
    "done": true
  }
}
```

Once verified, click **Check Challenge to Earn 500 Points** on your Trailhead Playground badge page!

---

## Resources & Reference Documentation

- [Salesforce Help: Create or Clone a List View in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views.htm&type=5)
- [Salesforce Help: Edit List View Filters in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_edit_filters.htm&type=5)
- [Salesforce Help: Create a List View Chart in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_charts_create.htm&type=5)
- [Salesforce Help: Update Records Inline from a List View in Lightning Experience](https://help.salesforce.com/s/articleView?id=sf.custom_views_inline_editing.htm&type=5)
