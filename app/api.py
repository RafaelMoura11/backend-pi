from fastapi import APIRouter, Query
from app.analytics import carregar_dados, gerar_histograma_preco

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API funcionando"}

@router.get("/grafico-preco")
def grafico_preco(
    cidade: str = Query(None),
    estado: str = Query(None),
    price_min: float = Query(None),
    price_max: float = Query(None),
    bed_min: int = Query(None),
    bath_min: int = Query(None)
):
    df = carregar_dados()
    img_base64 = gerar_histograma_preco(
        df,
        cidade=cidade,
        estado=estado,
        price_min=price_min,
        price_max=price_max,
        bed_min=bed_min,
        bath_min=bath_min
    )
    return {"image": img_base64}
