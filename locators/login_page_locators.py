from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.XPATH, "//input[contains(@type,'text')]")
    PASSWORD = (By.XPATH, "//input[contains(@type,'password')]")
    LOGIN = (By.XPATH, "//button[text()='Войти']")