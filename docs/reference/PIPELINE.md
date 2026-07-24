# Trailhead Documentation Pipeline

## Overview

This document codifies the process for turning a raw, scraped Trailhead unit into a polished, CLI-first technical doc under `docs/trails/`. The raw scrape is treated as an immutable scaffold: its prose is never edited, condensed, or rewritten — only reformatted into markdown headings, bold, and lists. Below each instruction — Guided Activity and Hands-On Challenge alike — the pipeline adds a CLI-equivalent payload for developers who prefer the terminal: a deploy code block, plus a separate verification code block that proves the change actually landed in the org, not just that the deploy command exited zero. Steps with no Metadata API surface are left as GUI-only, called out plainly rather than forced into a fake CLI payload. There are four stages: paste the raw content, draft the unit doc from it word for word, add CLI and verification payloads, then human execution against the live org. The last section covers what may run in parallel across a badge's units and what has to stay sequential.

## Table of Contents

- [Overview](#overview)
- [Stage 1 — Scrape](#stage-1-scrape)
- [Stage 2 — Draft the Unit Doc](#stage-2-draft-the-unit-doc)
- [Stage 3 — CLI Payload + Verification](#stage-3-cli-payload-verification)
- [Stage 4 — Human Execution & Audit (never delegated)](#stage-4-human-execution-audit-never-delegated)
- [Stage 5 — Post-Mortem](#stage-5-post-mortem)
- [Output Skeleton (per unit doc)](#output-skeleton-per-unit-doc)
- [Parallelizing Across Units](#parallelizing-across-units)

## Stage 1 — Scrape

Paste the raw Trailhead unit text — Guided Activity **and** Hands-On Challenge, word for word — into `docs/trails/developer_beginner/badges/<NN_badge>/raw/UNIT_<N>_RAW_GUIDED_ACTIVITY.md`. It's easy to stop pasting once the graded challenge starts; don't. Where the file lives matters less than completeness at this point — get the whole unit's text in, and worry about polish at Stage 2.

**The raw file is a scaffold, not a draft.** Once pasted, it is never edited to fix wording, condense a paragraph, or "clean it up" — the only edits a raw file should ever see are corrections of an actual copy-paste mistake (a dropped line, a mis-pasted alt-text fragment). Every later stage reads from the raw file; none of them write back to it.

## Stage 2 — Draft the Unit Doc

Create `docs/trails/developer_beginner/badges/<NN_badge>/UNIT_<N>_<NAME>.md` and copy the raw file's prose into it **word for word** — every sentence, every list item, both the Guided Activity and the Hands-On Challenge.

"Polish" here means markdown formatting only: turn plain-text headings into `##`/`###`, turn numbered click-paths into ordered lists, bold the literal values a reader has to type (`Property`, `Currency`, …), render Trailhead's tables as markdown tables, add the `**Source:**` link. It does **not** mean shortening a paragraph, dropping a sentence that reads like filler, or rephrasing something "more clearly." If Trailhead's own copy changes in a future re-scrape, the doc changes to match it exactly; until then, the raw file is the wording's source of truth, not the drafter's judgment.

Skip nothing — including narrative framing sentences that don't map to a graded step, and Trailhead's own boilerplate notes (accessibility callouts, inclusive-language notices). They're part of what Trailhead actually said, so they're part of the doc.

## Stage 3 — CLI Payload + Verification

For every discrete instruction that has a Metadata API / CLI surface, add two fenced `bash` code blocks directly under that step's prose:

1. **Payload** — the heredoc'd XML/config plus `sf project deploy start ... --json`, applying the standing rules in `docs/reference/SALESFORCE_DEVELOPMENT_RULES.md`: schema and FLS deployed atomically (Rule 2.1), no `fieldPermissions` for Master-Detail or required fields (Rules 2.2–2.3), always an explicit `-o <org>` (Rule 3.1).
2. **Verification** — a separate `sf data query --use-tooling-api --json` (or equivalent) that confirms the specific thing that step put at risk actually landed: a field's data type, an FLS grant, a tab visibility. This is not the same block as the deploy, and it isn't optional — a `--json` deploy result with a clean exit status only proves the command didn't error, not that the org now matches what the step describes.

Before drafting a payload, decide whether the step is actually worth hand-authoring as XML: only do it when (1) the Metadata API reference has a worked example of your exact structure, (2) the XML uses identifiers you'd choose yourself rather than builder-assigned ones, and (3) a structurally valid deploy is actually equivalent to whatever check you're trying to satisfy. If any of those three fails — a wizard-driven Setup screen, a canvas-generated structure with internal IDs, anything Trailhead's own builder produces that you'd otherwise be guessing at — it's `[GUI]`, not `[CLI]`.

Multiple steps that build toward one logical unit of schema (an object plus its fields, a field plus its FLS grant) can share one payload block and one verification block at the end of that group — they don't need to be deployed and verified one at a time, as long as the verification query actually checks every piece the group touched.

For a step with no clean CLI surface — a wizard-driven Setup screen, Schema Builder's canvas, an explicitly open-ended "make it whatever you want" demo — don't force a payload. Write one line directly under the prose: **"No CLI equivalent — do this in the browser."** If the wizard's output is itself worth capturing in source control, follow up with a retrieve → deploy round trip instead of a hand-authored payload: `sf project retrieve start -m "<MetadataType>:<Member>"` once, to pull the builder-generated result into source control, then `sf project deploy start -m "<MetadataType>:<Member>" --json` from then on to redeploy that exact retrieved file. The click-path is how the artifact gets authored correctly once; the deploy command is what makes it a reproducible CLI payload after that.

## Stage 4 — Human Execution & Audit (never delegated)

Per Rule 4.4, AI drafts files only — it never runs `sf`, `git commit`, or touches the live org. The developer runs the deploy and verification commands against the target org, one file per command, under `badges/<NN_badge>/logs/UNIT_<N>_<DEPLOY|VERIFICATION>....json`.

**The log file records the command, not just its output.** A raw `--json` blob with no record of what produced it is useless once it's sitting alone in a `logs/` folder next to a dozen others. Every payload and verification block assigns the exact command to a `CMD` variable first, then captures both in the same file as two JSON Lines — a `{"command": ...}` record followed by the real `--json` output:

```bash
CMD="sf project deploy start -d force-app/main/default/objects/Property__c -o trailhead-playground --json"
{ jq -n --arg cmd "$CMD" '{command: $cmd}'; eval "$CMD"; } | tee badges/<NN_badge>/logs/UNIT_<N>_GUIDED_DEPLOY_AUDIT.json
```

`jq -n --arg` handles quoting the command safely (SOQL's embedded single quotes, `sed`'s embedded double quotes) without hand-escaping it into the log line. This is what every payload/verification block in a unit doc should look like — not a bare `sf ...` invocation.

## Stage 5 — Post-Mortem

Any hiccup hit during Stage 4 gets appended to the unit doc's **Technical Post-Mortem & Engineering Learnings** section as a Hiccup → Resolution pair, and periodically rolled up into `docs/REPORT.md`.

---

## Output Skeleton (per unit doc)

```
# <Unit Name>
**Source:** link

## Learning Objectives
## <one section per Trailhead heading, in order — prose, then payload + verification (or the GUI-only line) inline>
## Resources

---

## Hands-On Challenge
  <same shape as the Guided Activity — prose, then payload + verification>

## Technical Post-Mortem & Engineering Learnings
```

File path: `docs/trails/developer_beginner/badges/<NN_badge>/UNIT_<N>_<NAME>.md`. Raw source: `.../raw/UNIT_<N>_RAW_GUIDED_ACTIVITY.md`. Deploy/verification logs: `.../logs/`.

---

## Parallelizing Across Units

Stages 2–3 (content authoring) are the parallelizable part — each unit's draft is a distinct file, so one subagent per unit is safe to run concurrently, as long as that unit's raw content has already been pasted in full. Stage 4 is never delegated and never parallel — it's one developer, one org, run in order.

Two things break naive fan-out, so hand every subagent a short shared-context note before it starts:

- **Naming continuity** — later units reference object/field names decided earlier in the same badge (e.g., `Property__c`, `Offer__c`). A subagent drafting Unit 3 blind can invent a name that collides with what Unit 1 already established.
- **Shared roll-up files** — a badge's index doc, if one exists, and the trail progress table are edited once per unit, by the coordinator, after each subagent's draft lands — never by two subagents at once.

Practical flow: paste in raw content for as many units as you've scraped → subagents fan out one-per-unit against this pipeline plus the current naming registry → drafts get reviewed and the roll-up files updated once → you take Stage 4 from there.
