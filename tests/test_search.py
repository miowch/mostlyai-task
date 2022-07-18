class TestSearch:
    def test_no_search_results(self, app):
        searched_text = "sythetic"

        app.main_page.open()
        app.search_for_text(searched_text)
        app.search_form.assert_no_search_results(searched_text)
