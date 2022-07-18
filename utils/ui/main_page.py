from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        url = "https://mostly.ai"

        self.driver.get(url)
        self.wait.until(EC.title_is("MOSTLY AI, the synthetic data company - MOSTLY AI"))

        self.close_cookie_consent_dialog()

    def assert_bookmark_is_displayed(self, bookmark):
        assert self.driver.find_element(By.CSS_SELECTOR, f"nav.main-menu>ul>li>a[href$='{bookmark}']").is_displayed()

    def close_cookie_consent_dialog(self):
        action_chains = ActionChains(self.driver)
        h1_headline_element = self.driver.find_element(By.CSS_SELECTOR, "h1.ct-headline")
        action_chains.move_to_element(h1_headline_element).perform()

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#CookieBoxTextHeadline")))
        self.driver.find_element(By.CSS_SELECTOR, "#CookieBoxSaveButton").click()
        action_chains.reset_actions()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h1.ct-headline")))
