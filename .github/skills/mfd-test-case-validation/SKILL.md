---
name: mfd-test-case-validation
description: "Use when drafting, revising, reviewing, or validating MFD Jira test-case steps during DRAFT and TEST CASE REVIEW, including Jira-import CSV artifacts."
argument-hint: "Provide Jira key(s), workflow phase, and target CSV path."
---

# MFD Test-Case Step Validation

## Phase Scope
- In scope phases:
  - DRAFT
  - TEST CASE REVIEW
- Out of scope phases:
  - TEST SCRIPT DRAFT
  - TEST SCRIPT REVIEW
  - TEST SCRIPT COMPLETE
- If phase is out of scope, report PHASE_OUT_OF_SCOPE and request script-phase routing.

## Purpose
- Draft, revise, and harden Jira test-case descriptions and test steps.
- Produce or revise Jira-importable CSV test-step artifacts.
- Keep expected-result wording traceable to linked requirements and observable outcomes.
- Apply one definitive description and step format for both missing and pre-existing Jira content.

## When To Use
- The user asks to create or revise test steps for Jira.
- The user asks to review, harden, or update existing test steps.
- The user asks to generate or validate a Jira-importable test-step CSV.

## Required Inputs
- Jira test-case key when available.
- Current workflow phase (DRAFT or TEST CASE REVIEW).
- Target CSV path when file output is requested.
- Requirement linkage context from Jira issue links.

## Definitive Jira Test-Case Description And Step Format
- This format is required for all test-case work in scope, whether Jira already has description/steps or not.

Description template:

**Objective**: Show that <page or feature> correctly <expected behavior>.

For this test, the <page or feature> will be tested by <operator/system action> and verifying <observable outcome>. <Include what the operator checks on-screen and where it appears when relevant.>

**Test**: <Page or feature> <test name> Test.

**REQ**: [DMFDREQ-####](https://avjira/browse/DMFDREQ-####)

If multiple requirements apply:
- **REQ**: [DMFDREQ-####](https://avjira/browse/DMFDREQ-####), [DMFDREQ-####](https://avjira/browse/DMFDREQ-####)

Step template (CSV):
- Header row must be exactly `"#",Step,Expected Result`.
- Keep exactly three columns in this order: `#`, `Step`, `Expected Result`.
- `#` must be an integer step number in execution order.
- `Step` must contain concrete, observable operator/system action text.
- `Expected Result` formatting:
   - If requirement(s) are verified:
      1. First line contains requirement tags, for example `[DMFDREQ-1234], [DMFDREQ-5678]`.
      2. One blank line.
      3. Observable expected-result prose.
   - If no requirement applies, value must be exactly `N/A`.
- Apply step-label overlay rules from `.github/instructions/mfd-test-step-annotation-overlay.instructions.md`.

Minimal CSV template:

```csv
"#",Step,Expected Result
1,[Precondition Check] Start test from nominal conditions.,N/A
2,[State Transition Test] Verify state indicator changes after action.,"[DMFDREQ-1234]

State indicator shows expected value after the action."
```

## Workflow
1. Intake and phase confirm:
   - Confirm scope is test-case step work.
   - Confirm phase is DRAFT or TEST CASE REVIEW.
2. Pull live Jira context first:
   - Use `.github/skills/jira-context-cli/SKILL.md` for named keys.
   - Capture status, links, comments, description, and authored steps.
3. Load evidence maps:
   - Open [Source-truth map](./references/source-truth-map.md).
   - Open [Authoritative references](./references/authoritative-references.md).
4. Author and normalize content:
   - If description and/or steps are missing, draft directly in the definitive format above.
   - If authored steps already exist, revise and harden them to the same definitive format.
5. Run quality and format gates:
   - Run [CSV checklist](./references/csv-checklist.md) before drafting.
   - Draft or revise steps.
   - Validate header, column order, expected-result structure, and `N/A` usage against the definitive format above.
   - Run [CSV checklist](./references/csv-checklist.md) again after revision.
6. Report:
   - Include assumptions, unknowns, and open questions.
   - If live Jira and repository CSV conflict, report both and treat live Jira metadata as current.

## Output Contract
- TEST_CASE_KEY
- TEST_CASE_TITLE
- TEST_CASE_DESCRIPTION
- TEST_STEPS (CSV form)
- CSV_FORMAT_REVIEW
- CSV_CHECKLIST_REVIEW
- VALIDATION_REPORT
- ASSUMPTIONS
- OPEN_QUESTIONS

## Safety And Blocking
- Do not invent requirement IDs, data IDs, enums, ranges, units, or timing.
- If linked requirement evidence is missing, mark UNKNOWN and ask focused follow-up questions.
- If required dictionary evidence is unavailable, flag BLOCKED_DICTIONARY_UNAVAILABLE.
- If phase cannot be determined, flag PHASE_UNKNOWN.

## References
- [CSV checklist](./references/csv-checklist.md)
- [Source-truth map](./references/source-truth-map.md)
- [Authoritative references](./references/authoritative-references.md)
