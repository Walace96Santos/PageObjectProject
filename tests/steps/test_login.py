import logging

from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.common import CommonMethods
from tests.pages.login import LoginPage
from tests.pages.home import HomePage


scenarios('../features/login.feature')


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@given('the user accesses the login page')
def step_given_user_accesses_login_page(driver):
    driver.common_methods = CommonMethods(driver)
    driver.common_methods.open_url('https://www.saucedemo.com/')
    driver.login_page = LoginPage(driver)
    driver.login_page.wait_for_login_page_to_load()


@when('clicks on the login button')
def step_when_user_clicks_on_login_button(driver):
    driver.login_page.click_login_button()


@then('the user should be redirected to the home page')
def step_then_user_should_be_redirected_to_home_page(driver):
    driver.home_page = HomePage(driver)
    assert driver.home_page.is_on_focus(), "User is not redirected to the home page"


@when(parsers.parse('the user enters the credentials "{username}" and "{password}"'))
def step_when_user_enters_the_credentials(driver, username, password):
    driver.login_page.enter_credentials(username, password)


@then('the user should remain on the login page')
def step_then_user_should_remain_on_login_page(driver):
    driver.login_page = LoginPage(driver)
    assert driver.login_page.is_on_focus(), "Error: The Home page is visible!"


@then('an error message should be displayed')
def step_then_error_message_should_be_displayed(driver):
    driver.login_page = LoginPage(driver)
    driver.login_page.is_error_message_displayed()
