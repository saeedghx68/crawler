from xml.dom import minidom


class XML:
    @classmethod
    def export_file(cls, data, file_address):
        """
        export xml file in file_address path
        :param data: the data that we want to create csv file
        :param file_address: path of file address
        :return:
        """

        # create root element
        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)

        # loop over data to create xml node
        for url, items in data:
            url_child = root.createElement("url")
            url_child.setAttribute('link', url)

            # add url
            child_of_url = root.createElement('urls')
            url_child.appendChild(child_of_url)
            for link in items.get('urls', []):
                child_of_child_of_url = root.createElement('url')
                child_of_child_of_url.appendChild(root.createTextNode(link))
                child_of_url.appendChild(child_of_child_of_url)

            # add css links
            child_of_url = root.createElement('css_links')
            url_child.appendChild(child_of_url)
            for link in items.get('css_links', []):
                child_of_child_of_url = root.createElement('css_link')
                child_of_child_of_url.appendChild(root.createTextNode(link))
                child_of_url.appendChild(child_of_child_of_url)

            # add js links
            child_of_url = root.createElement('js_links')
            url_child.appendChild(child_of_url)
            for link in items.get('js_links', []):
                child_of_child_of_url = root.createElement('js_link')
                child_of_child_of_url.appendChild(root.createTextNode(link))
                child_of_url.appendChild(child_of_child_of_url)

            # add img links
            child_of_url = root.createElement('img_links')
            url_child.appendChild(child_of_url)
            for link in items.get('img_links', []):
                child_of_child_of_url = root.createElement('img_link')
                child_of_child_of_url.appendChild(root.createTextNode(link))
                child_of_url.appendChild(child_of_child_of_url)

            # add icon links
            child_of_url = root.createElement('icon_links')
            url_child.appendChild(child_of_url)
            for link in items.get('icon_links', []):
                child_of_child_of_url = root.createElement('icon_link')
                child_of_child_of_url.appendChild(root.createTextNode(link))
                child_of_url.appendChild(child_of_child_of_url)

            xml.appendChild(url_child)

        xml_str = root.toprettyxml('\t')
        with open(file_address, "w") as f:
            f.write(xml_str)
