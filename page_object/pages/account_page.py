import allure

from page_object.locators.account_page_locators import AccountPageLocators
from page_object.pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Тап на раздел личного кабинета")
    def open_order_history_section(self):
        self.find_element_with_wait(AccountPageLocators.BUTTON_HISTORY_ORDERS)
        self.click_to_element(AccountPageLocators.BUTTON_HISTORY_ORDERS)
        if self.find_element_with_wait(AccountPageLocators.OPENED_HISTORY_ORDERS):
            return True
        return False

    @allure.step("Тап на кнопку выхода из аккаунта")
    def tap_button_exit(self):
        self.find_element_with_wait(AccountPageLocators.BUTTON_EXIT)
        self.click_to_element(AccountPageLocators.BUTTON_EXIT)