from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    FORM_LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")
    FORM_EMAIL_REGISTER = (By.CSS_SELECTOR, "#register_form input[type='email']")
    FORM_PASSWORD_REGISTER = (By.CSS_SELECTOR, "#register_form input[type='password']")
    FORM_BUTTON_REGISTER = (By.CSS_SELECTOR,"button[name='registration_submit']")
    FORM_REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    TOTAL_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong") 
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") 
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") 


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    


class BasketPageLocators():
    BASKET_MESSAGE = (By.CSS_SELECTOR, ".content p")
    BASKET_PRODUCT = (By.CSS_SELECTOR, ".basket_summary")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")