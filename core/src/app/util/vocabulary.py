import csv
from typing import Optional, Dict

from app.constants.eng_level import EnglishLevel


class Vocabulary:

    def __init__(self):
        self._word_level: Dict[str, EnglishLevel] = {}

    def init(self, csv_filename: str):
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                words, level = row[0], row[1]
                for word in words.split("/"):
                    self._word_level[word.strip()] = EnglishLevel(level)

    def get_word_level(self, word: str) -> Optional[EnglishLevel]:
        return self._word_level.get(word.lower(), None)
