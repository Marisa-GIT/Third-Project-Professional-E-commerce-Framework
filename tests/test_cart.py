from utils.test_data_manager import TestDataManager
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class TestCart:
     
     def test_add_product_to_cart(self, driver):
        login_page = LoginPage(driver)

        user = TestDataManager.get_user("standard_user")

        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        inventory_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        assert inventory_page.get_cart_badge_count() == 1