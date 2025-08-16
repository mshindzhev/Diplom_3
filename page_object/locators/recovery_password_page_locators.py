from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    BUTTON_HIDE_PASSWORD = (By.XPATH,
                            ".//*[@class='input__icon input__icon-action']//*[@xmlns='http://www.w3.org/2000/svg']")
    INPUT_FOCUSED = (By.XPATH,
                     ".//*[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    BUTTON_RESTORE = (By.XPATH,
                      ".//button[text()='Восстановить']")
    INPUT_EMAIL = (By.XPATH,
                   ".//*[@class='text input__textfield text_type_main-default']")

