from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    BUTTON_RESTORE = (By.XPATH,
                      ".//button[text()='Восстановить']")
    INPUT_EMAIL = (By.XPATH,
                   ".//label[@class='input__placeholder text noselect text_type_main-default'][text()='Email']")