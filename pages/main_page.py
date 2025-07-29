import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажать кнопку Заказать")
    def click_on_order(self, order):
        self.scroll_into_view(order)
        self.click_on_element(order)

    @allure.step("Проверка перехода по клику вкладки Конструктор")
    def check_go_to_page(self, locator_link, expected_link):
        self.click_on_element(locator_link)
        text_link = self.get_address_page()
        assert text_link == expected_link

    @allure.step("Проверка открытия деталей ингридиента")
    def check_open_details(self):
        self.click_on_element(MainPageLocators.SAUSE_SPICY)
        text_link = self.get_text_element(MainPageLocators.DETAILS_INGREDIENT)
        assert text_link == "Детали ингредиента"

    @allure.step("Проверка закрытия деталей ингридиентов по крестику")
    def check_closed_details(self):
        self.wait_for_element(MainPageLocators.SAUSE_SPICY)
        self.click_on_element(MainPageLocators.SAUSE_SPICY)
        self.wait_for_element(MainPageLocators.DETAILS_CLOSE)
        self.click_on_element(MainPageLocators.DETAILS_CLOSE)
        assert self.visible_element(MainPageLocators.SAUSE_SPICY) == True

    @allure.step("Проверка увеличения счётчика при добавлении ингредиента в заказ")
    def check_increase_counter(self):
        start_value = self.get_text_element(MainPageLocators.SPICY_COUNTER)
        self.drag_and_drop_element(MainPageLocators.SAUSE_SPICY, MainPageLocators.ORDER)
        end_value = self.get_text_element(MainPageLocators.SPICY_COUNTER)
        assert int(start_value) + 1 == int(end_value)

    @allure.step("Создание заказа")
    def create_order(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR)
        self.wait_for_element(MainPageLocators.BUN)
        self.drag_and_drop_element(MainPageLocators.BUN, MainPageLocators.ORDER)
        self.scroll_into_view(MainPageLocators.SAUSE_SPICY)
        self.drag_and_drop_element(MainPageLocators.SAUSE_SPICY, MainPageLocators.ORDER)
        self.click_on_element(MainPageLocators.CREATE_ORDER)
        self.wait_order_number()
        return self.get_text_element(MainPageLocators.NUMBER_ORDER)

    @allure.step("Переход на страницу заказов")
    def go_to_order_page(self):
        self.click_on_element(MainPageLocators.ORDER_HEAD)

    @allure.step("Закрыть окно заказа")
    def close_the_order_window(self):
        self.click_on_element(MainPageLocators.CLOSE_ORDER)
