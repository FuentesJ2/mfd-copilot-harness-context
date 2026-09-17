# MFD Harness Context Engineering Guide

## Purpose
This note defines where context should live so instructions stay stable, discoverable, and maintainable.

## Context Placement
- Root always-on context:
  - .github/copilot-instructions.md
  - Use for workspace topology, mission, source-of-truth precedence, and global safety rules.
- On-demand workflow logic:
  - .github/skills/mfd-test-authoring-validation/SKILL.md
  - Use for CSV and script validation procedures and output contracts.
- File-scoped coding conventions:
  - .github/instructions/mfd-delta-test-scripts-python.instructions.md
  - Use for Python script authoring conventions in delta-test-scripts only.
- Deep references and examples:
  - .github/agents/MFD Agent Supporting Docs/
  - Use for long examples, reference scripts, and supporting artifacts.

## CSV And Script Separation Rule
- CSV workflow validates Jira-exported test-step artifacts.
- Script workflow validates executable Python implementations.
- Keep checklist and review results separate, even when both are processed in one task.

## Source Of Truth Rule
- Jira/TestRay live data is current issue metadata source.
- Repository CSV files are workflow artifacts and style references.
- MFD source and VM-observed behavior are used to resolve ambiguous implementation intent.

## Maintenance
- Avoid duplicating long checklist logic in agent files and root instructions.
- Add details progressively to skill references rather than inflating always-on context.
