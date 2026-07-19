# Salesforce DX Project & Developer Learning Repository

**Project:** Dreamhouse Realty & Developer Beginner Trailhead Portfolio  
**Author:** Business Applications Engineering  
**Date:** July 19, 2026

---

## Executive Overview

Salesforce DX (SFDX) brings source-driven development, continuous integration, and version control to the Salesforce Platform. Instead of working directly in an org through a web browser, metadata is tracked as local source files, versioned in Git, and deployed via automated terminal CLI processes and AI Model Context Protocol (`@salesforce/mcp`) tools.

This repository serves as both the **Dreamhouse Realty** project codebase and the complete **Salesforce Developer Beginner Trailhead Portfolio**.

---

## Salesforce Platform Architecture

### Metadata-Driven Architecture

Unlike traditional software stacks where changes must be manually propagated from database schemas to APIs, access controls, and frontend components, Salesforce verticalizes this via metadata:

- **Declarative Schema Updates:** Defining objects and fields automatically generates REST/GraphQL API endpoints.
- **Vertical Security Integration:** Field-level security (FLS) and sharing rules are evaluated dynamically at runtime by the database routing engine.

### Data Virtualization & Multi-Tenancy

To route multi-tenant database requests through shared physical database tables, Salesforce uses a metadata-driven virtualization layer:

- **Dynamic Query Generator:** Translates virtual queries (e.g. querying custom fields) into references to shared physical columns (e.g. `Value42` in universal database tables).
- **Universal Indexer:** Manages custom index records in a dedicated table to prevent query degradation on shared columns.
- **Dynamic Sharing Filters:** Computes user sharing and row-level access permissions at execution runtime.

_(Note: In modern standalone systems like PostgreSQL, this virtualized multi-tenant structure can be handled natively using **JSONB schemas**, **GIN/Expression Indexes**, and native database-level **Row-Level Security (RLS)**)._

---

## Lightning Web Components (LWC) Architecture

LWC is a modern standards-based UI framework built natively on browser web components (Custom Elements, Shadow DOM, and HTML templates), bypassing heavy client-side framework wrapper overhead.

### React Developer Concept Mapping

| React Feature / Hook             | LWC Equivalent      | Description                                                                                       |
| :------------------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| **Component Props**              | `@api propertyName` | Public reactive properties exposed to parent components.                                          |
| **Component State / `useState`** | Class Fields        | LWC class fields are reactive by default; modifying them triggers a rerender.                     |
| **Side Effects / `useEffect`**   | Lifecycle Hooks     | `connectedCallback()` (insert), `renderedCallback()` (render), `disconnectedCallback()` (remove). |
| **Event Emission**               | `CustomEvent`       | Handled via standard DOM dispatch: `this.dispatchEvent(new CustomEvent('name'))`.                 |

---

## Project & Documentation Structure

- **`force-app/main/default/`** - Package source directory containing custom objects (`Offer__c`, `Property__c`, `Energy_Audit__c`), Apex classes, LWCs, and profiles.
- **`docs/REPORT.md`** - Global Trailhead progress report and roadblocks.
- **`docs/SALESFORCE_DEVELOPMENT_RULES.md`** - Mandatory Salesforce CLI & MCP Server Development Rules.
- **`docs/trails/developer_beginner/`** - Developer Beginner Trailhead Dashboard and 10 numbered badge directories (`01_` through `10_`).

---

## Hybrid SFDX CLI + `--json` Protocol

All developer activities from **Badge 05 onwards** adhere to the **Hybrid SFDX CLI + `--json` Protocol**:

```bash
sf project deploy start -d force-app/main/default/objects/Energy_Audit__c -o trailhead-playground --json
```

- **100% Hands-On CLI Mastery:** Engineers execute terminal commands, mastering SFDX flags (`-d`, `-o`, `-q`, `--use-tooling-api`).
- **100% Deterministic JSON Traceability:** Appending `--json` forces the CLI to output structured, unformatted JSON payloads matching MCP RPC standards for auditability.

---

## Prerequisites & Common CLI Commands

### Prerequisites

- **Salesforce CLI** (`sf`)
- **VS Code with Salesforce Extension Pack**
- **Salesforce Trailhead Playground Org** (`curious-impala-2bl463`)

### Common Commands

- `sf org login web --alias trailhead-playground`: Authorize target org
- `sf org open -o trailhead-playground`: Open org in browser
- `sf project deploy start -d <path> -o trailhead-playground --json`: Deploy metadata with JSON payload
- `sf project retrieve start -m <metadata> -o trailhead-playground`: Retrieve metadata from org
- `sf data query -o trailhead-playground --use-tooling-api -q "<SOQL>"`: Query Tooling API
