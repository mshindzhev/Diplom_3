import allure
import pytest

import data
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.recovery_password_page import RecoveryPasswordPage


class TestResetPasswordPage:

    @pytest.mark.parametrize('locator',[
        LoginPageLocators.BUTTON_FORGOT_PASSWORD
    ])
    @allure.title('Открытие и отображение активного поля ввода для восстановления пароля')
    def test_password_recovery(self, driver, create_user, locator):
        with allure.step("Переход на станицу ввода Email для восстановления пароля"):
            recovery_password = RecoveryPasswordPage(driver)
            recovery_password.go_to_url(f'{data.URL_BASE}{data.URL_LOGIN}')
            recovery_password.scroll_to_element(locator)
            recovery_password.click_to_element(locator)

        with allure.step('Заполнить Email и перейти на страницу обновления пароля'):
            recovery_password.go_to_password_reset_page()

        with allure.step('Проверить активное поле пароля после тапа на кнопку скрытия пароля'):
            assert recovery_password.click_show_password_makes_field_active() == True

