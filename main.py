import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, login, password):
        self.driver = driver
        self.login = login
        self.password = password
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='global_action_menu']//a[@class='global_action_link']"))
        )

    def click_enter(self):
        """Переходим на форму входа"""
        try:
            enter_button = self.driver.find_element(By.XPATH,
                                                    "//*[@id='global_action_menu']//a[@class='global_action_link']")
            enter_button.click()
        except Exception as e:
            print('Не удалось кликнуть на кнопку Войти:', e)
            raise

    def enter_login(self):
        """Кликаем на поле с логином и вставляем логин"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='responsive_page_template_content']//div[@class='_3XCnc4SuTz8V8-jXVwkt_s']"))
            )
            login = self.driver.find_element(By.XPATH,
                                             "//*[@id='responsive_page_template_content']//input[@type='text']")
            login.click()
            login.send_keys(self.login)
        except Exception as e:
            print('Не удалось кликнуть на поле с  логином:', e)
            raise

    def enter_password(self):
        """Кликаем на поле с паролем и вставляем пароль"""
        try:
            password = self.driver.find_element(By.XPATH,
                                                "//*[@id='responsive_page_template_content']//input[@type='password']")
            password.click()
            password.send_keys(self.password)
        except Exception as e:
            print('Не удалось кликнуть на поле с паролем:', e)
            raise

    def click_sign_in(self):
        """Нажимаем на кнопку войти"""
        try:
            enter = self.driver.find_element(By.XPATH,
                                             "//*[@id='responsive_page_template_content']//button[@type='submit']")
            enter.click()
            time.sleep(3)
        except Exception as e:
            print('Не удалось кликнуть на кнопку войти:', e)
            raise

    def error_text(self):
        """Текст с ошибкой, если неправильно ввели пароль"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='responsive_page_template_content']//div[@class='_1W_6HXiG4JJ0By1qN_0fGZ']")))
        return element.text

    def form_login(self):
        """Вводим некорректные логин и пароль"""
        self.click_enter()
        self.enter_login()
        self.enter_password()
        self.click_sign_in()


driver_chrome = webdriver.Chrome()
driver_chrome.get("https://store.steampowered.com/")
test = LoginPage(driver_chrome, 'test', '32323')
test.form_login()
