from pages.login_page import LoginPage
from config.settings import BASE_URL
from config.credentials import USERNAME, PASSWORD
class TestLogin:

    def test_successful_login(self, driver):

        login_page = LoginPage(driver)

        inventory_page = login_page.login(
            USERNAME,
            PASSWORD
        )

        assert inventory_page.is_loaded()