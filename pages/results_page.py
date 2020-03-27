from pages.base_page import Page
from selenium.webdriver.common.by import By


class ResultsPage(Page):
    TITLE = (By.CSS_SELECTOR, 'h1.search-title')
    PRODUCT = (By.CSS_SELECTOR, "div.product-tile-header a.h5")
    ICON = (By.CSS_SELECTOR, 'div.input-group-append button[type="submit"]')


    def choose_products(self):
        self.click(*self.ICON)
        self.click(*self.PRODUCT)