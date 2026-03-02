import json


class ConfigReader:

    @staticmethod
    def open_config():
        with open("config.json") as f:
            config = json.load(f)
        return config
