from enum import Enum


class FileType(Enum):
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
