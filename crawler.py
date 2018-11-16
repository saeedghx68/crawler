import asyncio
import async_timeout
import aiohttp
from urllib.parse import urljoin, urlparse
from lxml import html as lh


class Crawler:
    def __init__(self, start_url, max_async_call=200):
        self.start_url = start_url
        self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.base_url = f'{urlparse(self.start_url).scheme}://{urlparse(self.start_url).netloc}'
        self.max_async_call = max_async_call
        self.visited_urls = set()

    async def get_body(self, url):
        print(f'{30*"-"} > Get Body: {url}')
        async with aiohttp.ClientSession() as session:
            try:
                with async_timeout.timeout(30):
                    async with session.get(url, headers=self.headers) as response:
                        html = await response.read()
                        return html
            except Exception as err:
                print(err)
                return ''


    def fetch_urls(self, html):
        urls = []
        dom = lh.fromstring(html)
        for href in dom.xpath('//a/@href'):
            url = urljoin(self.base_url, href)
            if url not in self.visited_urls and url.startswith(self.base_url):
                urls.append(url)
        return urls

    async def extract(self, url):
        data = await self.get_body(url)
        urls = set()
        if data:
            for url in self.fetch_urls(data):
                urls.add(url)
        return url, data, sorted(urls)

    async def extract_data_urls(self, urls):
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
        fetch_urls = [self.start_url]
        results = []
        while len(fetch_urls):
            urls = await self.extract_data_urls(fetch_urls[0:self.max_async_call])
            del fetch_urls[0:self.max_async_call]
            fetch_urls = []
            for url, data, found_urls in urls:
                fetch_urls.extend(found_urls)
                result = self.parse_html_content(data)
                results.append((url, result))
        return results

    def parse_html_content(self, data):
        result = {}
        if data == '':
           return result
        dom = lh.fromstring(data)
        result['css_links'] = {urljoin(self.base_url, href) for href in dom.xpath('//link[@rel="stylesheet"]/@href')}
        result['js_links'] = {urljoin(self.base_url, src) for src in dom.xpath('//script/@src')}
        result['img_links'] = {urljoin(self.base_url, src) for src in dom.xpath('//img/@src')}
        result['icon_links'] = {urljoin(self.base_url, src) for src in dom.xpath('//link[contains(@rel,"icon")]/@href')}
        return result


if __name__ == '__main__':
    url = 'http://yoyowallet.com/'
    crawler = Crawler(url)
    task = asyncio.Task(crawler.crawl())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    loop.close()
    result = task.result()
    print(result)
