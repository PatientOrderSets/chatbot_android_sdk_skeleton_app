import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BUTTON_NEED_CARE = (AppiumBy.ACCESSIBILITY_ID, "I need care\nI need care")
BUTTON_BACK = (AppiumBy.XPATH, "//android.widget.Button")
BUTTON_FAB = (AppiumBy.ID, "com.thinkresearch.skeltonapp:id/fab")
BUTTON_NEW_CONVO = (AppiumBy.XPATH, "//android.widget.Button[@content-desc=\"Start a conversation\"]")
BUTTON_SELECT_OPTION = (AppiumBy.ACCESSIBILITY_ID, "Select an option")
OPTION_SELECT_SURVEY = (AppiumBy.ACCESSIBILITY_ID, "Survey")
OPTION_ENTER_INPUT = (AppiumBy.ACCESSIBILITY_ID, "Enter input")
OPTION_ASSIGN_AGENT = (AppiumBy.ACCESSIBILITY_ID, "Assign to agent")
OPTION_FORMATED = (AppiumBy.ACCESSIBILITY_ID, "Formatted Messages")
BUTTON_SEND = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[2]")
BUTTON_SEND_MESSAGE = (AppiumBy.XPATH, "//android.widget.EditText/android.widget.Button")
BUTTON_START_SURVEY = (AppiumBy.ACCESSIBILITY_ID, "Start")
INPUT_FIELD = (AppiumBy.XPATH, "//android.widget.EditText")
OPTION_CLOSE = (AppiumBy.ACCESSIBILITY_ID, "Close\nClose")
OPTION_BACK = (AppiumBy.ACCESSIBILITY_ID, "Back\nBack")
MESSAGE_ASSIGNED_TO = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Assigned')]")
HEADER_CHAT = (AppiumBy.XPATH, "//android.view.View[@content-desc=\"Chat with us!\"]")

BUTTON_SETTINGS = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id=\"com.thinkresearch.skeltonapp:id/settingsButton\"]")
SETTINGS_BUTTON_SAVE = (AppiumBy.XPATH, "//android.widget.Button[@resource-id=\"com.thinkresearch.skeltonapp:id/buttonSave\"]")


class TestAppium:
    @pytest.fixture(autouse=True)
    def set_up(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.click()
    
    def assert_visible(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        assert element.is_displayed()

    def test_smoke(self):
        self.assert_visible(BUTTON_FAB)

    def test_settings(self):
        self.click(BUTTON_SETTINGS)
        self.assert_visible(SETTINGS_BUTTON_SAVE)

    def test_save_settings(self):
        self.click(BUTTON_SETTINGS)
        self.click(SETTINGS_BUTTON_SAVE)
        self.assert_visible(BUTTON_FAB)

    def test_new_conversation(self):
        self.click(BUTTON_FAB)
        self.assert_visible(HEADER_CHAT)

    def test_option_list(self):
        self.click(BUTTON_FAB)
        self.assert_visible(BUTTON_NEED_CARE)
        
