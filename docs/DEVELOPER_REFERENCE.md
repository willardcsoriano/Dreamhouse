# Dreamhouse Developer Reference Guide

## Overview

This is a concise technical reference for Salesforce development on the Dreamhouse Realty project, covering platform architecture and Lightning Web Components. Section 1 explains how Salesforce's metadata-driven, multi-tenant architecture differs from a traditional app-plus-database stack. Section 2 maps LWC concepts to their React equivalents for developers coming from a JS framework background. Environment and CLI/deployment troubleshooting now lives in its own dedicated guide (`DEVELOPMENT_SETUP.md`) rather than being duplicated here, and Trailhead challenge-check failures have their own reference in `../trailhead/TROUBLESHOOTING.md`.

---

## Table of Contents

- [Overview](#overview)
- [1. Salesforce Platform Architecture](#1-salesforce-platform-architecture)
  - [Metadata-Driven Architecture](#metadata-driven-architecture)
  - [Data Virtualization & Multi-Tenancy](#data-virtualization-multi-tenancy)
- [2. Lightning Web Components (LWC)](#2-lightning-web-components-lwc)
  - [React Developer Concept Mapping](#react-developer-concept-mapping)
- [3. Where Setup & Troubleshooting Content Lives](#3-where-setup-troubleshooting-content-lives)

## 1. Salesforce Platform Architecture

### Metadata-Driven Architecture

Unlike traditional software stacks where changes must be manually propagated from database schemas to APIs, access controls, and frontend components, Salesforce verticalizes this via metadata:

- **Declarative Schema Updates:** Defining objects and fields automatically generates REST/GraphQL API endpoints.
- **Vertical Security Integration:** Field-level security (FLS) and sharing rules are evaluated dynamically at runtime by the database routing engine.

### Data Virtualization & Multi-Tenancy

To route multi-tenant database requests through shared physical database tables, Salesforce uses a metadata-driven virtualization layer:

- **Dynamic Query Generator:** Translates virtual queries (e.g., querying custom fields) into references to shared physical columns (e.g., `Value42` in universal database tables).
- **Universal Indexer:** Manages custom index records in a dedicated table to prevent query degradation on shared columns.
- **Dynamic Sharing Filters:** Computes user sharing and row-level access permissions at execution runtime.

_(Note: In modern standalone systems like PostgreSQL, this virtualized multi-tenant structure can be handled natively using **JSONB schemas**, **GIN/Expression Indexes**, and native database-level **Row-Level Security (RLS)**)._

---

## 2. Lightning Web Components (LWC)

LWC is a modern standards-based UI framework built natively on browser web components (Custom Elements, Shadow DOM, and HTML templates), bypassing heavy client-side framework wrapper overhead.

### React Developer Concept Mapping

| React Feature / Hook             | LWC Equivalent      | Description                                                                                       |
| :------------------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| **Component Props**              | `@api propertyName` | Public reactive properties exposed to parent components.                                          |
| **Component State / `useState`** | Class Fields        | LWC class fields are reactive by default; modifying them triggers a rerender.                     |
| **Side Effects / `useEffect`**   | Lifecycle Hooks     | `connectedCallback()` (insert), `renderedCallback()` (render), `disconnectedCallback()` (remove). |
| **Event Emission**               | `CustomEvent`       | Handled via standard DOM dispatch: `this.dispatchEvent(new CustomEvent('name'))`.                 |

---

## 3. Where Setup & Troubleshooting Content Lives

This guide stays focused on architecture and LWC concepts. Environment setup, CLI/deployment issues (JDK path, NVM PATH conflicts, `NoDefaultEnvError`, VS Code GPU crashes, and more) are documented in [`DEVELOPMENT_SETUP.md`](DEVELOPMENT_SETUP.md). Trailhead challenge-check failures — including the "field does not exist / wrong type" error caused by missing field-level security on Metadata API-deployed fields — are documented in [`../trailhead/TROUBLESHOOTING.md`](../trailhead/TROUBLESHOOTING.md).
