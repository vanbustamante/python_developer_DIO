import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configurações da Aplicação ---
PROJECT_NAME = "API Bancária Assíncrona"
PROJECT_VERSION = "1.0.0"
API_PREFIX = "/api/v1"

# --- Configurações JWT ---
# SECRET_KEY é lida do arquivo .env
SECRET_KEY = os.getenv("SECRET_KEY", "UM_DEFAULT_SEGURO_SE_NAO_ENV_DE_PRODUCAO")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# --- Configurações do Banco de Dados ---
# DATABASE_URL é lida do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
