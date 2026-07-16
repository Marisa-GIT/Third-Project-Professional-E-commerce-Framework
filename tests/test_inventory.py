import pytest
from pages.login_page import LoginPage
from utils.test_data_manager import TestDataManager

class TestInventory:
    
    @pytest.fixture(autouse=True)

    def setup_inventory(self, driver):

        login_page = LoginPage(driver)
        user = TestDataManager.get_user("standard_user")
        self.inventory = login_page.login(
            user["username"],
            user["password"]
            )
    def test_product_catalog_display(self):

        product_names = self.inventory.get_all_product_names()

        assert len(product_names) > 0, "El catálogo de productos se encuentra vacío"
        assert "Sauce Labs Backpack" in product_names, "La mochila clásica no aparece en el catálogo"
        assert "Sauce Labs Bike Light" in product_names, "La luz de bicicleta no aparece en el catálogo"
    
    def test_product_sorting_by_price(self):
        
        self.inventory.select_sort_option("lohi")
        print(self.inventory.get_all_product_prices())

        actual_prices = self.inventory.get_all_product_prices()

        expected_prices = sorted(actual_prices)
        
        assert actual_prices == expected_prices, \
            f"El ordenamiento falló. Lista en pantalla: {actual_prices}, Esperada: {expected_prices}"
        
    def test_add_products_updates_cart_badge(self):

        assert self.inventory.get_cart_badge_count() == 0, "El carrito no inició en 0"

        self.inventory.add_product_to_cart("Sauce Labs Backpack")
        assert self.inventory.get_cart_badge_count() == 1, "El contador del carrito no subió a 1"

        self.inventory.add_product_to_cart("Sauce Labs Bike Light")
        assert self.inventory.get_cart_badge_count() == 2, "El contador del carrito no subió a 2"



