import time
import pytest
import unittest
from configfiles.specification import BaseSpecification


class TestMainPage(BaseSpecification):

    def test_scroll(self):
        self.app.main_page.click_btnNavigate()
        self.app.navigate_page.scrollToPrivacy()