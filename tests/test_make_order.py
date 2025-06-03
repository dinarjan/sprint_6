import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
import data


class TestMakeOrder:

    @allure.title('Проверка кнопки "Заказать" вверху страницы ')
    def test_upper_order_button(self,driver):
        main_page = MainPage(driver)
        main_page.open_link()
        main_page.click_upper_order_button()
        assert '/order' in data.order_page, 'Кнопка ведёт на другую страницу'

    @allure.title('Проверка кнопки "Заказать" внизу страницы ')
    def test_lower_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_link()
        main_page.click_lower_order_button()
        assert '/order' in data.order_page, 'Кнопка ведёт на другую страницу'

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize('customer', data.order_data)
    def test_make_order(self, driver, customer):
        id_num = customer["id"]

        main_page = MainPage(driver)
        main_page.open_link()
        main_page.click_upper_order_button()

        order_page = OrderPage(driver)
        order_page.set_name(id_num)
        order_page.set_surname(id_num)
        order_page.set_address(id_num)
        order_page.set_station(id_num)
        order_page.set_phone(id_num)
        order_page.click_next()
        order_page.set_deliver_date(id_num)
        order_page.set_time_limit_dropdown()
        order_page.set_color()
        order_page.click_submit_order()
        order_page.click_yes()
        order_page.wait_success_windows()
        order_page.click_view_status()
        order_page.click_logo_scooter()
        assert order_page.get_page() in data.main_page, 'Нажатие на логотип "Самоката" ведёт на другую страницу'
        order_page.click_logo_yandex()
        order_page.switch_window()
        assert order_page.get_page() in data.dzen_page, 'главная страница Дзен не открылась'
