from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CoreFunctions:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def navigate(self, clickable_element):
        wait = 30
        element = WebDriverWait(self.driver, timeout=wait, poll_frequency=1).until(
            EC.visibility_of_element_located(clickable_element))
        element.click()

    def get_css_properties(self, element, wait=30):
        element = WebDriverWait(self.driver, timeout=5, poll_frequency=1).until(EC.visibility_of_element_located(element))
        css_dict = {
            "element-size": element.size
        }
        property_list = [css_dict['element-size']]
        return property_list
