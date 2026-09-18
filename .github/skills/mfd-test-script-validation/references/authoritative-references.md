# Authoritative References For Test-Script Work

Use this file to determine authority for each decision type during TEST SCRIPT DRAFT and TEST SCRIPT REVIEW.

## Decision-Type Authority
- Current Jira issue metadata (status, links, comments, authored steps):
  - Authority: live Jira/TestRay fetch via `.github/skills/jira-context-cli/SKILL.md`
- Data IDs, enums, units, and ranges:
  - Authority: DELTA data dictionary XMLs in `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA/`
- MFD runtime/page behavior:
  - Authority: MFD source in `mfd/source/` and `mfd/gls/`, plus VM-observed behavior
- Script implementation conventions:
  - Primary authority: `.github/instructions/mfd-delta-test-scripts-python.instructions.md`
  - Secondary authority: neighboring scripts only when conventions remain ambiguous after instruction-level rules
- Script quality and traceability review:
  - Authority: [Script checklist](./script-checklist.md)

## Known Style Exception In Legacy Examples
- `MFD-9226_HSI_Mode.py` and `MFD-9228_HSI_Wind.py` remain useful behavioral references.
- Their `log_step` wrapper pattern is not authoritative for new or revised scripts.
- Prefer plain in-line `self.log(...)` usage in `run()` per `.github/instructions/mfd-delta-test-scripts-python.instructions.md`.

## Exclusions
- Do not treat supporting artifacts as normative policy when they conflict with current instruction-level rules.
- Do not infer requirements or expected behavior solely from legacy script style patterns.
