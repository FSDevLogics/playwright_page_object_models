from playwright.async_api import Page

def test_003_check_loan(common_page, login_page, homepage, loan_page, page: Page):
    login_page.login("user1", "pass1")
    homepage.menu_access("Empréstimos")
    loan_page.select_amount("5.000,00")
    loan_page.get_loan()
    common_page.assert_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações.")
    common_page.back_homepage()
    common_page.assert_text("R$ 10.000,00")
    homepage.menu_access("Empréstimos")
    common_page.assert_text("Você já tem um empréstimo contratado em andamento. Novos empréstimos não estão disponíveis.")
    page.get_by_role("link", name="Voltar para Home").click()

    