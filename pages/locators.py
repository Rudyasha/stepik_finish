from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL= (By.NAME, "registration-email")
    REGISTRATION_PAS1= (By.NAME, "registration-password1")
    REGISTRATION_PAS2= (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT= (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main >.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main >h1")

    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert.alert-info >.alertinner strong")
    MESSAGE_PRODUCT = (By.CSS_SELECTOR, ".alert.alert-success >.alertinner >strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success >.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET=(By.CSS_SELECTOR,".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT = (By.CSS_SELECTOR, "#content_inner h2.col-sm-6")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
