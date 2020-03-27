from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

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


@when('Switch to create account')
def sign(context):
    #context.driver.find_element(*ACC_BUTTON).click()
    context.app.sign_in_page.sign_in()
    context.driver.wait.until(EC.element_to_be_clickable(ACC_BUTTON))


@when('Fill all fields with fake data')
def fill_fields(context):
    #fname = context.driver.find_element(*FNAME)
    #fname.click()
    #fname.clear()
    #fname.send_keys('Karina')
    context.app.sign_in_page.enter_text("Karina")
    #lname = context.driver.find_element(*LNAME)
    #lname.click()
    #lname.clear()
    #lname.send_keys('Sun')
    context.app.sign_in_page.enter_text1("Sun")
    #email = context.driver.find_element(*EMAIL)
    #email.click()
    #email.clear()
    #email.send_keys('karin@mail.com')
    context.app.sign_in_page.enter_text2("karikk@mail.com")
    #phone = context.driver.find_element(*PHONE)
    #phone.click()
    #phone.clear()
    #phone.send_keys('3474211111')
    context.app.sign_in_page.enter_text3("3474211111")
    #password = context.driver.find_element(*PASSWORD)
    #password.click()
    #password.clear()
    #password.send_keys('BlaBla12#')
    context.app.sign_in_page.enter_text4("BlaBla12#")


@then('Click submit')
def submit(context):
    #context.driver.find_element(*CREATE_BTN).click()
    context.app.sign_in_page.submit_click()


@then('Expected registration will be complete successfully')
@then('Expected login will be complete successful')
def reg_complete(context):
    #actual_text = context.driver.find_element(*TEXT).text
    #expected_text = "ACCOUNT DASHBOARD"
    #assert actual_text == expected_text
    context.app.sign_in_page.check_text("ACCOUNT DASHBOARD")

@when('Fill data from prev step')
def fill_data(context):
    #email = context.driver.find_element(*EMAILID)
    #email.click()
    #email.clear()
    #email.send_keys('karin@mail.com')
    context.app.sign_in_page.enter_text5('karikk@mail.com')
    #password = context.driver.find_element(*PASSW)
    #password.click()
    #password.clear()
    #password.send_keys('BlaBla12#')
    context.app.sign_in_page.enter_text6('BlaBla12#')


@then('Click signIn')
def sign_in(context):
    #context.driver.find_element(*SIGN).click()
    context.app.sign_in_page.sign()


