# API Bancária Assíncrona com FastAPI

Este projeto implementa uma API RESTful para gerenciar operações bancárias de depósito e saque em contas correntes. Ele utiliza o framework FastAPI, SQLAlchemy para interação com o banco de dados e autenticação JWT para proteger os endpoints.

## Funcionalidades Principais

-   **Cadastro de Contas:** Crie novas contas bancárias.
-   **Autenticação de Usuário (JWT):** Login para obter um token de acesso.
-   **Depósito:** Realize depósitos em uma conta.
-   **Saque:** Realize saques de uma conta, com validação de saldo.
-   **Extrato:** Visualize todas as transações de uma conta.

## Tecnologias Utilizadas

-   **FastAPI:** Framework web assíncrono.
-   **SQLAlchemy:** ORM para interação com o banco de dados (SQLite para desenvolvimento).
-   **Pydantic:** Validação e serialização de dados.
-   **JWT (JSON Web Tokens):** Para autenticação e autorização.
-   **Poetry:** Gerenciamento de dependências e ambiente virtual.
-   **Alembic:** Migrações de banco de dados.

## Estrutura do Projeto

O código é organizado em camadas para separar as responsabilidades:

banco_api/
├── .env                    # Variáveis de ambiente (não versionado)
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore              # Arquivos e pastas a serem ignorados pelo Git
├── README.md               # Este arquivo de documentação
├── alembic.ini             # Configuração do Alembic (migrações de DB)
├── poetry.lock             # Arquivo de bloqueio de dependências do Poetry
├── pyproject.toml          # Configuração do projeto e dependências do Poetry
├── migrations/             # Scripts de migração de banco de dados (gerenciados pelo Alembic)
│   ├── versions/           # Arquivos de versão das migrações
│   ├── env.py              # Script de ambiente do Alembic
│   └── script.py.mako      # Template para novas migrações
└── src/                    # Código-fonte principal da aplicação
├── controllers/        # Camada de controle: Recebe requisições HTTP e delega para serviços.
│   ├── account.py
│   ├── auth.py
│   └── transaction.py
├── models/             # Definição dos modelos de dados (SQLAlchemy ORM).
│   ├── account.py
│   └── transaction.py
├── schemas/            # Schemas Pydantic para validação de entrada/saída de dados.
│   ├── account.py
│   ├── auth.py
│   └── transaction.py
├── services/           # Camada de lógica de negócio: Contém as regras e validações da aplicação.
│   ├── account.py
│   └── transaction.py
├── views/              # Camada de visualização: Formatação de respostas (opcional, para transformações de saída).
│   ├── account.py
│   ├── auth.py
│   └── transaction.py
├── config.py           # Configurações globais da aplicação e variáveis de ambiente.
├── database.py         # Configuração da conexão e sessão do banco de dados.
├── exceptions.py       # Definição de exceções personalizadas da aplicação.
├── main.py             # Ponto de entrada da aplicação FastAPI.
└── security.py         # Funções para segurança (hashing de senhas, criação/validação JWT).

## Como Executar Localmente

Para executar este projeto em sua máquina, siga os passos abaixo.

Pré-requisitos:

-   Python 3.9+
-   Poetry (ferramenta de gerenciamento de dependências)

# 1. Clone o repositório para sua máquina
git clone https://github.com/SEU_USUARIO/python_developer_DIO.git

# 2. Navegue até o diretório da API
cd python_developer_DIO/banco_api/

# 3. Instale as dependências do projeto com Poetry
# Isso criará um ambiente virtual e instalará tudo que está no pyproject.toml
poetry install

# 4. Configure as variáveis de ambiente
# Copie o arquivo de exemplo para criar seu próprio arquivo de configuração
cp .env.example .env
# Agora, abra o arquivo '.env' e adicione uma SECRET_KEY (pode ser qualquer string longa e aleatória)

# 5. Aplique as migrações do banco de dados
# Este comando criará o arquivo de banco de dados (SQLite) com todas as tabelas necessárias
poetry run alembic upgrade head

# 6. Inicie o servidor da API
poetry run uvicorn src.main:app --reload

🚀 Pronto! A API estará em execução e disponível em http://127.0.0.1:8000.

Acesse a documentação interativa (Swagger UI) para explorar e testar os endpoints em:
http://127.0.0.1:8000/docs
