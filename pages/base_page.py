from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class BasePage:
    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принимаем куки')
    def click_cookie_button(self):
        cookie_button = self.driver.find_element(*BasePageLocators.COOKIE_BUTTON)
        cookie_button.click()

    @allure.step('Скроллим до нижней кнопки заказать')
    def scroll_down_order(self):
        element_2 = self.driver.find_element(*BasePageLocators.DOWN_BUTTON_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_2)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")))

    @allure.step('Скролим до появления вопросов и ждём, когда вопросы будут кликабельными')
    def scroll_down_question(self, index):
        element_1 = self.driver.find_element(*BasePageLocators.PRICE_QUESTION_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_1)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[@id = 'accordion__heading-{index}']")))



