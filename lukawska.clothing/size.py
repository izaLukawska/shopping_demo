from enum import Enum


class Size(Enum):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"

    def __str__(self):
        return self.value
