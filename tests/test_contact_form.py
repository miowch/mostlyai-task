class TestContactForm:
    def test_filling_in_contact_form(self, app):
        app.main_page.open()
        app.contact_us_form.open_from_footer()
        app.fill_in_contact_form()
        app.contact_us_form.hover_over_submit_btn()
