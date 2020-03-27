from behave import given, when, then
from selenium.webdriver.common.by import By

TITLE = (By.CSS_SELECTOR, 'h1.search-title')
PRODUCT = (By.CSS_SELECTOR, "div.product-tile-header a.h5")
ICON = (By.CSS_SELECTOR, 'div.input-group-append button[type="submit"]')


@then('Expect to see the search results page. Check that title is relevant to search text')
def search_result(context):
    text = 'gaming mouse'
    actual_text = context.driver.find_element(*TITLE).text
    assert text in actual_text.lower(), f'Expected to see {text} in {actual_text}'


@when('On search results page choose something and click it')
def choose_product(context):
    #context.driver.find_element(*ICON).click()
    #context.driver.find_element(*PRODUCT).click()
    context.app.results_page.choose_products()


@when('On search results page choose another product and click it')
def choose_another(context):
    products = context.driver.find_elements(*PRODUCT)
    products[1].click()


