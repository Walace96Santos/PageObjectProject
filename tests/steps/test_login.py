import time

from pytest_bdd import scenarios, given, when, then
from tests.pages.common import CommonMethods
from tests.pages.login import LoginPage
from tests.pages.home import HomePage


scenarios('../features/login.feature')


@given('the user accesses the login page')
def step_given_user_accesses_login_page(driver):
    driver.common_methods = CommonMethods()
    driver.common_methods.open_url('https://www.saucedemo.com/')
    driver.login_page = LoginPage()
    driver.login_page.wait_for_login_page_to_load()
    time.sleep(2)


@when('the user provides valid credentials')
def step_when_user_provides_valid_credentials(driver):
    username = 'standard_user'
    password = 'secret_sauce'
    driver.login_page.enter_credentials(username=username, password=password)
    time.sleep(1)


@when('clicks on the login button')
def step_when_user_clicks_on_login_button(driver):
    driver.login_page.click_login_button()


@then('the user should be redirected to the home page')
def step_then_user_should_be_redirected_to_home_page(driver):
    time.sleep(2)
    driver.home_page = HomePage()
    assert driver.home_page.is_on_focus(), "User is not redirected to the home page"
