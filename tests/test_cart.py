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
        product = TestDataManager.get_product("backpack")

        inventory_page.add_product_to_cart(product["name"])
        
        assert inventory_page.get_cart_badge_count() == 1


     def test_add_multiple_products_to_cart(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")
        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        products_to_purchanse = TestDataManager.get_specific_products(["backpack", "bike_light", "labs_onesie"]) 

        for product in products_to_purchanse:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        products_in_cart = cart_page.get_product_names()
        
        assert "Sauce Labs Backpack" in products_in_cart
        assert "Sauce Labs Bike Light" in products_in_cart
        assert "Sauce Labs Onesie" in products_in_cart


     def test_cart_badge_updates_correctly(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")
        inventory_page = login_page.login(
            user["username"],
            user["password"]
        )

        product = TestDataManager.get_product("backpack")

        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 1

        product = TestDataManager.get_product("bike_light")

        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 2
    
     def test_cart_badge_lifecycle(self, driver):
         
         login_page = LoginPage(driver)
         user = TestDataManager.get_user("standard_user")
         inventory_page = login_page.login(
                user["username"],
                user["password"]
            )
         
         product = TestDataManager.get_product("backpack")

         inventory_page.add_product_to_cart(product["name"])
         assert inventory_page.get_cart_badge_count() == 1

         product = TestDataManager.get_product("bike_light")

         inventory_page.add_product_to_cart(product["name"])
         assert inventory_page.get_cart_badge_count() == 2

         inventory_page.remove_product(product["name"])
         assert inventory_page.get_cart_badge_count() == 1


     def test_continue_shopping_from_cart(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")  
        inventory_page = login_page.login(
                    user["username"],
                    user["password"]
            )
        
        cart_page = inventory_page.open_cart()

        returned_inventory_page = cart_page.continue_shopping()
        assert  returned_inventory_page.is_loaded()

     def test_checkout_navigation_from_cart(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")          
        inventory_page = login_page.login(
                        user["username"],
                        user["password"]
                )

        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()
        assert checkout_info_page.is_loaded()







        
            
