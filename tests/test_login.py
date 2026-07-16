
from pages.login_page import LoginPage
from utils.test_data_manager import TestDataManager
class TestLogin:

    def test_successful_login(self, driver):

        login_page = LoginPage(driver)

        user = TestDataManager.get_user("standard_user")
        
        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        assert inventory_page.is_loaded()
    
    def test_locked_login(self, driver):

        login_page = LoginPage(driver)

        user = TestDataManager.get_user("locked_user")

        login_page.login(
        user["username"],
        user["password"]

        )
        
        assert login_page.get_error_message() == \
        "Epic sadface: Sorry, this user has been locked out."