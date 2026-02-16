from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    TIMEOUT_SHORT = 10
    TIMEOUT_LONG = 20
    INPUT_LOGIN = "//*[@id='responsive_page_template_content']//input[@type='text']"
    INPUT_PASSWORD = "//*[@id='responsive_page_template_content']//input[@type='password']"
    BUTTON_ENTER = "//*[@id='responsive_page_template_content']//button[@type='submit']"
    ERROR_TEXT = ("//*[@id='responsive_page_template_content']//div[contains(text(),"
                  "'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login(self, login):
        """Ввод логина в поле авторизации"""
        WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.presence_of_element_located((By.XPATH, LoginPage.INPUT_LOGIN)))
        self.find_element(By.XPATH, LoginPage.INPUT_LOGIN)
        self.click_element(By.XPATH, LoginPage.INPUT_LOGIN)
        self.send_keys(By.XPATH, LoginPage.INPUT_LOGIN, login)

    def enter_password(self, password):
        """Ввод пароля в поле авторизации """
        self.click_element(By.XPATH, LoginPage.INPUT_PASSWORD)
        self.send_keys(By.XPATH, LoginPage.INPUT_PASSWORD,
                       password)

    def click_sign_in(self):
        """Нажимаем на кнопку войти"""
        self.click_element(By.XPATH, LoginPage.BUTTON_ENTER)
        WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.visibility_of_element_located((By.XPATH, LoginPage.ERROR_TEXT)))

    def error_text(self):
        """Текст ошибки при неправильном вводе пароля"""
        element = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(ec.presence_of_element_located(
            (By.XPATH, LoginPage.ERROR_TEXT)))

        return element.text
