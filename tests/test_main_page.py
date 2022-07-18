from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker


class TestMainPage:
    BOOKMARKS = [
        "platform/",
        "synthetic-data/",
        "resources/",
        "about-us/"
    ]

    @staticmethod
    def open_main_page(driver):
        url = "https://mostly.ai"

        driver.get(url)
        WebDriverWait(driver, 10).until(EC.title_is("MOSTLY AI, the synthetic data company - MOSTLY AI"))

        action_chains = ActionChains(driver)
        h1_headline_element = driver.find_element(By.CSS_SELECTOR, "h1.ct-headline")
        action_chains.move_to_element(h1_headline_element).perform()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#CookieBoxTextHeadline")))
        driver.find_element(By.CSS_SELECTOR, "#CookieBoxSaveButton").click()
        action_chains.reset_actions()

    @pytest.mark.parametrize('bookmark', BOOKMARKS)
    def test_bookmarks_visibility(self, driver, bookmark):
        self.open_main_page(driver)
        assert driver.find_element(By.CSS_SELECTOR, f"nav.main-menu>ul>li>a[href$='{bookmark}']").is_displayed()

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

    def test_filling_in_contact_form(self, driver):
        action_chains = ActionChains(driver)
        fake = Faker()

        self.open_main_page(driver)

        driver.find_element(By.CSS_SELECTOR, "#footer a[href$='contact/']").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.ct-headline")))

        h1_headline_element = driver.find_element(By.CSS_SELECTOR, "h1.ct-headline")
        action_chains.move_to_element(h1_headline_element).perform()
        action_chains.reset_actions()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".hbspt-form input.btn")))

        driver.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys(fake.first_name())
        driver.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys(fake.last_name())
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(self.create_unique_email())
        driver.find_element(By.CSS_SELECTOR, "input[name='mobilephone']").send_keys(fake.phone_number())
        driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(fake.company())
        driver.find_element(By.CSS_SELECTOR, "textarea[name='message']").send_keys(fake.paragraph(nb_sentences=2))

        driver.find_element(By.CSS_SELECTOR, "input[id^='LEGAL_CONSENT']").click()

        submit_button = driver.find_element(By.CSS_SELECTOR, ".hbspt-form  input.btn")
        action_chains.move_to_element(submit_button).perform()
        action_chains.reset_actions()

    @staticmethod
    def create_unique_email():
        random_part_email = datetime.now().strftime("%m%d%Y%H%M%S")
        return f"mostlyaitask+{random_part_email}@example.com"
