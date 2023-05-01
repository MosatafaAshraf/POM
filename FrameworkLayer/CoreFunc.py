from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CoreFunctions:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def navigate(self, clickable_element):
        button = self.locators(clickable_element)
        wait = 30
        element = WebDriverWait(self.browser, timeout=wait, poll_frequency=1).until(
            EC.visibility_of_element_located(button))
        element.click()
