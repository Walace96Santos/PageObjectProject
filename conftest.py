import pytest
from selenium import webdriver

driver: webdriver.Remote


@pytest.fixture
def driver():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run tests
    yield driver

    # tear down
    driver.quit()
