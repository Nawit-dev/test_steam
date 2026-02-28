import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(metaclass=Singleton):
    def __init__(self):
        with open("config.json") as f:
            config = json.load(f)

        options = Options()
        if config["browser_options"].get("headless"):
            options.add_argument("--headless")
        if config["browser_options"].get("window_size"):
            options.add_argument(
                f'--window_size={config["browser_options"]["window_size"]}'
            )
        self.driver = webdriver.Chrome(options=options)
        self.timeout = config["timeout"]
        self.base_url = f'{config["base_url"]}'
