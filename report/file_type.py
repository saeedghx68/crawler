from enum import Enum


class FileType(Enum):
    """
    This class is using for argparse package and we want to select only csv or xml to choose file type output
    """
    xml = 1
    csv = 2

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return FileType[s]
        except KeyError:
            raise ValueError()
