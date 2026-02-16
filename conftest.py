import pytest
from selenium import webdriver
from faker import Faker

LINK_SITE = "https://store.steampowered.com/"


@pytest.fixture()
def driver():
    driver_chrome = webdriver.Chrome()
    driver_chrome.get(LINK_SITE)
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture()
def fake():
    fake = Faker("en_US")
    return fake
