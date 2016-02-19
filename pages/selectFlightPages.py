import basePages
from locators.locators import ChooseFlight


class SelectFlight(basePages.BasePage):
    def departFlight(self):
        elemDepartFlight=self.driver.find_element(*ChooseFlight.elemDepartFlight)
        elemDepartFlight.click()

    def returnFlight(self):
        elemReturnFlight=self.driver.find_element(*ChooseFlight.elemReturnFlight)
        elemReturnFlight.click()

    def saveFlight(self):
        elemSaveFlight=self.driver.find_element(*ChooseFlight.elemSaveFlight)
        self.mouse_click(elemSaveFlight)