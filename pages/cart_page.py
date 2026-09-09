from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.cart_title = page.locator("li.active", has_text="Shopping Cart")
        self.cart_table = page.locator("#cart_info_table")
        self.proceed_to_checkout = page.locator("a.check_out")
        self.product_name_in_cart = page.locator(".cart_description h4 a")
        self.product_quantity_in_cart = page.locator(".cart_quantity button")
        self.product_price_in_cart = page.locator(".cart_price p")
        self.remove_product_button = page.locator(".cart_quantity_delete")