import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


#Класс для проверки может ли авторизированый пользователь добавлять товары
#@pytest.mark.test_user
class TestUserAddToBasketFromProductPage():
    
    #Фикстура настроек регистрации пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser,"http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        self.login_page.open()
        email = str(time.time()) + "@fakemail.org"
        self.login_page.register_new_user(email, "sergey_my_007")
        self.login_page.should_be_authorized_user()
    
    
    #Проверка не видит ли пользователь сообщения об успешном добавлении на главной странице
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
        page.open()
        page.should_not_be_success_message()
    
    # Может ли зарегестрированый пользователь добавлять товары в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
        page.open()
        page.should_be_add_product_to_basket()




def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks = pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    #page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    #page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    
  
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
    page.open()
    page.add_to_basket()  
    page.should_not_be_success_message()
    
    
@pytest.mark.xfail(reason="fixing this bug right now")    
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()
   
   
#гость может перейти на страницу логина со страницы продукта
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    

    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product()
    basket_page.should_be_message_basket_empty()
