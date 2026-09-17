# Evidence Map For MFD Test Authoring

Use this map to locate supporting evidence quickly during CSV or script work.

## Repositories And Roles
- mfd/: source code for the MFD display behavior.
- mfd-test-framework/: test framework GUI, infrastructure, and support code.
- mfd-test-framework/scripts/delta-test-scripts/: nested repository where most MFD test-script authoring work is performed.

## Data Dictionary Sources
Primary for test-script authoring:
- mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA/
- mfd-test-framework/av_test_infrastructure/data_dictionary/DELTA_Data_Dictionary.xml

Cross-check source (can diverge):
- mfd/common/data_dictionary/DELTA/
- mfd/common/data_dictionary/DELTA_Data_Dictionary.xml

## Script Pattern Sources
- mfd-test-framework/scripts/delta-test-scripts/ (neighboring scripts in same area/page)
- .github/agents/MFD Agent Supporting Docs/ (reference scripts and reference CSV artifacts)

## Behavioral Truth Sources
When requirement wording and artifact behavior appear inconsistent:
1. Inspect relevant MFD source in mfd/source/ and mfd/gls/.
2. Compare with neighboring scripts in delta-test-scripts.
3. Reconcile with live Jira/TestRay data.

## Runtime Context
- MFD UI and mfd-test-framework run inside an Oracle VirtualBox VM.
- If VM-observed behavior conflicts with static artifacts, report the mismatch explicitly.

## Display Variants
- MFD_L
- MFD_C
- MFD_R

Keep display-specific differences explicit in both test-case and script reasoning.
