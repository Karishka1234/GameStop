from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignIn(Page):
    ACC_BUTTON = (By.XPATH, "//h2[contains(text(), 'Create Account')]")
    FNAME = (By.ID, 'registration-form-fname')
    LNAME = (By.ID, 'registration-form-lname')
    EMAIL = (By.ID, 'registration-form-email')
    PHONE = (By.ID, 'registration-form-phone')
    PASSWORD = (By.ID, 'registration-form-password')
    CREATE_BTN = (By.XPATH, "//button[contains(text(), 'Create Account')]")
    TEXT = (By.CSS_SELECTOR, "h1.account-dashboard-h1")
    SIGN = (By.CSS_SELECTOR, "div.order-1 button.btn-block")
    EMAILID = (By.ID, 'login-form-email')
    PASSW = (By.ID, 'login-form-password')

    def check_text(self, expected_text):
        self.verify_text(expected_text, *self.TEXT)

    def sign(self):
        self.click(*self.SIGN)

    def sign_in(self):
        self.click(*self.ACC_BUTTON)

    def submit_click(self):
        self.click(*self.CREATE_BTN)

    def enter_text(self, text):
        self.input_text(text, *self.FNAME)

    def enter_text1(self, text):
        self.input_text(text, *self.LNAME)

    def enter_text2(self, text):
        self.input_text(text, *self.EMAIL)

    def enter_text3(self, text):
        self.input_text(text, *self.PHONE)

    def enter_text4(self, text):
        self.input_text(text, *self.PASSWORD)

    def enter_text5(self, text):
        self.input_text(text, *self.EMAILID)

    def enter_text6(self, text):
        self.input_text(text, *self.PASSW)