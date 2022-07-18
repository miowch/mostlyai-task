from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker


class TestContactForm:
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