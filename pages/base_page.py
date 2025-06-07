import data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step('Открываем страницу')
    def open_link(self):
        self.driver.get(data.main_page)

    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def find(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def add_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_page(self):
        return self.driver.current_url

    def switch_to_last_page(self):
        handles = self.driver.window_handles[-1]
        self.driver.switch_to.window(handles)

    def wait_about_blank(self):
        self.wait.until(lambda d: d.current_url != "about:blank")

    def wait_download_page(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
