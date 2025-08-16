import allure
import pytest

import data
from page_object.locators.feed_page_locators import FeedPageLocators
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize('url, locator, expected_locator', [
        [f'{data.URL_BASE}', MainPageLocators.BUTTON_ORDER_FEED, FeedPageLocators.HEADER_ASSEMBLE_BURGER],
        [f'{data.URL_BASE}{data.URL_FEED}', MainPageLocators.BUTTON_CONSTRUCTOR, MainPageLocators.HEADER_MAIN_PAGE]
    ])
    @allure.title('Проверка переходов между разделами главной страницы и заказов')
    def test_switch_between_main_and_orders(self, driver, login_user, url, locator, expected_locator):

        with allure.step('Проверить переход на раздел'):
            main_page = MainPage(driver)
            main_page.go_to_url(url)
            main_page.click_to_element(locator)

        with allure.step('Проверить открытие раздела'):
            assert main_page.find_element_with_wait(expected_locator)

    @allure.title('Отображение деталей ингредиента')
    def test_show_details_ingredient(self, driver):

        with allure.step('Проверить открытие деталей ингредиента'):
            main_page = MainPage(driver)
            assert main_page.open_details_ingredient() == True

    @allure.title('Закрытие окна с деталями ингредиента по крестику')
    def test_close_details_ingredient(self, driver):
        with allure.step('Проверить закрытие деталей ингредиента'):
            main_page = MainPage(driver)
            assert main_page.close_details_ingredient() == True

    @pytest.mark.parametrize('element_from, element_to, element_counter, expect_count', [
        [MainPageLocators.INGREDIENT_BREAD, MainPageLocators.LIST_INGREDIENTS_BURGER_CONSTRUCTOR, MainPageLocators.COUNTER_INGREDIENT_BREAD, '2'],
        [MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.LIST_INGREDIENTS_BURGER_CONSTRUCTOR, MainPageLocators.COUNTER_INGREDIENT_SAUCE, '1'],
        [MainPageLocators.INGREDIENT_TOPPING, MainPageLocators.LIST_INGREDIENTS_BURGER_CONSTRUCTOR, MainPageLocators.COUNTER_INGREDIENT_TOPPING, '1']
    ])
    @allure.title('Увеличение счетчика ингредиента')
    def test_increase_counter_ingredients(self, driver, login_user, element_from, element_to, element_counter, expect_count):
        with allure.step('Перетащить ингредиент в конструктор'):
            main_page = MainPage(driver)
            main_page.move_ingredients_to_constructor(element_from, element_to)
        with allure.step('Проверить счетчик у ингредиента'):
            main_page.find_element_with_wait(element_counter)
            assert main_page.get_text_to_element(element_counter) == expect_count

    @allure.title('Проверка создания заказа')
    def test_create_order(self, driver, login_user):
        with allure.step('Собрать ингредиенты в конструктор'):
            main_page = MainPage(driver)
            main_page.assemble_burger_for_order()
        with allure.step('Тап на кнопку создания заказа'):
            main_page.click_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
        with allure.step('Проверить, что отображается ID созданного заказа'):
            assert main_page.find_element_with_wait(MainPageLocators.IDENTIFIER_ORDER)