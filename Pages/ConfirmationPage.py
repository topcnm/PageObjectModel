from SeleniumWebDriver.SeleniumWebDriver import SeleniumWebDriver
from selenium.webdriver.common.by import By


class ConfirmationPage(SeleniumWebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_registered_user_name(self):
        self.get_element(By.TAG_NAME, "a")
