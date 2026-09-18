# Source-Truth Map For Test-Script Work

Use this map for TEST SCRIPT DRAFT and TEST SCRIPT REVIEW work.

## Ordered Evidence Sources
1. Live Jira/TestRay context:
   - Use `.github/skills/jira-context-cli/SKILL.md` for named issue keys.
   - Treat live issue metadata as current truth for status, links, comments, and authored steps.
2. In-scope artifact under edit:
   - Python script artifact for current implementation behavior.
   - Source step intent from Jira-authored steps or CSV artifact.
3. Script convention authority:
   - Apply `.github/instructions/mfd-delta-test-scripts-python.instructions.md` first.
4. DELTA data dictionary:
   - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA/`
   - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA_Data_Dictionary.xml`
5. MFD source behavior:
   - `mfd/source/`
   - `mfd/gls/`
6. Neighboring script patterns:
   - `mfd-test-framework/scripts/delta-test-scripts/`
   - Use only when ambiguity remains after source inspection and instruction-level checks.

## Runtime Reality Rule
- MFD behavior is verified in the Oracle VirtualBox VM environment.
- If VM-observed behavior conflicts with static artifacts, report mismatch and prioritize VM-observed behavior.

## Display Scope Rule
- Keep side-specific behavior explicit when relevant:
  - `MFD_L`
  - `MFD_C`
  - `MFD_R`
