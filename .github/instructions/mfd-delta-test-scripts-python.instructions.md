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

## Readability And Style
- Prefer explicit in-line step logging in run(), for example self.log('Step 4: ...').
- Avoid one-line wrapper helpers that only pass through to an existing framework call (for example log_step()).
- Create helper methods only when they add clear behavior beyond pass-through logging, such as shared branching, validation, retry handling, or repeated multi-line actions.
- Do not create per-step temporary string variables when the text is used only once; log the step text directly.
- For nominal state setup, call self.testFramework.nominal_state_function(self.testFramework) directly in run() when that harness API is expected in this test family.
- Do not add defensive getattr or fallback wrappers around nominal_state_function unless the user explicitly asks for compatibility handling.
- Keep run() linear and traceable so reviewers can map each action and verify block to the corresponding test step without jumping between tiny helper methods.

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
