from .base_page import BasePage
import pytest

from .locators import LoginPageLocators

class LoginPage(BasePage):

    
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.FORM_EMAIL_REGISTER)
        input_email.send_keys(email)
        input_password = self.browser.find_elements(*LoginPageLocators.FORM_PASSWORD_REGISTER)
        input_password[0].send_keys(password)
        input_password[1].send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.FORM_BUTTON_REGISTER)
        btn_reg.click()
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка на корректный url адрес
    def should_be_login_url(self):
        assert self.browser.current_url == self.url
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN_LINK)
        # реализуйте проверку, что есть форма логина
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER_LINK)
        # реализуйте проверку, что есть форма регистрации на странице