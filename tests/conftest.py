import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import authorization_page, main_page
from data import DATA_LOGIN
from locators.login_page_locators import LoginPageLocators


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(main_page)
    yield driver
    driver.quit()


@pytest.fixture
def authorization(driver):
    driver.get(authorization_page)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL))
    driver.find_element(*LoginPageLocators.EMAIL).send_keys(DATA_LOGIN[0])
    driver.find_element(*LoginPageLocators.PASSWORD).send_keys(DATA_LOGIN[1])
    driver.find_element(*LoginPageLocators.LOGIN).click()
    return driver
