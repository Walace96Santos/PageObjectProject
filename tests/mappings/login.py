from selenium.webdriver.common.by import By


class LoginMapping:
    TITLE_LABEL = (By.XPATH, '//*[@class="login_logo"]')
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//*[@class="error-message-container error"]')
