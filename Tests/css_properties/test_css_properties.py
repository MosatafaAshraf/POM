import pytest
import selenium


class TestCSSProperties:
    def test_css_properties(self, assertion, first_page):
        css_properties = first_page.get_css_property(first_page.locators("customer_pic"))
        assertion.check_equality(css_properties[0]['height'], 48)
