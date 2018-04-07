from SeleniumWebDriver.SeleniumWebDriver import SeleniumWebDriver
from Pages.ConfirmationPage import ConfirmationPage


class RegistrationPage(SeleniumWebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locator_values = {
        "_user_name_field": "email",
        "_password_field": "password",
        "_confirm_password": "confirmPassword",
        "_submit_button": "register"
    }

    def enter_user_name(self, user_name):
        self.get_element("name", self.locator_values["_user_name_field"]).send_keys(user_name)

    def enter_password(self, password):
        self.get_element("name", self.locator_values["_password_field"]).send_keys(password)

    def confirm_password(self, confirm_password):
        self.get_element("name", self.locator_values["_confirm_password"]).send_keys(confirm_password)

    def click_on_submit_button(self):
        self.driver.find_element("name", self.locator_values["_submit_button"]).click()
        return ConfirmationPage(self.driver)



