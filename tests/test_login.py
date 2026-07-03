from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from core.logger import Logger


logger = Logger.get_logger(__name__)
logger.info("Starting test: test_successful_login")

def test_successful_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    logger.info("Testing successful login")
    #before
    #assert "inventory" in driver.current_url, "Login failed: User was not redirected to the inventory page."
    #after
    assert inventory.get_page_title() == "Products"