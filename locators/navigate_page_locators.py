from selenium.webdriver.common.by import By


class NavigatePageLocators:
    versionInfo = (By.ID, 'tvVersionInfo')
    privacyInfo = (By.XPATH, '//*[contains(@text, "Policy")]')
    menuOptions = (By.ID, 'design_menu_item_text')


