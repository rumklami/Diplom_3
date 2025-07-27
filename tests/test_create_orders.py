import allure

from locators.feed_page_locators import FeedPageLocators
from pages.main_page import MainPage


class TestCreateOrders:
    @allure.title("Проверка появления номера заказа")
    @allure.description("Проверка появления номера заказа в поле В работе на странице заказов")
    def test_get_order_number(self, authorization):
        main_page = MainPage(authorization)
        order_number = main_page.create_order()
        main_page.close_the_order_window()
        main_page.go_to_order_page()
        assert order_number in main_page.get_text_element(FeedPageLocators.ORDERS_AT_WORK)
