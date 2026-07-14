from utils.test_data_manager import TestDataManager
from pages.login_page import LoginPage


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

     def test_add_multiple_products_to_cart(self, driver):
        login_page = LoginPage(driver)
        
        user = TestDataManager.get_user("standard_user")

        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.add_product_to_cart("Sauce Labs Bike Light")
        inventory_page.add_product_to_cart("Sauce Labs Onesie")

        cart_page = inventory_page.open_cart()
        products_in_cart = cart_page.get_product_names()
        
        assert "Sauce Labs Backpack" in products_in_cart
        assert "Sauce Labs Bike Light" in products_in_cart
        assert "Sauce Labs Onesie" in products_in_cart


        
            
