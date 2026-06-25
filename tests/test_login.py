from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger()
logger.info("Starting test: test_successful_login")

def test_successful_login(driver):

    driver.get("https://www.saucedemo.com")

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