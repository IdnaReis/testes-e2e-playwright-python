import re

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.products_page import ProductsPage


def test_search_existing_product(page: Page):
    page.goto("/products")
    products_page = ProductsPage(page)

    products_page.search_product("Top")

    expect(products_page.search_results_title).to_be_visible()
    expect(products_page.product_list).to_be_visible()


def test_search_nonexistent_product(page: Page):
    page.goto("/products")
    products_page = ProductsPage(page)

    products_page.search_product("produtoquenaoexiste12345")

    expect(products_page.search_results_title).to_be_visible()
    expect(products_page.view_product_links).to_have_count(0)


def test_view_product_details(page: Page):
    page.goto("/products")
    products_page = ProductsPage(page)

    first_product = products_page.product_list.locator(".product-image-wrapper").first
    first_product.hover()
    first_product.locator("a", has_text="View Product").click(force=True)

    expect(page).to_have_url(re.compile(r"/product_details/"))
    expect(page.locator(".product-information h2")).to_be_visible()


def test_add_multiple_products_to_cart(page: Page):
    page.goto("/products")
    products_page = ProductsPage(page)

    products = products_page.product_list.locator(".product-image-wrapper")

    products.nth(0).hover()
    products.nth(0).locator("a", has_text="Add to cart").first.click(force=True)
    products_page.continue_shopping_button.click()

    products.nth(1).hover()
    products.nth(1).locator("a", has_text="Add to cart").first.click(force=True)
    products_page.continue_shopping_button.click()

    page.goto("/view_cart")
    cart_page = CartPage(page)
    expect(cart_page.product_name_in_cart).to_have_count(2)