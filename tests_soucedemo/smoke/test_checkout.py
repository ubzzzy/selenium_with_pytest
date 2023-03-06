import pytest
import logging
from page_object_model.login_page.login_page import LoginPage

# logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def setup_module(module):
    print("Default module setup function")


def teardown_module(module):
    print("default module teardown")


@pytest.mark.usefixtures('driver')
class TestCheckout:

    @pytest.mark.usefixtures()
    def test_checkout(self):
        """
        Test checkout on https://www.saucedemo.com
        :return:
        """
        LOGGER.info("$$$$$$$$$$$$$$$$$$$$$$ Checkout Test login started")

        self.login = LoginPage(self.driver)
        self.login.fill_fields()
        # self.instantiate_pages.fill_fields()

