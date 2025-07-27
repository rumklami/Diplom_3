from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = (By.XPATH, "//*[text()='Конструктор']")
    ORDER_HEAD = (By.XPATH, "//*[contains(text(),'Лента Заказов')]/..")

    SAUSE_SPICY = (By.XPATH, "//*[contains(@alt,'Соус Spicy-X')]/..")
    DETAILS_INGREDIENT = (By.XPATH, "//*[text()='Детали ингредиента']")
    DETAILS_CLOSE = (By.XPATH, "//*[contains(@class,'Modal_modal__close')]")
    SPICY_COUNTER = (By.XPATH, "//*[contains(@alt,'Соус Spicy-X')]/..//p[contains(@class,'counter_counter')]")
    ORDER = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")

    BUN = (By.XPATH, "//*[contains(text(),'Краторная булка N-200i')]/..")
    CREATE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    NUMBER_ORDER = (By.XPATH, "//*[contains(@class,'Modal_modal__title_shadow')]")
    CLOSE_ORDER = (By.XPATH, "//*[contains(@class,'Modal_modal__close')]")
