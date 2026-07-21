# Session Handoff — Badge 05, Unit 5

## Overview

This is a handoff note for picking up work on a different machine (or a fresh Claude Code session generally) — conversation memory is per-machine and doesn't travel with `git`, so this file, plus `docs/reference/PIPELINE.md` and the Unit 5 doc it produced, are what actually carry context forward. As of this writing, `master` has just absorbed two merged PRs: the authoring pipeline itself and a full draft of Unit 5 (Customize Record Page Components and Fields). Nothing in Unit 5 has been executed against a live org yet — it's a reviewed draft with two intentional open placeholders and a mandatory browser step that hasn't happened. The next session's job is Stage 4 of the pipeline: run the browser steps, run the commands, paste results back, fill in what's unknown until execution.

---

## Table of Contents

- [Overview](#overview)
- [What's on `master` Now](#whats-on-master-now)
- [What's Next: Executing Unit 5](#whats-next-executing-unit-5)
- [Branch & Shipping Convention in Effect](#branch-shipping-convention-in-effect)

## What's on `master` Now

- `docs/reference/PIPELINE.md` — the scrape → polish → CLI-payload → human-execution process, including the `[CLI]`/`[GUI]` classification rule and the required browser-vs-terminal flags per section.
- `docs/trails/developer_beginner/badges/05_lightning_experience_customization/UNIT_5_CUSTOMIZE_RECORD_PAGE_COMPONENTS_AND_FIELDS.md` — the full Unit 5 draft, drafted but **not yet executed**.
- `docs/reference/SALESFORCE_DEVELOPMENT_RULES.md` — Rule 4.4 is the operative boundary: the AI drafts/edits files only; the developer alone runs `sf`, `git commit`, `git checkout` against the live org.
- Badge 05 units with docs so far: `UNIT_1_SET_UP_YOUR_ORG.md`, `UNIT_2_CREATE_AND_CUSTOMIZE_LIGHTNING_APPS.md`, `UNIT_4_CUSTOMIZE_RECORD_HIGHLIGHTS_WITH_COMPACT_LAYOUTS.md`, and now `UNIT_5_...`. **There is no Unit 3 doc anywhere in the repo** — not referenced in the badge overview or trail dashboard either. Unclear whether it was done via pure GUI without documentation or genuinely skipped; worth resolving before treating Badge 05 as complete.

## What's Next: Executing Unit 5

Open the Unit 5 doc and work through it top to bottom. Per section, the doc now says explicitly whether the browser is needed first:

- **`G1`, `G3`, `C1`, `C3`** (`[GUI]`): do the Trailhead click-path in the browser first, then run the retrieve → deploy commands. No content to hand-author.
- **`G2`, `C2`** (`[CLI]` only): no browser at all — retrieve the current layout as a baseline, hand-edit the `relatedLists` block as shown, deploy.

Two things are placeholders until you actually execute:

1. **Source URL** for the unit header — wasn't captured in the original scrape.
2. **Contact FlexiPage's actual API name** (`C1`) — Lightning App Builder auto-generates it when cloning the org-default Contact page; confirm it in the page properties before running the `C1.RET` retrieve command, then fill it into both that command and the `C3.RET` command later in the doc.

As you go, paste the real retrieved XML and the `--json` deploy/retrieve output back — that's what turns the placeholders and command-only sections into a complete, audited record, the same way Unit 4's `logs/` directory holds real output.

## Branch & Shipping Convention in Effect

One branch per concern, `gh pr create` then `gh pr merge --squash --delete-branch` — never merge to `master` directly, never push without being asked in that turn (see Rule 4.1/4.2 in `docs/reference/SALESFORCE_DEVELOPMENT_RULES.md`). Start Unit 5 execution on a fresh branch, e.g. `feature/badge-05-unit-5-execution`, rather than continuing on a docs-only branch.
