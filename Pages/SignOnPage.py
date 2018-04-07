from SeleniumWebDriver.SeleniumWebDriver import SeleniumWebDriver
from selenium.webdriver.common.by import By


class SignOnPage(SeleniumWebDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    locator_values = {
        "_user_name_field": "userName",
        "_password_field": "password",
        "_submit_button": "login",
    }

    def enter_user_name(self, user_name):
        self.get_element(By.NAME, self.locator_values["_user_name_field"]).send_keys(user_name)

    def enter_user_password(self, password):
        self.get_element(By.NAME, self.locator_values["_password_field"]).send_keys(password)

    def click_on_submit_button(self):
        self.get_element(By.NAME, self.locator_values["_submit_button"]).click()


