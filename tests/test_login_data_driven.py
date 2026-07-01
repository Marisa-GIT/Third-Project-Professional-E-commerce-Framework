import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import BASE_URL

@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce")
    ]
)
def test_login_multiple_users(
    driver,
    username,
    password
):
    driver.get(BASE_URL)
    
    login = LoginPage(driver)
    
    login.login(username, password)
    
    inventory = InventoryPage(driver)
    
    assert inventory.get_page_title() == "Products"