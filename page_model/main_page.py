from locators.main_page_locators import MainPageLocators
from page_model.base_page import BasePage
from utility.waits import WaitForElement
from appium.webdriver.common.touch_action import TouchAction


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_btnNavigate(self):
        return self.click(MainPageLocators.btnNavigate)

    @property
    def get_btnLang_text(self):
        return self.__get__(MainPageLocators.btnLang)

    @property
    def get_dialog_options(self):
        WaitForElement.wait(self.driver, MainPageLocators.dialog)
        return self.driver.find_elements(*MainPageLocators.dialog_options)

    def set_wordToSearch(self, word):
        self.__set__(MainPageLocators.searchField, word)
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})

    @property
    def keyboardIsVisible(self):
        return self.driver.is_keyboard_shown()

    def click_searchField(self):
        return self.click(MainPageLocators.searchField)

    @property
    def get_allTab(self):
        WaitForElement.wait(self.driver, MainPageLocators.allTab)
        return self.driver.find_element(*MainPageLocators.allTab)

    @property
    def dialogIsShown(self):
        WaitForElement.wait(self.driver, MainPageLocators.dialog)
        dialog = self.driver.find_element(*MainPageLocators.dialog)
        if dialog is not None:
            return True
        else:
            return False

    @property
    def get_verbTab(self):
        WaitForElement.wait(self.driver, MainPageLocators.verbTab)
        return self.driver.find_element(*MainPageLocators.verbTab)

    def click_verbTab(self):
        return self.click(MainPageLocators.verbTab)

    def get_TranslationsList(self):
        text_translations = []
        WaitForElement.wait(self.driver, MainPageLocators.translationsList)
        elements = self.driver.find_elements(*MainPageLocators.translationsList)
        for element in elements:
            text = element.get_attribute("text")
            text_translations.append(text)
        print(text_translations)
        return text_translations

    def translationIsValid(self, translation):
        text_list = self.get_TranslationsList()
        for text in text_list:
            if translation in text:
                print(translation, text)
                return True
        return False

    def tapTranslation(self, translation):
        try:
            WaitForElement.wait(self.driver, MainPageLocators.translationsList)
            elements = self.driver.find_elements(*MainPageLocators.translationsList)
            for element in elements:
                if translation in element.text:
                    self.tap_element(element)
                    break
        except:
            raise Exception("Cannot tap an element with translation {}".format(translation))

    def LongTapTranslation(self, translation):
        try:
            WaitForElement.wait(self.driver, MainPageLocators.translationsList)
            elements = self.driver.find_elements(*MainPageLocators.translationsList)
            for element in elements:
                if translation in element.text:
                    self.long_press_element(element)
                    break
        except:
            raise Exception("Cannot tap an element with translation {}".format(translation))

    def originIsValid(self, word):
        WaitForElement.wait(self.driver, MainPageLocators.translationsList)
        elements = self.driver.find_elements(*MainPageLocators.translationsList)
        for element in elements:
            if word in element.text:
                return True
        return False

    def dialogOptionsAreValid(self):
        options = self.get_dialog_options
        list_of_texts = []
        if options is not None:
            for option in options:
                t = option.text
                list_of_texts.append(t)

            s = set(list_of_texts)
            dif = [x for x in options if x not in s]
            if len(dif) > 0:
                return False
            else:
                return True

        else:
            return False












