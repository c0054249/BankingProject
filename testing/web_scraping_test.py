import unittest
import json
from bs4 import BeautifulSoup
from content import web_scraping
from main import app


class TestWebScraping(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # function to test the fetch_top_stories method
    def test_fetch_top_stories(self):
        # set up url
        url = "https://www.ft.com/uk-banks"

        # retrieve top stories from url
        top_stories = web_scraping.fetch_top_stories(url)

        # test that a list is returned that is greater than four
        self.assertIsInstance(top_stories, list)
        self.assertGreaterEqual(len(top_stories), 4)

        # iterate through the stories checking the dictionary returned is formatted correctly
        for story in top_stories:
            # check that the story is an instance of a dictionary
            self.assertIsInstance(story, dict)
            # check the following keys are present in the dictionary
            self.assertIn("headline", story)
            self.assertIn("picture", story)
            self.assertIn("hyperlink", story)

    # test the init_function in web scraping file
    def test_init_web_scraping(self):
        # run the function
        top_stories = web_scraping.init_web_scraping()

        # check a list greater than 4 is returned
        self.assertIsInstance(top_stories, list)
        self.assertGreaterEqual(len(top_stories), 4)


if __name__ == '__main__':
    unittest.main()
