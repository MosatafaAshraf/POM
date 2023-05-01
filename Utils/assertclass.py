import logging


class AssertionBy:
    def check_equality(self, expected, actual):
        assert expected == actual, logging.info(f'Expected response: {expected}, Actual response: {actual}')
