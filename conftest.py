import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # setup
    webdriver_instance = Options()
    webdriver_instance.add_argument("--headless")  # Runs the browser in headless mode, without a GUI.
    webdriver_instance.add_argument("--no-sandbox")  # Disables the sandbox(Chrome security mode) for all process types.
    webdriver_instance.add_argument("--disable-dev-shm-usage")  # Avoids shared memory issues in CI environments.

    webdriver_instance = webdriver.Chrome(service=Service('chromedriver-linux64/chromedriver'),
                                          options=webdriver_instance)
    webdriver_instance.maximize_window()
    webdriver_instance.get("https://www.saucedemo.com/")

    # run tests
    yield webdriver_instance

    # tear down
    webdriver_instance.quit()
