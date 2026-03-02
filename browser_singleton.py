from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.config_reader import ConfigReader


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(metaclass=Singleton):
    def __init__(self, lang="en-US"):
        self.config = ConfigReader.open_config()

        options = Options()
        if self.config["browser_options"].get("headless"):
            options.add_argument("--headless")
        if self.config["browser_options"].get("window_size"):
            options.add_argument(
                f'--window_size={self.config["browser_options"]["window_size"]}'
            )
        options.add_argument(f"--lang={lang}")
        options.add_experimental_option(
            "prefs",
            {"intl.accept_languages": lang}
        )

        self._driver = webdriver.Chrome(options=options)
        self.timeout = self.config["timeout"]
        self.base_url = f'{self.config["base_url"]}'

    def get_driver(self):
        return self._driver

    @classmethod
    def reset(cls):
        if cls in cls._instances:
            cls._instances[cls]._driver.quit()
            del cls._instances[cls]
