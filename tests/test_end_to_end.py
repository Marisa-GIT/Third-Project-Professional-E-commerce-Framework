from pages.login_page import LoginPage
from utils.test_data_manager import TestDataManager
from pages.checkout_overview_page import CheckoutOverviewPage

class TestCheckout:

    def test_complete_purchase(self, driver):
        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")

        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        inventory_page.add_product_to_cart("Sauce Labs Backpack")

        cart_page = inventory_page.open_cart()
        assert cart_page.is_loaded()

        checkout_information_page = cart_page.checkout()
        assert checkout_information_page.is_loaded()

        checkout_information_page.complete_information(
            "Ana Maria",
            "Perez",
            "111071"
        )
        checkout_information_page.submit_information()

        assert checkout_information_page.get_error_message() is None

        checkout_overview_page = CheckoutOverviewPage(driver)
        assert checkout_overview_page.is_loaded()

        checkout_complete_page = checkout_overview_page.finish()

        assert (
            checkout_complete_page.get_complete_header()
            == "Thank you for your order!"
        )