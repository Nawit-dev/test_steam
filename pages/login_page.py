from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    TIMEOUT_SHORT = 10
    TIMEOUT_LONG = 20
    INPUT_LOGIN = (By.XPATH, "//*[@id='responsive_page_template_content']//input[@type='text']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='responsive_page_template_content']//input[@type='password']")
    BUTTON_ENTER = (By.XPATH, "//*[@id='responsive_page_template_content']//button[@type='submit']")
    ERROR_TEXT = (By.XPATH, "//form//div[5]")

    def __init__(self, driver):
        self.driver = driver

    def submit_login_form(self, login_name, password_user):
        login = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.element_to_be_clickable(LoginPage.INPUT_LOGIN))
        login.click()
        login = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.visibility_of_element_located(LoginPage.INPUT_LOGIN))
        login.send_keys(login_name)

        password = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.element_to_be_clickable(LoginPage.INPUT_PASSWORD))
        password.click()
        password = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.visibility_of_element_located(LoginPage.INPUT_PASSWORD))
        password.send_keys(password_user)

        enter = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.element_to_be_clickable(LoginPage.BUTTON_ENTER))
        enter.click()

    def get_error_text(self):
        """Текст ошибки при неправильном вводе пароля"""

        def text_not_empty(driver):
            el = driver.find_element(LoginPage.ERROR_TEXT)
            return el if el.text.strip() != "" else False

        element = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(text_not_empty)
        return element.text
