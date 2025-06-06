from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id")) 
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False) # 'deposit' ou 'withdraw'
    timestamp = Column(DateTime, default=datetime.utcnow)

    account = relationship("Account", back_populates="transactions")