import pytest
from pages.main_page import MainPage
from pages.result_page import ResultPage


@pytest.mark.parametrize(
    "game_name, expected_count",
    [("The Witcher", 10), ("Fallout", 20)],
    ids=["game 1", "game 2"]
)
def test_filter(browser, game_name, expected_count):
    for language in ["en", "ru"]:
        url = f"{browser.base_url}?l={language}"
        browser.driver.get(url)

        main_page = MainPage(browser.driver)
        main_page.wait_for_open()
        main_page.search_game(game_name)

        result_page = ResultPage(browser.driver)
        result_page.sort_list_game()
        games_price = result_page.get_results(expected_count)
        assert all(games_price[i] < games_price[i + 1] for i in range(len(games_price) - 1))
