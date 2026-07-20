import pytest
from pages.login_page import LoginPage
from utils.test_data_manager import TestDataManager
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

        backpack = TestDataManager.get_product("backpack")
        bike_light = TestDataManager.get_product("bike_light")

        assert len(product_names) > 0, \
            "El catálogo de productos se encuentra vacío"

        assert backpack["name"] in product_names, \
            f"{backpack['name']} no aparece en el catálogo"

        assert bike_light["name"] in product_names, \
            f"{bike_light['name']} no aparece en el catálogo"

    def test_product_sorting_by_price(self):
        self.inventory.select_sort_option("lohi")

        actual_prices = self.inventory.get_all_product_prices()
        expected_prices = sorted(actual_prices)

        assert actual_prices == expected_prices, (
            f"El ordenamiento falló.\n"
            f"Actual:   {actual_prices}\n"
            f"Esperado: {expected_prices}"
        )

    def test_add_product_to_cart(self):
        product = TestDataManager.get_product("backpack")

        self.inventory.add_product_to_cart(product["name"])

        assert self.inventory.get_cart_badge_count() == 1, (
            "El contador del carrito debería mostrar 1 producto."
        )

    def test_add_multiple_products_to_cart(self):
        products_to_purchase = TestDataManager.get_specific_products(
            [
                "backpack",
                "bike_light",
                "labs_onesie"
            ]
        )

        for product in products_to_purchase:
            self.inventory.add_product_to_cart(product["name"])

        cart_page = self.inventory.open_cart()

        products_in_cart = cart_page.get_product_names()

        for product in products_to_purchase:
            assert product["name"] in products_in_cart, (
                f"{product['name']} no se encontró en el carrito."
            )

    def test_add_products_updates_cart_badge(self):
        assert self.inventory.get_cart_badge_count() == 0, (
            "El carrito debería iniciar vacío."
        )

        backpack = TestDataManager.get_product("backpack")
        bike_light = TestDataManager.get_product("bike_light")

        self.inventory.add_product_to_cart(backpack["name"])

        assert self.inventory.get_cart_badge_count() == 1, (
            "El contador del carrito debería ser 1."
        )

        self.inventory.add_product_to_cart(bike_light["name"])

        assert self.inventory.get_cart_badge_count() == 2, (
            "El contador del carrito debería ser 2."
        )