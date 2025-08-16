import allure
import pytest

from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.account_page import AccountPage
from page_object.pages.main_page import MainPage


class TestAccountPage:

    @allure.title('Открытие и отображение раздела «История заказов»')
    def test_order_history_section(self, driver, login_user):

        with allure.step('Открыть личный кабинет'):
            main_page = MainPage(driver)
            main_page.tap_to_personal_account_section()

        with allure.step('Проверить открытие раздела «История заказов»'):
            account_page = AccountPage(driver)
            assert account_page.open_order_history_section() == True


    @pytest.mark.parametrize('locator', [
        LoginPageLocators.BUTTON_ENTER
    ])
    @allure.title('Проверка выхода из аккаунта')
    def test_order_history_section(self, driver, login_user, locator):
        with allure.step('Открыть личный кабинет'):
            main_page = MainPage(driver)
            main_page.tap_to_personal_account_section()

        with allure.step('Проверить выход из аккаунта'):
            account_page = AccountPage(driver)
            account_page.tap_button_exit()
            assert account_page.find_element_with_wait(locator)


