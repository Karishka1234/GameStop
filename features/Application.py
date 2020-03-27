from pages.main_page import MainPage
from pages.sign_in_page import SignIn
from pages.shopping_page import ShoppingPage
from pages.results_page import ResultsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.shopping_page = ShoppingPage(self.driver)
        self.results_page = ResultsPage(self.driver)

