from playwright.sync_api import Page, expect

from pages.products_page import ProductsPage


def test_products_page_elements(page: Page):
    page.goto("/products")

    products_page = ProductsPage(page)

    expect(products_page.products_title).to_be_visible()
    expect(products_page.product_list).to_be_visible()
    expect(products_page.search_input).to_be_visible()
    expect(products_page.search_button).to_be_visible()
def test_search_product(page: Page):
    page.goto("/products")

    products_page = ProductsPage(page)

    products_page.search_product("Blue Top")

    expect(products_page.product_list).to_be_visible()