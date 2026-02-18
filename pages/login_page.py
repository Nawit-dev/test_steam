from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    TIMEOUT_SHORT = 10
    TIMEOUT_LONG = 20
    XPATH = By.XPATH
    INPUT_LOGIN = "//*[@id='responsive_page_template_content']//input[@type='text']"
    INPUT_PASSWORD = "//*[@id='responsive_page_template_content']//input[@type='password']"
    BUTTON_ENTER = "//*[@id='responsive_page_template_content']//button[@type='submit']"
    ERROR_TEXT = "//*[@id='responsive_page_template_content']//div[contains(@class, '_1W_6HXiG4JJ0By1qN_0fGZ')]"

    def __init__(self, driver):
        self.driver = driver

    def submit_login_form(self, login_name, password_user):
        login = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.presence_of_element_located((LoginPage.XPATH, LoginPage.INPUT_LOGIN)))
        login.click()
        login.send_keys(login_name)

        password = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.presence_of_element_located((LoginPage.XPATH, LoginPage.INPUT_PASSWORD)))
        password.click()
        password.send_keys(password_user)

        enter = WebDriverWait(self.driver, LoginPage.TIMEOUT_SHORT).until(
            ec.presence_of_element_located((LoginPage.XPATH, LoginPage.BUTTON_ENTER))
        )
        enter.click()

    def get_error_text(self):
        """Текст ошибки при неправильном вводе пароля"""
        locator = (LoginPage.XPATH, LoginPage.ERROR_TEXT)

        def text_not_empty(driver):
            el = driver.find_element(*locator)
            return el if el.text.strip() != "" else False
        element = WebDriverWait(self.driver, 10).until(text_not_empty)
        return element.text
