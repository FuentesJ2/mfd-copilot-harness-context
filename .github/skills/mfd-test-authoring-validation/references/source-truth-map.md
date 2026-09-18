# Source-Truth Map For MFD Test Authoring

Use this map to determine where to pull reliable context for each authoring decision.

## Why This Exists
- This file defines what to inspect first and when.
- It makes evidence lookup explicit so the skill is not dependent on implicit memory.

## Ordered Evidence Sources
1. Live Jira/TestRay context:
   - Use `.github/skills/jira-context-cli/SKILL.md` for named issue keys.
   - Treat live issue metadata as current source of truth for status, links, comments, and authored steps.
2. In-scope artifact under edit:
   - CSV artifact for test-step wording and expected-result mapping.
   - Python script artifact for current behavior and implementation details.
3. DELTA data dictionary:
   - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA/`
   - `mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA_Data_Dictionary.xml`
4. MFD source behavior:
   - `mfd/source/`
   - `mfd/gls/`
5. Neighboring script patterns:
   - `mfd-test-framework/scripts/delta-test-scripts/`
6. Supporting references:
   - `.github/agents/MFD Agent Supporting Docs/`

## Repository Roles
- `mfd/`: MFD product behavior source.
- `mfd-test-framework/`: test framework interfaces and infrastructure.
- `mfd-test-framework/scripts/delta-test-scripts/`: executable test-script authoring area.

## Runtime Reality Rule
- MFD UI and framework run in Oracle VirtualBox VM.
- If VM-observed behavior conflicts with static artifacts, report mismatch and prioritize VM-observed behavior.

## Display Scope
- Keep side-specific behavior explicit when relevant:
  - `MFD_L`
  - `MFD_C`
  - `MFD_R`
