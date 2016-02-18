from selenium.webdriver.common.by import By


class baseLocators():
    pass


class SignOn(baseLocators):
    elemSignOn=(By.XPATH,"//td[@class='mouseOut']")
    elemUserName=(By.XPATH,"//input[@name='userName']")
    elemPwd=(By.XPATH,"//input[@name='password']")
    elemSubmit=(By.XPATH,"//input[@name='login']")
    elemFindFlight=(By.XPATH,"//input[@name='findFlights']")
    elemSaveFlight=(By.XPATH,"//input[@name='reserveFlights']")
    elemFirstName=(By.XPATH,"//input[@name='passFirst0']")
    elemLastName=(By.XPATH,"//input[@name='passLast0']")
    elemNumber=(By.XPATH,"//input[@name='creditnumber']")
    elemBuyFlight=(By.XPATH,"//input[@name='buyFlights']")

class BuyObj(baseLocators):
    elemCartBuy = (By.XPATH, "//div[@class='btn bt-primary size-s buy normal']")
    elemSize = (By.XPATH, "//div[@data-value='4']")
