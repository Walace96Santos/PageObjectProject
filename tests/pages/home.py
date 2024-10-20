from tests.pages.common import CommonMethods
from tests.mappings.home import HomeMapping


class HomePage(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.mapping = HomeMapping()

    def is_on_focus(self):
        return self.is_visible(self.mapping.TITLE_LABEL)
