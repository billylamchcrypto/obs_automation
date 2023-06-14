from pages.disclaimer_page import Disclaimer
from pages.privacy_policy_statements_page import PrivacyPolicyStatements
from pages.background_location_access_page import BackgroundLocationAccess
from pages.device_location_access_page import DeviceLocationAccess
from pages.privacy_policy_statements_page import PrivacyPolicyStatements
from pages.traffic_info_tutorial_page import TrafficInfoTutorial
from pages.whats_new_page import WhatsNew
from pages.home_page import Home
from pages.nine_days_forecast_page import NineDaysForecast


class Pages:
    def __init__(self, driver):
        self._driver = driver
        self.disclaimer = Disclaimer(self._driver)
        self.privacy_policy_statements = PrivacyPolicyStatements(self._driver)
        self.background_location_access = BackgroundLocationAccess(self._driver)
        self.device_location_access = DeviceLocationAccess(self._driver)
        self.privacy_policy_statements = PrivacyPolicyStatements(self._driver)
        self.whats_new = WhatsNew(self._driver)
        self.traffic_info_tutorial = TrafficInfoTutorial(self._driver)
        self.home = Home(self._driver)
        self.nine_days_forecast = NineDaysForecast(self._driver)





