from hamcrest import assert_that

from pages.base_screen import BaseScreen


class PrivacyPolicyStatements(BaseScreen):
    # aos element
    STATEMENTS_TITLE = ('id', 'txt_title')
    AGREE_BUTTON = ('id', 'btn_agree')

    def statements_here(self):
        assert_that(self.is_visible(self.STATEMENTS_TITLE), "Failed to go to the Privacy Policy Statements page")
        print("User is redirected to the Privacy Policy Statements page")

    def click_statements_agree(self):
        self.click(self.AGREE_BUTTON)
        print("User agrees the Privacy Policy Statements")
