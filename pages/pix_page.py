from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.pix_key = page.get_by_role("textbox", name="Chave Pix:")
        self.amount = page.get_by_role("textbox", name="Valor:")
        self.send_pix_button = page.get_by_role("button", name="Enviar Pix")

    def make_pix(self, key, amount):
        self.pix_key.fill(key)
        self.amount.fill(amount)
        self.send_pix_button.click()

    def assert_pix_successfull(self):
        expect(self.page.get_by_role("heading", name="Transação Realizada com")).to_be_visible()
        expect(self.page.get_by_text("A transação foi concluída com")).to_be_visible()

    

 
