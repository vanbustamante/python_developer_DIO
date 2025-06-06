# src/controllers/account.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.account import Account, AccountCreate
from src.schemas.transaction import Transaction as TransactionSchema # <--- Certifique-se que TransactionSchema está importado
from src.services.account import AccountService
from src.security import decode_access_token
from src.exceptions import CredentialsException
from src.schemas.auth import TokenData
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

async def get_current_account(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = decode_access_token(token)
    account_service = AccountService(db)
    account = account_service.get_account_by_number(token_data.username)
    if not account:
        raise CredentialsException(detail="Credenciais inválidas ou conta não encontrada.")
    return account

router = APIRouter()

@router.post("/accounts/", response_model=Account, status_code=status.HTTP_201_CREATED, summary="Criar nova conta bancária")
async def create_account_controller(account_data: AccountCreate, db: Session = Depends(get_db)):
    account_service = AccountService(db)
    new_account = account_service.create_account(account_data)
    return new_account

@router.get("/accounts/me", response_model=Account, summary="Obter detalhes da conta autenticada")
async def read_current_account_controller(current_account: Account = Depends(get_current_account)):
    return current_account

# CORRIGIDO: Altere o response_model para list[TransactionSchema]
@router.get("/accounts/me/statement", response_model=list[TransactionSchema], summary="Obter extrato da conta autenticada")
async def get_account_statement_controller(current_account: Account = Depends(get_current_account), db: Session = Depends(get_db)):
    account_service = AccountService(db)
    transactions = account_service.get_account_statement(current_account.id)
    return transactions