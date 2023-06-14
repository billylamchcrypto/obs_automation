from hamcrest import assert_that

from pages.base_screen import BaseScreen


class TrafficInfoTutorial(BaseScreen):
    # aos element
    TRAFFIC_INFO_TITLE = ('id', 'txt')
    CLOSE_BUTTON = ('id', 'btn_friendly_reminder_skip')

    def traffic_info_tutorial_here(self):
        assert_that(self.is_visible(self.TRAFFIC_INFO_TITLE), "Failed to go to the Privacy Policy Statements page")
        print("the user is redirected to the Traffic Information Tutorial page")

    def click_traffic_info_tutorial_close(self):
        self.click(self.CLOSE_BUTTON)
        print("the user clicks the close button in Traffic Information Tutorial page")
