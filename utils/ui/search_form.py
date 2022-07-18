from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SearchForm:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def expand(self):
        self.driver.find_element(By.CSS_SELECTOR, ".oxy-header-search > button").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.oxy-header-search_search-field")))

    def search_for(self, text):
        self.driver.find_element(
            By.CSS_SELECTOR, "input.oxy-header-search_search-field").send_keys(f"{text}{Keys.ENTER}")

    def assert_no_search_results(self, text):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-no-results")))

        search_result_msg = self.driver.find_element(
            By.CSS_SELECTOR, ".search-no-results > section > div > div:nth-child(2)").text

        assert f"Sorry, no results for:\n{text}" in search_result_msg
