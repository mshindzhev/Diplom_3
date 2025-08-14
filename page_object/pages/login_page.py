import allure

import data
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Переход на станицу восстановления пароля")
    def go_to_password_recovery_page(self):
        self.go_to_url(f'{data.URL_BASE}{data.URL_LOGIN}')
        self.scroll_to_element(LoginPageLocators.BUTTON_FORGOT_PASSWORD)
        self.click_to_element(LoginPageLocators.BUTTON_FORGOT_PASSWORD)