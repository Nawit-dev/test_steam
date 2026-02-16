from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_login(driver, fake):
    login = fake.name()
    password = fake.password()
    test_enter = MainPage(driver)
    test_enter.click_enter()
    test_login_form = LoginPage(driver)
    test_login_form.enter_login(login)
    test_login_form.enter_password(password)
    test_login_form.click_sign_in()
    assert test_login_form.error_text() == 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'
