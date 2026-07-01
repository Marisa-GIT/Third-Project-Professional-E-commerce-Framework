from selenium.webdriver.common.by import By
from core.base_page import BasePage

class InventoryPage(BasePage):
    
    TITLE = (By.CLASS_NAME, "title")

    ADD_BACKPACK =(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    def get_page_title(self):
        return self.get_text(self.TITLE)
    
    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

    def open_cart(self):
        self.click(self.CART_ICON)