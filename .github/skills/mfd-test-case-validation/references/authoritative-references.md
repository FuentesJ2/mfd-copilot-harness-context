# Authoritative References For Test-Case Step Work

Use this file to determine authority for each decision type during DRAFT and TEST CASE REVIEW.

## Decision-Type Authority
- Current Jira issue metadata (status, links, comments, authored steps):
  - Authority: live Jira/TestRay fetch via `.github/skills/jira-context-cli/SKILL.md`
- Requirement linkage and requirement wording:
  - Authority: linked requirements fetched from live Jira context
- CSV import shape and expected-result formatting:
  - Authority: `.github/skills/mfd-test-case-validation/SKILL.md` (Definitive Jira Test-Case Description And Step Format section)
- Step readability label policy:
  - Authority: `.github/instructions/mfd-test-step-annotation-overlay.instructions.md`
- Test-step quality and coverage review:
  - Authority: [CSV checklist](./csv-checklist.md)
- Behavior ambiguity resolution:
  - Authority order: MFD source first, neighboring scripts second

## Exclusions
- Do not treat repository CSV files as current Jira status truth when live Jira data is available.
- Do not treat supporting artifacts as normative policy when they conflict with current instructions.
