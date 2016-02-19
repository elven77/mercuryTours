import basePages
from locators.locators import BookFlight


class BookFlightPages(basePages.BasePage):
    def fillPersonalInfo(self,firstname,lastname,number):
        # First name
        elemFirstName=self.driver.find_element(*BookFlight.elemFirstName)
        elemFirstName.send_keys(firstname)

        # Last name
        elemLastName=self.driver.find_element(*BookFlight.elemLastName)
        elemLastName.send_keys(lastname)

        # Credit card number
        elemNumber=self.driver.find_element(*BookFlight.elemNumber)
        elemNumber.send_keys(number)

    def purchase(self):
        elemBuyFlight=self.driver.find_element(*BookFlight.elemBuyFlight)
        self.mouse_click(elemBuyFlight)