from sqlalchemy.orm import Session, joinedload
from src.models.account import Account 
from src.models.transaction import Transaction 
from src.schemas.account import AccountCreate 
from src.schemas.transaction import Transaction as TransactionSchema 
from src.security import get_password_hash
from src.exceptions import AccountAlreadyExistsException, AccountNotFoundException

class AccountService:
    def __init__(self, db: Session):
        self.db = db

    def create_account(self, account_data: AccountCreate) -> Account:
        db_account = self.db.query(Account).filter(Account.account_number == account_data.account_number).first()
        if db_account:
            raise AccountAlreadyExistsException()
        
        hashed_password = get_password_hash(account_data.password)
        new_account = Account(
            account_number=account_data.account_number,
            owner_name=account_data.owner_name,
            hashed_password=hashed_password
        )
        self.db.add(new_account)
        self.db.commit()
        self.db.refresh(new_account)
        return new_account

    def get_account_by_number(self, account_number: str) -> Account:
        account = self.db.query(Account).filter(Account.account_number == account_number).first()
        if not account:
            raise AccountNotFoundException()
        return account

    def get_account_statement(self, account_id: int) -> list[TransactionSchema]:
        account_with_transactions = self.db.query(Account).options(joinedload(Account.transactions)).filter(Account.id == account_id).first()
        if not account_with_transactions:
            raise AccountNotFoundException()
        
        return sorted(account_with_transactions.transactions, key=lambda t: t.timestamp, reverse=True)