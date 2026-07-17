# Dreamhouse Developer Reference Guide

## Overview

This is a concise technical reference for Salesforce development on the Dreamhouse Realty project, covering platform architecture, Lightning Web Components, and environmental troubleshooting. It exists so recurring setup pain points don't have to be re-diagnosed from scratch each time they resurface. Section 1 explains how Salesforce's metadata-driven, multi-tenant architecture differs from a traditional app-plus-database stack. Section 2 maps LWC concepts to their React equivalents for developers coming from a JS framework background. Section 3 catalogs environment and CLI/deployment issues hit during setup, each with cause and fix. Trailhead challenge-check failures specifically have their own dedicated reference — see `TRAILHEAD_TROUBLESHOOTING.md`.

---

## Table of Contents

- [Overview](#overview)
- [1. Salesforce Platform Architecture](#1-salesforce-platform-architecture)
  - [Metadata-Driven Architecture](#metadata-driven-architecture)
  - [Data Virtualization & Multi-Tenancy](#data-virtualization-multi-tenancy)
- [2. Lightning Web Components (LWC)](#2-lightning-web-components-lwc)
  - [React Developer Concept Mapping](#react-developer-concept-mapping)
- [3. Environment & Tooling Troubleshooting](#3-environment-tooling-troubleshooting)
  - [VS Code & Extension Host Diagnostics](#vs-code-extension-host-diagnostics)
  - [Salesforce CLI & Deployment Issues](#salesforce-cli-deployment-issues)

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

## 3. Environment & Tooling Troubleshooting

### VS Code & Extension Host Diagnostics

- **Java Runtime Missing (`Java runtime could not be located`):**
  - **Cause:** VS Code Apex Extension failed to auto-locate the local JDK path.
  - **Fix:** Define the JVM directory path explicitly in VS Code's `settings.json`:
    ```json
    "salesforce.salesforcedx-vscode-apex.java.home": "/usr/lib/jvm/default-java"
    ```
- **System-wide Node/CLI Path Conflicts:**
  - **Cause:** Dynamic NVM loading prevents non-interactive shell hosts or background extensions from recognizing binary paths.
  - **Fix:** Create global symbolic links:
    ```bash
    sudo ln -sf $(which node) /usr/local/bin/node
    sudo ln -sf $(npm config get prefix)/bin/sf /usr/local/bin/sf
    ```

### Salesforce CLI & Deployment Issues

- **Default Target Org Missing (`NoDefaultEnvError`):**
  - **Cause:** Authorizing with `-d` sets the org as the default DevHub but not the default Target Org for source deployments.
  - **Fix:** Set the default target org config key:
    ```bash
    sf config set target-org trailhead-playground
    ```
- **Local VS Code GPU Crash (Linux):**
  - **Cause:** Hardware acceleration or shader cache corruption on Wayland/Nvidia setups.
  - **Fix:** Perform a non-destructive GPU cache delete and configuration soft reset:
    ```bash
    rm -rf ~/.config/Code/GPUCache && mv ~/.config/Code ~/.config/Code.bak && mv ~/.vscode ~/.vscode.bak
    ```
- **Trailhead Challenge Check Failures:**
  - **Cause:** Varies — see the dedicated reference.
  - **Fix:** See [`TRAILHEAD_TROUBLESHOOTING.md`](TRAILHEAD_TROUBLESHOOTING.md) for diagnostic steps and fixes, including the "field does not exist / wrong type" error caused by missing field-level security on Metadata API-deployed fields.
