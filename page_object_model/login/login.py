class Login:
    def __init__(self, my_webdriver):
        self.driver = my_webdriver

    def fill_fields(self):
        self.driver.get("https://www.saucedemo.com")


