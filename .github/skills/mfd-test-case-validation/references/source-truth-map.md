# Source-Truth Map For Test-Case Step Work

Use this map for DRAFT and TEST CASE REVIEW work on Jira test-case steps.

## Ordered Evidence Sources
1. Live Jira/TestRay context:
   - Use `.github/skills/jira-context-cli/SKILL.md` for named issue keys.
   - Treat live issue metadata as current truth for status, links, comments, description, and authored steps.
2. In-scope test-step artifact under edit:
   - Jira-authored steps when available.
   - CSV artifact when one exists.
3. CSV structure and style authority:
   - `.github/skills/mfd-test-case-validation/SKILL.md` (Definitive Jira Test-Case Description And Step Format section)
   - `.github/instructions/mfd-test-step-annotation-overlay.instructions.md`
4. Requirement and parameter evidence:
   - Linked requirement text from live Jira context.
   - DELTA data dictionary only when requirement interpretation needs parameter-level confirmation.
5. MFD source behavior:
   - `mfd/source/`
   - `mfd/gls/`
6. Neighboring scripts:
   - `mfd-test-framework/scripts/delta-test-scripts/`
   - Use only when ambiguity remains after source inspection.

## Runtime Reality Rule
- MFD behavior is verified in the Oracle VirtualBox VM environment.
- If VM-observed behavior conflicts with static artifacts, report both and prioritize VM-observed behavior.

## Display Scope Rule
- Keep side-specific behavior explicit when relevant:
  - `MFD_L`
  - `MFD_C`
  - `MFD_R`
