import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os
import gdown

def carregar_dados():
    file_id = "14vCXaKwQSF_MMGX-WCu093Y_lvwzIfpw"
    url = f"https://drive.google.com/uc?id={file_id}"
    output = "realtor-data.csv"

    # Baixar somente se ainda não estiver salvo localmente
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

    df = pd.read_csv(output)

    print("Colunas disponíveis:", df.columns.tolist())  # Para debug

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
