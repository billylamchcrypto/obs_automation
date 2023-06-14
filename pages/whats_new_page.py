from hamcrest import assert_that

from pages.base_screen import BaseScreen


class WhatsNew(BaseScreen):
    # aos element
    WHATS_NEW_TITLE = ('id', 'whatsNewTitle')
    NEXT_BUTTON = ('id', 'btn_friendly_reminder_skip')

    def whats_new_here(self):
        assert_that(self.is_visible(self.WHATS_NEW_TITLE), "Failed to go to the Privacy Policy Statements page")
        print("The user is redirected to the whats new page")

    def click_whats_new_next(self):
        self.click(self.NEXT_BUTTON)
        print("The user click next in the whats new page")
