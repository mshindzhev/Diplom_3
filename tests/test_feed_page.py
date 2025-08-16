import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait

import data
from page_object.locators.account_page_locators import AccountPageLocators
from page_object.locators.feed_page_locators import FeedPageLocators
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.account_page import AccountPage
from page_object.pages.feed_page import FeedPage
from page_object.pages.main_page import MainPage


class TestFeedPage:

    @pytest.mark.parametrize('locator',[
        MainPageLocators.BUTTON_ORDER_FEED
    ])
    @allure.title('Открытие деталей заказа')
    def test_open_order_details(self, driver, login_user, locator):

        with allure.step('Открыть ленту заказов'):
            feed_page = FeedPage(driver)
            feed_page.click_to_element(locator)
        with allure.step('Открыть детали заказа по тапу'):
            feed_page.find_element_with_wait(FeedPageLocators.ORDER_BURGER)
            feed_page.click_to_element(FeedPageLocators.ORDER_BURGER)
        with allure.step('Проверить отображение деталей заказа'):
            assert feed_page.find_element_with_wait(FeedPageLocators.DETAILS_BURGER)


    @allure.title('Отображение заказа из истории заказов в ленте заказов')
    def test_sync_orders_between_sections(self, driver, login_user):
        with allure.step('Открыть личный кабинет'):
            main_page = MainPage(driver)
            main_page.click_to_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        with allure.step('Перейти в раздел "История заказов" и запомнить номер заказа'):
            account_page = AccountPage(driver)
            account_page.click_to_element(AccountPageLocators.BUTTON_HISTORY_ORDERS)
            order_num_history = account_page.get_text_to_element(AccountPageLocators.NUMBER_ORDER)
        with allure.step('Перейти в раздел "Лента заказов" и проверить, что заказ из истории есть на странице'):
            main_page.click_to_element(MainPageLocators.BUTTON_ORDER_FEED)
            feed_page = FeedPage(driver)
            order_num_feed = feed_page.get_text_to_element(FeedPageLocators.NUMBER_ORDER)
            assert order_num_history == order_num_feed


    @allure.title('Отображение заказа в разделе "В работе"')
    def test_order_in_progress(self, driver, login_user):
        with allure.step('Открыть список "В работе" и убедиться, что он пуст'):
            main_page = MainPage(driver)
            feed_page = FeedPage(driver)
            main_page.click_to_element(MainPageLocators.BUTTON_ORDER_FEED)
            feed_page.not_find_element_on_page(FeedPageLocators.ORDER_IN_PROGRESS)
        with allure.step('Перейти на мэйн и создать заказ'):
            main_page.click_to_element(MainPageLocators.BUTTON_CONSTRUCTOR)
            main_page.assemble_burger_for_order()
            main_page.click_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
            main_page.find_element_with_wait(MainPageLocators.IDENTIFIER_ORDER)
            main_page.press_esc()
        with allure.step('Открыть список "В работе" и проверить, что теперь там появился заказ'):
            main_page.go_to_url(f'{data.URL_BASE}{data.URL_FEED}')
            feed_page.find_element_with_wait(FeedPageLocators.ORDER_IN_PROGRESS)

            assert feed_page.find_element_with_wait(FeedPageLocators.ORDER_IN_PROGRESS)


    @pytest.mark.parametrize('locator', [
        FeedPageLocators.COUNTER_ORDER_TODAY,
        FeedPageLocators.COUNTER_ORDER_ALL_TIME
    ])
    @allure.title('Проверка увеличения счетчиков заказов')
    def test_increase_count_orders(self, driver, login_user, locator):
        with allure.step('Открыть историю заказов и запомнить оттуда номер заказа'):
            main_page = MainPage(driver)
            feed_page = FeedPage(driver)
            main_page.click_to_element(MainPageLocators.BUTTON_ORDER_FEED)
            feed_page.scroll_to_element(locator)
            initial_counter = int(feed_page.get_text_to_element(locator))
        with allure.step('Открыть конструктор и создать заказ'):
            main_page.scroll_to_element(MainPageLocators.BUTTON_CONSTRUCTOR)
            main_page.click_to_element(MainPageLocators.BUTTON_CONSTRUCTOR)
            main_page.assemble_burger_for_order()
            main_page.click_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
            main_page.press_esc()
        with allure.step('Проверяем, что счетчик увеличился'):
            main_page.go_to_url(f'{data.URL_BASE}{data.URL_FEED}')

            # Ожидаем, пока счетчик увеличится
            def counter_increased(driver):
                current_counter = int(feed_page.get_text_to_element(locator))
                return current_counter == initial_counter + 1
            WebDriverWait(driver, 10).until(counter_increased)
            updated_counter = int(feed_page.get_text_to_element(locator))
            assert updated_counter == initial_counter + 1



