from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="Backend PySpark + ML")

app.include_router(api_router)

# Para rodar localmente: uvicorn app.main:app --reload
