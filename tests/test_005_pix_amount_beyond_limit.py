def test_005_pix_amount_beyond_limit(common_page, login_page, homepage, pix_page):
    login_page.login("user1", "pass1")
    homepage.menu_access("Fazer Pix")
    pix_page.make_pix("999.999.999-99", "3001")
    common_page.assert_text("O valor do Pix não pode ultrapassar R$ 3.000,00. Tente novamente.")
