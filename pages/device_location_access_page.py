from hamcrest import assert_that

from pages.base_screen import BaseScreen


class DeviceLocationAccess(BaseScreen):
    # aos element only for AOS version 9
    DEVICE_LOCATION_ACCESS_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    DEVICE_LOCATION_ACCESS_ALLTIME_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    ALLOW_BUTTON = ('id', 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    ALLOW_ALL_TIME_BUTTON = ('id', 'com.android.permissioncontroller:id/permission_allow_button')

    def device_location_access_here(self):
        assert_that(self.is_visible(self.DEVICE_LOCATION_ACCESS_TITLE), "failed reason")
        print("The user is redirected to the Device location access page")

    def click_device_location_access_allow(self):
        self.click(self.ALLOW_BUTTON)
        print("The user clicks Allow only while using the app in Device Location Access page")

    def device_location_access_alltime_here(self):
        assert_that(self.is_visible(self.DEVICE_LOCATION_ACCESS_ALLTIME_TITLE), "failed reason")
        print("The user is redirected to the Device location access page with time factor")

    def click_device_location_access_allow_all_time(self):
        self.click(self.ALLOW_ALL_TIME_BUTTON)

# aos element only for AOS version 12
    NEW_LOCATION_ACCESS_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    WHILE_USING_THE_APP = ('id', 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    LOCATION_PERMISSION_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    BACK = ('xpath', '//android.widget.ImageButton[@content-desc="Back"]')

    def new_device_location_access_here(self):
        assert_that(self.is_visible(self.NEW_LOCATION_ACCESS_TITLE), "Failed to go to The Device location access page")
        print("The user is redirected to the Device location access page")

    def click_while_using_the_app(self):
        self.click(self.WHILE_USING_THE_APP)
        print("The user clicks Allow only while using the app in Device Location Access page")

    def location_permission_here(self):
        assert_that(self.is_visible(self.LOCATION_PERMISSION_TITLE), "Failed to go to the location permission page")
        print("The user is redirected to the location permission page")

    def click_back_in_location_permission(self):
        self.click(self.BACK)
        print("The user clicks the back button")

    def click_device_back(self):
        self.device_back()
        print("The user clicks the back button")
