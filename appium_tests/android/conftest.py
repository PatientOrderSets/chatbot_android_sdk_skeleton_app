import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    app='C:\\Users\\EimantasMacius\\code\\think-research-android-skelton-app\\appium_tests\\android\\Skelton App Final.apk',
)



# appium_server_url = 'http://hub.browserstack.com/wd/hub'
appium_server_url = 'http://localhost:4723'

@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()