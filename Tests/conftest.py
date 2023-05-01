import pytest
import logging
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="session", autouse=True)
def url(pytestconfig):
    url = "<insert_url>"
    logging.info('Portal Url: {}'.format(url))
    return url