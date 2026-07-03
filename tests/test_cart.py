from config.credentials import PASSWORD, USERNAME
from core.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.settings import BASE_URL
from selenium.webdriver.common.by import By

class CartPage(BasePage):
     def test_add_product_to_cart(self, driver):
        login_page = LoginPage(driver)

        inventory_page = login_page.login(
            USERNAME,
            PASSWORD
        )

        inventory_page.add_product_to_cart(
            "Sauce Labs Backpack"
        )

        assert inventory_page.get_cart_badge_count() == 1