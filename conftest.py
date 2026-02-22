import pytest
from selenium import webdriver
from locales import LOCALES


@pytest.fixture(params=["ru", "en"])
def driver(request):
    lang = request.param
    driver = webdriver.Chrome()

    driver.get(f"https://store.steampowered.com/?l={lang}")
    driver.locale = LOCALES[lang]
    yield driver
    driver.quit()
