# Test Script API Reference (MFD Test Script 101)

Use this quick reference when drafting or revising MFD delta test scripts.

## Purpose
- Provide common framework call patterns used in script authoring.
- Keep API examples close to the script validation workflow.

## Page Navigation APIs
Set a top page:

```python
self.set_top_page('SYSTEMS')
```

Set a bottom page without a subpage:

```python
self.set_bottom_page('PNEU')
```

Set a bottom page with a subpage:

```python
self.set_bottom_page('DIAG', 'HBEAT')
```

## Knob And Bezel Interaction APIs
Spin a knob:

```python
self.bezel_knob(right_outer_knob=CLOCKWISE)
self.sleep(0.3)
```

Press knob center:

```python
self.bezel_knob(center_right_press=1)
self.sleep(0.3)
```

Press a bezel button:

```python
self.bezel_button(BEZEL_B3)
```

Common bezel button constants:
- Top row: `BEZEL_T1`, `BEZEL_T2`, `BEZEL_T3`, `BEZEL_T4`
- Bottom row: `BEZEL_B1`, `BEZEL_B2`, `BEZEL_B3`, `BEZEL_B4`
- Left column: `BEZEL_L1` through `BEZEL_L6`
- Right column: `BEZEL_R1` through `BEZEL_R6`

## Nominal State Setup
For tests that start in nominal flight conditions, use the framework nominal-state call expected by this test family:

```python
self.testFramework.nominal_state_function(self.testFramework)
```

## MFD Page Layout Quick Reference
Canonical source:
- `.github/copilot-instructions.md` contains the root-level page layout context used for both test-case ideation and script authoring.
- Keep this quick reference synchronized with root context; if a mismatch appears, treat `.github/copilot-instructions.md` as authoritative.

Top pages:
- `PDF`
- `SYSTEMS`

Bottom pages and subpages:
- `NAV`: `MAP`, `NAV`, `SETUP`
- `COM`: `COM`, `XPDR`
- `PNEU`
- `ELEC`
- `ECS`: `PRESS`, `TEMP`
- `RKT`: `ALL`, `PRESS`, `VALVE`, `CTN`
- `FTHR`
- `CTRL`: `SURFC`, `RCS`, `FBW-CMD`, `STAB`, `RUDDER`, `ELEVON`
- `PLAN`: `FLT`, `W&B`, `ROUTE`, `INS`
- `DIAG`: `HIST`, `CAS`, `ADC`, `A&B`, `INS-A`, `INS-B`, `XPDR`, `DAU`, `MFD`, `HBEAT`, `ANALOG`, `DIO`, `BEZEL`, `RMC`, `BMS`, `FCC-ANA`, `FCC-DIO`, `FCC-FAULT`, `CTRLR`, `CTRLR-FAULT`, `STICK`, `FTHR`

## Safety Notes
- Do not invent API names, data IDs, enums, timing, or helper interfaces.
- For script style and structure conventions, apply `.github/instructions/mfd-delta-test-scripts-python.instructions.md` first.
- Use neighboring script references only when ambiguity remains after instruction-level rules are applied.
- Prefer plain in-line `self.log(...)` step logging in `run()`; do not treat `log_step` wrappers from legacy examples as the default pattern for new scripts.
- When uncertain, confirm against neighboring scripts and framework base classes.
