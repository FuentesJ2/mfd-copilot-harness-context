---
description: "Use when creating or revising Jira-import test-step CSV artifacts. Enforces CSV header, column shape, and expected-result formatting."
applyTo: "**/*test-steps*.csv"
---

# MFD Jira Test-Step CSV Conventions

## Scope
- Applies to Jira test-step CSV artifacts in this workspace that match `*test-steps*.csv`.
- These files are authoring artifacts created in developer environments and imported into Jira.

## Required CSV Shape
- First row must be exactly:
  `"#",Step,Expected Result`
- Keep exactly three columns in this exact order:
  1. `#`
  2. `Step`
  3. `Expected Result`

## Field Rules
- `#` must be a numeric execution order value.
- `Step` must contain concrete, observable operator/system action text.
- `Expected Result` rules:
  - If requirement(s) are verified in the step:
    1. First line contains requirement tag(s), for example `[DMFDREQ-1651]`.
    2. Then one blank line.
    3. Then expected-result prose.
  - If no requirement applies, value must be exactly `N/A`.

## Authoring Flow Expectations
- Draft steps in chat before generating CSV.
- Use the CSV checklist before drafting and after CSV generation.
- Do not invent requirement IDs, enums, ranges, or timing values.

## Layering Model
- These core CSV rules are mandatory and are evaluated first.
- Optional step-prefix annotation preferences may be layered afterward using `.github/instructions/mfd-test-step-annotation-overlay.instructions.md`.
- Overlay rules must not alter core requirements for header, column order, or Expected Result formatting.

## References
- `.github/skills/mfd-test-authoring-validation/references/csv-import-style.md`
- `.github/skills/mfd-test-authoring-validation/references/csv-checklist.md`
- `.github/instructions/mfd-test-step-annotation-overlay.instructions.md`
