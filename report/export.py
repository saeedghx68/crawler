from .export_file.csv import CSV
from .export_file.xml import XML
from .export_factory import ExportFactory


class Export:
    def __init__(self):
        """
        register export file class in export factory
        """
        self.__export_factory = ExportFactory()
        self.__export_factory.register_type('csv', CSV)
        self.__export_factory.register_type('xml', XML)

    def print(self, file_type, data, file_address):
        """
        fetch export file class and call export_file method to generate report file
        :param file_type: [csv | xml] using it we can choose export file class
        :param data: pass to export_file method to print and generate file
        :param file_address: export file path
        :return:
        """
        file_class = self.__export_factory.get_type(file_type)
        file_class.export_file(data, file_address)
