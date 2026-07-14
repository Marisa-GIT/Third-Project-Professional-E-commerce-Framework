from typing import TYPE_CHECKING
from core.base_page import BasePage
from locators.checkout_overview_locators import CheckoutOverviewLocators
from pages.checkout_complete_page import CheckoutCompletePage
from selenium.webdriver.support import expected_conditions as EC

if TYPE_CHECKING:
    from pages.inventory_page import InventoryPage

class CheckoutOverviewPage(BasePage):

    def is_loaded(self) -> bool:
        self.logger.info("Checking if Checkout Overview page is loaded")
        return self.is_visible(CheckoutOverviewLocators.OVERVIEW_CONTAINER)
    
    def get_product_names(self) -> list[str]:
        self.logger.info("Getting product names in the checkout overview")
        product_elements = CheckoutOverviewLocators.PRODUCT_NAMES
        return self.get_text_from_elements(product_elements)

    def get_product_prices(self) -> list[str]:
        return self.get_text_from_elements(
            CheckoutOverviewLocators.PRODUCT_PRICES
        )
        
    def get_item_total(self) -> str:
        self.logger.info("Getting item total from checkout overview")
        item_total_locator = CheckoutOverviewLocators.ITEM_TOTAL
        return self.get_text(item_total_locator)

    def get_tax(self) -> str:
        self.logger.info("Getting tax from checkout overview")
        tax_locator = CheckoutOverviewLocators.TAX
        return self.get_text(tax_locator)

    def get_total(self) -> str:
        self.logger.info("Getting total from checkout overview")
        total_locator = CheckoutOverviewLocators.TOTAL
        return self.get_text(total_locator)
    
    def get_product_count(self) -> int:
        return self.get_element_count(
            CheckoutOverviewLocators.PRODUCT_NAMES
        )
    
    def finish(self) -> "CheckoutCompletePage":
        self.logger.info("Finishing checkout")
        self.click(CheckoutOverviewLocators.FINISH_BUTTON)

        self.wait.until(EC.url_contains("checkout-complete.html"))

        return CheckoutCompletePage(self.driver)
    
    def cancel(self) -> "InventoryPage":
        self.logger.info("Cancelling checkout")
        # Local import to avoid circular dependency
        from pages.inventory_page import InventoryPage
        self.click(CheckoutOverviewLocators.CANCEL_BUTTON)
        return InventoryPage(self.driver)