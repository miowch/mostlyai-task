from datetime import datetime
from faker import Faker
from selenium import webdriver

from utils.ui.contact_us_form import ContactUsForm
from utils.ui.main_page import MainPage
from utils.ui.search_form import SearchForm


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.search_form = SearchForm(self.driver)
        self.contact_us_form = ContactUsForm(self.driver)

    def quit(self):
        self.driver.quit()

    def search_for_text(self, text):
        self.search_form.expand()
        self.search_form.search_for(text)

    def fill_in_contact_form(self):
        fake = Faker()
        self.contact_us_form.firstname_input.send_keys(fake.first_name())
        self.contact_us_form.lastname_input.send_keys(fake.last_name())
        self.contact_us_form.email_input.send_keys(self.create_unique_email())
        self.contact_us_form.phone_input.send_keys(fake.phone_number())
        self.contact_us_form.company_input.send_keys(fake.company())
        self.contact_us_form.message_field.send_keys(fake.paragraph(nb_sentences=2))

        self.contact_us_form.tick_legal_consent()

    @staticmethod
    def create_unique_email():
        random_part_email = datetime.now().strftime("%m%d%Y%H%M%S")
        return f"mostlyaitask+{random_part_email}@example.com"
