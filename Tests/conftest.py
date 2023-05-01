import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Pages.page_1 import Page1
from Utils.assertclass import AssertionBy


@pytest.fixture(scope="session", autouse=True)
def url():
    url = "file:///C:/Users/Mostafa_Ashraf/Downloads/SkyView-Updated/SkyView-NewVersion/newProject.html"
    return url


@pytest.fixture(scope="session")
def firefox_driver():
    remote_host = "http://127.0.0.1:4444"
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_options = Options()
    firefox_options.add_argument("--window-size=1920,1080")
    firefox_options.add_argument("--start-fullscreen")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.set_capability("acceptInsecureCerts", True)
    caps = DesiredCapabilities.FIREFOX()
    driver = webdriver.Remote(
        command_executor=remote_host, options=firefox_options, desired_capabilities=caps)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def assertion():
    assert_fixture = AssertionBy()
    yield assert_fixture
    del assert_fixture


@pytest.fixture(scope="session")
def first_page():
    page_one = Page1(url, firefox_driver)
    yield page_one
    del page_one
