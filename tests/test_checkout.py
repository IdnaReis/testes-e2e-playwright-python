import time

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage, PaymentPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage


def test_checkout_flow(page: Page):
    email = f"idna_teste_{int(time.time())}@email.com"

    # Cadastro de um usuário novo (já loga automaticamente)
    page.goto("/login")
    signup_page = SignupPage(page)
    signup_page.signup("Idna Test", email)
    signup_page.complete_registration()

    # Adiciona produto ao carrinho
    page.goto("/products")
    products_page = ProductsPage(page)
    products_page.add_first_product_to_cart()

    # Vai pro carrinho e clica em finalizar compra
    page.goto("/view_cart")
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout.click()

    # Valida a tela de checkout
    checkout_page = CheckoutPage(page)
    expect(page.locator("li.active", has_text="Checkout")).to_be_visible()
    expect(checkout_page.address_delivery).to_be_visible()
    expect(checkout_page.address_delivery).to_contain_text("Idna")

    # Finaliza o pedido
    checkout_page.go_to_payment()

    # Preenche cartão de teste e paga
    payment_page = PaymentPage(page)
    payment_page.pay_with_test_card()

    # Confirma que o pedido foi realizado
    expect(page.locator("h2", has_text="Order Placed!")).to_be_visible()
