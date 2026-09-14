from playwright.sync_api import Page, expect

class Homepage:
    def __init__(self, page: Page):
        self.page = page

    def menu_access(self, menu):
        self.page.get_by_role("button", name=f"{menu}").click()