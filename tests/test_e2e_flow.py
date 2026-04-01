from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_e2e_purchase_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # login
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # add to cart
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    # validate cart
    item = cart.get_cart_item_name()
    assert "Sauce" in item

    # checkout
    cart.click_checkout()
    checkout.fill_details("Ash", "Raj", 560001)
    checkout.continue_checkout()
    checkout.finish_checkout()

    # validate success
    success = checkout.get_success_message()
    assert "Thank you" in success