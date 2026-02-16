from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    ENTER = "//*[@id='global_action_menu']//a[contains(text(),'вход')]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_enter(self):
        """Переходим на форму входа"""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, MainPage.ENTER))
        )
        self.click_element(By.XPATH, MainPage.ENTER)
