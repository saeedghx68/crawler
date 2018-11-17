import unittest
import asyncio
from crawl import Crawler


class TestGetBody(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def test_valid_url(self):
        async def valid_url():
            url = 'http://yoyowallet.com'
            crawler = Crawler('')
            result = await crawler.get_body(url)
            self.assertTrue(result)
        self.loop.run_until_complete(valid_url())

    def test_invalid_url(self):
        async def invalid_url():
            url = 'http://yoyowalletxxxx.com'
            crawler = Crawler('')
            result = await crawler.get_body(url)
            self.assertEqual(result, '')
        self.loop.run_until_complete(invalid_url())
