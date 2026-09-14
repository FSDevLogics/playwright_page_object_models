def test_002_login_sucessfull(common_page, login_page, homepage, pix_page):
    login_page.login("user1", "pass1")
    homepage.menu_access("Fazer Pix")
    pix_page.make_pix("999.999.999-99", "100")
    pix_page.assert_pix_successfull()
    common_page.back_homepage()
    common_page.assert_text("4.900,00")
    homepage.menu_access("Ver Extrato")
    common_page.assert_text("Pix para 999.999.999-99 - R$ -100,00")
    