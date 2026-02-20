from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_login(driver, fake):
    login_name = fake.name()
    password = fake.password()

    test_enter = MainPage(driver)
    test_enter.wait_for_open()
    test_enter.open_login_form()
    test_login_form = LoginPage(driver)
    test_login_form.submit_login_form(login_name, password)
    actual_text = test_login_form.get_error_text()
    expected_text = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'
    assert actual_text == expected_text, f'Ожидали: {expected_text}, получили: {actual_text}'
