from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    BUTTON_HIDE_PASSWORD = (By.XPATH,
                            ".//*[@class='input__icon input__icon-action']//*[@xmlns='http://www.w3.org/2000/svg']")
    INPUT_FOCUSED = (By.XPATH,
                     ".//*[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused input__placeholder-filled'][text()='Пароль']")