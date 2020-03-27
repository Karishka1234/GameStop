from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    PRODUCT = (By.CSS_SELECTOR, 'input.search-field')
    ICON = (By.CSS_SELECTOR, 'div.input-group-append button[type="submit"]')
    ACC_ICON = (By.CSS_SELECTOR, "img.account")
    CART_ICON = (By.CSS_SELECTOR, "a.minicart-link img.shopping-cart")
    REVIEW = (By.CSS_SELECTOR, "button.bv-write-review")

    def review_link(self):
        self.click(*self.REVIEW)

    def icon_click(self):
        self.click(*self.ICON)

    def acc_click(self):
        self.click(*self.ACC_ICON)

    def cart_click(self):
        self.click(*self.CART_ICON)

    def open_url(self, url):
        self.open_page(url)

    def enter_text(self, text):
        self.input_text(text, *self.PRODUCT)




