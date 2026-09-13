def test_001_login_sucessfull(login_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_sucessfull()
    