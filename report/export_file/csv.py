import csv


class CSV:
    @classmethod
    def export_file(cls, data, file_address):
        """
        export csv file in file_address path
        :param data: the data that we want to create csv file
        :param file_address: path of file address
        :return:
        """
        with open(file_address, mode='w') as csv_file:
            fieldnames = [
                'url',
                'urls',
                'css_links',
                'js_links',
                'img_links',
                'icon_links']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for url, items in data:
                writer.writerow({
                    'url': url,
                    'urls': ','.join(items['urls']),
                    'css_links': ','.join(items.get('css_links', [])),
                    'js_links': ','.join(items.get('js_links', [])),
                    'img_links': ','.join(items.get('img_links', [])),
                    'icon_links': ','.join(items.get('icon_links', [])),
                })
