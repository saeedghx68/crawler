from enum import Enum


class FileType(Enum):
    xml = 1
    csv = 2

    @staticmethod
    def from_string(s):
        try:
            return FileType[s]
        except KeyError:
            raise ValueError()
