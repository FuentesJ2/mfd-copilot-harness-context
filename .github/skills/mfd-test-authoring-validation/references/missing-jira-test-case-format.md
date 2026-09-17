# Missing Jira Test-Case Format

Use this template when a Jira test case has missing description text and/or no authored test steps.

## Description Template
Use this exact section order:

**Objective**: Show that <page or feature> correctly <expected behavior>.

For this test, the <page or feature> will be tested by <operator/system action> and verifying <observable outcome>. <Include what the operator checks on-screen and where it appears when relevant.>

**Test**: <Page or feature> <test name> Test.

**REQ**: [DMFDREQ-####](https://avjira/browse/DMFDREQ-####)

If multiple requirements apply:
- **REQ**: [DMFDREQ-####](https://avjira/browse/DMFDREQ-####), [DMFDREQ-####](https://avjira/browse/DMFDREQ-####)

## Step Template (CSV-Ready)
Use columns:
- #
- Step
- Expected Result

For Jira CSV artifacts, include this exact header row:
`"#",Step,Expected Result`

Expected Result cell format:
1. First line requirement tags:
   [DMFDREQ-####], [DMFDREQ-####]
2. One blank line.
3. Expected-result prose.

If no requirement applies to a step:
- Expected Result must contain only N/A.

For detailed CSV shape and formatting rules, use [CSV import style gate](./csv-import-style.md).

## Quality Rules
- Use explicit, observable actions and outcomes.
- Keep wording concise and unambiguous.
- Include side/display context when relevant (MFD_L, MFD_C, MFD_R).
- Do not invent requirement IDs, enums, or data dictionary identifiers.
