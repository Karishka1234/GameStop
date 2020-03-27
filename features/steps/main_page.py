from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRODUCT = (By.CSS_SELECTOR, 'input.search-field')
ICON = (By.CSS_SELECTOR, 'div.input-group-append button[type="submit"]')
ACC_ICON = (By.CSS_SELECTOR, "img.account")
CART_ICON = (By.CSS_SELECTOR, "a.minicart-link img.shopping-cart")
REVIEW = (By.CSS_SELECTOR, "button.bv-write-review")
SUGGESTION = (By.CSS_SELECTOR, "img.suggestion-product-image")


@given('Open https://www.gamestop.com/ page')
def open_page(context):
    #context.driver.get('https://www.gamestop.com/')
    context.app.main_page.open_page()


@when('Insert {word} in search field')
def search_for_product(context, word):
    #product = context.driver.find_element(*PRODUCT)
    #product.click()
    #product.clear()
    #product.send_keys(word)
    context.app.main_page.enter_text(word)


@when('Click search button or click enter button')
def click_icon(context):
    #context.driver.find_element(*ICON).click()
    context.app.main_page.icon_click()


@when('Click account button')
def acc_icon(context):
    #context.driver.find_element(*ACC_ICON).click()
    context.app.main_page.acc_click()


@when('Click cart button')
def cart_click(context):
    #context.driver.find_element(*CART_ICON).click()
    context.app.main_page.cart_click()


@then('click "write review" button')
def write_review(context):
    #context.driver.find_element(*REVIEW).click()
    context.app.main_page.review_link()


@then('expected product has "write review" button')
def write_button(context):
    context.driver.wait.until(EC.presence_of_element_located(REVIEW))


@then('Wait a couple of seconds')
def wait(context):
    context.driver.wait.until(EC.presence_of_element_located(SUGGESTION))


@then('Expected to see some suggestions. Count them')
def keywords(context):
    amount = context.driver.find_elements(*SUGGESTION)
    print(len(amount))
