'''
WARNING: THIS DOCUMENT CONTAINS TRADE SECRET INFORMATION OF VIRGIN GALACTIC, LLC.
UNAUTHORIZED DISCLOSURE IS STRICTLY PROHIBITED AND MAY RESULT IN SERIOUS LEGAL CONSEQUENCES.
This source code is also protected under Copyright Laws.
'''

from scripts.mfd_test_script import *


class MFD_9226_NAV_HSI_MODE_TEST_(MfdTestScript):

    def log_step(self, step_id, step_text, header=None):
        self.log(f'Step {step_id}: {step_text}', header=header)

    def verify_with_golden(self, step_id, verify_text, golden_image, diff_allowed=10):
        self.log(f'Step {step_id}: Verification uses golden image: {golden_image}')
        self.verify(
            f'Step {step_id}: {verify_text}',
            image_template=golden_image,
            diff_allowed=diff_allowed
        )

    def verify_with_ocr(self, step_id, verify_text, expected_value, image_template,
                        text_mask=None, custom_whitelist=None):
        self.log(f'Step {step_id}: Verification uses OCR with template: {image_template}')
        self.verify(
            f'Step {step_id}: {verify_text}',
            expected_value=expected_value,
            image_template=image_template,
            text_mask=text_mask,
            custom_whitelist=custom_whitelist
        )

    def run(self):

        self.log('Running MFD-9226 NAV HSI Mode Test')

        # Step 1: Start test from nominal flight conditions
        self.log_step(1, 'Start test from nominal flight conditions')
        self.testFramework.nominal_state_function(self.testFramework)
        
        # Step 2: *Subtest 1: Compass Ring ARC Test*
        self.log_step(2, 'Subtest 1: Compass Ring ARC Test', header=1)

        # Step 3: Navigate to the NAV MAP page.
        self.set_bottom_page('NAV', 'MAP')
        arc_map_msg = 'the compass ARC displays:'
        arc_map_msg += '\n\tAn Icon of the SS2 at the center of the ARC, with'
        arc_map_msg += '\n\t210 degrees with 105 degrees to each side of center,'
        arc_map_msg += '\n\tLabeled marking every 30 degrees,'
        arc_map_msg += '\n\tLarge ticks every 10 degrees within the markings, and'
        arc_map_msg += '\n\tSmall ticks every 5 degrees with the other markings.'
        self.verify_with_golden(3, arc_map_msg, 'NAV/MAP/HSI_Compass_Arc.png')

        # Step 4: Navigate to the NAV NAV page.
        self.set_bottom_page('NAV', 'NAV')
        arc_nav_setup_msg = 'the compass ARC displays:'
        arc_nav_setup_msg += '\n\tAn Icon of the SS2 at the center of the ARC, with'
        arc_nav_setup_msg += '\n\t120 degrees with 60 degrees to each side of center,'
        arc_nav_setup_msg += '\n\tLabeled marking every 30 degrees,'
        arc_nav_setup_msg += '\n\tLarge ticks every 10 degrees within the markings, and'
        arc_nav_setup_msg += '\n\tSmall ticks every 5 degrees with the other markings.'
        self.verify_with_golden(4, arc_nav_setup_msg, 'NAV/NAV/HSI_Compass_Arc.png')

        # Step 5: Navigate to the NAV SETUP page.
        self.set_bottom_page('NAV', 'SETUP')
        self.verify_with_golden(5, arc_nav_setup_msg, 'NAV/SETUP/HSI_Compass_Arc.png')

        # Step 6: *Subtest 2: HSI Mode Test*
        self.log_step(6, 'Subtest 2: HSI Mode Test', header=1)

        # Step 7: Navigate MFD to NAV NAV page
        self.set_bottom_page('NAV', 'NAV')
        self.verify_with_ocr(
            7,
            'The HSI mode displayed is "ARC"',
            'ARC',
            'NAV/NAV/HSI_Mode_ARC.png'
        )

        # Step 8: Press the HSI Mode soft key
        self.log_step(8, 'Press the HSI Mode soft key')
        self.bezel_button(BEZEL_L5)
        self.sleep(0.3)
        self.verify_with_ocr(
            8,
            'The HSI mode displayed changed from "ARC" to "CNT".',
            'CNT',
            'NAV/NAV/HSI_Mode_CNT.png'
        )

        # Step 9: Return to last subpage
        self.set_bottom_page('NAV', 'SETUP')
        self.log_step(9, 'Return to last subpage')

        # Step 10: *Subtest 3: Compass Ring CTN Test*
        self.log_step(10, 'Subtest 3: Compass Ring CTN Test', header=1)

        circle_msg = 'verify that display of the compass circle is/has:'
        circle_msg += '\n\tA complete circle, with'
        circle_msg += '\n\tAn icon of the SS2 at the center of the circle'
        circle_msg += '\n\tLabeled marking every 30 degrees using only the first 2 digits of the heading value,'
        circle_msg += '\n\tLarge ticks every 10 degrees within those markings, and'
        circle_msg += '\n\tSmall ticks every 5 degrees within the other markings.'

        # Step 11: Navigate to NAV SETUP
        self.set_bottom_page('NAV', 'SETUP')
        self.verify_with_golden(11, circle_msg, 'NAV/MAP/HSI_Compass_CNT.png')

        # Step 12: Navigate to NAV NAV
        self.set_bottom_page('NAV', 'NAV')
        self.verify_with_golden(12, circle_msg, 'NAV/NAV/HSI_Compass_CNT.png')

        # Step 13: Navigate to NAV MAP
        self.set_bottom_page('NAV', 'MAP')
        self.verify_with_golden(13, circle_msg, 'NAV/MAP/HSI_Compass_CNT.png')

        # Step 14: Navigate to NAV NAV page and then press the HSI Mode soft key on the NAV NAV page
        self.set_bottom_page('NAV', 'NAV')
        self.bezel_button(BEZEL_L5)
        self.sleep(0.3)
        self.verify_with_ocr(
            14,
            'The HSI mode displayed changed from "CNT" to "ARC".',
            'ARC',
            'NAV/NAV/HSI_Mode_ARC.png'
        )

        # Step 15: Repeat steps 9-10 for the NAV NAV and NAV SETUP page.
        self.log_step(
            15,
            'Repeat ARC compass-ring verification checks for NAV NAV and NAV SETUP pages'
        )
        self.set_bottom_page('NAV', 'NAV')
        self.verify_with_golden(15, arc_nav_setup_msg, 'NAV/NAV/HSI_Compass_Arc.png')
        self.set_bottom_page('NAV', 'SETUP')
        self.verify_with_golden(15, arc_nav_setup_msg, 'NAV/SETUP/HSI_Compass_Arc.png')
