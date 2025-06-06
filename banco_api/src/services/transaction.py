from sqlalchemy.orm import Session
from src.models.account import Account
from src.models.transaction import Transaction 
from src.schemas.transaction import TransactionCreate, Transaction as TransactionSchema 
from src.exceptions import InsufficientFundsException, InvalidAmountException, InvalidTransactionTypeException

class TransactionService:
    def __init__(self, db: Session):
        self.db = db

    def deposit(self, account: Account, transaction_data: TransactionCreate) -> TransactionSchema:
        if transaction_data.amount <= 0:
            raise InvalidAmountException()
        
        if transaction_data.type != "deposit":
            raise InvalidTransactionTypeException(detail="Tipo de transação inválido para depósito. Use 'deposit'.")

        account.balance += transaction_data.amount
        
        new_transaction = Transaction(
            account_id=account.id,
            amount=transaction_data.amount,
            type="deposit"
        )
        self.db.add(new_transaction)
        self.db.commit()
        self.db.refresh(account)
        self.db.refresh(new_transaction)
        return new_transaction

    def withdraw(self, account: Account, transaction_data: TransactionCreate) -> TransactionSchema:
        if transaction_data.amount <= 0:
            raise InvalidAmountException()
        
        if transaction_data.type != "withdraw":
            raise InvalidTransactionTypeException(detail="Tipo de transação inválido para saque. Use 'withdraw'.")

        if account.balance < transaction_data.amount:
            raise InsufficientFundsException()
        
        account.balance -= transaction_data.amount
        
        new_transaction = Transaction(
            account_id=account.id,
            amount=transaction_data.amount,
            type="withdraw"
        )
        self.db.add(new_transaction)
        self.db.commit()
        self.db.refresh(account)
        self.db.refresh(new_transaction)
        return new_transaction