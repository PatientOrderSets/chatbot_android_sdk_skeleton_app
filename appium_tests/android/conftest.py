import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    app='app/build/outputs/apk/release/*.apk',
)



# appium_server_url = 'http://hub.browserstack.com/wd/hub'
appium_server_url = 'http://localhost:4723'

@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()
