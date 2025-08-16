from selenium.webdriver.common.by import By

class AccountPageLocators:
    BUTTON_HISTORY_ORDERS = (By.XPATH,
                             ".//*[text()='История заказов']")
    OPENED_HISTORY_ORDERS = (By.XPATH,
                             ".//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9'][text()='История заказов']")
    BUTTON_EXIT = (By.XPATH,
                             ".//*[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive'][text()='Выход']")

    NUMBER_ORDER = (By.XPATH,
                             ".//*[@class='text text_type_digits-default'][text()='#0280801']")
