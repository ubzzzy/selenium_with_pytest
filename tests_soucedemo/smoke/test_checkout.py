import pytest
import logging
from page_object_model.login.login import Login

# logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def setup_module(module):
    print("Default module setup function")


def teardown_module(module):
    print("default module teardown")


@pytest.mark.usefixtures('my_webdriver')
class TestCheckout:

    @pytest.mark.usefixtures('instantiate_pages')
    def test_checkout(self):
        """
        Test checkout on https://www.saucedemo.com
        :return:
        """
        LOGGER.info("$$$$$$$$$$$$$$$$$$$$$$ Checkout Test login started")
        self.login = Login(self.my_webdriver)
        self.instantiate_pages.fill_fields()

