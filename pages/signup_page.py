from playwright.sync_api import Page


class SignupPage:

    def __init__(self, page: Page):
        self.page = page

        self.name_input = page.locator(
            '[data-qa="signup-name"]'
        )
        self.email_input = page.locator(
            '[data-qa="signup-email"]'
        )
        self.signup_button = page.locator(
            '[data-qa="signup-button"]'
        )

    def signup(self, name, email):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def complete_registration(self):
        self.page.locator("#id_gender1").check()
        self.page.locator("#password").fill("Senha@123")
        self.page.locator("#days").select_option("10")
        self.page.locator("#months").select_option("5")
        self.page.locator("#years").select_option("1995")

        self.page.locator("#first_name").fill("Idna")
        self.page.locator("#last_name").fill("Reis")
        self.page.locator("#address1").fill("Rua de Teste, 123")
        self.page.locator("#country").select_option(label="United States")
        self.page.locator("#state").fill("Goias")
        self.page.locator("#city").fill("Valparaiso de Goias")
        self.page.locator("#zipcode").fill("72876000")
        self.page.locator("#mobile_number").fill("61999999999")

        self.page.locator("button[data-qa='create-account']").click()
        self.page.locator("a[data-qa='continue-button']").click()