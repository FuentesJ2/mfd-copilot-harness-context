# CSV Validation Checklist

Use this checklist when a test-case CSV is created, reviewed, compared, revised, or prepared for Jira re-import.

## CSV Artifact Meaning
- In this workflow, CSV files represent Jira test steps exported from the Jira test case page.
- Typical flow: export CSV from Jira test steps, edit/review CSV, then re-import to Jira.
- Some Jira test cases may have missing description text and/or no authored steps. When missing, generate those fields using the standard fallback template in [Missing Jira test-case format](./missing-jira-test-case-format.md).

## Scope Boundary
- This checklist evaluates test-step quality and requirement coverage.
- CSV import shape and formatting are enforced separately by [CSV import style gate](./csv-import-style.md).
- Run this checklist before drafting steps and again after generating the CSV artifact.

## Table Shape
Use this table structure:

| # | Checklist item | Status | Reason | Recommended fix |
|---|---|---|---|---|

Allowed status values:
- MET
- NOT MET
- NOT APPLICABLE
- UNKNOWN

Rules:
- Every NOT MET and UNKNOWN row must include Reason and Recommended fix.
- Use None in Recommended fix for MET and NOT APPLICABLE.
- Show totals for all status values after the table.
- Never hide failed or unknown rows.

## Checklist Items (Order Is Mandatory)
1. Are the requirements linked?
2. Is Description in Objective clear?
3. Are Pass/Fail Conditions clear?
4. Is initial status confirmed?
5. Do expected steps list which requirement(s) are being verified?
6. Tables annotated?
7. For numerical requirements, are minimum, maximum and negative numbers tested?
8. At limits do we approach and then exceed and return?
9. Are all state transitions tested?
10. All conditional statements from requirement tested?
11. Are tolerances defined?
12. Is Test Status (pass/fail) measurable and defined?
13. Do steps with no expected result have N/A?
14. Does the test case test for robustness beyond expected min/max values (within test-environment bounds)?
15. Does the test case test ways in which bugs could be present even if requirements are met (adjacent behavior)?
16. If differences are calculated, are negative differences checked?
17. Are each variable tested independently or with different values?
18. Are all relevant requirement variations tested (for example CC-A/B/C, Left/Right, PRI/SEC)?
19. Are all requirements linked to this test case verified?
20. Are requirements linked to this test case not linked to other test cases?

## Step Content Rules
- Steps that verify requirements should identify requirement tags in Expected Result.
- If no requirement applies, Expected Result must contain only N/A.
- Keep step order aligned to the intended execution sequence.
- For exact header, column shape, and multiline formatting, use [CSV import style gate](./csv-import-style.md).

## Missing Jira Content Rules
- If Jira description is empty, create a draft description using this exact heading order:
  - Objective
  - Context paragraph
  - Test
  - REQ
- If Jira authored steps are missing, create CSV-ready rows for `#`, `Step`, and `Expected Result` derived from requirements and available source truth.
- Keep wording concrete, observable, and verifiable.
- Do not invent requirement IDs; if requirement mapping is unknown, keep requirement linkage explicit as unknown and add an open question.
