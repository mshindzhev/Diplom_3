import allure

from page_object.pages.account_page import AccountPage
from page_object.pages.main_page import MainPage


class TestAccountPage:

    @allure.title('Открытие и отображение раздела «История заказов»')
    def test_order_history_section(self, driver, create_user, login_user):

        with allure.step('Открыть личный кабинет'):
            main_page = MainPage(driver)
            main_page.tap_to_personal_account_section()

        with allure.step('Проверить открытие раздела «История заказов»'):
            account_page = AccountPage(driver)
            assert account_page.open_order_history_section() == True


