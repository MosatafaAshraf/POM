from selenium.webdriver.common.by import By
from FrameworkLayer.CoreFunc import CoreFunctions


class Page1(CoreFunctions):
    def __init__(self, url, driver):
        super().__init__(driver, url)

    def locators(self, element_name):
        page1 = {
            "customer_pic"": (By.XPATH, "<Element_XPath>")
        }
        return page1[element_name]

