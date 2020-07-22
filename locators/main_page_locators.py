from selenium.webdriver.common.by import By


class MainPageLocators:
    btnLang = (By.ID, 'btnLanguage')
    btnNavigate = (By.XPATH, '//*[contains(@content-desc, "Navigate up")]')
    searchField = (By.ID, 'editTextMain')
    allTab = (By.XPATH, '//*[@class="android.widget.TextView" and contains(@text, "ВСЕ")]')
    verbTab = (By.XPATH, '//*[@class="android.widget.TextView" and contains(@text, "ГЛАГ")]')
    translationsList = (By.ID, 'tvWordName')
    dialog = (By.ID, 'select_dialog_listview')
    dialog_options = (By.XPATH, '//*[@id="select_dialog_listview"]/*[@class="android.widget.ListView"]')
    dialog_options_texts = ['Play', 'Copy', 'Add to Favorites']



