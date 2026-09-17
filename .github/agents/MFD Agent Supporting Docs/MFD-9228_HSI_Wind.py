'''
WARNING: THIS DOCUMENT CONTAINS TRADE SECRET INFORMATION OF VIRGIN GALACTIC, LLC.
UNAUTHORIZED DISCLOSURE IS STRICTLY PROHIBITED AND MAY RESULT IN SERIOUS LEGAL CONSEQUENCES.
This source code is also protected under Copyright Laws.
'''
from scripts.mfd_test_script import *
import numpy as np

class MFD_9228_NAV_HSI_WIND_TEST_(MfdTestScript):

    ACTION_DELAY = 0.5
    KNOB_DELAY = 0.3
    VERIFY_SPACING = 0.4
    POST_INPUT_SETTLE_DELAY = 1.0
    VERIFY_DWELL_TIME = 0.8
    DATA_SET_RETRIES = 4
    DATA_VERIFY_DELAY = 0.4

    # Log a test step with a consistent Step <id> prefix.
    def log_step(self, step_id, step_text, header=None):
        self.log(f'Step {step_id}: {step_text}', header=header)

    # Return the next INS source in the T2 softkey cycle.
    def _next_ins_source(self, source_name):
        if source_name == 'AUTO_INS_L':
            return 'INS_L'
        if source_name == 'INS_L':
            return 'INS_R'
        return 'AUTO_INS_L'

    # Initialize the expected INS source from the active MFD config.
    def _initialize_ins_source(self):
        configured_mfd = getattr(self.testFramework, 'config_type', '')
        if configured_mfd in ('MFD_L', 'MFD_C'):
            return 'AUTO_INS_L'
        return 'INS_R'

    # Return the next ADC source in the T1 softkey cycle.
    def _next_adc_source(self, source_name):
        source_order = self._get_adc_source_order()
        if source_name not in source_order:
            return source_order[0]
        source_index = source_order.index(source_name)
        return source_order[(source_index + 1) % len(source_order)]

    # Provide the ADC source cycle order for the current MFD config.
    def _get_adc_source_order(self):
        configured_mfd = getattr(self.testFramework, 'config_type', '')
        if configured_mfd in ('MFD_L', 'MFD_C'):
            # T1 cycle: ADC AUTO L -> ADC L -> ADC R -> ADC ESIS
            return ['AUTO_ADC_L', 'ADC_L', 'ADC_R', 'ADC_ESIS']
        # T1 cycle for MFD_R: ADC R -> ADC ESIS -> ADC AUTO L -> ADC L
        return ['ADC_R', 'ADC_ESIS', 'AUTO_ADC_L', 'ADC_L']

    # Initialize the expected ADC source from the active MFD config.
    def _initialize_adc_source(self):
        return self._get_adc_source_order()[0]

    # Press T2 as needed until the requested INS source is selected.
    def _set_ins_source(self, target_source, step_id):
        if self.current_ins_source == target_source:
            self.log(f'Step {step_id}: INS source already set to {target_source}.')
            return

        safety_counter = 0
        while self.current_ins_source != target_source and safety_counter < 4:
            self.bezel_button(BEZEL_T2)
            self.sleep(self.KNOB_DELAY)
            self.current_ins_source = self._next_ins_source(self.current_ins_source)
            safety_counter += 1

        self.log(f'Step {step_id}: INS source set to {self.current_ins_source}.')

    # Press T1 as needed until the requested ADC source is selected.
    def _set_adc_source(self, target_source, step_id):
        if self.current_adc_source == target_source:
            self.log(f'Step {step_id}: ADC source already set to {target_source}.')
            return

        safety_counter = 0
        max_presses = len(self._get_adc_source_order()) + 1
        while self.current_adc_source != target_source and safety_counter < max_presses:
            self.bezel_button(BEZEL_T1)
            self.sleep(self.KNOB_DELAY)
            self.current_adc_source = self._next_adc_source(self.current_adc_source)
            safety_counter += 1

        self.log(f'Step {step_id}: ADC source set to {self.current_adc_source}.')

    # Select INS and ADC sources for a step based on current MFD context.
    def _set_sources_for_step(self, step_id, target_ins, target_adc):
        configured_mfd = getattr(self.testFramework, 'config_type', '')
        self.log(
            f'Step {step_id}: Booted into {configured_mfd}; selecting INS={target_ins} with T2 and ADC={target_adc} with T1.'
        )
        self._set_ins_source(target_ins, step_id)
        self._set_adc_source(target_adc, step_id)

    # Set true airspeed using the CC_A ADC data ID for the selected side.
    def _set_adc_true_airspeed(self, side_prefix, airspeed_value, step_id):
        adc_true_airspeed_id = {
            'L': 'CC_A_L_ADC_TRUE_AIRSPEED',
            'R': 'CC_A_R_ADC_TRUE_AIRSPEED',
        }.get(side_prefix)

        if adc_true_airspeed_id is None:
            self.log(f'Step {step_id}: Unsupported ADC side prefix {side_prefix}.')
            return False

        return self._set_data_id_with_verify(adc_true_airspeed_id, airspeed_value, step_id)

    # Safely read a data ID value from the test framework.
    def _read_data_id(self, data_id):
        try:
            return self.testFramework.get_data_dictionary_value(data_id)
        except Exception:
            return None

    # Set a data ID and verify that the value is latched, with limited retries.
    def _set_data_id_with_verify(self, data_id, value, step_id):
        for attempt in range(1, self.DATA_SET_RETRIES + 1):
            self.set_data_id(data_id, value)
            self.sleep(self.DATA_VERIFY_DELAY)
            readback = self._read_data_id(data_id)

            if readback == value:
                self.log(f'Step {step_id}: Set {data_id}={value} (readback OK on attempt {attempt}).')
                return True

            self.log(
                f'Step {step_id}: {data_id} readback mismatch on attempt {attempt} '
                f'(expected {value}, got {readback}). Retrying.'
            )

        self.log(f'Step {step_id}: WARNING - could not verify {data_id}={value} after retries.')
        return False

    # Toggle MAG/TRUE softkey state only when a change is required.
    def _set_mag_var(self, target_mag_var):
        if self.current_mag_var != target_mag_var:
            self.bezel_button(BEZEL_R4)
            self.sleep(self.KNOB_DELAY)
            self.current_mag_var = target_mag_var

    # Toggle ORIENT softkey state only when a change is required.
    def _set_orient(self, target_orient):
        if self.current_orient != target_orient:
            self.bezel_button(BEZEL_R5)
            self.sleep(self.KNOB_DELAY)
            self.current_orient = target_orient

    # Build a mask that limits image comparisons to the lower half of a template.
    def _build_bottom_half_mask(self, image_template):
        template_image = self.imageRecognition.load_image(image_template)
        if template_image is None:
            return None

        mask = np.zeros_like(template_image, dtype=np.uint8)
        height = template_image.shape[0]
        mask[height // 2 :, :] = 255
        return mask

    # Verify wind presentation using golden image comparison only.
    def _verify_wind(self, step_id, wind_direction, wind_speed, arrow_direction, image_template):
        full_template = f'NAV/{image_template}'
        bottom_half_mask = self._build_bottom_half_mask(full_template)

        verify_msg = f'Step {step_id}: DMFDREQ-1011/1012/1013 wind display matches expected values'
        if arrow_direction is None:
            verify_msg += '\n\tWIND CALM'
        else:
            verify_msg += f'\n\tWind direction: {wind_direction}'
            verify_msg += f'\n\tWind speed: {wind_speed}'
            verify_msg += f'\n\tArrow pointing: {arrow_direction}'
        verify_msg += f'\n\tGolden image used: YES ({full_template})'
        verify_msg += '\n\tOCR used: NO'

        self.verify(
            verify_msg,
            diff_allowed=2,
            dwell_time=self.VERIFY_DWELL_TIME,
            image_template=full_template,
            mask=bottom_half_mask,
        )

        self.sleep(self.VERIFY_SPACING)

    # Execute each wind test step for a given source side (L or R).
    def _run_wind_steps_for_side(self, step_definitions, prefix):
        for step in step_definitions:
            # Step <id>: <exact step text from CSV>
            self.log_step(step['id'], step['step_text'])

            target_ins = 'INS_L' if prefix == 'L' else 'INS_R'
            target_adc = 'ADC_L' if prefix == 'L' else 'ADC_R'
            self._set_sources_for_step(step['id'], target_ins, target_adc)

            if step['id'] in (13, '15.13'):
                self.log(f"Step {step['id']}: Source re-check before low-speed edge case.")

            self.set_bottom_page('NAV', 'SETUP')
            self.sleep(self.ACTION_DELAY)

            self._set_adc_true_airspeed(prefix, step['adc_true_airspeed'], step['id'])
            self.set_data_id(f'{prefix}_INS_PVA_AZIMUTH', step['ins_azimuth'])
            self.set_data_id(f'{prefix}_INS_PVA_EAST_VELOCITY', step['ins_east_velocity'])
            self.set_data_id(f'{prefix}_INS_PVA_NORTH_VELOCITY', step['ins_north_velocity'])
            self.sleep(self.ACTION_DELAY)

            # Hardware bench safeguard: enforce true airspeed again if drifted.
            adc_data_id = 'CC_A_L_ADC_TRUE_AIRSPEED' if prefix == 'L' else 'CC_A_R_ADC_TRUE_AIRSPEED'
            current_airspeed = self._read_data_id(adc_data_id)
            if current_airspeed != step['adc_true_airspeed']:
                self.log(
                    f"Step {step['id']}: {adc_data_id} drift detected before verify "
                    f"(expected {step['adc_true_airspeed']}, got {current_airspeed}). Re-applying."
                )
                self._set_adc_true_airspeed(prefix, step['adc_true_airspeed'], step['id'])

            self._set_mag_var(step['mag_var'])
            self._set_orient(step['orient'])
            self.sleep(self.POST_INPUT_SETTLE_DELAY)

            # Workaround used in existing NAV scripts due to MFD-9219.
            self.set_bottom_page('NAV', 'MAP')
            self.sleep(self.ACTION_DELAY)

            # Verify on NAV/NAV only to reduce transition drift and false positives.
            self.set_bottom_page('NAV', 'NAV')
            self.sleep(self.ACTION_DELAY)
            self._verify_wind(
                step_id=step['id'],
                wind_direction=step['wind_direction'],
                wind_speed=step['wind_speed'],
                arrow_direction=step['arrow_direction'],
                image_template=step['image_template'],
            )

    def run(self):
        self.log('Running MFD-9228 NAV HSI Wind Test')
        self.current_ins_source = self._initialize_ins_source()
        self.current_adc_source = self._initialize_adc_source()

        # Step 1: Start test from nominal flight conditions
        self.log_step(1, 'Start test from nominal flight conditions')
        self.testFramework.nominal_state_function(self.testFramework)

        # Step 2: Set source to INS L using T2 softkey (as needed until INS L is selected).
        #         Set source to ADC L using T1 softkey (as needed until ADC L is selected).
        self.log_step(2, 'Set source to INS L using T2 softkey (as needed until INS L is selected).\nSet source to ADC L using T1 softkey (as needed until ADC L is selected).')
        self._set_sources_for_step(2, 'INS_L', 'ADC_L')

        # Step 3: Navigate MFD to NAV NAV
        self.log_step(3, 'Navigate MFD to NAV NAV')
        self.set_bottom_page('NAV', 'NAV')
        self.sleep(1.0)

        # Step 4: Set DCLTR TO "HSI" using L6 softkey
        self.log_step(4, 'Set DCLTR TO "HSI" using L6 softkey')
        for _ in range(4):
            self.bezel_button(BEZEL_L6)
            self.sleep(self.KNOB_DELAY)

        # Step 5: Navigate MFD to NAV SETUP
        self.log_step(5, 'Navigate MFD to NAV SETUP')
        self.set_bottom_page('NAV', 'SETUP')
        self.sleep(self.ACTION_DELAY)

        self.current_mag_var = 'MAG'
        self.current_orient = 'TRK UP'

        left_side_steps = [
            # Step 6: Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=0 m/s; MAG VAR -> MAG; ORIENT -> HDG UP
            {
                'id': 6,
                'step_text': 'Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=0 m/s; MAG VAR -> MAG; ORIENT -> HDG UP',
                'adc_true_airspeed': 100,
                'ins_azimuth': 9,
                'ins_east_velocity': 0,
                'ins_north_velocity': 0,
                'mag_var': 'MAG',
                'orient': 'HDG UP',
                'wind_direction': '001',
                'wind_speed': '100',
                'arrow_direction': 'Down',
                'image_template': 'Wind_001_100.png',
            },
            # Step 7: Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=0 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP
            {
                'id': 7,
                'step_text': 'Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=0 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP',
                'adc_true_airspeed': 100,
                'ins_azimuth': 9,
                'ins_east_velocity': 0,
                'ins_north_velocity': 0,
                'mag_var': 'TRUE',
                'orient': 'HDG UP',
                'wind_direction': 'T009',
                'wind_speed': '100',
                'arrow_direction': 'Down',
                'image_template': 'Wind_T009_100.png',
            },
            # Step 8: Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=50.8 m/s; MAG VAR -> TRUE; ORIENT -> TRK UP
            {
                'id': 8,
                'step_text': 'Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=50.8 m/s; MAG VAR -> TRUE; ORIENT -> TRK UP',
                'adc_true_airspeed': 100,
                'ins_azimuth': 9,
                'ins_east_velocity': 0,
                'ins_north_velocity': 50.8,
                'mag_var': 'TRUE',
                'orient': 'TRK UP',
                'wind_direction': 'T090',
                'wind_speed': '016',
                'arrow_direction': 'Left',
                'image_template': 'Wind_T090_16.png',
            },
            # Step 9: Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=50.8 m/s; MAG VAR -> MAG; ORIENT -> TRK UP
            {
                'id': 9,
                'step_text': 'Set the following: L_ADC_TRUE_AIRSPEED=100 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=50.8 m/s; MAG VAR -> MAG; ORIENT -> TRK UP',
                'adc_true_airspeed': 100,
                'ins_azimuth': 9,
                'ins_east_velocity': 0,
                'ins_north_velocity': 50.8,
                'mag_var': 'MAG',
                'orient': 'TRK UP',
                'wind_direction': '082',
                'wind_speed': '016',
                'arrow_direction': 'Left',
                'image_template': 'Wind_T082_16.png',
            },
            # Step 10: Set the following: L_ADC_TRUE_AIRSPEED=200 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=70 m/s; L_INS_PVA_NORTH_VELOCITY=70 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP
            {
                'id': 10,
                'step_text': 'Set the following: L_ADC_TRUE_AIRSPEED=200 kts; L_INS_PVA_AZIMUTH=9 degrees; L_INS_PVA_EAST_VELOCITY=70 m/s; L_INS_PVA_NORTH_VELOCITY=70 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP',
                'adc_true_airspeed': 200,
                'ins_azimuth': 9,
                'ins_east_velocity': 70,
                'ins_north_velocity': 70,
                'mag_var': 'TRUE',
                'orient': 'HDG UP',
                'wind_direction': 'T300',
                'wind_speed': '121',
                'arrow_direction': 'Lower Right',
                'image_template': 'Wind_T300_121.png',
            },
            # Step 11: Set the following: L_ADC_TRUE_AIRSPEED=200 kts; L_INS_PVA_AZIMUTH=90 degrees; L_INS_PVA_EAST_VELOCITY=140 m/s; L_INS_PVA_NORTH_VELOCITY=100 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP
            {
                'id': 11,
                'step_text': 'Set the following: L_ADC_TRUE_AIRSPEED=200 kts; L_INS_PVA_AZIMUTH=90 degrees; L_INS_PVA_EAST_VELOCITY=140 m/s; L_INS_PVA_NORTH_VELOCITY=100 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP',
                'adc_true_airspeed': 200,
                'ins_azimuth': 90,
                'ins_east_velocity': 140,
                'ins_north_velocity': 100,
                'mag_var': 'TRUE',
                'orient': 'HDG UP',
                'wind_direction': 'T200',
                'wind_speed': '207',
                'arrow_direction': 'Upper Left',
                'image_template': 'Wind_T200_207.png',
            },
            # Step 12: Set the following: L_ADC_TRUE_AIRSPEED=0 kts; L_INS_PVA_AZIMUTH=90 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=0 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP
            {
                'id': 12,
                'step_text': 'Set the following: L_ADC_TRUE_AIRSPEED=0 kts; L_INS_PVA_AZIMUTH=90 degrees; L_INS_PVA_EAST_VELOCITY=0 m/s; L_INS_PVA_NORTH_VELOCITY=0 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP',
                'adc_true_airspeed': 0,
                'ins_azimuth': 90,
                'ins_east_velocity': 0,
                'ins_north_velocity': 0,
                'mag_var': 'TRUE',
                'orient': 'HDG UP',
                'wind_direction': '0',
                'wind_speed': '0',
                'arrow_direction': None,
                'image_template': 'WIND_CALM.png',
            },
            # Step 13: Set the following for non-zero wind speed less than 5 knots: L_ADC_TRUE_AIRSPEED=4 kts; L_INS_PVA_AZIMUTH=0 degrees; L_INS_PVA_EAST_VELOCITY=1 m/s; L_INS_PVA_NORTH_VELOCITY=1 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP
            {
                'id': 13,
                'step_text': 'Set the following for non-zero wind speed less than 5 knots: L_ADC_TRUE_AIRSPEED=4 kts; L_INS_PVA_AZIMUTH=0 degrees; L_INS_PVA_EAST_VELOCITY=1 m/s; L_INS_PVA_NORTH_VELOCITY=1 m/s; MAG VAR -> TRUE; ORIENT -> HDG UP',
                'adc_true_airspeed': 4,
                'ins_azimuth': 0,
                'ins_east_velocity': 1,
                'ins_north_velocity': 1,
                'mag_var': 'TRUE',
                'orient': 'HDG UP',
                'wind_direction': '0',
                'wind_speed': '0',
                'arrow_direction': None,
                'image_template': 'WIND_CALM.png',
            },
        ]
        self._run_wind_steps_for_side(left_side_steps, 'L')

        # Step 14: Set to INS R using T2 softkey (as needed until INS R is selected).
        #          Set to ADC R using T1 softkey (as needed until ADC R is selected).
        self.log_step(14, 'Set to INS R using T2 softkey (as needed until INS R is selected).\nSet to ADC R using T1 softkey (as needed until ADC R is selected).')
        self._set_sources_for_step(14, 'INS_R', 'ADC_R')

        # Step 15: Repeat Steps 6-13. For all variable names in those steps, replace the L_ prefix with R_.
        self.log_step(15, 'Repeat Steps 6-13 with R_ prefixed variables.')
        right_side_steps = []
        for step in left_side_steps:
            repeated_step = dict(step)
            repeated_step['id'] = f"15.{step['id']}"
            repeated_step['step_text'] = f"Repeat of Step {step['id']} using R_ variable prefixes"
            right_side_steps.append(repeated_step)

        self._run_wind_steps_for_side(right_side_steps, 'R')

        # Restore script defaults for subsequent tests.
        self.set_bottom_page('NAV', 'SETUP')
        self.sleep(self.ACTION_DELAY)
        self._set_mag_var('MAG')
        self._set_orient('TRK UP')
        self.set_bottom_page('NAV', 'NAV')
        self.bezel_button(BEZEL_L6)
        self.sleep(self.KNOB_DELAY)
