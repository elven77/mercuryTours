import time
import string

import baseTest
from pages.SignOnPages import SignOnPage


class SignOn(baseTest.BaseTest):
    def setUp(self):
        super(SignOn, self).setUp()

    def test_signon(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        signOnPage=SignOnPage(self.driver)
        #SignOnbPage=SignOnPage(self.driver)

        # Enter Sign On
        signOnPage.enterSignOn()

        # Input Username & Pwd
        signOnPage.inputSignInfo("aaa","aaa")

        # Submit
        signOnPage.submit()

        # Find Flight
        signOnPage.findFlight()

        # Save Flight
        signOnPage.saveFlight()

        # Fill personal info
        signOnPage.fillPersonalInfo("aaa","aaa","12345678")

        # Buy flight
        signOnPage.buyFlight()