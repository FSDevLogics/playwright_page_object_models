from playwright.sync_api import Page, expect

class LoanPage:
    def __init__(self, page: Page):
        self.page = page
        self.get_loan_button = self.page.get_by_role("button", name="Contratar Empréstimo")

    def select_amount(self, amount):
        self.page.get_by_role("radio", name=f"R$ {amount}").click()

    def get_loan(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.get_loan_button.click()
