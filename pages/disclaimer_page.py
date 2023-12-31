from hamcrest import assert_that

from pages.base_screen import BaseScreen


class Disclaimer(BaseScreen):
    # aos element
    DISCLAIMER_TITLE = ('id', 'txt_title')
    AGREE_BUTTON = ('id', 'btn_agree')
    CONTAINER = ('id', 'content')

    def click_disclaimer_agree(self):
        self.click(self.AGREE_BUTTON)
        print("User agrees the disclaimer")

    def disclaimer_here(self):
        assert_that(self.is_visible(self.DISCLAIMER_TITLE), "Failed to go to the Disclaimer page")
        print("\nDisclaimer page is opened")
