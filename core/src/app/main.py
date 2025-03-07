import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.root import vocabulary
from app.routers.word import word_router

profile = os.environ.get("PROFILE", default="local")


@asynccontextmanager
async def lifespan(api: FastAPI):
    vocabulary_path = "../resources/data/vocabulary.csv" if profile == "local" else "resources/data/vocabulary.csv"
    vocabulary.init(csv_filename=vocabulary_path)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(word_router, prefix="/v1/words", tags=["Word v1 Router"])
