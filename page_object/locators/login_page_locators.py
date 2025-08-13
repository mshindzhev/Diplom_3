from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_FORGOT_PASSWORD = (By.XPATH,
                              ".//*[@href='/forgot-password']")