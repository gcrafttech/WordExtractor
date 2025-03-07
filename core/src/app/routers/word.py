from typing import List

from fastapi import APIRouter, UploadFile, File

from app.constants.eng_level import EnglishLevel
from app.dto.word import Word
from app.root import english_word_service, pdf_reader

word_router = APIRouter()


@word_router.post("", response_model=List[Word])
def get_words(min_level: EnglishLevel,
              pdf_file: UploadFile = File(...)) -> List[Word]:
    pdf_bytes = pdf_file.file.read()
    text = pdf_reader.extract_text(pdf_bytes)

    return english_word_service.find_all_by_min_level(min_level=min_level,
                                                      text=text)
