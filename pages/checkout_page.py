from pytest_playwright.pytest_playwright import page

class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.success_message = page.locator(".complete-header")

    def fill_details(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(str(postal))

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def get_success_message(self):
        return self.success_message.text_content()