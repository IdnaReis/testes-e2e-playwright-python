from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_login_page_elements(page: Page):
    page.goto("/login")

    login_page = LoginPage(page)

    expect(login_page.email_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


def test_login_invalid_credentials(page: Page):
    page.goto("/login")

    login_page = LoginPage(page)

    login_page.login(
        "teste@email.com",
        "senha_incorreta"
    )

    expect(login_page.error_message).to_be_visible()
def test_login_empty_email(page: Page):
    page.goto("/login")

    login_page = LoginPage(page)

    login_page.login(
        "",
        "senha_incorreta"
    )

    expect(login_page.email_input).to_be_visible()
def test_login_empty_password(page: Page):
    page.goto("/login")

    login_page = LoginPage(page)

    login_page.login(
        "teste@email.com",
        ""
    )

    expect(login_page.password_input).to_be_visible()