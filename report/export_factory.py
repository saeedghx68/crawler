class ExportFactory:
    def __init__(self):
        self.__resource_types = {}  # name:class

    def register_type(self, name, klass):
        if name in self.__resource_types:
            raise Exception(f'Resource Type {name} Already Registered!')
        self.__resource_types[name] = klass

    def get_type(self, name):
        if name in self.__resource_types.keys():
            return self.__resource_types[name]
        raise Exception(f'Resource Type {name} is Not Registered!')

