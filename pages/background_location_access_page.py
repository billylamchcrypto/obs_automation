from hamcrest import assert_that

from pages.base_screen import BaseScreen


class BackgroundLocationAccess(BaseScreen):
    # aos element
    BACKGROUND_LOCATION_ACCESS_TITLE = ('id', 'alertTitle')
    OK_BUTTON = ('id', 'android:id/button1')

    def background_location_access_here(self):
        assert_that(self.is_visible(self.BACKGROUND_LOCATION_ACCESS_TITLE), "Failed to go to the background Location access page")
        print("The user is redirected to the Background Access to Location Information page")

    def click_click_background_location_access_ok(self):
        self.click(self.OK_BUTTON)
        print("User agrees background location access")
