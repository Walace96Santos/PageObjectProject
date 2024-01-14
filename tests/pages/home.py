from tests.pages.common import CommonMethods
from tests.mappings.home import HomeMapping


class HomePage(CommonMethods):
    def __init__(self):
        super().__init__()
        self.mapping = HomeMapping()

    def is_on_focus(self):
        return self.is_visible(self.mapping.TITLE_LABEL)
