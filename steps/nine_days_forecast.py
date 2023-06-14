from time import sleep
from pages import Pages
from pytest_bdd import given, when, then


@given('the user is in Disclaimer page')
def in_disclaimer_page(pages: Pages):
    pages.disclaimer.disclaimer_here()


@when('the user clicks Agree button on the disclaimer page')
def clicks_agree_button_on_the_disclaimer_page(pages: Pages):
    pages.disclaimer.click_disclaimer_agree()


@then('the user is redirected to the Privacy Policy Statements page')
def in_privacy_policy_statements_page(pages: Pages):
    pages.privacy_policy_statements.statements_here()


@when('the user clicks Agree button on the Privacy Policy Statements page')
def clicks_agree_button_on_the_statements_page(pages: Pages):
    pages.privacy_policy_statements.click_statements_agree()


@then('the user is redirected to the Background Access to Location Information page')
def in_background_access_to_location_information_page(pages: Pages):
    pages.background_location_access.background_location_access_here()


@when('the user clicks OK button')
def clicks_ok_button(pages: Pages):
    pages.background_location_access.click_click_background_location_access_ok()


@then('the user is redirected to the new Location Access page')
def in_new_location_access_page(pages: Pages):
    pages.device_location_access.new_device_location_access_here()


@when('the user clicks While using the app button')
def click_while_using_the_app(pages: Pages):
    pages.device_location_access.click_while_using_the_app()


@then('the user is redirected to the Location Permission page')
def in_location_permission(pages: Pages):
    pages.device_location_access.location_permission_here()


@when('the user clicks the Back button')
def click_back_button_in_location_permission(pages: Pages):
    pages.device_location_access.device_back()


@then('the user is redirected to the device location access page')
def in_device_location_access_page(pages: Pages):
    pages.device_location_access.device_location_access_here()


@when('the user clicks Allow only while using the app')
def clicks_allow_only_while_using_the_app(pages: Pages):
    pages.device_location_access.click_device_location_access_allow()
    # I know sleep is not a good method compared to wait but only sleep can give time for the driver to find the next element
    sleep(3)


@then('the user is redirected to the device location access page with time factor')
def in_device_location_access_page_with_time(pages: Pages):
    pages.device_location_access.device_location_access_alltime_here()


@when('the user clicks Allow all the time')
def clicks_allow_all_the_time_in_device_location_access_page_with_time(pages: Pages):
    pages.device_location_access.click_device_location_access_allow_all_time()


@then('the user is redirected to the Whats new page')
def in_whats_new_page(pages: Pages):
    pages.whats_new.whats_new_here()


@when('the user clicks the next button in whats new page')
def clicks_next_in_whats_new_page(pages: Pages):
    pages.whats_new.click_whats_new_next()


@then('the user is redirected to the Traffic Information Tutorial page')
def in_traffic_info_tutorial_page(pages: Pages):
    pages.traffic_info_tutorial.traffic_info_tutorial_here()


@when('the user clicks the close button in Traffic Information Tutorial page')
def close_the_traffic_info_tutorial_page(pages: Pages):
    pages.traffic_info_tutorial.click_traffic_info_tutorial_close()


@then('the user is redirected to the Home page')
def in_home_page(pages: Pages):
    # pages.home.go()
    pages.home.home_here()


@when('the user clicks the menu bar')
def click_menu_bar(pages: Pages):
    pages.home.click_menu_bar()


@then('the user scroll down in menu bar and clicks the "9-Day Forecast" from the menu bar')
def scroll_down_menu_bar_and_click_nine_days_forecast(pages: Pages):
    pages.home.scroll_menu_bar()
    pages.home.click_nine_days_forecast()


@then('the user can see the "9-Day Forecast"')
def in_nine_days_forecast(pages: Pages):
    pages.nine_days_forecast.nine_days_forecast_here()
