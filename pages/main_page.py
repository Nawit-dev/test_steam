from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:
    UNIQUE_ELEMENT = (By.XPATH, "//*[@id='content_login']//a//span[contains(text(),'Войти')]")
    ENTER = (By.XPATH, "//*[@id='global_action_menu']//a[contains(text(),'вход')]")
    TIMEOUT_SHORT = 10
    TIMEOUT_LONG = 20

    def __init__(self, driver):
        self.driver = driver

    def wait_for_open(self):
        WebDriverWait(self.driver, MainPage.TIMEOUT_SHORT).until(
            ec.visibility_of_element_located(MainPage.UNIQUE_ELEMENT))

    def open_login_form(self):
        """Переходим на форму входа"""
        enter = WebDriverWait(self.driver, MainPage.TIMEOUT_LONG).until(
            ec.element_to_be_clickable(
                MainPage.ENTER)
        )
        enter.click()
