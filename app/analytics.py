import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import sqlalchemy

# String de conexão ao banco Neon
DATABASE_URL = "postgresql://banco_pi_owner:npg_nLSXmdj45eAQ@ep-cool-wildflower-a8xnke2o-pooler.eastus2.azure.neon.tech/banco_pi?sslmode=require"

# Engine do SQLAlchemy
engine = sqlalchemy.create_engine(DATABASE_URL)

def carregar_dados():
    query = "SELECT * FROM real_estate"
    df = pd.read_sql(query, engine)
    return df

def gerar_histograma_preco(
    dados: pd.DataFrame,
    cidade: str = None,
    estado: str = None,
    price_min: float = None,
    price_max: float = None,
    bed_min: int = None,
    bath_min: int = None
) -> str:
    # Aplicar filtros
    if cidade:
        dados = dados[dados['city'].str.lower() == cidade.lower()]
    if estado:
        dados = dados[dados['state'].str.lower() == estado.lower()]
    if price_min is not None:
        dados = dados[dados['price'] >= price_min]
    if price_max is not None:
        dados = dados[dados['price'] <= price_max]
    if bed_min is not None:
        dados = dados[dados['bed'] >= bed_min]
    if bath_min is not None:
        dados = dados[dados['bath'] >= bath_min]

    # Remover valores extremos
    dados_filtrados = dados[(dados['price'] > 0) & (dados['price'] < 10_000_000)]

    # Gerar gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    dados_filtrados['price'].hist(bins=50, ax=ax, color='skyblue', edgecolor='black')

    titulo = "Distribuição dos Preços dos Imóveis"
    if cidade and estado:
        titulo += f" - {cidade}, {estado}"
    elif estado:
        titulo += f" - {estado}"
    elif cidade:
        titulo += f" - {cidade}"

    ax.set_title(titulo)
    ax.set_xlabel('Preço (USD)')
    ax.set_ylabel('Quantidade de Imóveis')
    plt.tight_layout()

    # Converter imagem para base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return img_base64
