from locators.navigate_page_locators import NavigatePageLocators
from page_model.base_page import BasePage


class NavigatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def get_info_version_text(self):
        return self.__get__(NavigatePageLocators.versionInfo)

    def scrollToPrivacy(self):
        self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Privacy Policy\"))")


