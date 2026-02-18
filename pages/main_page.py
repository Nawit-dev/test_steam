from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    XPATH = By.XPATH
    ENTER = "//*[@id='global_action_menu']//a[contains(text(),'вход')]"
    TIMEOUT_LONG = 20
    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        """Переходим на форму входа"""
        enter = WebDriverWait(self.driver, MainPage.TIMEOUT_LONG).until(
            EC.element_to_be_clickable(
                (MainPage.XPATH, MainPage.ENTER))
        )
        enter.click()

