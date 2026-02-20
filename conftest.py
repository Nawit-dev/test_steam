import pytest
from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

LINK_SITE = "https://store.steampowered.com/"
UNIQUE_ELEMENT = (By.XPATH, "//*[@id='content_login']//a//span[contains(text(),'Войти')]")
TIMEOUT_SHORT = 10


@pytest.fixture()
def driver():
    driver_chrome = webdriver.Chrome()
    driver_chrome.get(LINK_SITE)
    WebDriverWait(driver_chrome, 10).until(ec.visibility_of_element_located(UNIQUE_ELEMENT))
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture()
def fake():
    fake = Faker("en_US")
    return fake
