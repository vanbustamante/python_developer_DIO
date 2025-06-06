from pydantic import BaseModel, Field
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float = Field(..., gt=0, description="Valor da transação (positivo)")
    type: str = Field(..., pattern="^(deposit|withdraw)$", description="Tipo da transação: 'deposit' ou 'withdraw'")

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    account_id: int
    timestamp: datetime

    class Config:
        from_attributes = True