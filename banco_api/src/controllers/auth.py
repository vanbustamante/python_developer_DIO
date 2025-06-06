from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.auth import Token 
from src.security import verify_password, create_access_token
from src.models.account import Account 
from src.exceptions import CredentialsException 

router = APIRouter()

@router.post("/auth/token", response_model=Token, summary="Gerar token de acesso (Login)")
async def login_for_access_token_controller(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.account_number == form_data.username).first()
    if not account or not verify_password(form_data.password, account.hashed_password):
        raise CredentialsException(detail="Número da conta ou senha incorretos.")
    
    access_token = create_access_token(data={"sub": account.account_number})
    return {"access_token": access_token, "token_type": "bearer"}