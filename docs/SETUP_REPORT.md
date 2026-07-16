# Dreamhouse Development Setup & Environment Report

**Date:** July 16, 2026  
**Developer:** Willard Soriano  
**Project:** Salesforce Dreamhouse Realty App  

---

## Executive Summary
This report documents the initial setup phase of the Dreamhouse Realty application development environment. It details the local tooling installation, Salesforce org authorization, version control baseline, and the integration of the Salesforce Model Context Protocol (MCP) server for AI-assisted development.

---

## 1. Local Tooling & Project Dependencies
The development environment has been configured with the necessary compilers, formatters, and Salesforce Command Line Interface (CLI) components.

| Tool / Dependency | Version / Status | Description |
| :--- | :--- | :--- |
| **Node.js** | `v24.14.1` | Runtime environment for local JS tooling and build tasks. |
| **Salesforce CLI (`sf`)** | `@salesforce/cli/2.143.6` | The primary CLI tool for deploying and retrieving metadata. |
| **npm packages** | 785 packages installed | Dev dependencies including ESLint, Prettier, and LWC Jest. |
| **Husky & Lint-Staged** | Configured | Automatically formats and lints code changes before commits. |

---

## 2. Salesforce Org Authorization
To establish a connection between the local project files and the cloud, the Salesforce CLI was authorized to connect to the Trailhead Playground.

*   **Default Target Org Alias:** `myDevOrg`
*   **Active Instance URL:** `https://willardcsoriano.my.salesforce.com`
*   **Authentication Flow:** OAuth 2.0 Web Server Flow (`sf org login web`)
*   **Connection Verification Status:** **Successful**
*   **Playground Setup Experience:** Resolved a common verification issue by resetting the auto-generated Playground password via the `Playground Starter` application and authenticating using the specific Playground credentials rather than personal developer credentials.

---

## 3. Version Control (Git)
A Git repository has been initialized to implement source-driven development. A branching strategy has been adopted to maintain clear code ownership:

*   **Repository Init:** Running `git init` in the project root.
*   **Initial Commit (`cb922af`):** Baseline files and the retrieved `House__c` Custom Object metadata.
*   **Branching Strategy:**
    *   **`master` (Current):** A clean working branch kept at a baseline state. This branch will contain only the code written step-by-step by the developer.
    *   **`agent-solution`:** An isolated branch containing the AI assistant's generated solutions (Apex classes and LWC maps) to serve as a reference.

---

## 4. Salesforce MCP Server Integration
To enable advanced AI pair-programming, the official Salesforce Model Context Protocol (MCP) server (`@salesforce/mcp`) was configured. 

*   **Configuration File:** [mcp_config.json](file:///home/willard/.gemini/config/mcp_config.json)
*   **Launch Syntax:** `npx @salesforce/mcp@latest -o myDevOrg --toolsets all`
*   **Verification Tests Run:**
    1.  **`list_all_orgs`:** Confirmed the MCP server is communicating with the CLI.
    2.  **`run_soql_query`:** Confirmed database connectivity by querying the active user's name and email.
    3.  **`run_apex_test`:** Verified Apex test-running capability by executing existing cloud unit tests (4/4 tests passed).

---

## 5. Next Milestones
1.  **Apex Service Implementation:** Write the `HouseService` Apex controller in `force-app/main/default/classes/` to execute security-enforced SOQL queries.
2.  **Lightning Web Component (LWC) Creation:** Build the `housingMap` component using Salesforce base elements (`lightning-card` and `lightning-map`) to plot properties.
3.  **UI Deployment & Page Layout Placement:** Deploy the LWC bundle and place it on the Dreamhouse App Home Page layout using Lightning App Builder.
