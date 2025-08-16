import allure

import data
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.base_page import BasePage


class LoginPage(BasePage):



    @allure.step("Логин пользователя")
    def login(self):
        self.go_to_url(f'{data.URL_BASE}{data.URL_LOGIN}')
        self.add_text_to_element(LoginPageLocators.INPUT_EMAIL, data.EMAIL)
        self.add_text_to_element(LoginPageLocators.INPUT_PASSWORD, data.PASSWORD)
        self.click_to_element(LoginPageLocators.BUTTON_ENTER)

