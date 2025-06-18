from fastapi import APIRouter
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

    # Aplicar filtros
    if cidade:
        df = df[df['city'].str.lower() == cidade.lower()]
    if estado:
        df = df[df['state'].str.lower() == estado.lower()]
    if price_min is not None:
        df = df[df['price'] >= price_min]
    if price_max is not None:
        df = df[df['price'] <= price_max]
    if bed_min is not None:
        df = df[df['bed'] >= bed_min]
    if bath_min is not None:
        df = df[df['bath'] >= bath_min]

    # Gerar imagem
    img_base64 = gerar_histograma_preco(df)
    return {"image": img_base64}