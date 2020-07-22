import time
import pytest
import unittest
from ddt import ddt, data, unpack
from configfiles.specification import BaseSpecification
from configfiles.read_testdata_file import getDataFromFile


@ddt
class TestTranslation(BaseSpecification, unittest.TestCase):

    '''
    1. Retrieve a word and its translation from a csv-file
    2. Put the word in an input filed and click Search
    3. Assert if a list contains an expected translation
    '''
    @data(*getDataFromFile('test_translation_shown.csv'))
    @unpack
    def test_translation(self, word, translation):
        self.app.main_page.click_searchField()
        self.app.main_page.set_wordToSearch(word)

        assert self.app.main_page.translationIsValid(translation) is True

    '''
    1. Retrieve a word and its translation from a csv-file
    2. Put the word in an input filed and click Search (origin -> translation)
    3. Tap the translation in a list (translation -> origin)
    4. Assert if a list contains the word that we have translated before    
    '''
    @data(*getDataFromFile('test_translation_shown.csv'))
    @unpack
    def test_translation_to_origin(self, word, translation):
        self.app.main_page.click_searchField()
        self.app.main_page.set_wordToSearch(word)
        self.app.main_page.tapTranslation(translation)

        assert self.app.main_page.originIsValid(word) is True

    '''
    1. Retrieve a word and its translation from a csv-file
    2. Put the word in an input filed and click Search (origin -> translation)
    3. Tap the translation in a list 
    4. Assert that a dialog window is shown
    '''
    @data(*getDataFromFile('test_translation_shown.csv'))
    @unpack
    def test_dialog_window_shown(self, word, translation):
        self.app.main_page.click_searchField()
        self.app.main_page.set_wordToSearch(word)
        self.app.main_page.LongTapTranslation(translation)

        assert self.app.main_page.dialogIsShown is True

    '''
    1. Retrieve a word and its translation from a csv-file
    2. Put the word in an input filed and click Search (origin -> translation)
    3. Tap the translation in a list 
    4. Assert that a dialog window consists options
    5. Assert that the found options are equal (valid) to expected
    '''
    @data(*getDataFromFile('test_translation_shown.csv'))
    @unpack
    def test_dialog_options_shown(self, word, translation):
        self.app.main_page.click_searchField()
        self.app.main_page.set_wordToSearch(word)
        self.app.main_page.LongTapTranslation(translation)

        assert self.app.main_page.get_dialog_options is not None
        assert self.app.main_page.dialogOptionsAreValid() is True

