import pytest


class TestMainPage:
    BOOKMARKS = [
        "platform/",
        "synthetic-data/",
        "resources/",
        "about-us/"
    ]

    @pytest.mark.parametrize('bookmark', BOOKMARKS)
    def test_bookmarks_visibility(self, app, bookmark):
        app.main_page.open()
        app.main_page.assert_bookmark_is_displayed(bookmark)
