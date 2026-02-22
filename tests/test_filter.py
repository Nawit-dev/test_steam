import pytest
from pages.main_page import MainPage
from pages.results_page import ResultPage


@pytest.mark.parametrize("game_name, expected_count", [("The Witcher", 10), ("Fallout", 20)])
def test_filter(driver, game_name, expected_count):
    test_enter = MainPage(driver)
    test_enter.wait_for_open()
    test_enter.search_game(game_name)

    test_sort = ResultPage(driver)
    test_sort.sort_list_game()
    len_list = test_sort.get_results(expected_count)
    assert len(len_list) == expected_count, \
        f"Игра '{game_name}': ожидалось {expected_count} результатов, получено {len(len_list)}: {len_list}"
