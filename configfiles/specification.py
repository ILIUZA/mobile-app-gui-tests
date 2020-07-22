import unittest
from appium import webdriver
from utility.application import Application
"""
This class is responsible for creating driver connection with appium server
"""


class BaseSpecification(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '9',
                        'deviceName': 'Android Emulator',
                        'app': 'D:/Projects/Pets/multitran.apk',
                        'automationName': 'UiAutomator2',
                        'unicodeKeyboard': True,
                        "resetKeyboard": True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.app = Application(self.driver)

    def tearDown(self):
        self.driver.quit()
