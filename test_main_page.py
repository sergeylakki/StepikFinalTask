from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_should_see_to_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.skip(reason="no way of currently testing this")    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

#def test_guest_should_see_login_and_register_form(browser):  
#    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
#    page.open()
#    page.should_be_login_page()

