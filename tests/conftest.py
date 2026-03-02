import pytest
from browser_singleton import Driver


@pytest.fixture(scope="function")
def browser(language) -> Driver:
    driver_instance = Driver(lang=language)
    yield driver_instance

    driver_instance.get_driver().quit()
    Driver._instances = {}
