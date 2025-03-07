from typing import List

from app.constants.eng_level import EnglishLevel
from app.dto.word import Word
from app.util.text import TextParser
from app.util.vocabulary import Vocabulary


class EnglishWordService:

    def __init__(self, vocabulary: Vocabulary,
                 text_parser: TextParser):
        self._vocabulary = vocabulary
        self._text_parser = text_parser

    def find_all_by_min_level(self,
                              min_level: EnglishLevel,
                              text: str) -> List[Word]:
        result: List[Word] = []
        words = self._text_parser.extract_words(text)
        unique_words = set(words)
        word_in_sentence = self._text_parser.build_word_sentence_map(text=text)
        for word in unique_words:
            level = self._vocabulary.get_word_level(word)
            if not level:
                continue
            if level >= min_level:
                if word not in word_in_sentence:
                    continue

                used_in_sentence = word_in_sentence[word]
                result.append(Word(value=word, level=level, used_in_sentence=used_in_sentence))

        return result
