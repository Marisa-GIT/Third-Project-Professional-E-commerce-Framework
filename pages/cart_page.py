from selenium.webdriver.common.by import By
from core.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def get_product_name(self):
        return self.get_text(self.CART_ITEM)