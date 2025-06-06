from fastapi import FastAPI
from src.database import Base, engine 
from src.config import PROJECT_NAME, PROJECT_VERSION, API_PREFIX
from src.controllers.account import router as account_router
from src.controllers.transaction import router as transaction_router
from src.controllers.auth import router as auth_router


app = FastAPI(
    title=PROJECT_NAME,
    version=PROJECT_VERSION,
    description="API RESTful para gerenciar operações bancárias com FastAPI e autenticação JWT.",
    openapi_url=f"{API_PREFIX}/openapi.json",
    docs_url=f"{API_PREFIX}/docs",
    redoc_url=f"{API_PREFIX}/redoc"
)

app.include_router(auth_router, prefix=API_PREFIX, tags=["Autenticação"])
app.include_router(account_router, prefix=API_PREFIX, tags=["Contas"])
app.include_router(transaction_router, prefix=API_PREFIX, tags=["Transações"])


@app.get(f"{API_PREFIX}/health", summary="Verifica a saúde da API")
async def health_check():
    return {"status": "ok", "message": "API está funcionando!"}