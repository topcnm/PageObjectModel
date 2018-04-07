from EnvironmentalSetUp.EnvironmentalSetUp import EnvironmentalSetUp
from Pages.HomePage import HomePage
from Pages.RegistrationPage import RegistrationPage
from Pages.ConfirmationPage import ConfirmationPage


class RegistrationPageTests(EnvironmentalSetUp, HomePage, RegistrationPage, ConfirmationPage):

    def test_valid_registration(self):
        registration_page = self.get_register_page()
        registration_page.enter_user_name("test@test.com")
        registration_page.enter_password("qwerty")
        registration_page.confirm_password("qwerty")
        registration_page.click_on_submit_button()