class CartPage:

    def __init__(self, page):
        self.page = page

        self.cart_items = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_cart_item_name(self):
        return self.cart_items.first.text_content()

    def click_checkout(self):
        self.checkout_button.click()