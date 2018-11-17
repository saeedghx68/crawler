import os
import asyncio
import async_timeout
import aiohttp
from aiohttp import ServerDisconnectedError, ClientResponseError, ClientConnectorError
from urllib.parse import urljoin, urlparse
from lxml import html as lh
from logger import global_logger


class Crawler:
    def __init__(self, start_url, max_async_call=200):
        self.start_url = start_url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.base_url = f'{urlparse(self.start_url).scheme}://{urlparse(self.start_url).netloc}'
        self.max_async_call = max_async_call
        self.visited_urls = set()

    async def get_body(self, url):
        """
        open url with aiohttp package
        :param url: url address
        :return: return html content of url if url is not valid then return ''
        """
        print(f'{30*"-"} > Get Body: {url}')
        try:
            async with aiohttp.ClientSession() as session:
                try:
                    with async_timeout.timeout(30):
                        async with session.get(url, headers=self.headers) as response:
                            html = await response.read()
                            return html
                except (asyncio.TimeoutError, ValueError):
                    global_logger.write_log('error', f"error: {ValueError}")
        except (ServerDisconnectedError, ClientResponseError, ClientConnectorError) as s:
            global_logger.write_log('error', f"error: {s}")
        except (Exception, ValueError):
            global_logger.write_log('error', f"error: {ValueError}")
        return ''

    def fetch_urls(self, html):
        """
        fetch all of urls which are'nt in visited_urls
        :param html: html content
        :return: return new urls and all_urls in the html content
        """
        urls = []
        all_urls = set()
        dom = lh.fromstring(html)
        for href in dom.xpath('//a/@href'):
            url = urljoin(self.base_url, href)
            path = urlparse(url).path
            ext = os.path.splitext(path)[1]
            if bool(ext) and ext not in ['.html', '.htm']:
                continue
            if url not in self.visited_urls and url.startswith(self.base_url):
                urls.append(url)
            if url not in all_urls and url.startswith(self.base_url):
                all_urls.add(url)
        return urls, all_urls

    async def extract(self, url):
        data = await self.get_body(url)
        urls, all_urls = set(), []
        if data:
            urls, all_urls = self.fetch_urls(data)
            urls = set(urls)
        return url, data, sorted(urls), all_urls

    async def extract_data_urls(self, urls):
        """
        This method can extract all data from list of url and every url add to visited_urls set
        :param urls: list of ulr
        :return: result of urls data which contains url, data, sorted(urls), all_urls
        """
        futures, results = [], []
        for url in urls:
            if url in self.visited_urls:
                continue
            self.visited_urls.add(url)
            futures.append(self.extract(url))

        for future in asyncio.as_completed(futures):
            results.append((await future))
        return results

    async def crawl(self):
        """
        The main method that you want crawl a domain
        :return: A list of result that contain a url and dictionary
        which is in set objects (css_links, js_links, img_links, and icon_links)
        """
        fetch_urls = [self.start_url]
        results = []
        while len(fetch_urls):
            """
            slicing array urls with max_async_call arg and then run extract_data_urls
            extract_data_urls return a object that contains url, data, found_urls, and all_urls
            url is a url that we crawled
            data is Html content of the url
            found_urls are new urls that we have to crawl that
            all_urls are all links in the html page
            """
            urls = await self.extract_data_urls(fetch_urls[0:self.max_async_call])
            del fetch_urls[0:self.max_async_call]
            for url, data, found_urls, all_urls in urls:
                fetch_urls.extend(found_urls)
                result = self.parse_html_content(data)
                result['urls'] = all_urls
                results.append((url, result))
        return results

    def parse_html_content(self, data):
        """
        parse html data to fetch css_links, js_links, img_links, and icon_links using lxml
        :param data:
        :return: a dictionary of set objects that contains css_links, js_links, img_links, and icon_links
        """
        result = {}
        if data == '':
            return result
        dom = lh.fromstring(data)
        result['css_links'] = {
            urljoin(
                self.base_url,
                href) for href in dom.xpath('//link[@rel="stylesheet"]/@href')}
        result['js_links'] = {urljoin(self.base_url, src)
                              for src in dom.xpath('//script/@src')}
        result['img_links'] = {urljoin(self.base_url, src)
                               for src in dom.xpath('//img/@src')}
        result['icon_links'] = {
            urljoin(
                self.base_url,
                src) for src in dom.xpath('//link[contains(@rel,"icon")]/@href')}
        return result
