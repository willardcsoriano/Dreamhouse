# Dreamhouse Development Setup & Environment Guide

This guide documents the local tooling installation, Salesforce org authorization, version control configuration, and the integration of the Salesforce Model Context Protocol (MCP) server for the Dreamhouse Realty project.

---

## 1. Local Tooling & Project Dependencies

The development environment has been configured with the necessary compilers, compilers, formatters, and Salesforce Command Line Interface (CLI) components:

- **Node.js:** `v24.14.1` (using NVM for node version management).
- **Salesforce CLI (`sf`):** `@salesforce/cli/2.143.6`.
- **npm packages:** Dev dependencies including ESLint, Prettier, and LWC Jest installed in the repository workspace.
- **Husky & Lint-Staged:** Configured to automatically format and lint code changes before commits.

---

## 2. Salesforce Org Authorization

To establish a connection between the local project files and the Salesforce Cloud:

- **Authentication Flow:** OAuth 2.0 Web Server Flow (`sf org login web`).
- **Target Org Alias:** `trailhead-playground`.
- **Authentication Command:**
  ```bash
  sf org login web -d -a trailhead-playground
  ```

---

## 3. Salesforce MCP Server Integration

To enable advanced AI pair-programming, the official Salesforce Model Context Protocol (MCP) server (`@salesforce/mcp`) was configured.

- **Configuration File:** [mcp_config.json](file:///home/willard/.gemini/config/mcp_config.json)
- **Launch Command:**
  ```bash
  npx @salesforce/mcp@latest -o trailhead-playground --toolsets all
  ```

---

## 4. Setup Troubleshooting & Configuration Fixes

### VS Code & Extension Host Settings

- **Java Runtime Missing (`Java runtime could not be located`):**
  - _Cause:_ VS Code Apex Extension failed to auto-locate the local JDK path.
  - _Fix:_ Define the JVM directory path explicitly in VS Code's `settings.json`:
    ```json
    "salesforce.salesforcedx-vscode-apex.java.home": "/usr/lib/jvm/default-java"
    ```
- **System-wide Node/CLI Path Conflicts:**
  - _Cause:_ Dynamic NVM loading prevents non-interactive shell hosts or background extensions from recognizing binary paths.
  - _Fix:_ Create global symbolic links:
    ```bash
    sudo ln -sf $(which node) /usr/local/bin/node
    sudo ln -sf $(npm config get prefix)/bin/sf /usr/local/bin/sf
    ```

### CLI Environment & OS-Level Fixes

- **Default Target Org Missing (`NoDefaultEnvError`):**
  - _Cause:_ Authorizing with `-d` sets the org as the default DevHub but not the default Target Org for source deployments.
  - _Fix:_ Set the default target org config key globally:
    ```bash
    sf config set target-org trailhead-playground
    ```
- **Local VS Code GPU Crash (Linux):**
  - _Cause:_ Hardware acceleration or shader cache corruption on Wayland/Nvidia setups.
  - _Fix:_ Perform a non-destructive GPU cache delete and configuration soft reset:
    ```bash
    rm -rf ~/.config/Code/GPUCache && mv ~/.config/Code ~/.config/Code.bak && mv ~/.vscode ~/.vscode.bak
    ```
- **Netdata Package Mismatch (`Hash Sum mismatch`):**
  - _Cause:_ Intermittent repository mirror sync failures on Netdata servers during `sudo apt full-upgrade`.
  - _Fix:_ Temporarily hold Netdata packages before running upgrades:
    ```bash
    sudo apt-mark hold netdata netdata-dashboard netdata-plugin-apps netdata-plugin-chartsd netdata-plugin-debugfs netdata-plugin-ebpf netdata-plugin-go netdata-plugin-nfacct netdata-plugin-otel netdata-plugin-perf netdata-plugin-pythond netdata-plugin-slabinfo netdata-plugin-systemd-journal netdata-user
    ```
