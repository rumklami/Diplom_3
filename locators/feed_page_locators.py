from selenium.webdriver.common.by import By


class FeedPageLocators:
    COMPLETED_ALLTIME = (By.XPATH, "//*[text()='Выполнено за все время:']/../p[2]")
    COMPLETED_TODAY = (By.XPATH, "//*[text()='Выполнено за сегодня:']/../p[2]")
    ORDERS_AT_WORK = (By.XPATH, "//*[contains(@class,'OrderFeed_orderListReady')]/li")
