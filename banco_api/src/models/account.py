from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from src.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True, nullable=False)
    balance = Column(Float, default=0.0)
    owner_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="account")