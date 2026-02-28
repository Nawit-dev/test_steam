import pytest
from browser_singleton import Driver


@pytest.fixture(scope="function")
def browser() -> Driver:
    driver_instance = Driver()
    yield driver_instance

    driver_instance.driver.quit()
    Driver._instances = {}
