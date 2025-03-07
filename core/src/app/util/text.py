import re
from typing import List, Dict

from cachetools import cached, TTLCache


class TextParser:

    @cached(TTLCache(maxsize=100, ttl=60 * 30))
    def extract_words(self, text: str) -> List[str]:
        words = re.findall(r'\b\w+\b', text)

        return words

    @cached(TTLCache(maxsize=100, ttl=60 * 30))
    def build_word_sentence_map(self, text: str) -> Dict[str, str]:
        sentences = re.split(r'(?<=[.!?])\s+', text)

        word_sentence_map = {}

        for sentence in sentences:
            if len(sentence) > 250:
                continue

            words = re.findall(r'\b\w+\b', sentence.lower())
            for word in words:
                if word not in word_sentence_map:
                    word_sentence_map[word] = sentence

        return word_sentence_map
