# Authoritative References For MFD Test Authoring

Use this file to understand which references are authoritative for each decision type.

## Decision-Type Authority
- Current Jira issue metadata (status, links, comments, authored steps):
  - Authority: live Jira/TestRay fetch via `.github/skills/jira-context-cli/SKILL.md`
- Data IDs, enums, ranges, and units:
  - Authority: DELTA data dictionary XMLs in `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA/`
- MFD runtime/page behavior:
  - Authority: MFD source in `mfd/source/` and `mfd/gls/`, plus VM-observed behavior
- Script implementation conventions:
  - Authority: neighboring scripts and `.github/instructions/mfd-delta-test-scripts-python.instructions.md`
- CSV import shape and expected-result formatting:
  - Authority: `.github/instructions/mfd-jira-test-steps-csv.instructions.md` and `csv-import-style.md`

## Curated Supporting References
- Supporting examples are under `.github/agents/MFD Agent Supporting Docs/`.
- Treat these as style/behavior references, not live Jira status truth.
- Recommended paired reference for end-to-end alignment:
  - `MFD-9228_HSI_Wind.py`
  - `MFD-9228-test-stepsv6.csv`

## Exclusions
- Do not treat stale requirement export CSVs as primary requirement source when live Jira data is available.
- If supporting references conflict with current rules, follow current rules and report the mismatch.
