# MFD Workspace Copilot Instructions

## Project Scope
- This workspace contains multiple repositories with different purposes:
  - `mfd/`: MFD display application source code.
  - `mfd-test-framework/`: test framework GUI and infrastructure.
  - `mfd-test-framework/scripts/delta-test-scripts/`: nested repository where most new MFD test-script work is authored.
- `mfd/` and `mfd-test-framework/` are separate repositories. `delta-test-scripts/` is a nested repository under `mfd-test-framework/scripts/`.
- Default target for new MFD test-script authoring is `mfd-test-framework/scripts/delta-test-scripts/` unless the user specifies another location.

## Primary Mission
- Support MFD verification workflows:
  - test-case work (including CSV artifacts), and
  - Python test-script generation or revision.
- In this workspace, default intent is to write or revise MFD test cases and then produce corresponding test scripts.
- Phase-focused skills:
  - `.github/skills/mfd-test-case-validation/SKILL.md` for DRAFT and TEST CASE REVIEW.
  - `.github/skills/mfd-test-script-validation/SKILL.md` for TEST SCRIPT DRAFT and TEST SCRIPT REVIEW.

## Jira Verification Workflow
- Test Case Draft and Requirement Linking:
  - Create the Jira test case and link all in-scope requirements.
  - Initial test-case state is DRAFT.
- Test Steps Draft (CSV Authoring for Jira Import):
  - Draft test steps in AI chat first.
  - Run the CSV checklist before drafting to guide coverage.
  - Generate a Jira-importable CSV artifact in the developer environment.
  - Apply the definitive Jira test-case description and step format from `.github/skills/mfd-test-case-validation/SKILL.md`.
  - Apply the active step-prefix annotation overlay from `.github/instructions/mfd-test-step-annotation-overlay.instructions.md` (default for this workspace).
  - If a different annotation style is needed, modify or replace only the overlay file while keeping the same path.
  - Re-run the CSV checklist after CSV creation before Jira import.
- Test Case Review:
  - Submit the test case for TEST CASE REVIEW.
  - Resolve review feedback and keep requirement linkage accurate.
- Test Script Draft:
  - After test-case review, draft the Python test script in `mfd-test-framework/scripts/delta-test-scripts/`.
- Test Script Review and Merge:
  - Submit for TEST SCRIPT REVIEW.
  - Resolve feedback; validated scripts are merged by leads.

## MFD Domain Context
- `MFD` means `Multi Function Display`.
- The MFD software is the pilot-facing cockpit display for DELTA.
- The MFD presents flight, navigation, vehicle, and diagnostic information.
- Pilots interact with the display through bezel buttons and knobs.
- The UI is organized into top and bottom page regions.
- Test artifacts in this workspace validate both data presentation and operator interaction behavior.

## MFD Page Layout Reference
- Use this as foundational test-authoring context for page-navigation intent.
- This root-level layout is canonical for both test-case ideation and script authoring.

Top pages:
- `PDF`
- `SYSTEMS`

Bottom pages and subpages:
- `NAV`: `MAP`, `NAV`, `SETUP`
- `COM`: `COM`, `XPDR`
- `PNEU`
- `ELEC`
- `ECS`: `PRESS`, `TEMP`
- `RKT`: `ALL`, `PRESS`, `VALVE`, `CTN`
- `FTHR`
- `CTRL`: `SURFC`, `RCS`, `FBW-CMD`, `STAB`, `RUDDER`, `ELEVON`
- `PLAN`: `FLT`, `W&B`, `ROUTE`, `INS`
- `DIAG`: `HIST`, `CAS`, `ADC`, `A&B`, `INS-A`, `INS-B`, `XPDR`, `DAU`, `MFD`, `HBEAT`, `ANALOG`, `DIO`, `BEZEL`, `RMC`, `BMS`, `FCC-ANA`, `FCC-DIO`, `FCC-FAULT`, `CTRLR`, `CTRLR-FAULT`, `STICK`, `FTHR`

Script-level API examples for navigation and control interactions are documented in:
- `.github/skills/mfd-test-script-validation/references/test-script-api-reference.md`

## Runtime Environment
- MFD UI and MFD test-framework execution are performed in an Oracle VirtualBox virtual machine environment.
- If runtime behavior differs from static artifacts, prioritize VM-observed behavior and identify the artifact mismatch.

## MFD Display Topology
- There are three display instances: `MFD_L`, `MFD_C`, and `MFD_R`.
- These correspond to left, center, and right cockpit display roles.
- When a requirement or script behavior is side- or display-dependent, keep display-specific context explicit.

## Source Of Truth And Data Precedence
- For named Jira/TestRay issues (for example `MFD-####`, `DMFDREQ-####`), use the Jira context CLI skill early and often, and fetch live context first under `.github/skills/jira-context-cli/`.
- Default workflow for issue-driven work: run Jira CLI fetch first, then analyze repository artifacts.
- Use Jira CLI first for current requirement text, status, links, comments, authored steps, and related issue context.
- After Jira fetches that save normalized JSON, read the saved JSON file directly from the workspace; do not use terminal parsing wrappers (PowerShell/Python/jq) unless the user explicitly asks for command-based parsing output.
- Treat repository CSV files as workflow artifacts and style references, not as the primary source for current Jira status.
- CSV files in this workflow are typically exported from Jira test steps, edited, and re-imported.
- If live Jira data conflicts with repository CSV content, report both and prefer live Jira for current issue metadata.
- For ambiguous expected behavior, inspect MFD source first, then consult relevant neighboring test scripts if ambiguity remains.

## Foundational Safety Rules
- Do not fabricate data dictionary identifiers, enums, value ranges, units, timing, or framework interfaces.
- If required dictionary or interface details are missing, mark the gap explicitly and request clarification.
- Keep assumptions explicit and separate from confirmed facts.
- Keep edits scoped to the repository and paths requested by the user.

## Key Reference Map
- Primary test-script authoring area:
  - `mfd-test-framework/scripts/delta-test-scripts/`
- Test framework script base and helpers:
  - `mfd-test-framework/scripts/mfd_test_script.py`
  - `mfd-test-framework/scripts/delta-test-scripts/helpers/`
- DELTA data dictionary XMLs used for data IDs and enums:
  - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA/`
  - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA_Data_Dictionary.xml`
- Parallel dictionary tree in MFD source repo (may be in or out of sync with framework copy):
  - `mfd/common/data_dictionary/DELTA/`
  - `mfd/common/data_dictionary/DELTA_Data_Dictionary.xml`
- MFD source-truth code areas to inspect for behavior:
  - `mfd/source/`
  - `mfd/gls/`
- MFD runtime interaction and page-wiring references:
  - `mfd/source/Common/Input/`
  - `mfd/source/Common/Display/`
  - `mfd/source/SpaceShip/DELTA/DeltaMfd.cpp`

## Repository Context References
- Canonical MFD supporting artifacts in this workspace are under `.github/agents/MFD Agent Supporting Docs/`.
- If a referenced mirror path is unavailable, do not assume it exists; use available workspace paths and report the mismatch.
- Additional supporting docs can be added under `.github/agents/MFD Agent Supporting Docs/`.
- Keep normative workflow policy in `.github/skills/` and `.github/instructions/`; treat Supporting Docs as examples and artifacts.

## Context Engineering Guidance
- Keep this file minimal and always-on.
- Put detailed procedural workflows, long checklists, and role-specific generation logic in skills or agent files.
- Put file-type-specific coding conventions in `.github/instructions/*.instructions.md` using focused `applyTo` patterns.
- Keep personal or team-specific step-annotation preferences in one hot-swappable repo-level overlay instruction file.
- Keep context-placement policy in `.github/context-placement.md`.