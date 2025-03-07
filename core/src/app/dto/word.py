from typing import Optional

from pydantic import BaseModel

from app.constants.eng_level import EnglishLevel


class Word(BaseModel):
    value: Optional[str]
    level: Optional[EnglishLevel]
    used_in_sentence: Optional[str]
