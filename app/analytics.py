import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def carregar_dados(caminho_csv: str) -> pd.DataFrame:
    # mesma lógica de leitura com fallback
    try:
        dados = pd.read_csv(caminho_csv, sep=',', encoding='utf-8')
    except UnicodeDecodeError:
        dados = pd.read_csv(caminho_csv, sep=',', encoding='latin1')
    return dados

def gerar_histograma_preco(dados: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(10,6))
    dados_filtrados = dados[(dados['price'] > 0) & (dados['price'] < 10_000_000)]
    dados_filtrados['price'].hist(bins=50, ax=ax)
    ax.set_title('Distribuição dos preços dos imóveis')
    ax.set_xlabel('Preço')
    ax.set_ylabel('Quantidade de imóveis')
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return img_base64
