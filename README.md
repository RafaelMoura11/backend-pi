# 📦 Backend - API de Análise de Imóveis

## 🧠 Propósito

Este backend foi desenvolvido como parte de um projeto de análise imobiliária que permite a visualização de gráficos interativos com base em dados de imóveis. Ele fornece uma **API RESTful** que:
- Realiza autenticação via JWT.
- Permite o registro e login de usuários.
- Retorna um gráfico de histograma com base em filtros como cidade, estado, preço, número de quartos e banheiros.
- Conecta-se a um banco de dados PostgreSQL hospedado na plataforma **Neon**.

---

## 🚀 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** – Framework web moderno e rápido para Python.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** – ORM para manipulação do banco de dados.
- **[PostgreSQL](https://www.postgresql.org/)** – Banco de dados relacional utilizado.
- **[Neon](https://neon.tech/)** – Plataforma usada para hospedar o banco.
- **[Uvicorn](https://www.uvicorn.org/)** – Servidor ASGI para rodar o FastAPI.
- **[Passlib](https://passlib.readthedocs.io/)** – Para hashing de senhas.
- **[Python-Jose](https://python-jose.readthedocs.io/)** – Para geração e verificação de tokens JWT.
- **[Matplotlib](https://matplotlib.org/)** – Para gerar o histograma dos preços.
- **[Pandas](https://pandas.pydata.org/)** – Manipulação de dados tabulares.

---

## 🔧 Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/backend-imoveis.git
cd backend-imoveis
```

### 2. Crie um ambiente virtual e ative

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o servidor

```bash
uvicorn app.main:app --reload
```

> A aplicação estará disponível por padrão em `http://127.0.0.1:8000`

---

## 🌐 Rotas da API

### `POST /register`
Registra um novo usuário.  
Parâmetros via **query**: `name`, `email`, `password`.

### `POST /login`
Realiza login e retorna token JWT.  
Parâmetros via **query**: `email`, `password`.

### `GET /grafico-preco`
Gera um histograma com base nos filtros fornecidos:  
Parâmetros (todos opcionais):
- `cidade`
- `estado`
- `price_min`
- `price_max`
- `bed_min`
- `bath_min`

---

## 🛠️ Conexão com o Banco de Dados

A conexão é feita via string do SQLAlchemy, já configurada no arquivo `analytics.py`:

```python
DATABASE_URL = "postgresql://banco_pi_owner:<senha>@ep-cool-wildflower-<...>.neon.tech/banco_pi?sslmode=require"
```

Você pode configurar variáveis de ambiente se desejar manter a URL fora do código.

---

## ☁️ Deploy

A aplicação está preparada para ser **deployada no [Render](https://render.com/)** com suporte a Docker. O Dockerfile já está configurado, e as dependências estão no `requirements.txt`.

---

## 🧪 Testes

Testes manuais podem ser feitos via Swagger:

> Acesse `http://127.0.0.1:8000/docs` ou `/redoc`

---

## 📁 Estrutura

```
app/
│
├── main.py         # Ponto de entrada
├── auth.py         # Autenticação e JWT
├── database.py     # Configuração do banco via SQLAlchemy
├── models.py       # Modelos do banco (User)
├── utils.py        # Utilidades (hash, JWT)
├── analytics.py    # Lógica de gráficos e conexão ao Neon
```

---

## ✅ Requisitos

- Python 3.10+
- Conta na plataforma [Neon](https://neon.tech/)
- Render (ou outra plataforma de cloud para deploy, opcional)

---

## 👨‍💻 Autor

Projeto desenvolvido por Rafael Moura como parte de um projeto acadêmico/técnico.
