# Trailhead Documentation Pipeline

## Overview

This document codifies the process for turning a raw, scraped Trailhead unit into a polished, CLI-first technical doc under `docs/trails/`. The raw scrape is treated as an immutable scaffold: its prose is never edited, condensed, or rewritten — only reformatted into markdown headings, bold, and lists. CLI-equivalent payload and verification blocks are added under every discrete instruction that has a Metadata API surface, full stop — in the Guided Activity and the Hands-On Challenge alike. The pipeline is **challenge-agnostic** about this: it doesn't special-case which section the code lives in, because both get it wherever an instruction actually builds something. Every block is commented for a mixed audience — a plain-language line above the block explaining what it does and why, plus inline comments on the individual lines that carry a decision or a non-obvious flag — since these are read standalone by learners who may never run a terminal command outside this walkthrough. The one thing that does need a per-unit check, every time, is whether a Challenge instruction is a literal restatement of something the Guided Activity already built (confirmed so far only for badge 05 unit 1) or a genuinely different artifact under the same heading (the common case) — a literal restatement gets a one-line mention instead of a second payload; anything else gets built and verified on its own, same as any other step. Steps with no Metadata API surface are left as GUI-only, called out plainly rather than forced into a fake CLI payload. There are four stages: paste the raw content, draft the unit doc from it word for word, add CLI and verification payloads, then human execution against the live org. The last section covers what may run in parallel across a badge's units and what has to stay sequential.

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

**If the unit already has an existing doc whose payload blocks have already been deployed and confirmed against a live org** — drafted under an earlier version of this pipeline, before the current prose/skeleton conventions existed — don't touch the code. It's already working and already verified; re-deriving or re-running it produces no new signal, only wasted Stage 4 time re-proving something Stage 5 already closed out. Carry every existing payload block forward byte-for-byte, in place, and run only the surrounding prose, headings, and structure back through this stage — that's the part that's actually out of date, not the commands. **Check each payload for a verification block directly beneath it** — an older doc may have shipped with the deploy only. If one's missing, add it now per Stage 3's rule (a separate `sf data query --use-tooling-api --json` confirming the specific thing that step put at risk, not just a clean deploy exit status) so the step has something to actually execute against, not just re-run.

Create `docs/trails/developer_beginner/badges/<NN_badge>/UNIT_<N>_<NAME>.md` and copy the raw file's prose into it **word for word** — every sentence, every list item, both the Guided Activity and the Hands-On Challenge.

"Polish" here means markdown formatting only: turn plain-text headings into `##`/`###`, turn numbered click-paths into ordered lists, bold the literal values a reader has to type (`Property`, `Currency`, …), render Trailhead's tables as markdown tables, add the `**Source:**` link. It does **not** mean shortening a paragraph, dropping a sentence that reads like filler, or rephrasing something "more clearly." If Trailhead's own copy changes in a future re-scrape, the doc changes to match it exactly; until then, the raw file is the wording's source of truth, not the drafter's judgment.

Skip nothing — including narrative framing sentences that don't map to a graded step, and Trailhead's own boilerplate notes (accessibility callouts, inclusive-language notices). They're part of what Trailhead actually said, so they're part of the doc.

## Stage 3 — CLI Payload + Verification

For every discrete instruction that has a Metadata API / CLI surface — in the Guided Activity **or** the Hands-On Challenge, wherever it actually appears — add two fenced `bash` code blocks directly under that step's prose:

1. **Payload** — the heredoc'd XML/config plus `sf project deploy start ... --json`, applying the standing rules in `docs/reference/SALESFORCE_DEVELOPMENT_RULES.md`: schema and FLS deployed atomically (Rule 2.1), no `fieldPermissions` for Master-Detail or required fields (Rules 2.2–2.3), always an explicit `-o <org>` (Rule 3.1).
2. **Verification** — a separate `sf data query --use-tooling-api --json` (or equivalent) that confirms the specific thing that step put at risk actually landed: a field's data type, an FLS grant, a tab visibility. This is not the same block as the deploy, and it isn't optional — a `--json` deploy result with a clean exit status only proves the command didn't error, not that the org now matches what the step describes.

**Comment both blocks for a mixed audience** — a reader who's comfortable in a terminal and a reader who's only ever clicked through Trailhead's UI and is seeing this code as a translation of what they just did by hand. Two levels, on every payload and every verification block, no exceptions:

- **A plain-language comment as the first line _inside_ the fence** stating what the block does and _why it matters to this step_ — not a restatement of the heading (`# Creates the custom object` tells a reader nothing the `### Create Custom Object` heading didn't), but the specific reason this shape was chosen: ` ```bash` on its own line, then `# Deploys Energy_Audit__c with all 5 fields in one pass — Rule 2.1 requires schema and FLS to land atomically, so this can't be split into a per-field deploy.` as the very next line, before any `mkdir`/`cat`/`CMD=`. **Never put this line in the surrounding markdown, above the opening ` ```bash ` fence itself** — a line starting with `# ` outside a code fence is Markdown's H1 heading syntax, so it renders as a giant top-level heading and breaks the doc's structure. This has already happened twice from misreading "above the block" as "above the fence" instead of "at the top of the fence" — it's not a one-off slip, so treat "first line inside every fence, never before the ` ```bash `" as a hard placement rule, not a stylistic preference. **This line is the requirement statement — it's the only place that context lives.** Don't also add a separate Requirement-ID heading (`#### [REQ-N.G1.1] ...`) or a "Requirement Specifications" bullet list above the block to restate the same thing a second time in a different format; that's a duplicate layer sitting on top of the comment, not additional information, and it drags the doc's headings and Table of Contents out of sync with Trailhead's own, which Stage 2 requires to stay word for word. If an older doc still carries `[REQ-N.G*]`/`[REQ-N.C*]`-style headings from an earlier draft of this pipeline, that's a leftover to clean up when you're already touching that section — not a pattern to replicate into a new one.
- **Inline comments on every line that carries content, not just the ones that seem non-obvious** — a field type, a flag, a picklist default, a `mkdir -p` path, an `-o <org>` target, a `sed` pattern, a `tee` destination. Err on the side of over-commenting: `<!-- Picklist: locks input to these 3 options so consultants can't free-type a typo -->`, `# --use-tooling-api: FieldDefinition only exists in the Tooling API, not the regular REST API`, `-o trailhead-playground # deploys to the org launched from this unit's Launch button`, `mkdir -p force-app/main/default/objects/Property__c/fields # scaffolds the folder sf expects field metadata to live in`. Skip a line only when there's truly nothing to say — a bare closing tag (`</CustomObject>`), a `EOF` heredoc terminator, a blank line — or it's a word-for-word echo of prose the reader just read directly above (a `<label>Energy Audit</label>` matching text already on the page doesn't need its own comment).

Use `<!-- -->` inline for XML, `#` above (or trailing on) the bash line it explains. This is a deliberate exception to writing sparse, only-when-non-obvious comments elsewhere in this codebase — these blocks are a stand-in for a GUI walkthrough, read on their own by someone who may not know what a flag does, so they lean toward over-explaining rather than under.

Before drafting a payload, decide whether the step is actually worth hand-authoring as XML: only do it when (1) the Metadata API reference has a worked example of your exact structure, (2) the XML uses identifiers you'd choose yourself rather than builder-assigned ones, and (3) a structurally valid deploy is actually equivalent to whatever check you're trying to satisfy. If any of those three fails — a wizard-driven Setup screen, a canvas-generated structure with internal IDs, anything Trailhead's own builder produces that you'd otherwise be guessing at — it's `[GUI]`, not `[CLI]`.

Multiple steps that build toward one logical unit of schema (an object plus its fields, a field plus its FLS grant) can share one payload block and one verification block at the end of that group — they don't need to be deployed and verified one at a time, as long as the verification query actually checks every piece the group touched.

**A payload block with no verification directly beneath it is ambiguous to a reader skimming code blocks — they can't tell a deliberate grouping from a writer who forgot the second block.** Whenever a payload's verification is deferred to a later step for this reason, say so immediately under that payload block, as its own standalone line, in a fixed and recognizable form: `**Deploy and verification deferred — folded into the *<Section Name>* step below, because <the actual reason: e.g. the object has no independent existence in the org until this field joins it>.**` Don't fold that explanation into a longer paragraph of surrounding prose — a reader who's skimming from code block to code block, not reading every sentence, needs to hit it without having to go looking. Every payload block that lacks its own verification must have one of these two things directly below it, no third option: this deferral line, or its own verification query. "Neither" is always a bug to fix, not a stylistic gap to leave for the reader to puzzle out.

**The pipeline is challenge-agnostic: it never special-cases which section CLI lives in.** Code goes wherever a step with a Metadata API surface actually is, in Guided or Challenge alike, symmetrically. The only thing that ever needs a per-unit check is narrower: is a given Challenge instruction a literal restatement of something the Guided Activity already built, or a genuinely different artifact under the same heading? Don't assume either answer — not from the section title, not from what one other unit in the badge turned out to be. Read the raw scrape for both sections and diff what each actually builds: object, artifact type, name. Badge 05 is proof this goes both ways: unit 1's Challenge is a literal restatement (identical object, tab, fields, feed tracking); units 3, 4, 5, and 6's Challenges each build something new instead — unit 3's Opportunity list view where Guided builds an Account list view + chart, unit 4's Opportunity compact layout where Guided builds one on `Energy_Audit__c`, unit 5's Contact record page where Guided builds one on `Energy_Audit__c`, unit 6's Contact WebLink where Guided builds three on `Energy_Audit__c`/Account. One restatement out of five, so the check has to run every time, not just once per badge.

That check changes exactly one thing — whether the Challenge instruction gets a fresh payload or a mention — and nothing else about where code blocks appear:

- **Literal restatement:** author and deploy the payload **once**, under the Guided Activity's own step, resolving any wording mismatch up front (casing, a field-name suffix — pick whichever spec is more precise, usually the Challenge's, since that's what the grader checks). Don't discover the mismatch mid-deploy as a Stage 5 hiccup; that's what caused the `Ground mounted` vs `Ground Mounted` picklist collision in badge 05 unit 1, where the two specs were authored independently instead of reconciled first. The Challenge section still carries its prose verbatim (Stage 2's word-for-word rule doesn't change), but instead of its own payload block it gets a one-line mention (`Already deployed — see the Guided Activity's payload above.`) plus its own verification block — that verification is the one genuinely Challenge-specific artifact, since it's what actually gates clicking "Check Challenge."
- **Different artifact wearing the same heading** (the common case — badge 05 units 3/4/5/6): the Challenge instruction gets its own full payload and verification, same as any other step. Don't collapse it into a mention — that would assert metadata was already deployed when it wasn't.

A unit whose Challenge is multiple-choice only (badge 05 units 2 and 7 — nothing to build there) doesn't raise this question at all: the Guided Activity is the only section building anything, so it's the only section with payload/verification blocks, as usual.

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
  <same prose as the Challenge, copied verbatim per Stage 2>
  <if a literal restatement of Guided: one-line mention that it's already deployed, plus its own verification block>
  <otherwise: its own payload + verification blocks, per requirement, same as any Guided step>

## Technical Post-Mortem & Engineering Learnings
```

File path: `docs/trails/developer_beginner/badges/<NN_badge>/UNIT_<N>_<NAME>.md`. Raw source: `.../raw/UNIT_<N>_RAW_GUIDED_ACTIVITY.md`. Deploy/verification logs: `.../logs/`.

A unit whose Challenge is multiple-choice only has no Hands-On Challenge payload section at all — every payload+verification block lives inline under the Guided Activity steps, same as the general case above.

---

## Parallelizing Across Units

Stages 2–3 (content authoring) are the parallelizable part — each unit's draft is a distinct file, so one subagent per unit is safe to run concurrently, as long as that unit's raw content has already been pasted in full. Stage 4 is never delegated and never parallel — it's one developer, one org, run in order.

Two things break naive fan-out, so hand every subagent a short shared-context note before it starts:

- **Naming continuity** — later units reference object/field names decided earlier in the same badge (e.g., `Property__c`, `Offer__c`). A subagent drafting Unit 3 blind can invent a name that collides with what Unit 1 already established.
- **Shared roll-up files** — a badge's index doc, if one exists, and the trail progress table are edited once per unit, by the coordinator, after each subagent's draft lands — never by two subagents at once.

Practical flow: paste in raw content for as many units as you've scraped → subagents fan out one-per-unit against this pipeline plus the current naming registry → drafts get reviewed and the roll-up files updated once → you take Stage 4 from there.
