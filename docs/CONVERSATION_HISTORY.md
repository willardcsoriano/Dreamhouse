# Dreamhouse Developer Reference Guide

A concise technical reference for Salesforce development, architecture, and environmental troubleshooting.

---

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
