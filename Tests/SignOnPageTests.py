from EnvironmentalSetUp.EnvironmentalSetUp import EnvironmentalSetUp
from Pages.HomePage import HomePage
from Pages.SignOnPage import SignOnPage


class SignOnPageTests(EnvironmentalSetUp, HomePage, SignOnPage):

    def test_valid_login(self):
        sign_on_page = self.get_sign_on_page()
        sign_on_page.enter_user_name("selenium@gmail.com")
        sign_on_page.enter_user_password("qwerty")
        sign_on_page.click_on_submit_button()