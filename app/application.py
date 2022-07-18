from selenium import webdriver

from utils.ui.main_page import MainPage


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)

    def quit(self):
        self.driver.quit()
