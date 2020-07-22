from page_model.main_page import MainPage
from page_model.navigate_page import NavigatePage

"""
This class will be responsible for creating a instance of page object
"""


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.navigate_page = NavigatePage(driver)
        #  self.login = Login(driver)
