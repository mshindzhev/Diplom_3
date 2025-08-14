import allure

import data
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Тап на раздел личного кабинета")
    def tap_to_personal_account_section(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_to_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)