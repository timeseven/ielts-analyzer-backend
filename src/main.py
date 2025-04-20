from fastapi import FastAPI

from src.config import settings
from src.routes import analyze_router

app = FastAPI()


app.include_router(analyze_router, prefix=settings.API_V1_STR)
