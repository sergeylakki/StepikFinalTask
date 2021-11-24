from .base_page import BasePage


from .locators import LoginPageLocators

class LoginPage(BasePage):
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