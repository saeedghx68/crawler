class ExportFactory:
    def __init__(self):
        self.__resource_types = {}  # name:class

    def register_type(self, name, klass):
        """
        register file export class on ExportFactory
        :param name: class name
        :param klass: class object
        :return:
        """
        if name in self.__resource_types:
            raise Exception(f'Resource Type {name} Already Registered!')
        self.__resource_types[name] = klass

    def get_type(self, name):
        """
        fetch Class file export from ExportFactory
        :param name: name of class
        :return: file export class
        """
        if name in self.__resource_types.keys():
            return self.__resource_types[name]
        raise Exception(f'Resource Type {name} is Not Registered!')

