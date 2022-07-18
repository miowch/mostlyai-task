from selenium import webdriver



class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def quit(self):
        self.driver.quit()
