from xml.dom import minidom


class XML:
    @classmethod
    def export_file(cls, data, file_address):
        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)
        for url, items in data:
            urlChild = root.createElement("url")
            urlChild.setAttribute('link', url)

            # add url
            childOfUrl = root.createElement('urls')
            urlChild.appendChild(childOfUrl)
            for link in items['urls']:
                childOfChildOfUrl = root.createElement('url')
                childOfChildOfUrl.appendChild(root.createTextNode(link))
                childOfUrl.appendChild(childOfChildOfUrl)

            # add css links
            childOfUrl = root.createElement('css_links')
            urlChild.appendChild(childOfUrl)
            for link in items['css_links']:
                childOfChildOfUrl = root.createElement('css_link')
                childOfChildOfUrl.appendChild(root.createTextNode(link))
                childOfUrl.appendChild(childOfChildOfUrl)

            # add js links
            childOfUrl = root.createElement('js_links')
            urlChild.appendChild(childOfUrl)
            for link in items['js_links']:
                childOfChildOfUrl = root.createElement('js_link')
                childOfChildOfUrl.appendChild(root.createTextNode(link))
                childOfUrl.appendChild(childOfChildOfUrl)

            # add img links
            childOfUrl = root.createElement('img_links')
            urlChild.appendChild(childOfUrl)
            for link in items['img_links']:
                childOfChildOfUrl = root.createElement('img_link')
                childOfChildOfUrl.appendChild(root.createTextNode(link))
                childOfUrl.appendChild(childOfChildOfUrl)

            # add icon links
            childOfUrl = root.createElement('icon_links')
            urlChild.appendChild(childOfUrl)
            for link in items['icon_links']:
                childOfChildOfUrl = root.createElement('icon_link')
                childOfChildOfUrl.appendChild(root.createTextNode(link))
                childOfUrl.appendChild(childOfChildOfUrl)

            xml.appendChild(urlChild)

        xml_str = root.toprettyxml('\t')
        with open(file_address, "w") as f:
            f.write(xml_str)
