from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_FORGOT_PASSWORD = (By.XPATH,
                              ".//*[text()='Восстановить пароль']")
    INPUT_EMAIL = (By.XPATH,
                              ".//*[@class='text input__textfield text_type_main-default'][@name='name']")
    INPUT_PASSWORD = (By.XPATH,
                              ".//*[@class='text input__textfield text_type_main-default'][@name='Пароль']")
    BUTTON_ENTER = (By.XPATH,
                      ".//*[text()='Войти']")