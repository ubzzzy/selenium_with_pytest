import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def setup_module(module):
    print("Default module setup function")

def teardown_module(module):
    print("default module teardown")

# @pytest.fixture(scope="class")
# def driver(request):
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-extensions")
#     # chrome_options.add_argument("headless")
#
#     s = Service(ChromeDriverManager().install())
#     my_driver = webdriver.Chrome(service=s, options=chrome_options)
#     print("\n Creating and installing chrome driver - once per class")
#
#     request.cls.driver = my_driver
#     print(request.cls.driver)
#     yield
#     print("\n Closing webdriver once pre class")
#     print(request.cls.driver)
#     my_driver.quit()


# @pytest.fixture()
# def scope_function_default():
#     LOGGER.info("Setup test executed - default scope function")
#     yield
#     LOGGER.info("Teardown test executed - default scope function")


@pytest.mark.usefixtures('driver')
class TestLogin:
    attr_class = "Buhaha"

    @pytest.mark.usefixtures('scope_function_default')
    def test_login_success(self):
        """
        Test succesfull login on https://www.saucedemo.com
        :return:
        """
        LOGGER.info("$$$$$$$$$$$$$$$$$$$$$$ INFOTest login started")
        LOGGER.warning("Logger WARNING")
        LOGGER.error("Logger ERROR")
        LOGGER.critical("Logger CRITICAL")
        LOGGER.debug("Logger DEBUG")
        # self.driver = self.my_
        self.driver.get("https://www.saucedemo.com")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        #
        # self.driver.find_element(By.XPATH, "//input[@id='password']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        #
        # LOGGER.info("Click login button")
        # self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        #
        # TestLogin.attr = "Changed by test 1"
        # assert "Products".casefold() == self.driver.find_element(By.XPATH, "//span[@class='title']").text.casefold()

    def test_login_fail(self):
        """
        Test succesfull login on https://www.saucedemo.com
        :return:
        """
        LOGGER.info("$$$$$$$$$$$$$$$$$$$$$$ INFOTest login FAIL started")

        # self.my_webdriver.get("https://www.saucedemo.com")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")

        self.driver.find_element(By.XPATH, "//input[@id='password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("wrong_pass")

        LOGGER.info("Click login button")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
