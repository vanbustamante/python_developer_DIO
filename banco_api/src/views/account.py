from src.schemas.account import Account as AccountSchema
from src.schemas.transaction import Transaction as TransactionSchema
from src.models.account import Account 

def format_account_response(account: Account) -> AccountSchema:
    return AccountSchema.model_validate(account)

def format_statement_response(transactions: list[TransactionSchema]) -> list[TransactionSchema]:
    return transactions 