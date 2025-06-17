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

def gerar_histograma_preco(dados: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(10, 6))
    dados_filtrados = dados[(dados['price'] > 0) & (dados['price'] < 10_000_000)]
    dados_filtrados['price'].hist(bins=50, ax=ax)
    ax.set_title('Distribuição dos preços dos imóveis')
    ax.set_xlabel('Preço')
    ax.set_ylabel('Quantidade de imóveis')

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return img_base64
