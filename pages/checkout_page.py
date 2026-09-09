from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.address_delivery = page.locator("#address_delivery")
        self.place_order_button = page.locator("a.check_out")

    def go_to_payment(self):
        for _ in range(3):
            self.place_order_button.click()
            self.page.wait_for_timeout(2000)
            if "payment" in self.page.url:
                return
        raise Exception("Nao foi possivel navegar ate a pagina de pagamento apos varias tentativas")


class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_on_card = page.locator('input[data-qa="name-on-card"]')
        self.card_number = page.locator('input[data-qa="card-number"]')
        self.cvc = page.locator('input[data-qa="cvc"]')
        self.expiry_month = page.locator('input[data-qa="expiry-month"]')
        self.expiry_year = page.locator('input[data-qa="expiry-year"]')
        self.pay_button = page.locator('button[data-qa="pay-button"]')

    def pay_with_test_card(self):
        self.name_on_card.fill("Idna Test")
        self.card_number.fill("4111111111111111")
        self.cvc.fill("123")
        self.expiry_month.fill("12")
        self.expiry_year.fill("2030")
        self.pay_button.click()