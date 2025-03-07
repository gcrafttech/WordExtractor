from app.services.word import EnglishWordService
from app.util.pdf import PdfReader
from app.util.text import TextParser
from app.util.vocabulary import Vocabulary

vocabulary = Vocabulary()
text_parser = TextParser()
english_word_service = EnglishWordService(vocabulary=vocabulary, text_parser=text_parser)
pdf_reader = PdfReader()
