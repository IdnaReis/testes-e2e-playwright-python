from playwright.sync_api import Page, expect

from pages.signup_page import SignupPage


def test_signup_page_elements(page: Page):
    page.goto("/login")

    signup_page = SignupPage(page)

    expect(signup_page.name_input).to_be_visible()
    expect(signup_page.email_input).to_be_visible()
    expect(signup_page.signup_button).to_be_visible()
def test_signup_valid_data(page: Page):
    page.goto("/login")

    signup_page = SignupPage(page)

    signup_page.signup(
        "Idna Test",
        "idna_teste@email.com"
    )