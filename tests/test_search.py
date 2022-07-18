from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:
    def test_no_search_results(self, driver):
        searched_text = "sythetic"

        self.open_main_page(driver)
        driver.find_element(By.CSS_SELECTOR, ".oxy-header-search > button").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.oxy-header-search_search-field")))

        driver.find_element(By.CSS_SELECTOR, "input.oxy-header-search_search-field").send_keys(f"{searched_text}{Keys.ENTER}")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-no-results")))

        search_result_text = driver.find_element(By.CSS_SELECTOR,
                                                 ".search-no-results > section > div > div:nth-child(2)").text

        assert f"Sorry, no results for:\n{searched_text}" in search_result_text
