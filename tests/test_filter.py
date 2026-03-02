import pytest
from pages.main_page import MainPage
from pages.result_page import ResultPage
from tests.language import Language


@pytest.mark.parametrize(
    "language",
    [Language.English, Language.Russian],
    ids=["english", "russian"]
)
@pytest.mark.parametrize(
    "game_name, expected_count",
    [("The Witcher", 10), ("Fallout", 20)],
    ids=["game 1", "game 2"]
)
def test_filter(browser, language, game_name, expected_count):
    url = f"{browser.base_url}?l={language}"
    browser.get_driver().get(url)

    main_page = MainPage()
    main_page.wait_for_open()
    main_page.search_game(game_name)

    result_page = ResultPage()
    result_page.sort_list_game()
    games_price = result_page.get_results(expected_count)
    assert games_price == sorted(games_price,
                                 reverse=True), \
        f'Актуальный результат {games_price}, ожидаемый результат {sorted(games_price, reverse=True)}'



