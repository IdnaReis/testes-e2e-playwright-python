from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.products_page import ProductsPage


def test_cart_page_elements(page: Page):
    page.goto("/products")
    products_page = ProductsPage(page)
    product_name = products_page.get_first_product_name()
    products_page.add_first_product_to_cart()

    page.goto("/view_cart")
    cart_page = CartPage(page)

    expect(cart_page.cart_title).to_be_visible()
    expect(cart_page.cart_table).to_be_visible()
    expect(cart_page.proceed_to_checkout).to_be_visible()
    expect(cart_page.product_name_in_cart).to_have_text(product_name)
    expect(cart_page.product_quantity_in_cart).to_have_text("1")
    expect(cart_page.product_price_in_cart).to_be_visible()
    expect(cart_page.product_price_in_cart).to_contain_text("Rs.")

    cart_page.remove_product_button.click()
    expect(cart_page.product_name_in_cart).not_to_be_visible()