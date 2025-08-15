import allure

import data
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Тап на раздел личного кабинета")
    def tap_to_personal_account_section(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_to_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step("Открытие деталей ингредиента")
    def open_details_ingredient(self):
        self.go_to_url(data.URL_BASE)
        self.find_element_with_wait(MainPageLocators.INGREDIENT)
        self.click_to_element(MainPageLocators.INGREDIENT)
        if self.find_element_with_wait(MainPageLocators.HEADER_DETAILS_INGREDIENT):
            return True
        return False

    @allure.step("Открытие деталей ингредиента")
    def close_details_ingredient(self):
        self.open_details_ingredient()
        self.click_to_element(MainPageLocators.BUTTON_CLOSE_MODAL_INGREDIENT)
        if self.find_element_with_wait(MainPageLocators.HEADER_ASSEMBLE_BURGER):
            return True
        return False