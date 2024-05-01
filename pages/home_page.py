from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class HomePage(BasePage):
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
        header_order = self.driver.find_element(*HomePageLocators.HEADER_BUTTON_ORDER)
        header_order.click()

    @allure.step('Нажимаем на лого самоката')
    def click_scooter_logo(self):
        scooter_logo = self.driver.find_element(*HomePageLocators.HEADER_LOGO_SCOOTER)
        scooter_logo.click()

    @allure.step('Нажимаем на лого яндекса')
    def click_yandex_logo(self):
        yandex_logo = self.driver.find_element(*HomePageLocators.HEADER_LOGO_YANDEX)
        yandex_logo.click()

    @allure.step('Переходим на открывшееся новое окно')
    def switch_to_window(self):
        new_window = self.driver.switch_to.window(self.driver.window_handles[-1])
        return new_window
