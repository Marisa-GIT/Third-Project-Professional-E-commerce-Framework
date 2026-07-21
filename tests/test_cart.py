from utils.test_data_manager import TestDataManager

class TestCart:

    def test_cart_badge_increments_after_adding_product(self, login):
        inventory_page = login()

        product = TestDataManager.get_product("backpack")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 1

        product = TestDataManager.get_product("bike_light")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 2

    def test_cart_badge_decrements_after_removing_product(self, login):
        inventory_page = login()

        product = TestDataManager.get_product("backpack")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 1

        product = TestDataManager.get_product("bike_light")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 2

        inventory_page.remove_product(product["name"])
        assert inventory_page.get_cart_badge_count() == 1

    def test_continue_shopping_from_cart(self, login):
        inventory_page = login()

        cart_page = inventory_page.open_cart()

        returned_inventory_page = cart_page.continue_shopping()
        assert returned_inventory_page.is_loaded()

    def test_checkout_navigation_from_cart(self, login):
        inventory_page = login()
    
        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()
        assert checkout_info_page.is_loaded()

    def test_purchase_two_products(self, login):
        inventory_page = login()

        purchase_two_products = TestDataManager.get_specific_products(
            ["fleece_jacket", "labs_onesie"]
        )

        for product in purchase_two_products:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()

        checkout_info_page.complete_information("Juan", "Pérez", "110111")
        checkout_overview_page = checkout_info_page.submit_information()

        checkout_complete_page = checkout_overview_page.finish()

        success_message = checkout_complete_page.get_complete_header()
        assert success_message == "Thank you for your order!", \
            f"La compra falló o el mensaje es incorrecto. Mensaje obtenido: '{success_message}'"

    def test_purchase_after_remove_product(self, login):
        inventory_page = login()

        purchase_two_products = TestDataManager.get_specific_products(
            ["fleece_jacket", "bolt_tshirt"]
        )

        for product in purchase_two_products:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        product = TestDataManager.get_product("fleece_jacket")

        cart_page.remove_product(product["name"])

        checkout_info_page = cart_page.checkout()

        checkout_info_page.complete_information("Juan", "Pérez", "110111")
        checkout_overview_page = checkout_info_page.submit_information()

        checkout_complete_page = checkout_overview_page.finish()

        success_message = checkout_complete_page.get_complete_header()
        assert success_message == "Thank you for your order!", \
            f"La compra falló o el mensaje es incorrecto. Mensaje obtenido: '{success_message}'"
        
    def test_purchase_problem_user(self, login):
        inventory_page = login("problem_user")
     
        product = TestDataManager.get_product("bike_light")
        inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()

        checkout_info_page.fill_first_name("John")
        checkout_info_page.fill_last_name("Due")
        checkout_info_page.fill_postal_code("111076")
        checkout_info_page.submit_information()

        assert checkout_info_page.get_error_message() == "Error: Last Name is required"






        
            
