from selenium import webdriver



class BaseCommand:
    def __init__(self, driver):
        self.local_driver: webdriver.Chrome = driver
        self.wait:

    def click_element(self, element):
        pass
