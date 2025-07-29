import pytest
from selenium import webdriver

from curl import authorization_page, main_page
from data import DATA_LOGIN
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


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
    base_page = BasePage(driver)
    driver.get(authorization_page)
    base_page.wait_for_element(LoginPageLocators.EMAIL)
    base_page.send_keys_to_element(LoginPageLocators.EMAIL, DATA_LOGIN[0])
    base_page.send_keys_to_element(LoginPageLocators.PASSWORD, DATA_LOGIN[1])
    base_page.click_on_element(LoginPageLocators.LOGIN)
    return driver
