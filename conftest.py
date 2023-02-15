import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def my_webdriver(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("headless")

    s = Service(ChromeDriverManager().install())
    my_driver = webdriver.Chrome(service=s, options=chrome_options)
    LOGGER.info("Creating and installing chrome driver - from CONFTEST !!!!!!!!!!!!!!!!!!!")
    print("\n Creating and installing chrome driver - once per class  CONFTEST !!!!!!!!!!!!!!!!!!!")

    request.cls.my_webdriver = my_driver
    print(request.cls.my_webdriver)
    yield
    LOGGER.info("Closing chrome driver - once per class,  CONFTEST !!!!!!!!!!!!!!!!!!!")
    print("\n Closing webdriver once pre class,  CONFTEST !!!!!!!!!!!!!!!!!!!")
    print(request.cls.my_webdriver)
    my_driver.quit()

@pytest.fixture()
def scope_function_default():
    LOGGER.info("Setup test executed - default scope function CONFTEST !!!!!!!!!!!!!!!!!!!" )
    yield
    LOGGER.info("Teardown test executed - default scope function CONFTEST !!!!!!!!!!!!!!!!!!!")
