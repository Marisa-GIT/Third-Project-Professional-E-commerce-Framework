from pages.login_page import LoginPage
from utils.test_data_manager import TestDataManager

class TestCheckout:

    def test_complete_purchase(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")
        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        product = TestDataManager.get_product("backpack")

        inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()
        assert cart_page.is_loaded()

        checkout_information_page = cart_page.checkout()
        assert checkout_information_page.is_loaded()

        checkout_information_page.complete_information(
            "Ana Maria",
            "Perez",
            "111071"
        )

        checkout_overview_page = checkout_information_page.submit_information()
        assert checkout_overview_page.is_loaded()

        checkout_complete_page = checkout_overview_page.finish()
        assert (
            checkout_complete_page.get_complete_header()
            == "Thank you for your order!"
        )
    
    def test_purchace_multiple_products(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")
        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        products_to_purchanse = TestDataManager.get_specific_products(["fleece_jacket", "labs_onesie", "bolt_tshirt"]) 
        
        for product in products_to_purchanse:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()
        assert cart_page.is_loaded()

        checkout_information_page = cart_page.checkout()
        assert checkout_information_page.is_loaded()

        checkout_information_page.complete_information(
            "Ana Maria",
            "Perez",
            "111071"
        )

        checkout_overview_page = checkout_information_page.submit_information()
        assert checkout_overview_page.is_loaded()

        checkout_complete_page = checkout_overview_page.finish()
        assert (
            checkout_complete_page.get_complete_header()
            == "Thank you for your order!"
        )

        


