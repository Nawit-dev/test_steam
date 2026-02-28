from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ResultPage:
    TIMEOUT_SHORT = 10
    SORT_BUTTON = (By.XPATH, "//button[@id='sort_by_trigger']")
    LINK_DOWN_PRICE = (By.XPATH, "//a[@id='Price_DESC']")
    NAME_GAME = (By.XPATH, "//*[@id='search_resultsRows']//div[@class='discount_final_price']")

    def __init__(self, driver):
        self.driver = driver

    def sort_list_game(self):
        """Сортируем список игр"""
        sort = WebDriverWait(self.driver, ResultPage.TIMEOUT_SHORT).until(
            ec.element_to_be_clickable(ResultPage.SORT_BUTTON))
        sort.click()
        sort_list = WebDriverWait(self.driver, ResultPage.TIMEOUT_SHORT).until(
            ec.element_to_be_clickable(ResultPage.LINK_DOWN_PRICE))
        sort_list.click()

    def get_results(self, expected_count) -> list:
        """Получаем отсортированный список цен на игры"""
        all_name_game = WebDriverWait(self.driver, ResultPage.TIMEOUT_SHORT).until(
            ec.presence_of_all_elements_located(ResultPage.NAME_GAME))
        list_name_game = [str(elem.text.replace("руб", "")) for elem in all_name_game[:expected_count]]
        result_list_name_game = [float(elem.replace(",", ".")) for elem in list_name_game]
        return result_list_name_game
