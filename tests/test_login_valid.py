import time

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_login_with_valid_credentials(page: Page):
    email = f"idna_login_{int(time.time())}@email.com"
    password = "Senha@123"

    # Cria uma conta nova (fica logada automaticamente)
    page.goto("/login")
    signup_page = SignupPage(page)
    signup_page.signup("Idna Login Test", email)
    signup_page.complete_registration()

    login_page = LoginPage(page)
    expect(login_page.logged_in_as).to_be_visible()

    # Faz logout de propósito pra testar o login de verdade
    login_page.logout_link.click()

    # Loga com as credenciais recém-criadas
    page.goto("/login")
    login_page.login(email, password)

    expect(login_page.logged_in_as).to_be_visible()


def test_logout(page: Page):
    email = f"idna_logout_{int(time.time())}@email.com"

    page.goto("/login")
    signup_page = SignupPage(page)
    signup_page.signup("Idna Logout Test", email)
    signup_page.complete_registration()

    login_page = LoginPage(page)
    expect(login_page.logged_in_as).to_be_visible()

    login_page.logout_link.click()

    expect(login_page.email_input).to_be_visible()