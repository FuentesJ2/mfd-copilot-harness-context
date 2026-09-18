---
name: mfd-test-authoring-validation
description: 'Use when creating, revising, reviewing, or validating MFD Jira-exported test-step CSV artifacts and Python test scripts in delta-test-scripts. This skill keeps CSV validation and script validation distinct inside one workflow.'
argument-hint: 'Provide artifact type (csv, script, or both), Jira key, and target path(s).'
---

# MFD Test Authoring and Validation

## Purpose
- Provide one repeatable workflow for MFD verification artifacts while keeping two artifact types separate:
  - CSV test-step artifacts exported from Jira and later re-imported.
  - Python test scripts that implement those test steps in the test bench framework.
- Support ad-hoc engineering investigation when test intent requires source-truth checks in MFD code, data dictionary XMLs, and neighboring scripts.

## Jira Workflow Phase Awareness
- This skill is phase-aware and should determine the current Jira workflow phase before generating or revising artifacts.
- Use this phase model in order:
  1. DRAFT:
     - Test case may have complete steps, partial steps, or no authored steps.
     - If no authored steps exist, draft CSV-ready steps and expected results from live test-case context and linked requirements fetched via jira-context-cli, then confirm behavior against source-truth references.
  2. TEST CASE REVIEW:
     - Revise description/steps from review feedback.
     - Re-run CSV style and checklist validation before re-submission.
  3. TEST SCRIPT DRAFT:
     - Draft script from reviewed or approved test-step intent.
  4. TEST SCRIPT REVIEW:
     - Revise script from review feedback and re-run script checklist.
  5. TEST SCRIPT COMPLETE:
     - Script is validated and merged; only perform edits when a new change request appears.
- If phase cannot be determined from user/Jira context, set phase status to PHASE_UNKNOWN in validation notes and ask one focused follow-up.

## When to Use
- The user asks to create, revise, compare, or review MFD test-step CSV artifacts.
- The user asks to create, revise, compare, or review MFD Python test scripts.
- The user asks for checklist-based validation of test cases or scripts.
- The user needs cross-checking across Jira, CSV steps, data dictionary XMLs, neighboring scripts, and MFD source behavior.

## Artifact Model
- CSV artifact:
  - Represents Jira test steps exported to CSV for Jira re-import.
  - Jira import artifacts use three columns with exact header: `"#",Step,Expected Result`.
  - Is a workflow artifact for editing and review, then re-import into Jira.
  - Some Jira test cases may be missing description text and/or authored steps; in those cases, create draft content using the standard format template in this skill.
- Script artifact:
  - Implements executable verification logic in Python.
  - Must map to CSV step intent and framework interfaces.
- Rule:
  - Do not apply the script checklist to CSV-only work.
  - Do not apply the CSV checklist to script-only work.
  - If both artifacts are in scope, run and report both checklists separately.

## Activation And Applicability
- This skill is activated for CSV work, script work, or both.
- Apply CSV workflow during DRAFT and TEST CASE REVIEW phases.
- Apply script workflow during TEST SCRIPT DRAFT and TEST SCRIPT REVIEW phases.

## Evidence Priority
1. Live Jira/TestRay context via [jira-context-cli skill](../jira-context-cli/SKILL.md) for named issues (MFD-####, DMFDREQ-####).
2. Current CSV artifact in scope for exact step wording and expected-result mapping.
3. DELTA data dictionary XMLs in mfd-test-framework; then cross-check with MFD repo XMLs when needed.
4. Existing scripts and neighboring scripts in delta-test-scripts for established local patterns.
5. MFD source code and page-flow behavior when artifact text is ambiguous.

Before deep inspection, open:
- [Source-truth map](./references/source-truth-map.md)
- [Authoritative references](./references/authoritative-references.md)

For script implementation details, open:
- [Test script API reference](./references/test-script-api-reference.md)

## Key Reference Paths
- Script authoring target:
  - `mfd-test-framework/scripts/delta-test-scripts/`
- Framework base script:
  - `mfd-test-framework/scripts/mfd_test_script.py`
- Framework DELTA dictionary:
  - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA/`
  - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA_Data_Dictionary.xml`
- MFD repo dictionary mirror:
  - `mfd/common/data_dictionary/DELTA/`
  - `mfd/common/data_dictionary/DELTA_Data_Dictionary.xml`
- MFD source truth areas:
  - `mfd/source/`
  - `mfd/gls/`
- Supporting references:
  - `.github/agents/MFD Agent Supporting Docs/`

## Workflow
1. Intake and classify scope:
   - Determine whether work is CSV, script, or both.
  - Determine the Jira workflow phase when possible: DRAFT, TEST CASE REVIEW, TEST SCRIPT DRAFT, TEST SCRIPT REVIEW, or TEST SCRIPT COMPLETE.
   - Identify Jira keys, requirement keys, and target file paths.
   - Detect whether Jira description or test steps are missing.
2. Gather evidence:
   - Pull live Jira context first for named issues unless user explicitly requests CSV-only offline flow.
   - Load [Source-truth map](./references/source-truth-map.md) and [Authoritative references](./references/authoritative-references.md) to guide evidence lookup.
   - Read relevant CSV, script(s), dictionary XMLs, and neighboring scripts.
   - Inspect MFD source if behavior intent is unclear.
3. Execute artifact-specific workflow:
   - If Jira description and/or steps are missing, generate the missing test-case content using [Missing Jira Test-Case Format](./references/missing-jira-test-case-format.md). When authored steps are missing, derive draft steps from live test-case context and linked requirements from jira-context-cli, then align with source-truth evidence.
   - For CSV work in DRAFT or TEST CASE REVIEW:
     - Run [CSV checklist](./references/csv-checklist.md) before drafting to drive coverage planning.
     - Draft or revise test steps.
     - Enforce [CSV import style gate](./references/csv-import-style.md) before artifact handoff.
     - Run [CSV checklist](./references/csv-checklist.md) again after CSV artifact creation and report remaining gaps.
   - For script work in TEST SCRIPT DRAFT or TEST SCRIPT REVIEW:
     - Use [Test script API reference](./references/test-script-api-reference.md) for framework call patterns.
     - Use [Script checklist](./references/script-checklist.md).
4. Cross-artifact consistency (only when both are in scope):
   - Verify script step order and expected outcomes align with CSV steps.
   - Verify requirement tags and script requirement comments are consistent.
5. Report output:
   - Include explicit assumptions, unknowns, and open questions.
   - Do not invent IDs, enums, ranges, timing, or framework interfaces.

## Output Contract
- CSV-focused tasks:
  - TEST CASE KEY
  - TEST CASE TITLE
  - TEST CASE DESCRIPTION
  - TEST STEPS (CSV form)
  - CSV_IMPORT_STYLE_GATE_REVIEW
  - CSV_CHECKLIST_REVIEW
  - VALIDATION_REPORT
  - ASSUMPTIONS
  - OPEN_QUESTIONS
- Script-focused tasks:
  - SUMMARY
  - SCRIPT
  - SCRIPT_CHECKLIST_REVIEW
  - VALIDATION_REPORT
  - ASSUMPTIONS
  - OPEN_QUESTIONS
- Combined tasks:
  - Include both checklist sections and clearly separate CSV findings from script findings.

## Safety and Blocking
- If dictionary artifacts are unavailable for required parameter resolution, set status to BLOCKED_DICTIONARY_UNAVAILABLE and request corrected paths.
- If a parameter or enum cannot be resolved, flag BLOCKED_PARAMETER_NOT_FOUND.
- If multiple matches exist, flag AMBIGUOUS_PARAMETER and list candidates.
- If workflow phase cannot be determined, flag PHASE_UNKNOWN and request minimal missing phase context.
- Keep assumptions explicit and keep unresolved items in OPEN_QUESTIONS.

## References
- [CSV import style gate](./references/csv-import-style.md)
- [CSV checklist](./references/csv-checklist.md)
- [Script checklist](./references/script-checklist.md)
- [Test script API reference](./references/test-script-api-reference.md)
- [Source-truth map](./references/source-truth-map.md)
- [Authoritative references](./references/authoritative-references.md)
- [Evidence map (legacy alias)](./references/evidence-map.md)
- [Missing Jira test-case format](./references/missing-jira-test-case-format.md)
