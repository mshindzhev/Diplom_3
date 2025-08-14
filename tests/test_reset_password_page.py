import allure

from page_object.pages.recovery_password_page import RecoveryPasswordPage


class TestResetPasswordPage:

    @allure.title('Открытие и отображение активного поля ввода для восстановления пароля')
    def test_password_recovery(self, driver, create_user):
        with allure.step('Тап "Восстановить пароль"'):
            recovery_password = RecoveryPasswordPage(driver)
            recovery_password.go_to_password_recovery_page()

        with allure.step('Заполнить Email и перейти на страницу обновления пароля'):
            recovery_password.go_to_password_reset_page()

        with allure.step('Проверить активное поле пароля после тапа на кнопку скрытия пароля'):
            assert recovery_password.click_show_password_makes_field_active() == True

