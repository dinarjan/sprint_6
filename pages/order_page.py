import allure
from selenium.webdriver.common.keys import Keys
from locators.order_locators import OrderLocators
from data import order_data
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим имя')
    def set_name(self, id_num):
        self.add_text(OrderLocators.NAME, order_data[id_num]['name'])

    @allure.step('Вводим фамилию')
    def set_surname(self, id_num):
        self.add_text(OrderLocators.SURNAME, order_data[id_num]['surname'])

    @allure.step('Вводим адрес')
    def set_address(self, id_num):
        self.add_text(OrderLocators.ADDRESS, order_data[id_num]['address'])

    @allure.step('Вводим станцию метро')
    def set_station(self, id_num):
        self.add_text(OrderLocators.STATION, order_data[id_num]['station'])
        self.add_text(OrderLocators.STATION, Keys.DOWN)
        self.add_text(OrderLocators.STATION, Keys.ENTER)

    @allure.step('Вводим номер телефона')
    def set_phone(self, id_num):
        self.add_text(OrderLocators.PHONE_NUMBER, order_data[id_num]['phone_number'])

    @allure.step('Проходим далее')
    def click_next(self):
        self.click(OrderLocators.NEXT)

    @allure.step('Выбираем дату для доставки самоката')
    def set_deliver_date(self, id_num):
        self.add_text(OrderLocators.DELIVER_DATE, order_data[id_num]['rental_period'])
        self.add_text(OrderLocators.DELIVER_DATE, Keys.DOWN)
        self.add_text(OrderLocators.DELIVER_DATE, Keys.ENTER)

    @allure.step('Выбираем срок аренды')
    def set_time_limit_dropdown(self):
        self.click(OrderLocators.TIME_LIMIT)
        self.click(OrderLocators.TIME_LIMIT_DROPDOWN)

    @allure.step('Выбираем цвет самоката')
    def set_color(self):
        self.click(OrderLocators.COLOR)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_submit_order(self):
        self.click(OrderLocators.SUBMIT_ORDER)

    @allure.step('Соглашаемся с оформлением заказа')
    def click_yes(self):
        self.click(OrderLocators.YES)

    @allure.step('Появляется окно об успешном оформлении заказа')
    def wait_success_windows(self):
        self.click(OrderLocators.SUCCESS_WINDOW)

    @allure.step('Нажимаем на кнопку "Просмотреть статус"')
    def click_view_status(self):
        self.click(OrderLocators.VIEW_STATUS)

    @allure.step('По клику на лого "Самоката" переходим на главную страницу "Самоката"')
    def click_logo_scooter(self):
        self.click(OrderLocators.LOGO_SCOOTER)

    @allure.step('Нажимаем на лого "Яндекс"')
    def click_logo_yandex(self):
        self.click(OrderLocators.LOGO_YANDEX)

    def get_current_page(self):
        self.get_page()

    @allure.step('Переходим на главную страницу Дзен')
    def switch_window(self):
        self.switch_to_last_page()
        self.wait_about_blank()
        self.wait_download_page(OrderLocators.YANDEX_POP_UP)
