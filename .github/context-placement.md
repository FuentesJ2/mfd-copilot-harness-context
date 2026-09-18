# MFD Harness Context Placement Policy

Use this policy to keep MFD context concise, discoverable, and phase-oriented.

## Purpose
- Keep always-on context short and stable.
- Keep phase workflows in phase-specific skills.
- Keep file-type conventions in scoped instruction files.
- Keep supporting examples separate from normative policy.

## Placement Map
- Root always-on context:
  - `.github/copilot-instructions.md`
  - Store workspace topology, mission, workflow phase boundaries, precedence rules, and safety guardrails.
- Orchestrator behavior:
  - `.github/agents/MFD Test Script Agent.agent.md`
  - Keep orchestration thin; do not duplicate long checklists.
- Test-case phase workflow (DRAFT, TEST CASE REVIEW):
  - `.github/skills/mfd-test-case-validation/SKILL.md`
- Test-script phase workflow (TEST SCRIPT DRAFT, TEST SCRIPT REVIEW):
  - `.github/skills/mfd-test-script-validation/SKILL.md`
- File-scoped conventions:
  - `.github/instructions/mfd-test-step-annotation-overlay.instructions.md`
  - `.github/instructions/mfd-delta-test-scripts-python.instructions.md`
- Supporting examples and artifacts:
  - `.github/agents/MFD Agent Supporting Docs/`
  - Treat as examples only, not normative policy.

## Source-Of-Truth And Ambiguity Order
1. Live Jira/TestRay context for named issues.
2. In-scope artifact under edit.
3. DELTA data dictionary evidence.
4. MFD source behavior when intent is ambiguous.
5. Neighboring scripts only when ambiguity remains after source inspection.

## Script Style Precedence
- Primary authority: `.github/instructions/mfd-delta-test-scripts-python.instructions.md`.
- Secondary authority: neighboring scripts only for unresolved ambiguity.
- If an older example conflicts with instruction-level rules, instruction-level rules win.

## CSV Overlay Policy For This Workspace
- The step-annotation overlay is active by default for matching test-step CSV artifacts.
- To switch label style, edit or replace only `.github/instructions/mfd-test-step-annotation-overlay.instructions.md` while keeping the same path.

## Maintenance Rules
- Avoid duplicating policy across root, agent, and skills.
- When workflow policy changes, update root and agent glue plus the affected phase skill in one change set.
