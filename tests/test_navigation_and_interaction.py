import allure
import pytest

from curl import main_page, feed_page
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestNavigationAndInteraction:
    @allure.title("Проверка навигации")
    @allure.description("Проверка перехода по клику на вкладку Конструктор и на раздел Лента заказов")
    @pytest.mark.parametrize("locator, expected_link",
                             ([MainPageLocators.CONSTRUCTOR, main_page], [MainPageLocators.ORDER_HEAD, feed_page]))
    def test_go_to_constructor(self, driver, locator, expected_link):
        main_page = MainPage(driver)
        main_page.check_go_to_page(locator, expected_link)

    @allure.title("Проверка деталей ингредиента")
    @allure.description("Проверка открытия деталей ингредиента по клику на ингредиент")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.check_open_details()

    @allure.title("Проверка закрытия деталей ингридиента")
    @allure.description("Проверка закрытия деталей ингридиента при нажатии по крестику")
    def test_closed_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.check_closed_details()
