from fastapi import FastAPI
from app.api import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Liberar requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou restrinja para ["http://localhost:3000"] em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
