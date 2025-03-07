from enum import Enum


class EnglishLevel(str, Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

    def __lt__(self, other):
        levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
        return levels.index(self.value) < levels.index(other.value)
