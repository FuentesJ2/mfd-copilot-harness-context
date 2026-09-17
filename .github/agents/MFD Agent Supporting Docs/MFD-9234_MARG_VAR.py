"""

WARNING: THIS DOCUMENT CONTAINS TRADE SECRET INFORMATION OF VIRGIN GALACTIC, LLC.

UNAUTHORIZED DISCLOSURE IS STRICTLY PROHIBITED AND MAY RESULT IN SERIOUS LEGAL CONSEQUENCES.

This source code is also protected under Copyright Laws.

"""



from scripts.mfd_test_script import *





class MFD_9234_NAV_SETUP_MAG_VAR_TEST_(MfdTestScript):



    def run(self):

        self.log("Running MFD-9234 NAV SETUP MAG VAR Test")

        # Step 1: Start test from nominal flight conditions
        # Note: This script assumes nominal flight conditions are already established by test setup.
        self.log("Step 1: Start test from nominal flight conditions (precondition)")

        # Navigate to the NAV MAP page twice due to bug MFD-9219

        # Step 2: Set the MFD to display the NAV MAP page.
        self.set_bottom_page("NAV", "MAP")
        self.sleep(1)
        self.log(
            "Step 2: Verify MAG VAR soft key (R4) is NOT displayed on NAV MAP page "
            "using golden image NAV/MAP/MAG_VAR_Not_Displayed.png"
        )
        self.set_bottom_page("NAV", "MAP")
        self.sleep(0.5)
        self.verify(
            "Step 2: the MAG VAR soft key (R4) is NOT displayed on the NAV MAP page "
            "(golden image: NAV/MAP/MAG_VAR_Not_Displayed.png)",
            image_template="NAV/MAP/MAG_VAR_Not_Displayed.png",
        )

        # Step 3: Set the MFD to display the NAV NAV page.
        self.log(
            "Step 3: Verify MAG VAR soft key (R4) is NOT displayed on NAV NAV page "
            "using golden image NAV/NAV/MAG_VAR_Not_Displayed.png"
        )
        self.set_bottom_page("NAV", "NAV")
        self.sleep(0.5)
        self.verify(
            "Step 3: the MAG VAR soft key (R4) is NOT displayed on the NAV NAV page "
            "(golden image: NAV/NAV/MAG_VAR_Not_Displayed.png)",
            image_template="NAV/NAV/MAG_VAR_Not_Displayed.png",
        )

        # Step 4: Set the MFD to display the NAV SETUP page.
        self.set_bottom_page("NAV", "SETUP")
        self.sleep(0.5)
        # DMFDREQ-925
        self.log(
            "Step 4: Verify MAG VAR soft key (R4) is displayed on NAV SETUP page "
            "using golden image NAV/SETUP/MAG_VAR_MAG.png"
        )
        self.verify(
            "Step 4: the MAG VAR soft key (R4) is displayed "
            "(golden image: NAV/SETUP/MAG_VAR_MAG.png)",
            image_template="NAV/SETUP/MAG_VAR_MAG.png"
        )

        # Step 5: N/A
        # DMFDREQ-925
        self.log(
            "Step 5: Verify MAG is displayed under MAG VAR label "
            "using golden image NAV/SETUP/MAG_VAR_MAG.png"
        )
        self.verify(
            'Step 5: "MAG" is displayed under the "MAG VAR" label '
            '(golden image: NAV/SETUP/MAG_VAR_MAG.png)',
            image_template="NAV/SETUP/MAG_VAR_MAG.png"
        )

        # Step 6: Press the MAG VAR soft key (R4).
        self.log("Step 6: Press the MAG VAR soft key (R4)")
        self.bezel_button(BEZEL_R4)
        # DMFDREQ-1521
        self.log(
            "Step 6: Verify TRUE is displayed under MAG VAR label "
            "using golden image NAV/SETUP/MAG_VAR_TRUE.png"
        )
        self.verify(
            'Step 6: "TRUE" is displayed under the "MAG VAR" label '
            '(golden image: NAV/SETUP/MAG_VAR_TRUE.png)',
            image_template="NAV/SETUP/MAG_VAR_TRUE.png"
        )

        # Step 7: Set the MFD to display the NAV NAV page.
        self.log(
            "Step 7: Verify MAG VAR soft key (R4) is NOT displayed on NAV NAV page "
            "using golden image NAV/NAV/MAG_VAR_Not_Displayed.png"
        )
        self.set_bottom_page("NAV", "NAV")
        self.sleep(0.5)
        self.verify(
            "Step 7: the MAG VAR soft key (R4) is NOT displayed "
            "(golden image: NAV/NAV/MAG_VAR_Not_Displayed.png)",
            image_template="NAV/NAV/MAG_VAR_Not_Displayed.png"
        )

        # Step 8: Set the MFD to display the NAV SETUP page.
        self.log("Step 8: Set the MFD to display the NAV SETUP page")
        self.set_bottom_page("NAV", "SETUP")
        # DMFDREQ-925
        self.log(
            "Step 8: Verify MAG VAR soft key (R4) is displayed "
            "using golden image NAV/SETUP/MAG_VAR_TRUE.png"
        )
        self.verify(
            "Step 8: the MAG VAR soft key (R4) is displayed "
            "(golden image: NAV/SETUP/MAG_VAR_TRUE.png)",
            image_template="NAV/SETUP/MAG_VAR_TRUE.png"
        )

        # Step 9: Press the MAG VAR soft key (R4).
        self.log("Step 9: Press the MAG VAR soft key (R4)")
        self.bezel_button(BEZEL_R4)
        self.sleep(0.5)
        # DMFDREQ-1521
        self.log(
            "Step 9: Verify MAG is displayed under MAG VAR label "
            "using golden image NAV/SETUP/MAG_VAR_MAG.png"
        )
        self.verify(
            'Step 9: "MAG" is displayed under the "MAG VAR" label '
            '(golden image: NAV/SETUP/MAG_VAR_MAG.png)',
            image_template="NAV/SETUP/MAG_VAR_MAG.png"
        )

        # Step 10: Press the MAG VAR soft key (R4).
        self.log("Step 10: Press the MAG VAR soft key (R4)")
        self.bezel_button(BEZEL_R4)
        self.sleep(0.5)
        # DMFDREQ-1521
        self.log(
            "Step 10: Verify TRUE is displayed under MAG VAR label "
            "using golden image NAV/SETUP/MAG_VAR_TRUE.png"
        )
        self.verify(
            'Step 10: "TRUE" is displayed under the "MAG VAR" label '
            '(golden image: NAV/SETUP/MAG_VAR_TRUE.png)',
            image_template="NAV/SETUP/MAG_VAR_TRUE.png"
        )

        # Step 11: Press the MAG VAR soft key (R4).
        self.log("Step 11: Press the MAG VAR soft key (R4)")
        self.bezel_button(BEZEL_R4)
        self.sleep(0.5)
        # DMFDREQ-1521
        self.log(
            "Step 11: Verify MAG is displayed under MAG VAR label "
            "using golden image NAV/SETUP/MAG_VAR_MAG.png"
        )
        self.verify(
            'Step 11: "MAG" is displayed under the "MAG VAR" label '
            '(golden image: NAV/SETUP/MAG_VAR_MAG.png)',
            image_template="NAV/SETUP/MAG_VAR_MAG.png"
        )
