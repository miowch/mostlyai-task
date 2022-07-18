from selenium import webdriver

from utils.ui.main_page import MainPage
from utils.ui.search_form import SearchForm


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.search_form = SearchForm(self.driver)

    def quit(self):
        self.driver.quit()

    def search_for_text(self, text):
        self.search_form.expand()
        self.search_form.search_for(text)
