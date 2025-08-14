import allure

import data
from page_object.locators.forgot_password_page_locators import ForgotPasswordPageLocators
from page_object.pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step("Переход на страницу сброса пароля с введенным email")
    def go_to_password_reset_page(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.INPUT_EMAIL)
        self.add_text_to_element(ForgotPasswordPageLocators.INPUT_EMAIL, data.EMAIL)
        self.click_to_element(ForgotPasswordPageLocators.BUTTON_RESTORE)