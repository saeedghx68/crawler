from .export_file.csv import CSV
from .export_file.xml import XML
from .export_factory import ExportFactory


class Export:
    def __init__(self):
        self.__export_factory = ExportFactory()
        self.__export_factory.register_type('csv', CSV)
        self.__export_factory.register_type('xml', XML)

    def print(self, file_type, data, file_address):
        file_class = self.__export_factory.get_type(file_type)
        file_class.export_file(data, file_address)
