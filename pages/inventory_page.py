class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.add_to_cart_buttons = page.locator("button:has-text('Add to cart')")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.product_names = page.locator(".inventory_item_name")

    def add_first_product_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def go_to_cart(self):
        self.cart_icon.click()