from tests.pages.common import CommonMethods
from tests.mappings.login import LoginMapping


class LoginPage(CommonMethods):

    def __init__(self):
        super().__init__()
        self.mapping = LoginMapping()

    def wait_for_login_page_to_load(self):
        self.wait_until_element_is_visible(self.mapping.USERNAME_INPUT)

    def enter_credentials(self, username, password):
        self.wait_until_element_is_visible(self.mapping.USERNAME_INPUT).send_keys(username)
        self.wait_until_element_is_visible(self.mapping.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_until_element_is_clickable(self.mapping.LOGIN_BUTTON).click()
