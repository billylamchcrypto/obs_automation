from time import sleep
from typing import Optional, Tuple
from appium.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *


class BaseScreen:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    # explicit wait to find the element
    def _wait(self, locator: Tuple[str, str], timeout: Optional[int] = None,
              expected_condition: EC = EC.visibility_of_element_located, ) -> WebElement:
        if not timeout:
            timeout = self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout).until(expected_condition(locator))

    def is_visible(self, locator) -> bool:
        try:
            return self._wait(locator).is_displayed()
        except Exception:
            return False

    # clicks
    def click(self, locator):
        self._wait(locator).click()

    def device_back(self):
        return self.driver.press_keycode(4)

    # keyboard handling
    def hide_keyboard(self):
        try:
            sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def send_keys(self, locator, text):
        self._wait(locator).send_keys(text)
        sleep(0.5)

    def clear(self, locator):
        self._wait(locator).clear()

    # android scroll
    def android_scroll(self, container_locator, target_locator):
        for _ in range(15):
            try:
                element = self._wait(container_locator)
                container = element.rect
                x = (container.get('width') / 2 + container.get('x'))
                y = (container.get('height') / 2 + container.get('y'))
                y2 = y - y * 0.3
                self.driver.swipe(x, y, x, y2, 250)

                value = self._wait(target_locator).is_displayed()
                if value is True:
                    break
            except NoSuchElementException:
                pass

    # ios method is not used in this homework
    def ios_scroll(self, locator):
        el = self._wait(locator)
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})

    # redirect to different method according to your os
    def scrolling(self, container_locator, target_locator):
        if platform == 'ios':
            self.ios_scroll(container_locator, target_locator)
        else:
            self.android_scroll(container_locator, target_locator)
