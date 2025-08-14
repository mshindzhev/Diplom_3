import data
from page_object.locators.forgot_password_page_locators import ForgotPasswordPageLocators
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators
from page_object.pages.forgot_password_page import ForgotPasswordPage
from page_object.pages.login_page import LoginPage
from page_object.pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:

    def test_password_recovery(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.go_to_password_recovery_page()


        forgot_password = ForgotPasswordPage(driver)
        forgot_password.go_to_password_reset_page()

        reset_password = ResetPasswordPage(driver)
        reset_password.click_to_element(ResetPasswordPageLocators.BUTTON_HIDE_PASSWORD)
        assert reset_password.find_element_with_wait(ResetPasswordPageLocators.INPUT_FOCUSED)
