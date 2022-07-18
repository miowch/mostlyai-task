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

