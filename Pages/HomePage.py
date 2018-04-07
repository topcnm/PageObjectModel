from selenium.webdriver.common.by import By
from SeleniumWebDriver.SeleniumWebDriver import SeleniumWebDriver
from Pages.SignOnPage import SignOnPage
from Pages.RegistrationPage import RegistrationPage


class HomePage(SeleniumWebDriver):

    # Home Page Locators

    locator_values = {
        "_sign_on_link": "SIGN-ON",
        "_register_link": "REGISTER",
        "_support_link": "SUPPORT",
        "_contact_link": "CONTACT",
        "_user_name_field": "userName",
        "_password_field": "password",
        "_sign_in_button": "login"
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Fields
    def enter_user_name(self, user_name):
        self.get_element(By.NAME, self.locator_values["_user_name_field"]).send_keys(user_name)

    def enter_user_password(self, password):
        self.get_element(By.NAME, self.locator_values["_password_field"]).send_keys(password)

    def click_on_sign_in_button(self):
        self.get_element(By.NAME, self.locator_values["_sign_in_button"]).click()

    # Links
    def get_sign_on_page(self):
        self.get_element(By.LINK_TEXT, self.locator_values["_sign_on_link"]).click()
        return SignOnPage(self.driver)

    def get_register_page(self):
        self.get_element(By.LINK_TEXT, self.locator_values["_register_link"]).click()
        return RegistrationPage(self.driver)






