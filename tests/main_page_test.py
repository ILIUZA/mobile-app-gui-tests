import time
import pytest
import unittest
from ddt import ddt, data, unpack
from configfiles.specification import BaseSpecification
from configfiles.read_testdata_file import getDataFromFile


@ddt
class TestMainPage(BaseSpecification, unittest.TestCase):
    expected_info_text = 'Multitran v'
    word = 'tree'

    def test_menu(self):
        self.app.main_page.click_btnNavigate()
        info_text = self.app.navigate_page.get_info_version_text
        assert self.expected_info_text in info_text

    def test_enter_word(self):
        assert 'en' in self.app.main_page.get_btnLang_text.lower()

        self.app.main_page.click_searchField()
        assert self.app.main_page.keyboardIsVisible is True

        self.app.main_page.set_wordToSearch(self.word)
        assert self.app.main_page.keyboardIsVisible is False

        assert self.app.main_page.get_allTab is not None
