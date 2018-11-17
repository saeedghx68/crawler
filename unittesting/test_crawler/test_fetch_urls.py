import unittest
from crawl import Crawler


class TestFetchUrl(unittest.TestCase):

    def test_fetch_urls(self):
        html = """
        <!DOCTYPE html>
        <html>
        <title>Test</title>
        <body>
        <a href='link1'/>
        <a href='link2'/>
        </body>
        </html>
        """
        crawler = Crawler('http://test.com')
        fetch_urls, all_urls = crawler.fetch_urls(html)
        self.assertListEqual(
            fetch_urls, [
                'http://test.com/link1', 'http://test.com/link2'])
        self.assertSetEqual(
            all_urls, {
                'http://test.com/link2', 'http://test.com/link1'})
