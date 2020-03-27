from pages.base_page import Page
from selenium.webdriver.common.by import By


class ShoppingPage(Page):
    TITLE = (By.CSS_SELECTOR, "div.col-12>h1")
    ICON = (By.CSS_SELECTOR, 'div.input-group-append button[type="submit"]')
    ADD_CART = (By.CSS_SELECTOR, "button.add-to-cart")
    CART_ICON = (By.CSS_SELECTOR, "img.shopping-cart.minicart-icon")
    CART_ITEM = (By.CSS_SELECTOR, "div.product-name")
    POPUP = (By.XPATH, "//button[contains(text(), '17 or older')]")
    QUANTITY = (By.CSS_SELECTOR, 'div.ml-1 img.ae-img')
    ITEMS = (By.CSS_SELECTOR, "span.number-of-home-delivery-items")


    def empty_cart(self, word):
        self.word_in_text(word, *self.TITLE)

    
    def to_cart(self):
        self.click(*self.ADD_CART)


    def popup(self):
        self.click(*self.POPUP)


    def cart(self):
        self.click(*self.CART_ICON)


    def quantity(self):
        self.click(*self.QUANTITY)


    def items_cart(self, amount):
        self.word_in_text(amount, *self.ITEMS)