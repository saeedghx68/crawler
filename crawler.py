import asyncio
import argparse
from crawl import Crawler
from report.file_type import FileType
from report.export import Export

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This is a crawler that can fetch urls, css links, js links and image links')
    parser.add_argument(
        '-u',
        '--url',
        required=True,
        type=str,
        help='For example => http://yoyowallet.com/')
    parser.add_argument(
        '-o',
        '--out',
        required=True,
        type=str,
        help='You have to enter a valid file address')
    parser.add_argument(
        '-t',
        '--type',
        required=True,
        type=FileType.from_string,
        choices=list(FileType),
        help='You have to choose one of theme => csv or xml')
    args = parser.parse_args()
    crawler = Crawler(str(args.url))
    task = asyncio.Task(crawler.crawl())
    loop = asyncio.get_event_loop()
    print(f'\n{30*"*"} crawler is working {30*"*"}\n\n')
    loop.run_until_complete(task)
    loop.close()
    result = task.result()
    print(f'\n\n{30*"*"} crawling was done {30*"*"}\n\n')
    Export().print(str(args.type), result, str(args.out))
    print(f'{30*"*"} output save on {args.out} {30*"*"}\n')
