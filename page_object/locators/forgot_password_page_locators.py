from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    BUTTON_RESTORE = (By.XPATH,
                      ".//button[text()='Восстановить']")
    INPUT_EMAIL = (By.XPATH,
                   ".//*[@class='text input__textfield text_type_main-default']")