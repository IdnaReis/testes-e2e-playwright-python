from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.products_title = page.locator(
            "text=All Products"
        )

        self.product_list = page.locator(
            ".features_items"
        )

        self.search_input = page.locator(
            "#search_product"
        )

        self.search_button = page.locator(
            "#submit_search"
        )

        self.add_to_cart_buttons = page.locator("a.add-to-cart")
        self.continue_shopping_button = page.locator("button", has_text="Continue Shopping")
        self.search_results_title = page.locator("h2", has_text="Searched Products")
        self.view_product_links = page.locator("a", has_text="View Product")
    def search_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()

    def get_first_product_name(self):
        return self.product_list.locator(".productinfo p").first.inner_text()

    def add_first_product_to_cart(self):
        self.add_to_cart_buttons.first.click()
        self.continue_shopping_button.click()
        