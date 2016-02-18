import time
import basePages
from locators.locators import SignOn


class SignOnPage(basePages.BasePage):
    def enterSignOn(self):
        elemEnterSignon=self.driver.find_element(*SignOn.elemSignOn)
        self.mouse_click(elemEnterSignon)

    def inputSignInfo(self,username,pwd):
        elemUserName=self.driver.find_element(*SignOn.elemUserName)
        elemPwd=self.driver.find_element(*SignOn.elemPwd)
        elemUserName.send_keys(username)
        elemPwd.send_keys(pwd)

    def submit(self):
        elemSubmit=self.driver.find_element(*SignOn.elemSubmit)
        self.mouse_click(elemSubmit)
        #elemSubmit.click()

    def findFlight(self):
        elemSaveInfo=self.driver.find_element(*SignOn.elemFindFlight)
        self.mouse_click(elemSaveInfo)

    def saveFlight(self):
        elemSaveFlight=self.driver.find_element(*SignOn.elemSaveFlight)
        self.mouse_click(elemSaveFlight)

    def fillPersonalInfo(self,firstname,lastname,number):
        # First name
        elemFirstName=self.driver.find_element(*SignOn.elemFirstName)
        elemFirstName.send_keys(firstname)

        # Last name
        elemLastName=self.driver.find_element(*SignOn.elemLastName)
        elemLastName.send_keys(lastname)

        # Credit card number
        elemNumber=self.driver.find_element(*SignOn.elemNumber)
        elemNumber.send_keys(number)

    def buyFlight(self):
        elemBuyFlight=self.driver.find_element(*SignOn.elemBuyFlight)
        self.mouse_click(elemBuyFlight)