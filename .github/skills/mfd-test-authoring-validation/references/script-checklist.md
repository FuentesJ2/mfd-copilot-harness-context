# Script Validation Checklist

Use this checklist when a Python test script is created, reviewed, compared, revised, or prepared for bench execution.

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
1. Is the required copyright notice included?
2. Is the test logic implemented according to the test case, including step order and expected results?
3. Does the file name follow the standard format [project]-[Jira test case ID]_[test name].py?
4. Are shared helper functions used where established helpers exist or repeated logic justifies a helper?
5. Is the script deterministic, repeatable, and readable?
6. Are logging and verification messages appropriate and traceable to test step numbers?
7. Is the script free of spelling mistakes and typographical errors?
8. Are shared wrappers used for communication interfaces used across components?
9. Do functions provide the setup and actions required to execute each test step?
10. Does the script include functions or framework verification calls that evaluate expected behavior?
11. Are prompt functions used for manual test actions, or marked NOT APPLICABLE for fully automated tests?

## Script-Specific Rules
- Do not invent data IDs, enums, units, ranges, or timing.
- Add step comments at execution points in format: # Step <id>: <exact CSV Step text>.
- Include step number context in verification messages.
- Keep requirement comments tied only to requirement IDs present in that step's CSV expected result.
