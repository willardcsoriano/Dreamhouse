# Trailhead Progress Report

**Date:** July 18, 2026  
**Subject:** Developer Beginner Trailhead Progress & Learnings

---

## Learnings

1. **Enterprise Operations Tracking:** Salesforce is used extensively by businesses to track and manage end-to-end business operations seamlessly within a single unified platform.
2. **Salesforce Paradigm vs. Traditional RDBMS:** Salesforce abstracts standard database concepts into its own business-centric terminology:
   - **Objects & Fields:** Objects represent database tables, Fields represent columns, and Records represent rows.
   - **Primary Keys (`Id`):** Every record is automatically assigned a unique 18-character alphanumeric string (`Id`).
   - **Foreign Keys (Lookup vs. Master-Detail):** Both are Foreign Key columns storing the parent's `Id` under the hood. **Lookup** acts as an optional FK with independent record ownership, while **Master-Detail** acts as a strict `NOT NULL` FK with cascading deletes, parent-inherited security (`ControlledByParent`), and support for real-time **Roll-Up Summary fields** (`SUM`, `COUNT`, `MIN`, `MAX`).

---

## Supplemental Learnings

1. **Database Architecture & Evolution:** Salesforce patented their multi-tenant database approach in the 2000s (virtualized schemas using universal data tables, custom indexers, and dynamic sharing rules). However, as database technology rapidly advanced, modern relational databases easily handle these concerns natively today (e.g., PostgreSQL using `JSONB` schemas, GIN/Expression indexing, and native Row-Level Security / RLS). For a deeper breakdown, refer to [DEVELOPER_REFERENCE.md](../setup/DEVELOPER_REFERENCE.md).
2. **Cost & Investment:** Salesforce represents a heavy financial investment for organizations. Entry-level pricing starts at **$25 per user/month** for the Starter Suite (billed annually), scaling to **$80/user/month** for Pro Suite, and reaching **$165–$330+ per user/month** for Enterprise and Unlimited editions.

---

## Roadblocks

1. **Out-of-Order Badge Completion & Setup Friction:** Completed the first badge, then unknowingly jumped directly to Badge 3 inside the web Playground without VS Code. Discovering that Badge 2 was skipped (which covered the initial VS Code connection) caused significant confusion and consumed extra time connecting the Trailhead Playground org to VS Code. Additionally, navigating the Salesforce GUI initially presented a steep learning curve, though following the included tutorial videos helped clarify the navigation.
2. **Hardware Limitations & Remote VM Migration:** Local hardware constraints (8 GB RAM) were insufficient to run VS Code alongside developer tooling without performance degradation. To resolve this, development was migrated to a 16 GB Hetzner VM via Remote SSH, which required setting up the development stack from scratch and cost setup time.
3. **CLI Deployment vs. GUI Challenge Verification (Field-Level Security):** Completing activities via the Salesforce CLI (`sf project deploy start`) instead of the point-and-click Setup GUI caused Trailhead challenge checks to fail with misleading "field does not exist" errors. Unlike the Setup UI wizard, CLI metadata deployments do not automatically grant Field-Level Security (FLS) access permissions to user profiles. This was resolved by diagnosing the missing access via Tooling API SOQL queries and deploying an explicit `Admin.profile-meta.xml` profile component with `fieldPermissions` (read/edit) for the new fields.
