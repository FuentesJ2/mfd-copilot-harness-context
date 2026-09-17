---
description: "Use when creating or revising MFD Python test scripts in delta-test-scripts. Covers script shape, step traceability, and data-dictionary-safe parameter usage."
applyTo: "mfd-test-framework/scripts/delta-test-scripts/**/*.py"
---

# MFD Delta Test Script Conventions

## Scope
- Applies only to Python files in delta-test-scripts.
- Keep behavior deterministic, readable, and traceable to test-step intent.

## Script Shape
- Follow established local patterns in neighboring scripts before introducing new patterns.
- Inherit from MfdTestScript where applicable in this test family.
- Keep setup, action, and verification flow easy to follow in run().

## Step Traceability
- Map script actions to CSV test steps.
- Add step comments in this format at execution points:
  - # Step <id>: <exact CSV Step text>
- Include step number context in verification messages and relevant logs.

## Data Dictionary Safety
- Do not invent data IDs, enums, ranges, units, or timing.
- Resolve IDs and enums from DELTA dictionary XML sources.
- If unresolved, flag the gap and request clarification instead of guessing.

## Cross-Checks
- When behavior is ambiguous, check:
  - neighboring scripts in the same area/page,
  - DELTA dictionary XMLs in mfd-test-framework,
  - MFD source behavior in mfd/source and mfd/gls.
- Keep display-specific logic explicit for MFD_L, MFD_C, and MFD_R when relevant.
