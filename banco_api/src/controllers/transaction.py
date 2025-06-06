from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.transaction import TransactionCreate, Transaction as TransactionSchema
from src.services.transaction import TransactionService 
from src.controllers.account import get_current_account 
from src.models.account import Account 

router = APIRouter()

@router.post("/transactions/deposit", response_model=TransactionSchema, status_code=status.HTTP_201_CREATED, summary="Realizar um depósito em uma conta")
async def deposit_controller(
    transaction_data: TransactionCreate,
    current_account: Account = Depends(get_current_account),
    db: Session = Depends(get_db)
):
    transaction_service = TransactionService(db) 
    # Delega a lógica para o serviço. O serviço fará as validações e as alterações no DB.
    new_transaction = transaction_service.deposit(current_account, transaction_data)
    return new_transaction

@router.post("/transactions/withdraw", response_model=TransactionSchema, status_code=status.HTTP_201_CREATED, summary="Realizar um saque de uma conta")
async def withdraw_controller(
    transaction_data: TransactionCreate,
    current_account: Account = Depends(get_current_account),
    db: Session = Depends(get_db)
):
    transaction_service = TransactionService(db) 
    # Delega a lógica para o serviço.
    new_transaction = transaction_service.withdraw(current_account, transaction_data)
    return new_transaction