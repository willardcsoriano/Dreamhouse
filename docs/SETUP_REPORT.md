# Dreamhouse Development Setup & Environment Report

**Date:** July 16, 2026  
**Developer:** Willard Soriano  
**Project:** Salesforce Dreamhouse Realty App

---

## Executive Summary

This report documents the initial setup phase of the Dreamhouse Realty application development environment. It details the local tooling installation, Salesforce org authorization, version control baseline, and the integration of the Salesforce Model Context Protocol (MCP) server for AI-assisted development.

The developer's workflow is strictly CLI-first and keyboard-centric; consequently, navigating browser-based configuration tools (such as Salesforce Setup navigation and the Object Creator spreadsheet import wizard) was a notable source of friction during this phase.

### Development Environment Architecture

Due to local hardware constraints (the initial local developer machine only having **8 GB of RAM**, leading to out-of-memory/RAM exhaustion during heavy development workloads), a **dual-machine architecture** was established:

- **Local Client:** 8 GB RAM Linux PC used for remote access interfaces and local SSH connection.
- **Remote Development Host (VM):** A **Hetzner CX43 Cloud VM** (equipped with **4 vCPUs and 16 GB RAM**) hosting the primary project workspace, Salesforce CLI (`sf`), Node.js environment, Git repository, and the Salesforce Model Context Protocol (MCP) servers.

---

## 1. Local Tooling & Project Dependencies

The development environment has been configured with the necessary compilers, formatters, and Salesforce Command Line Interface (CLI) components.

| Tool / Dependency         | Version / Status          | Description                                                  |
| :------------------------ | :------------------------ | :----------------------------------------------------------- |
| **Node.js**               | `v24.14.1`                | Runtime environment for local JS tooling and build tasks.    |
| **Salesforce CLI (`sf`)** | `@salesforce/cli/2.143.6` | The primary CLI tool for deploying and retrieving metadata.  |
| **npm packages**          | 785 packages installed    | Dev dependencies including ESLint, Prettier, and LWC Jest.   |
| **Husky & Lint-Staged**   | Configured                | Automatically formats and lints code changes before commits. |

---

## 2. Salesforce Org Authorization

To establish a connection between the local project files and the cloud, the Salesforce CLI was authorized to connect to the Trailhead Playground.

- **Default Target Org Alias:** `myDevOrg`
- **Active Instance URL:** `https://willardcsoriano.my.salesforce.com`
- **Authentication Flow:** OAuth 2.0 Web Server Flow (`sf org login web`)
- **Connection Verification Status:** **Successful**
- **Playground Setup Experience:** Resolved a common verification issue by resetting the auto-generated Playground password via the `Playground Starter` application and authenticating using the specific Playground credentials rather than personal developer credentials.

---

## 3. Version Control (Git)

A Git repository has been initialized to implement source-driven development. A branching strategy has been adopted to maintain clear code ownership:

- **Repository Init:** Running `git init` in the project root.
- **Initial Commit (`cb922af`):** Baseline files and the retrieved `House__c` Custom Object metadata.
- **Branching Strategy:**
  - **`master` (Current):** A clean working branch kept at a baseline state. This branch will contain only the code written step-by-step by the developer.
  - **`agent-solution`:** An isolated branch containing the AI assistant's generated solutions (Apex classes and LWC maps) to serve as a reference.

---

## 4. Salesforce MCP Server Integration

To enable advanced AI pair-programming, the official Salesforce Model Context Protocol (MCP) server (`@salesforce/mcp`) was configured.

- **Configuration File:** [mcp_config.json](file:///home/willard/.gemini/config/mcp_config.json)
- **Launch Syntax:** `npx @salesforce/mcp@latest -o myDevOrg --toolsets all`
- **Verification Tests Run:**
  1.  **`list_all_orgs`:** Confirmed the MCP server is communicating with the CLI.
  2.  **`run_soql_query`:** Confirmed database connectivity by querying the active user's name and email.
  3.  **`run_apex_test`:** Verified Apex test-running capability by executing existing cloud unit tests (4/4 tests passed).

---

## 5. Roadblocks & Resolutions Encountered

During the setup phase, several environmental, licensing, and workflow roadblocks were encountered and resolved:

- **GUI Configuration Overhead & Friction (CLI-First Preference):**
  - **Roadblock:** Significant workflow friction and navigation difficulties encountered during browser-based point-and-click tasks (specifically navigating Salesforce Setup menus and utilizing the web-based Object Creator spreadsheet wizard), due to the developer's strong preference for terminal-based, keyboard-centric environments.
  - **Resolution:** Tabled browser-based configuration tasks as quickly as possible, immediately syncing the resulting metadata changes back to the terminal using the `sf project retrieve` command to return to a pure CLI and local text editor workflow.
- **Wrong Org Authorized (Trailhead Verification Failure):**
  - **Roadblock:** The CLI was initially connected using a personal Salesforce Developer org (`hello@willardcsoriano.dev`), which caused the Trailhead page challenge validator to fail.
  - **Resolution:** Logged into the playground in the browser, accessed the `Playground Starter` credentials tab, reset the playground password, and re-authenticated the CLI using `sf org login web -a myDevOrg -s` with the playground's specific username.
- **Missing Java Compiler (JDK):**
  - **Roadblock:** VS Code's Salesforce Apex Extension failed to compile or support class structures because Java was missing on the local Debian 13 environment (`javac: command not found`).
  - **Resolution:** Installed the default JDK using Debian's package manager (`sudo apt install default-jdk -y`), configuring `javac 21.0.11`.
- **NVM PATH Conflict (VS Code CLI Recognition Gap):**
  - **Roadblock:** NVM loaded Node and npm binaries dynamically in active terminal shell sessions. VS Code's background processes and non-interactive shell hosts (`/bin/sh`) could not read NVM variables, failing with `sf: not found` errors.
  - **Resolution:** Created symbolic links from NVM's binary directory shortcuts directly into `/usr/local/bin/node` and `/usr/local/bin/sf` to expose them system-wide.
- **Agentforce Vibes Licensing:**
  - **Roadblock:** The LWC coding agent pane in VS Code returned a block screen saying "Agentforce Vibes is not enabled in your org."
  - **Resolution:** Opened Setup in the browser, accepted the native `Agentforce Vibes IDE` terms and conditions under the Development menu, and re-authenticated the CLI credentials to refresh the workspace licenses.
- **Local VS Code Crash & CLI Transition (Loss of Remote SSH Window):**
  - **Roadblock:** The local VS Code application crashed and failed to open (prompted to close immediately on launch) due to local GPU/cache corruption, preventing remote SSH access through the IDE interface.
  - **Resolution:** Transitioned completely to the Agentic CLI command-line workflow over remote SSH. Handled code viewing (using `less` and syntax highlighting tips), project navigation, and executing Python (`uv run`) and Go (`go run`) CLI files directly via terminal commands.
- **Salesforce CLI Default Target Org Missing (`NoDefaultEnvError`):**
  - **Roadblock:** Authenticated with `sf org login web -d -a trailhead-playground` successfully, but subsequent metadata deployment failed with `NoDefaultEnvError: No default environment found` because the login command configured the alias as the default DevHub (`target-dev-hub` 🌳) but not the default active target org (`target-org` 🍁).
  - **Resolution:** Configured the target-org default value explicitly via `sf config set target-org trailhead-playground` (or passing the `-o` flag), allowing the metadata deploy to succeed.
- **Netdata Repository Package Mismatch (`Hash Sum mismatch`):**
  - **Roadblock:** Run-time system updates via `sudo apt full-upgrade` failed due to ongoing Netdata repository CDN/mirror synchronization conflicts, causing package downloads to abort due to checksum size and hash mismatches.
  - **Resolution:** Placed temporary holds on Netdata packages (`sudo apt-mark hold ...`) to bypass the mismatch errors, allowing the rest of the system upgrades to proceed smoothly.
- **VS Code Apex Extension Missing Java Path (`Java runtime could not be located`):**
  - **Roadblock:** Local VS Code Apex Extension failed to detect the Java runtime even after installing the default JDK, displaying a `Java runtime could not be located` warning.
  - **Resolution:** Defined the Java home folder path explicitly in VS Code's `settings.json` under `salesforce.salesforcedx-vscode-apex.java.home` (pointing to `/usr/lib/jvm/default-java` or the active OpenJDK home directory `/usr/lib/jvm/java-21-openjdk-amd64`).

---

## 6. Next Milestones

1.  **Apex Service Implementation:** Write the `HouseService` Apex controller in `force-app/main/default/classes/` to execute security-enforced SOQL queries.
2.  **Lightning Web Component (LWC) Creation:** Build the `housingMap` component using Salesforce base elements (`lightning-card` and `lightning-map`) to plot properties.
3.  **UI Deployment & Page Layout Placement:** Deploy the LWC bundle and place it on the Dreamhouse App Home Page layout using Lightning App Builder.
