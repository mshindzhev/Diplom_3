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
    def test_switch_between_main_and_orders(self, driver, create_user, login_user, url, locator, expected_locator):

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