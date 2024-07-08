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

    def test_new_conversation(self):
        self.assert_visible(BUTTON_NEED_CARE)

    def test_formatted_msg(self):
        self.click(BUTTON_BACK)
        self.click(BUTTON_NEW_CONVO)
        self.click(BUTTON_SELECT_OPTION)
        self.click(OPTION_FORMATED)
        self.click(BUTTON_SEND)
        self.assert_visible(OPTION_BACK)

    def test_survey(self):
        self.click(BUTTON_BACK)
        self.click(BUTTON_NEW_CONVO)
        self.click(BUTTON_SELECT_OPTION)
        self.click(OPTION_SELECT_SURVEY)
        self.click(BUTTON_SEND)
        self.assert_visible(BUTTON_START_SURVEY)

    def test_enter_input(self):
        self.click(BUTTON_BACK)
        self.click(BUTTON_NEW_CONVO)
        self.click(BUTTON_SELECT_OPTION)
        self.click(OPTION_ENTER_INPUT)
        self.click(BUTTON_SEND)
        self.click(INPUT_FIELD)
        input_field = self.driver.find_element(*INPUT_FIELD)
        input_field.send_keys('hello')
        self.click(BUTTON_SEND_MESSAGE)
        self.assert_visible(OPTION_CLOSE)
    
    def test_assign_agent(self):
        self.click(BUTTON_BACK)
        self.click(BUTTON_NEW_CONVO)
        self.click(BUTTON_SELECT_OPTION)
        self.click(OPTION_ASSIGN_AGENT)
        self.click(BUTTON_SEND)
        self.assert_visible(MESSAGE_ASSIGNED_TO)

        



