from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import QaScooterData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class OrderPage(BasePage):
    name = (By.XPATH, "//input[@placeholder = '* Имя']")
    surname = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    adress = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    phone = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    metro = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    farther_button = (By.XPATH, "//button[text() = 'Далее']")
    select_station_1 = (By.XPATH, "//div[contains(text(), 'Боровицкая')]")
    select_station_2 = (By.XPATH, "//div[contains(text(), 'Черкизовская')]")
    cookie_button = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    header_button_order = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")
    down_button_order = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    date_order = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    day_order_1 = (By.XPATH, "//div[@aria-label = 'Choose среда, 1-е мая 2024 г.']")
    day_order_2 = (By.XPATH, "//div[@aria-label = 'Choose понедельник, 22-е апреля 2024 г.']")
    rental_period = (By.XPATH, "//div[@class = 'Dropdown-root']")
    rental_period_1 = (By.XPATH, "//div[@class='Dropdown-option'and text()='четверо суток']")
    rental_period_2 = (By.XPATH, "//div[@class='Dropdown-option'and text()='сутки']")
    scooter_color_1 = (By.XPATH, "//input[@id= 'black']")
    scooter_color_2 = (By.XPATH, "//input[@id= 'grey']")
    comment_courier = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")
    approval_button = (By.XPATH, "//button[text() = 'Да']")
    order_placed = (By.XPATH, "//div[text() = 'Заказ оформлен']")

    @allure.step('Принимаем куки')
    def click_cookie_button(self):
        cookie_button_click = self.driver.find_element(*self.cookie_button)
        cookie_button_click.click()

    @allure.step('Жмём кнопку заказа вверху страницы')
    def click_header_order(self):
        header_order = self.driver.find_element(*self.header_button_order)
        header_order.click()

    @allure.step('Жмём на нижнюю кнопку заказать')
    def click_down_button_order(self):
        down_order = self.driver.find_element(*self.down_button_order)
        down_order.click()

    @allure.step('Скроллим до нижней кнопки заказать')
    def scroll_down_order(self):
        element_2 = self.driver.find_element(*self.down_button_order)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_2)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")))

    @allure.step('Вводим имя')
    def input_name_1(self):
        name_1 = self.driver.find_element(*self.name)
        name_1.send_keys(QaScooterData.NAME_1)

    @allure.step('Вводим имя')
    def input_name_2(self):
        name_2 = self.driver.find_element(*self.name)
        name_2.send_keys(QaScooterData.NAME_2)

    @allure.step('Вводим фамилию')
    def input_surname_1(self):
        surname_1 = self.driver.find_element(*self.surname)
        surname_1.send_keys(QaScooterData.SURNAME_1)

    @allure.step('Вводим фамилию')
    def input_surname_2(self):
        surname_2 = self.driver.find_element(*self.surname)
        surname_2.send_keys(QaScooterData.SURNAME_2)

    @allure.step('Вводим адрес')
    def input_adress_1(self):
        adress_1 = self.driver.find_element(*self.adress)
        adress_1.send_keys(QaScooterData.ADRESS_1)

    @allure.step('Вводим адрес')
    def input_adress_2(self):
        adress_2 = self.driver.find_element(*self.adress)
        adress_2.send_keys(QaScooterData.ADRESS_2)

    @allure.step('Вводим номер телефона')
    def input_phone_1(self):
        phone_number_1 = self.driver.find_element(*self.phone)
        phone_number_1.send_keys(QaScooterData.PHONE)

    @allure.step('Вводим номер телефона')
    def input_phone_2(self):
        phone_number_2 = self.driver.find_element(*self.phone)
        phone_number_2.send_keys(QaScooterData.PHONE)

    @allure.step('Выбираем станцию метро Боровицкая')
    def select_metro_station_1(self):
        metro_station_1 = self.driver.find_element(*self.metro)
        metro_station_1.click()
        select_metro_1 = self.driver.find_element(*self.select_station_1)
        select_metro_1.click()

    @allure.step('Выбираем станцию метро Черкизовская')
    def select_metro_station_2(self):
        metro_station_2 = self.driver.find_element(*self.metro)
        metro_station_2.click()
        select_metro_2 = self.driver.find_element(*self.select_station_2)
        select_metro_2.click()

    @allure.step('Жмём кнопку далее')
    def click_farther_button(self):
        farther_button_click = self.driver.find_element(*self.farther_button)
        farther_button_click.click()

    @allure.step('Выбираем, когда привезти самокат')
    def select_date_order_1(self):
        date_1 = self.driver.find_element(*self.date_order)
        date_1.click()
        select_date_1 = self.driver.find_element(*self.day_order_1)
        select_date_1.click()

    @allure.step('Выбираем, когда привезти самокат')
    def select_date_order_2(self):
        date_2 = self.driver.find_element(*self.date_order)
        date_2.click()
        select_date_2 = self.driver.find_element(*self.day_order_2)
        select_date_2.click()

    @allure.step('Выбираем срок аренды')
    def select_rental_period_1(self):
        period_1 = self.driver.find_element(*self.rental_period)
        period_1.click()
        choose_period_1 = self.driver.find_element(*self.rental_period_1)
        choose_period_1.click()

    @allure.step('Выбираем срок аренды')
    def select_rental_period_2(self):
        period_2 = self.driver.find_element(*self.rental_period)
        period_2.click()
        choose_period_2 = self.driver.find_element(*self.rental_period_2)
        choose_period_2.click()

    @allure.step('Выбираем цвет самоката')
    def select_color_scooter_1(self):
        color_1 = self.driver.find_element(*self.scooter_color_1)
        color_1.click()

    @allure.step('Выбираем цвет самоката')
    def select_color_scooter_2(self):
        color_2 = self.driver.find_element(*self.scooter_color_2)
        color_2.click()

    @allure.step('Оставляем комментарий для курьера')
    def set_comment(self):
        comment = self.driver.find_element(*self.comment_courier)
        comment.send_keys('Привет курьер')

    @allure.step('Жмём кнопку заказать')
    def click_order_button(self):
        order_button = self.driver.find_element(*self.down_button_order)
        order_button.click()

    @allure.step('Нажимаем кнопку да')
    def click_approval_button(self):
        approval_button = self.driver.find_element(*self.approval_button)
        approval_button.click()

    @allure.step('Проверяем, что появилось всплывающее окно об успешном создании заказа')
    def check_order_placed(self):
        order_placed = self.driver.find_element(*self.order_placed)
        return order_placed.is_displayed()















