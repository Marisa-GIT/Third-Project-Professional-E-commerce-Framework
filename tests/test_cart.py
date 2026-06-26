from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_product_to_cart(driver):

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack_to_cart()

    inventory.open_cart()

    cart = CartPage(driver)

    assert(
        cart.get_product_name() 
        == "Sauce Labs Backpack"
    )