from selenium.webdriver.common.by import By

class BasePageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    DOWN_BUTTON_ORDER = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    PRICE_QUESTION_BUTTON = (By.XPATH, "//div[@id = 'accordion__heading-0']")