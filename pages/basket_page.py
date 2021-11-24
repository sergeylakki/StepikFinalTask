from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException 
import math
import time


class BasketPage(BasePage):
    
    #Ожидаем, что в корзине нет товаров
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT)
    
    
    #Ожидаем сообщение о пустой корзине  
    def should_be_message_basket_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text 
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
      
    
    def should_be_alert_message(self, name):
        alert = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE).text
        text = f"{name} has been added to your basket."
        assert text == alert
    
    def should_be_total_price(self, price):
        alert = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET).text
        assert price == alert
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_MESSAGE)
    
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_MESSAGE)
    
    def add_to_basket(self):
        self.product_name = self.get_product_name()
        self.product_price = self.get_product_price()
        btn_add_to_cart = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_cart.click()
        self.pass_captcha()
        
        
    def pass_captcha(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")        
            alert.accept()     
        except NoAlertPresentException:
            print("No second alert presented")
    
    
    def should_be_add_product_to_basket(self):
        #time.sleep(30)  
        self.add_to_basket()        
        self.should_be_alert_message(self.product_name)
        self.should_be_total_price(self.product_price)     
   
    
    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)
    