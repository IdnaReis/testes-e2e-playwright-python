from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator(
            'input[data-qa="login-email"]'
        )

        self.password_input = page.locator(
            'input[data-qa="login-password"]'
        )

        self.login_button = page.locator(
            'button[data-qa="login-button"]'
        )

        self.error_message = page.get_by_text(
            "Your email or password is incorrect!"
        )
        self.logged_in_as = page.locator("a", has_text="Logged in as")
        self.logout_link = page.locator('a[href="/logout"]')

    
    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        