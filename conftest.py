from selenium import webdriver
import pytest
from data import QaScooterData

@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    firefox_driver.get(QaScooterData.URL_SCOOTER)


    yield firefox_driver

    firefox_driver.quit()