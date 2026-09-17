# CSV Import Style Gate

Use this gate when creating or revising Jira-importable MFD test-step CSV artifacts.

## Purpose
- Enforce a consistent CSV shape so Jira imports produce the expected Step and Expected Result columns.
- Keep file-format checks separate from test-step quality checks in [CSV checklist](./csv-checklist.md).

## Required Header and Columns
- The first row must be exactly:
  `"#",Step,Expected Result`
- The CSV must have exactly three columns in this order:
  1. `#`
  2. `Step`
  3. `Expected Result`

## Row and Cell Rules
- `#` must be an integer step number, increasing in execution order.
- `Step` contains the action text.
- `Expected Result` rules:
  - If the step verifies one or more requirements:
    1. First line requirement tags, for example: `[DMFDREQ-1234], [DMFDREQ-5678]`
    2. One blank line
    3. Observable expected-result prose
  - If the step does not verify a requirement, the value must be exactly `N/A`.

## CSV Encoding and Formatting
- Use comma-separated CSV.
- Use double quotes only when needed by CSV rules (for example multiline expected results).
- Do not add extra columns, trailing delimiters, or alternate header names.
- Keep whitespace intentional; avoid leading/trailing spaces around cell values.

## Validation Sequence
1. Run [CSV checklist](./csv-checklist.md) before drafting to confirm coverage intent.
2. Draft/refine test steps.
3. Validate this style gate before handoff or Jira import.
4. Run [CSV checklist](./csv-checklist.md) again after CSV generation.

## Minimal Template
```csv
"#",Step,Expected Result
1,[Precondition Check] Start test from nominal conditions.,N/A
2,[State Transition Test] Verify state indicator changes after action.,"[DMFDREQ-1234]

State indicator shows expected value after the action."
```
