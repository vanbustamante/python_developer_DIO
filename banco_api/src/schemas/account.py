from pydantic import BaseModel, Field

class AccountBase(BaseModel):
    account_number: str = Field(..., example="12345-6")
    owner_name: str = Field(..., example="João da Silva")

class AccountCreate(AccountBase):
    password: str = Field(..., min_length=6, example="senha_segura")

class Account(AccountBase):
    id: int
    balance: float

    class Config:
        from_attributes = True