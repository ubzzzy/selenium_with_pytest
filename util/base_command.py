from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseCommand:
    def __init__(self, driver):
        self.local_driver: webdriver.Chrome = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 3)

    def open_webpage(self, webpage_url):
        self.local_driver.get(webpage_url)

    def click_element(self, element):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).click()
