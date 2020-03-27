from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

TITLE = (By.CSS_SELECTOR, "div.col-12>h1")
ICON = (By.CSS_SELECTOR, 'div.input-group-append button[type="submit"]')
ADD_CART = (By.CSS_SELECTOR, "button.add-to-cart")
CART_ICON = (By.CSS_SELECTOR, "img.shopping-cart.minicart-icon")
CART_ITEM = (By.CSS_SELECTOR, "div.product-name")
POPUP = (By.XPATH, "//button[contains(text(), '17 or older')]")
QUANTITY = (By.CSS_SELECTOR, 'div.ml-1 img.ae-img')
ITEMS = (By.CSS_SELECTOR, "span.number-of-home-delivery-items")


@then('Expected cart page will have {word} in the title')
def cart_empty(context, word):
    #actual_text = context.driver.find_element(*TITLE).text
    #assert word in actual_text
    context.app.shopping_page.empty_cart(word)


@when('Add product to shopping cart')
def add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_CART))
    #context.driver.find_element(*ADD_CART).click()
    context.app.shopping_page.to_cart()


@then('Expected product would be in cart')
def product_in_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON))
    context.driver.find_element(*CART_ICON).click()
    actual_text = context.driver.find_element(*CART_ITEM).text
    product = 'outer worlds'
    assert product == actual_text.lower()


@then('Close all pop-ups')
def close_popup(context):
    #context.driver.find_element(*POPUP).click
    context.app.shopping_page.popup()


@when('Return to product search page')
def return_back(context):
    context.driver.back()


@then('Expected products would be in cart')
def products_in_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON))
    context.driver.find_element(*CART_ICON).click()
    actual_text = context.driver.find_element(*CART_ITEM).text
    product1 = 'outer worlds'
    product2 = 'Outer Worlds'
    assert product1 == actual_text.lower()
    assert product2 == actual_text, f'Expected to see product2 in {actual_text}'


@when('Click cart icon')
def cart_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON))
    #context.driver.find_element(*CART_ICON).click()
    context.app.shopping_page.cart()


@then('Change quantity from 1 to 2')
def change_quantity(context):
    #context.driver.find_element(*QUANTITY).click()
    context.app.shopping_page.quantity()
    sleep(2)


@then('Expected items in cart will be {amount}')
def items_in_cart(context, amount):
    #actual_items = context.driver.find_element(*ITEMS).text
    #assert amount in actual_items, f'Expected to see {amount} of items in {actual_items}'
    context.app.shopping_page.items_cart(amount)