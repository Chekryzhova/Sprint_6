from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import QaScooterData
import allure

class OrderPage(BasePage):
    @allure.step('Жмём кнопку заказа вверху страницы')
    def click_header_order(self):
        header_order = self.driver.find_element(*OrderPageLocators.HEADER_BUTTON_ORDER)
        header_order.click()

    @allure.step('Жмём на нижнюю кнопку заказать')
    def click_down_button_order(self):
        down_order = self.driver.find_element(*OrderPageLocators.DOWN_BUTTON_ORDER)
        down_order.click()

    @allure.step('Вводим имя')
    def input_name_1(self):
        name_1 = self.driver.find_element(*OrderPageLocators.NAME)
        name_1.send_keys(QaScooterData.NAME_1)

    @allure.step('Вводим имя')
    def input_name_2(self):
        name_2 = self.driver.find_element(*OrderPageLocators.NAME)
        name_2.send_keys(QaScooterData.NAME_2)

    @allure.step('Вводим фамилию')
    def input_surname_1(self):
        surname_1 = self.driver.find_element(*OrderPageLocators.SURNAME)
        surname_1.send_keys(QaScooterData.SURNAME_1)

    @allure.step('Вводим фамилию')
    def input_surname_2(self):
        surname_2 = self.driver.find_element(*OrderPageLocators.SURNAME)
        surname_2.send_keys(QaScooterData.SURNAME_2)

    @allure.step('Вводим адрес')
    def input_adress_1(self):
        adress_1 = self.driver.find_element(*OrderPageLocators.ADRESS)
        adress_1.send_keys(QaScooterData.ADRESS_1)

    @allure.step('Вводим адрес')
    def input_adress_2(self):
        adress_2 = self.driver.find_element(*OrderPageLocators.ADRESS)
        adress_2.send_keys(QaScooterData.ADRESS_2)

    @allure.step('Вводим номер телефона')
    def input_phone_1(self):
        phone_number_1 = self.driver.find_element(*OrderPageLocators.PHONE)
        phone_number_1.send_keys(QaScooterData.PHONE)

    @allure.step('Вводим номер телефона')
    def input_phone_2(self):
        phone_number_2 = self.driver.find_element(*OrderPageLocators.PHONE)
        phone_number_2.send_keys(QaScooterData.PHONE)

    @allure.step('Выбираем станцию метро Боровицкая')
    def select_metro_station_1(self):
        metro_station_1 = self.driver.find_element(*OrderPageLocators.METRO)
        metro_station_1.click()
        select_metro_1 = self.driver.find_element(*OrderPageLocators.SELECT_STATION_1)
        select_metro_1.click()

    @allure.step('Выбираем станцию метро Черкизовская')
    def select_metro_station_2(self):
        metro_station_2 = self.driver.find_element(*OrderPageLocators.METRO)
        metro_station_2.click()
        select_metro_2 = self.driver.find_element(*OrderPageLocators.SELECT_STATION_2)
        select_metro_2.click()

    @allure.step('Жмём кнопку далее')
    def click_farther_button(self):
        farther_button_click = self.driver.find_element(*OrderPageLocators.FARTHER_BUTTON)
        farther_button_click.click()

    @allure.step('Выбираем, когда привезти самокат')
    def select_date_order_1(self):
        date_1 = self.driver.find_element(*OrderPageLocators.DATE_ORDER)
        date_1.click()
        select_date_1 = self.driver.find_element(*OrderPageLocators.DAY_ORDER_1)
        select_date_1.click()

    @allure.step('Выбираем, когда привезти самокат')
    def select_date_order_2(self):
        date_2 = self.driver.find_element(*OrderPageLocators.DATE_ORDER)
        date_2.click()
        select_date_2 = self.driver.find_element(*OrderPageLocators.DAY_ORDER_2)
        select_date_2.click()

    @allure.step('Выбираем срок аренды')
    def select_rental_period_1(self):
        period_1 = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD)
        period_1.click()
        choose_period_1 = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_1)
        choose_period_1.click()

    @allure.step('Выбираем срок аренды')
    def select_rental_period_2(self):
        period_2 = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD)
        period_2.click()
        choose_period_2 = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_2)
        choose_period_2.click()

    @allure.step('Выбираем цвет самоката')
    def select_color_scooter_1(self):
        color_1 = self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_1)
        color_1.click()

    @allure.step('Выбираем цвет самоката')
    def select_color_scooter_2(self):
        color_2 = self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_2)
        color_2.click()

    @allure.step('Оставляем комментарий для курьера')
    def set_comment(self):
        comment = self.driver.find_element(*OrderPageLocators.COMMENT_COURIER)
        comment.send_keys('Привет курьер')

    @allure.step('Жмём кнопку заказать')
    def click_order_button(self):
        order_button = self.driver.find_element(*OrderPageLocators.DOWN_BUTTON_ORDER)
        order_button.click()

    @allure.step('Нажимаем кнопку да')
    def click_approval_button(self):
        approval_button = self.driver.find_element(*OrderPageLocators.APPROVAL_BUTTON)
        approval_button.click()

    @allure.step('Проверяем, что появилось всплывающее окно об успешном создании заказа')
    def check_order_placed(self):
        order_placed = self.driver.find_element(*OrderPageLocators.ORDER_PLACED)
        return order_placed.is_displayed()















