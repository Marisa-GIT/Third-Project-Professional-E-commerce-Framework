from utils.test_data_manager import TestDataManager
from pages.login_page import LoginPage


class TestCheckoutOverview:

    def test_checkout_summary_and_completion(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")
        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        product = TestDataManager.get_product("bike_light")

        inventory_page.add_product_to_cart(product["name"])

        product = TestDataManager.get_product("backpack")

        inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()
        checkout_info_page.fill_first_name("John")
        checkout_info_page.fill_last_name("Doe")
        checkout_info_page.fill_postal_code("12345")

        overview_page = checkout_info_page.submit_information()

        products_in_overview = overview_page.get_product_names()
        assert "Sauce Labs Backpack" in products_in_overview
        assert "Sauce Labs Bike Light" in products_in_overview

        product_prices = overview_page.get_product_prices()
        subtotal = overview_page.get_item_total() 
        tax = overview_page.get_tax()              
        total = overview_page.get_total()  

        expected_subtotal = round(sum(product_prices), 2)
        assert subtotal == expected_subtotal, \
            f"El subtotal de la UI ({subtotal}) no coincide con la suma de sus productos ({expected_subtotal})"

        expected_tax = round(subtotal * 0.08, 2)
        assert tax == expected_tax, \
            f"El impuesto calculado por el sistema ({tax}) no es el 8% esperado ({expected_tax})"

        expected_total = round(subtotal + tax, 2)
        assert total == expected_total, \
            f"El total final de la UI ({total}) no equivale a la suma de subtotal + tax ({expected_total})"
        
        complete_page = overview_page.finish()
        assert complete_page.get_complete_header() == "Thank you for your order!", \
            "No se visualizó el mensaje de éxito final de la compra"