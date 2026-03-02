from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from browser_singleton import Driver


class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//*[@id='content_login']//a//span")
    SEARCH_INPUT = (By.XPATH, "//input[@type='text']")

    def __init__(self):
        self.driver = Driver().get_driver()
        self.timeout = Driver().timeout

    def wait_for_open(self):
        WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(MainPage.LOGIN_BUTTON))

    def search_game(self, name_game):
        """Ищем игру"""
        input_search_game = WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(MainPage.SEARCH_INPUT))
        input_search_game.click()
        input_search_game = WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(MainPage.SEARCH_INPUT))
        input_search_game.send_keys(name_game + Keys.ENTER)
