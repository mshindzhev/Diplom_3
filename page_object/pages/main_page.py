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
        self.find_element_with_wait(MainPageLocators.INGREDIENT_BREAD)
        self.click_to_element(MainPageLocators.INGREDIENT_BREAD)
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

    @allure.step("Перемещение ингредиента в конструктор")
    def move_ingredients_to_constructor(self, element_from, element_to):
        self.find_element_with_wait(element_from)
        self.scroll_to_element(element_from)
        self.find_element_with_wait_on_page(element_to)
        self.drag_and_drop_element(element_from, element_to)

    @allure.step("Собрать бургер в конструктор")
    def assemble_burger_for_order(self):
        self.move_ingredients_to_constructor(MainPageLocators.INGREDIENT_BREAD, MainPageLocators.LIST_INGREDIENTS_BURGER_CONSTRUCTOR)
        self.move_ingredients_to_constructor(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.LIST_INGREDIENTS_BURGER_CONSTRUCTOR)
        self.move_ingredients_to_constructor(MainPageLocators.INGREDIENT_TOPPING, MainPageLocators.LIST_INGREDIENTS_BURGER_CONSTRUCTOR)