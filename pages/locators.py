from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    FORM_LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    TOTAL_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong") 
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") 
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") 


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")