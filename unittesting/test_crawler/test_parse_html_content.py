import unittest
from crawl import Crawler


class TestParseHtmlContent(unittest.TestCase):

    def test_parse_html_content(self):
        html = """
        <!DOCTYPE html>
        <html>
            <title>Test</title>
            <link rel="stylesheet" href="/assets/v2/css/app.css">
            <link rel="stylesheet" href="/assets/v2/css/app2.css">
            <link rel="apple-touch-icon" sizes="152x152" href="/assets/v2/apple-icon-152x152.png">
            <link rel="icon" type="image/png" sizes="192x192" href="/assets/v2/android-icon-192x192.png">
            <link href="/assets/v2/favicon.ico" rel="shortcut icon">
            <link href="/assets/v2/apple-touch-icon.png" rel="apple-touch-icon">
        <body>
            <a href='test1'/>
            <a href='test2'/>
            <div class="col-lg-6">
               <img src="/assets/v2/images/screen-yoyo-apps-2x.png" class="hero-img"/>
            </div>
            <script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/v2.js"></script>
        </body>
        </html>
        """
        data = {
            'css_links': {
                'http://test.com/assets/v2/css/app2.css',
                'http://test.com/assets/v2/css/app.css'},
            'js_links': {'http://js.hsforms.net/forms/v2.js'},
            'img_links': {'http://test.com/assets/v2/images/screen-yoyo-apps-2x.png'},
            'icon_links': {
                'http://test.com/assets/v2/apple-touch-icon.png',
                'http://test.com/assets/v2/android-icon-192x192.png',
                'http://test.com/assets/v2/favicon.ico',
                'http://test.com/assets/v2/apple-icon-152x152.png'}}
        crawler = Crawler('http://test.com')
        result = crawler.parse_html_content(html)
        self.assertSetEqual(result['css_links'], data['css_links'])
        self.assertSetEqual(result['js_links'], data['js_links'])
        self.assertSetEqual(result['img_links'], data['img_links'])
        self.assertSetEqual(result['icon_links'], data['icon_links'])

    def test_parse_empty_html_content(self):
        html = ""
        data = {}
        crawler = Crawler('http://test.com')
        result = crawler.parse_html_content(html)
        self.assertDictEqual(result, data)
