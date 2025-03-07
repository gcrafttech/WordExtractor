import os
import tempfile
import uuid

import fitz
from cachetools import cached, TTLCache


class PdfReader:

    @cached(TTLCache(maxsize=200, ttl=60 * 30))
    def extract_text(self, pdf_bytes: bytes) -> str:
        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, f"{uuid.uuid4()}.pdf")

        with open(temp_file_path, "wb") as f:
            f.write(pdf_bytes)

        text = ""
        with fitz.open(temp_file_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"

        os.remove(temp_file_path)

        return text
