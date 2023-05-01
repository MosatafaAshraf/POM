import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Utils.assertclass import AssertionBy


@pytest.fixture(scope="session", autouse=True)
def url():
    url = "<insert_url>"
    return url

@pytest.fixture(scope="session", autouse=True)
def host(pytestconfig):
    return pytestconfig.getoption("host")


@pytest.fixture(scope="session")
def firefox_driver(host):
    remote_host = "http://selenium-chrome:4444"
    firfox_options = Options()
    firfox_options.add_argument("--window-size=1920,1080")
    firfox_options.add_argument("--start-fullscreen")
    firfox_options.add_argument("--no-sandbox")
    firfox_options.add_argument("--disable-dev-shm-usage")
    firfox_options.set_capability("acceptInsecureCerts", True)
    caps = DesiredCapabilities.FIREFOX.copy()
    caps['loggingPrefs'] = {
        'browser': 'ALL',
        'performance': 'ALL',
    }
    firfox_options.add_experimental_option('perfLoggingPrefs', {
        'enableNetwork': True,
        'enablePage': False,
    })

    driver = webdriver.Remote(
        command_executor=remote_host, options=firfox_options, desired_capabilities=caps)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def assertion():
    assert_fixture = AssertionBy()
    yield assert_fixture
    del assert_fixture
