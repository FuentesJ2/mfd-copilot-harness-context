---
name: mfd-test-script-validation
description: "Use when drafting, revising, reviewing, or validating MFD Python test scripts during TEST SCRIPT DRAFT and TEST SCRIPT REVIEW phases."
argument-hint: "Provide Jira key(s), workflow phase, source test-step context, and target script path."
---

# MFD Test-Script Validation

## Phase Scope
- In scope phases:
  - TEST SCRIPT DRAFT
  - TEST SCRIPT REVIEW
- Out of scope phases:
  - DRAFT
  - TEST CASE REVIEW
  - TEST SCRIPT COMPLETE
- If phase is out of scope, report PHASE_OUT_OF_SCOPE and request test-case routing.

## Purpose
- Draft executable Python scripts from reviewed test-step intent.
- Review and harden existing scripts during TEST SCRIPT REVIEW.
- Keep script actions and verifications traceable to step IDs and expected results.
- Keep implementation aligned to framework interfaces and dictionary-backed parameters.

## When To Use
- The user asks to create or revise a delta test script.
- The user asks to review script quality, traceability, or checklist compliance.
- The user asks to reconcile script behavior with reviewed test-step intent.

## Required Inputs
- Jira test-case key when available.
- Current workflow phase (TEST SCRIPT DRAFT or TEST SCRIPT REVIEW).
- Source step intent from Jira-authored steps or CSV artifact.
- Target script path.

## Workflow
1. Intake and phase confirm:
   - Confirm scope is script work.
   - Confirm phase is TEST SCRIPT DRAFT or TEST SCRIPT REVIEW.
2. Pull live Jira context first:
   - Use `.github/skills/jira-context-cli/SKILL.md` for named keys.
   - Capture current status, links, comments, and authored steps.
3. Load authority references:
   - Open [Authoritative references](./references/authoritative-references.md).
4. Build or revise script behavior:
   - Map script flow to step order and expected results.
   - Use [Test script API reference](./references/test-script-api-reference.md) for common framework patterns.
5. Apply style and traceability rules:
   - Apply `.github/instructions/mfd-delta-test-scripts-python.instructions.md` first for style and structure decisions.
   - Resolve remaining ambiguity via neighboring scripts only after source inspection.
   - Run [Script checklist](./references/script-checklist.md).
6. Report:
   - Include assumptions, unknowns, and open questions.
   - If live Jira and local artifacts conflict, report both and treat live Jira metadata as current.

## Output Contract
- SUMMARY
- SCRIPT
- SCRIPT_CHECKLIST_REVIEW
- VALIDATION_REPORT
- ASSUMPTIONS
- OPEN_QUESTIONS

## Safety And Blocking
- Do not invent data IDs, enums, ranges, units, timing, or framework interfaces.
- If parameter or enum resolution fails, flag BLOCKED_PARAMETER_NOT_FOUND.
- If required dictionary evidence is unavailable, flag BLOCKED_DICTIONARY_UNAVAILABLE.
- If multiple candidates are valid, flag AMBIGUOUS_PARAMETER.
- If phase cannot be determined, flag PHASE_UNKNOWN.

## References
- [Script checklist](./references/script-checklist.md)
- [Test script API reference](./references/test-script-api-reference.md)
- [Authoritative references](./references/authoritative-references.md)
