from selenium.webdriver.common.by import By


class FeedPageLocators:
    COMPLETED_ALLTIME = (By.XPATH, "//*[text()='Выполнено за все время:']/../*[contains(@class,'OrderFeed_number')]")
    COMPLETED_TODAY = (By.XPATH, "//*[text()='Выполнено за сегодня:']/../*[contains(@class,'OrderFeed_number')]")
    ORDERS_AT_WORK = (By.XPATH, "//*[contains(@class,'OrderFeed_orderListReady')]/li")
