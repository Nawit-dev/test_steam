from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser_singleton import Driver
from tests.config_reader import ConfigReader


class ResultPage:
    SORT_BUTTON = (By.ID, "sort_by_trigger")
    LINK_DOWN_PRICE = (By.ID, "Price_DESC")
    PRICE_GAME = (By.XPATH, "//*[@id='search_resultsRows']//div[contains(@class,'discount_final_price')]")
    SEARCH_INPUT = (By.XPATH, "//span[@class='title']")
    SHORT_TIME = ConfigReader.open_config()['timeout']

    def __init__(self):
        self.driver = Driver().get_driver()

    def sort_list_game(self):
        """Сортируем список игр"""
        sort = WebDriverWait(self.driver, ResultPage.SHORT_TIME).until(
            ec.element_to_be_clickable(ResultPage.SORT_BUTTON))
        sort.click()
        sort_list = WebDriverWait(self.driver, ResultPage.SHORT_TIME).until(
            ec.element_to_be_clickable(ResultPage.LINK_DOWN_PRICE))
        sort_list.click()
        WebDriverWait(self.driver, ResultPage.SHORT_TIME).until(ec.element_to_be_clickable(ResultPage.SEARCH_INPUT))

    def get_results(self, expected_count) -> list:
        """Получаем отсортированный список цен на игры"""
        all_name_game = WebDriverWait(self.driver, ResultPage.SHORT_TIME).until(
            ec.presence_of_all_elements_located(ResultPage.PRICE_GAME))
        list_name_game = [str(elem.text.replace("руб", "")) for elem in all_name_game[:expected_count]]
        result_list_name_game = [float(elem.replace(",", ".")) for elem in list_name_game]
        return result_list_name_game
