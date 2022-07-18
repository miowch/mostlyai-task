from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ContactUsForm:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def firstname_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='firstname']")

    @property
    def lastname_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='lastname']")

    @property
    def email_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")

    @property
    def phone_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='mobilephone']")

    @property
    def company_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='company']")

    @property
    def message_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "textarea[name='message']")

    def tick_legal_consent(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[id^='LEGAL_CONSENT']").click()

    def hover_over_submit_btn(self):
        action_chains = ActionChains(self.driver)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".hbspt-form  input.btn")
        action_chains.move_to_element(submit_button).perform()
        action_chains.reset_actions()

    def open_from_footer(self):
        self.driver.find_element(By.CSS_SELECTOR, "#footer a[href$='contact/']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.ct-headline")))
        self.wait_for_fields_appearance()

    def wait_for_fields_appearance(self):
        action_chains = ActionChains(self.driver)

        h1_headline_element = self.driver.find_element(By.CSS_SELECTOR, "h1.ct-headline")
        action_chains.move_to_element(h1_headline_element).perform()
        action_chains.reset_actions()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".hbspt-form input.btn")))
