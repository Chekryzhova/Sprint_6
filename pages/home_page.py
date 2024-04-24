from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class HomePage(BasePage):

    PRICE_QUESTION_BUTTON = (By.XPATH, "//div[@id = 'accordion__heading-0']")
    PRICE_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-0']")
    SEVERAL_SCOOTER_QUESTION_BUTTON = (By.XPATH, "//div[@id = 'accordion__heading-1']")
    SEVERAL_SCOOTER_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-1']")
    RENTAL_TIME_QUESTION = (By.XPATH, "//div[@id = 'accordion__heading-2']")
    RENTAL_TIME_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-2']")
    ORDER_TODAY_QUESTION = (By.XPATH, "//div[@id = 'accordion__heading-3']")
    ORDER_TODAY_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-3']")
    EXTEND_RENTAL_QUESTION = (By.XPATH, "//div[@id = 'accordion__heading-4']")
    EXTEND_RENTAL_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-4']")
    CHARGING_QUESTION = (By.XPATH, "//div[@id = 'accordion__heading-5']")
    CHARGING_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-5']")
    CANCEL_ORDER_QUESTION = (By.XPATH, "//div[@id = 'accordion__heading-6']")
    CANCEL_ORDER_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-6']")
    MOSCOW_RING_ROAD_QUESTION = (By.XPATH, "//div[@id = 'accordion__heading-7']")
    MOSCOW_RING_ROAD_ANSWER = (By.XPATH, "//div[@id = 'accordion__panel-7']")
    COOKIE_BUTTON = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    header_logo_scooter = (By.XPATH, "//a[@class = 'Header_LogoScooter__3lsAR']")
    header_logo_yandex = (By.XPATH, "//a[@class = 'Header_LogoYandex__3TSOI']")
    header_button_order = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")

    @allure.step('Принимаем куки')
    def click_cookie_button(self):
        cookie_button = self.driver.find_element(*self.COOKIE_BUTTON)
        cookie_button.click()

    @allure.step('Скролим до появления вопросов и ждём, когда вопросы будут кликабельными')
    def scroll_down_question(self,index):
        element_1 = self.driver.find_element(*self.PRICE_QUESTION_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_1)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[@id = 'accordion__heading-{index}']")))

    @allure.step('Ждём появления ответов')
    def wait_element(self, index):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, f"//div[@id = 'accordion__panel-{index}']")))

    @allure.step('Кликаем вопросы и получаем ответы')
    def click_questions(self, index):
        question = (By.XPATH, f"//div[@id = 'accordion__heading-{index}']")
        answer = (By.XPATH, f"//div[@id = 'accordion__panel-{index}']")
        self.driver.find_element(*question).click()
        self.wait_element(index)
        return self.driver.find_element(*answer).text

    @allure.step('Нажимаем кнопку заказать вверху страницы')
    def click_header_order(self):
        header_order = self.driver.find_element(*self.header_button_order)
        header_order.click()

    @allure.step('Нажимаем на лого самоката')
    def click_scooter_logo(self):
        scooter_logo = self.driver.find_element(*self.header_logo_scooter)
        scooter_logo.click()

    @allure.step('Нажимаем на лого яндекса')
    def click_yandex_logo(self):
        yandex_logo = self.driver.find_element(*self.header_logo_yandex)
        yandex_logo.click()

    @allure.step('Переходим на открывшееся новое окно')
    def switch_to_window(self):
        new_window = self.driver.switch_to.window(self.driver.window_handles[-1])
        return new_window
