from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser_singleton import Driver
import time


class ResultPage:
    SORT_BUTTON = (By.ID, "sort_by_trigger")
    LINK_DOWN_PRICE = (By.ID, "Price_DESC")
    PRICE_GAME = (By.XPATH, "//*[@id='search_resultsRows']//div[contains(@class,'discount_final_price')]")
    SEARCH_INPUT = (By.XPATH, "//span[@class='title']")

    def __init__(self):
        self.driver = Driver().driver
        self.timeout = Driver().timeout

    def price_before_sort(self):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_element_located(ResultPage.PRICE_GAME)
        ).text

    def sort_list_game(self):
        """Сортируем список игр"""
        old = self.driver.find_element(*ResultPage.SEARCH_INPUT)
        sort = WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(ResultPage.SORT_BUTTON))
        sort.click()
        sort_list = WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(ResultPage.LINK_DOWN_PRICE))
        sort_list.click()
        WebDriverWait(self.driver, 5).until_not(
            lambda d: d.find_element(*ResultPage.SEARCH_INPUT).id == old.id
        )
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_elements(*ResultPage.SEARCH_INPUT)
        )

    def get_results(self, expected_count) -> list:
        """Получаем отсортированный список цен на игры"""
        all_name_game = WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_all_elements_located(ResultPage.PRICE_GAME))
        list_name_game = [str(elem.text.replace("руб", "")) for elem in all_name_game[:expected_count]]
        result_list_name_game = [float(elem.replace(",", ".")) for elem in list_name_game]
        return result_list_name_game
