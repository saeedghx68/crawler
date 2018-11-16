import asyncio
import argparse
from crawl import Crawler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a crawler that can fetch urls, css links, js links and image links')
    parser.add_argument('-u', '--url', required=True, type=str, help='for example => http://yoyowallet.com/')
    args = parser.parse_args()
    crawler = Crawler(args.url)
    task = asyncio.Task(crawler.crawl())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    loop.close()
    result = task.result()
    print(result)
