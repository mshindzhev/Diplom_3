import allure

import data
from page_object.locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from page_object.pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):

    @allure.step("Переход на страницу сброса пароля с введенным email")
    def go_to_password_reset_page(self):
        self.find_element_with_wait(RecoveryPasswordPageLocators.INPUT_EMAIL)
        self.add_text_to_element(RecoveryPasswordPageLocators.INPUT_EMAIL, data.EMAIL)
        self.click_to_element(RecoveryPasswordPageLocators.BUTTON_RESTORE)

    def click_show_password_makes_field_active(self):
        self.click_to_element(RecoveryPasswordPageLocators.BUTTON_HIDE_PASSWORD)
        if self.find_element_with_wait(RecoveryPasswordPageLocators.INPUT_FOCUSED):
            return True
        return False