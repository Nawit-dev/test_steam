class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_type, value):
        """Найти элемент на стр"""
        return self.driver.find_element(locator_type, value)

    def click_element(self, locator_type, value):
        """Кликнуть на элемент на стр"""
        self.find_element(locator_type, value).click()

    def send_keys(self, locator_type, value, inf):
        """Подставить значение в найденное поле"""
        self.find_element(locator_type, value).send_keys(inf)
