from EnvironmentalSetUp.EnvironmentalSetUp import EnvironmentalSetUp
from Pages.HomePage import HomePage


class HomePageTests(EnvironmentalSetUp, HomePage):

    def test_valid_login_home_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_user_name("test@test.com")
        home_page.enter_user_password("qwerty")
        home_page.click_on_sign_in_button()
