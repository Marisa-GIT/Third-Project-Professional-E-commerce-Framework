from selenium.webdriver.common.by import By
from core.base_page import BasePage
from locators.inventory_locators import InventoryLocators
from pages.cart_page import CartPage

class InventoryPage(BasePage):

    def is_loaded(self) -> bool:
        return self.is_visible((By.ID, "inventory_container"))
    
    def get_page_title(self) -> str:
        title_locator = InventoryLocators.get_page_title_locator()
        return self.get_text(title_locator)

    def add_product_to_cart(self, product_name) -> "InventoryPage":
        self.logger.info(
            f"Adding product '{product_name}' to cart"
            )
        add_to_cart_button_locator = InventoryLocators.get_add_to_cart_button_locator(product_name)
        self.click(add_to_cart_button_locator)
        return self 
    
    def remove_product(self, product_name) -> "InventoryPage":
        remove_button_locator = InventoryLocators.get_remove_button_locator(product_name)
        self.click(remove_button_locator)
        return self

    def get_product_price(self, product_name) -> str:
        product_price_locator = InventoryLocators.get_product_price_locator(product_name)
        return self.get_text(product_price_locator)

    def get_product_name(self, product_name) -> str:
        product_name_locator = InventoryLocators.get_product_name_locator(product_name)
        return self.get_text(product_name_locator)

    def get_cart_badge_count(self) -> int:
        cart_badge_locator = InventoryLocators.get_cart_badge_locator()
        if self.is_visible(cart_badge_locator):
            return int(self.get_text(cart_badge_locator))
        return 0

    def open_cart(self) -> CartPage:
        self.logger.info("Opening shopping cart")
        cart_icon_locator = InventoryLocators.get_cart_icon_locator()
        self.click(cart_icon_locator)
        return CartPage(self.driver)
