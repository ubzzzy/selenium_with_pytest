from util.base_command import BaseCommand


class Login(BaseCommand):
    def __init__(self, my_webdriver):
        super().__init__(my_webdriver)
        self.base_command = BaseCommand(my_webdriver)
        self.base_command.open_webpage("https://www.saucedemo.com")

    def fill_fields(self):
        self.base_command.click_element("//input[@id='user-name']")


