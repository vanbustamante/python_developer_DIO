from src.schemas.transaction import Transaction as TransactionSchema
from src.models.transaction import Transaction

def format_transaction_response(transaction: Transaction) -> TransactionSchema:
    return TransactionSchema.model_validate(transaction)