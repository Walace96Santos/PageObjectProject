from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class CommonMethods:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()

    def wait_until_element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_visible(self, locator, timeout=5):
        try:
            element_present = EC.presence_of_element_located(locator)
            WebDriverWait(self.driver, timeout).until(element_present)
            return True
        except NoSuchElementException:
            return False

    def is_clickable(self, locator, timeout=5):
        try:
            self.wait_until_element_is_clickable(locator, timeout)
            return True
        except NoSuchElementException:
            return False

    def scroll_to_find_element(self, locator, attempts=3):
        for _ in range(attempts):
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                return element
            except NoSuchElementException:
                pass
        raise NoSuchElementException(f"Element {locator} not found after scrolling.")
