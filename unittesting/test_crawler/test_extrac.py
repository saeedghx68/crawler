import unittest
import asyncio
from crawl import Crawler


class TestExtractDataUrls(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def test_extract_data_urls(self):
        async def valid_url():
            url = 'http://yoyowallet.com'
            urls = [
                'http://yoyowallet.com',
                'http://yoyowallet.com/',
                'http://yoyowallet.com/about.html',
                'http://yoyowallet.com/assets.html',
                'http://yoyowallet.com/banks/index.html',
                'http://yoyowallet.com/basket-data.html',
                'http://yoyowallet.com/careers.html',
                'http://yoyowallet.com/case-studies/caffe-nero-case-study.html',
                'http://yoyowallet.com/caterers/index.html',
                'http://yoyowallet.com/cookies.html',
                'http://yoyowallet.com/epos.html',
                'http://yoyowallet.com/get-in-touch.html',
                'http://yoyowallet.com/retailers/index.html']
            all_urls = {
                'http://yoyowallet.com/about.html',
                'http://yoyowallet.com/case-studies/caffe-nero-case-study.html',
                'http://yoyowallet.com/careers.html',
                'http://yoyowallet.com/banks/index.html',
                'http://yoyowallet.com',
                'http://yoyowallet.com/assets.html',
                'http://yoyowallet.com/caterers/index.html',
                'http://yoyowallet.com/cookies.html',
                'http://yoyowallet.com/',
                'http://yoyowallet.com/basket-data.html',
                'http://yoyowallet.com/epos.html',
                'http://yoyowallet.com/retailers/index.html',
                'http://yoyowallet.com/get-in-touch.html'}
            crawler = Crawler(url)
            _url, data, _urls, _all_urls = await crawler.extract(url)
            self.assertEqual(_url, url)
            self.assertListEqual(_urls, urls)
            self.assertSetEqual(_all_urls, all_urls)
        self.loop.run_until_complete(valid_url())
