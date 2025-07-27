import allure
import pytest

from locators.feed_page_locators import FeedPageLocators
from pages.main_page import MainPage


class TestIncreaseCounter:
    @allure.title("Проверка увеличения счётчика ингредиента")
    @allure.description("Проверка увеличения счётчика при добавлении ингридиента в заказ")
    def test_increase_counter_by_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.check_increase_counter()

    @allure.title("Проверка увеличения счётчика при создании заказа")
    @allure.description(
        "Проверка увеличения счётчика «Выполнено за всё время» и «Выполнено за сегодня» при создании заказа")
    @pytest.mark.parametrize("counter", (FeedPageLocators.COMPLETED_ALLTIME, FeedPageLocators.COMPLETED_TODAY))
    def test_increase_counter_by_create_order(self, authorization, counter):
        main_page = MainPage(authorization)
        main_page.go_to_order_page()
        count = main_page.get_text_element(counter)
        main_page.create_order()
        main_page.close_the_order_window()
        main_page.go_to_order_page()
        new_count = main_page.get_text_element(counter)
        assert int(count) < int(new_count)
