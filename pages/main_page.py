from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class MainPage:
    TIMEOUT_SHORT = 10

    def __init__(self, driver):
        self.driver = driver

    def wait_for_open(self):
        unique_element = (By.XPATH, self.driver.locale['login_button'])

        WebDriverWait(self.driver, MainPage.TIMEOUT_SHORT).until(
            ec.visibility_of_element_located(unique_element))

    def search_game(self, name_game):
        """Ищем игру"""
        input_search = (By.XPATH, self.driver.locale['search_input'])

        search_game = WebDriverWait(self.driver, MainPage.TIMEOUT_SHORT).until(
            ec.element_to_be_clickable(input_search))
        search_game.click()
        search_game = WebDriverWait(self.driver, MainPage.TIMEOUT_SHORT).until(
            ec.visibility_of_element_located(input_search))
        search_game.send_keys(name_game + Keys.ENTER)
