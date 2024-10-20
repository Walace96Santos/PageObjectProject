import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # setup
    options = Options()
    options.headless = False
    webdriver_instance = webdriver.Chrome(options=options)
    webdriver_instance.maximize_window()
    webdriver_instance.get("https://www.saucedemo.com/")

    # run tests
    yield webdriver_instance

    # tear down
    webdriver_instance.quit()
