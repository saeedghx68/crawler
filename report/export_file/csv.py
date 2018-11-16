import csv

class CSV:
    @classmethod
    def export_file(cls, data, file_address):
        with open(file_address, mode='w') as csv_file:
            fieldnames = ['url', 'urls', 'css_links', 'js_links', 'img_links', 'icon_links']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for url, items in data:
                writer.writerow({
                    'url': url,
                    'urls': ','.join(items['urls']),
                    'css_links': ','.join(items['css_links']),
                    'js_links': ','.join(items['js_links']),
                    'img_links': ','.join(items['img_links']),
                    'icon_links': ','.join(items['icon_links']),
            })

