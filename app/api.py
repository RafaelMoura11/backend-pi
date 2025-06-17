from fastapi import APIRouter
from app.analytics import carregar_dados, gerar_histograma_preco

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API funcionando"}

@router.get("/grafico-preco")
def grafico_preco():
    df = carregar_dados()
    img_base64 = gerar_histograma_preco(df)
    return {"image": img_base64}
