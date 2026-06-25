from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    
    TITLE = (By.CLASS_NAME, "title")

    def get_page_title(self):
        return self.get_text(self.TITLE)