from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ResultPage:
    TIMEOUT_SHORT = 10

    def __init__(self, driver):
        self.driver = driver

    def sort_list_game(self):
        drop_down_sort = (By.XPATH, self.driver.locale['sort_button'])
        sort = WebDriverWait(self.driver, ResultPage.TIMEOUT_SHORT).until(ec.element_to_be_clickable(drop_down_sort))
        sort.click()

        sort_by_lists = (By.XPATH, self.driver.locale['link_down_price'])
        sort_list = WebDriverWait(self.driver, ResultPage.TIMEOUT_SHORT).until(
            ec.element_to_be_clickable(sort_by_lists))
        sort_list.click()

    def get_results(self, expected_count):
        name_game = (By.XPATH, "//*[@id='search_resultsRows']//span[@class='title']")
        all_name_game = WebDriverWait(self.driver, ResultPage.TIMEOUT_SHORT).until(
            ec.presence_of_all_elements_located(name_game))
        list_name_game = [elem.text for elem in all_name_game[:expected_count]]
        return list_name_game
