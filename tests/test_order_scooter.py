import time
import allure
from pages.order_page import OrderPage
from pages.home_page import HomePage
from conftest import driver
from data import QaScooterData


class TestOrderScooter:
    @allure.description('Проверяем заказ самоката по первому сценарию, через вкрхнюю кнопку заказать')
    @allure.title('Заказ самоката по первому сценарию')
    def test_order_scooter_flow_1(self, driver):
        order_page_1 = OrderPage(driver)
        order_page_1.click_cookie_button()
        order_page_1.click_header_order()
        order_page_1.input_name_1()
        order_page_1.input_surname_1()
        order_page_1.input_adress_1()
        order_page_1.select_metro_station_1()
        order_page_1.input_phone_1()
        order_page_1.click_farther_button()
        order_page_1.select_date_order_1()
        order_page_1.select_rental_period_1()
        order_page_1.select_color_scooter_1()
        order_page_1.set_comment()
        order_page_1.click_order_button()
        order_page_1.click_approval_button()

        assert order_page_1.check_order_placed()

    @allure.description('Проверяем заказ самоката по второму сценарию, через нижнюю кнопку заказать')
    @allure.title('Заказ самоката по второму сценарию')
    def test_order_scooter_flow_2(self, driver):
        order_page_2 = OrderPage(driver)
        order_page_2.click_cookie_button()
        order_page_2.scroll_down_order()
        order_page_2.click_down_button_order()
        order_page_2.input_name_2()
        order_page_2.input_surname_2()
        order_page_2.input_adress_2()
        order_page_2.select_metro_station_2()
        order_page_2.input_phone_2()
        order_page_2.click_farther_button()
        order_page_2.select_date_order_2()
        order_page_2.select_rental_period_2()
        order_page_2.select_color_scooter_2()
        order_page_2.click_order_button()
        order_page_2.click_approval_button()

        assert order_page_2.check_order_placed()

    @allure.description('Проверяем, если нажать на логотип самоката, попадаем на главную страницу самоката')
    @allure.title('Проверка лого самоката')
    def test_click_scooter_logo(self, driver):
        scooter_logo = HomePage(driver)
        scooter_logo.click_cookie_button()
        scooter_logo.click_header_order()
        scooter_logo.click_scooter_logo()

        assert driver.current_url == QaScooterData.URL_SCOOTER

    @allure.description('Проверяем, если нажать на лого яндекса, то в новом окне откроется Дзен')
    @allure.title('Проверка лого Яндекса')
    def test_click_yandex_logo(self, driver):
        yandex_logo = HomePage(driver)
        yandex_logo.click_cookie_button()
        yandex_logo.click_yandex_logo()
        time.sleep(3)
        yandex_logo.switch_to_window()
        time.sleep(3)


        assert driver.current_url == QaScooterData.URL_DZEN



