from pydantic import BaseModel, ConfigDict
from app.enum.Transaction import TransactionType 
from decimal import Decimal
from datetime import date

class TransactionBase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str | None = None
    amount: Decimal
    transaction_type: TransactionType
    transaction_date: date
    category_id: int
    
class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str | None = None
    description: str | None = None
    amount: Decimal | None = None
    transaction_type: TransactionType | None = None
    category_id: int | None = None

class TransactionOut(TransactionBase):
    id: int
    model_config = ConfigDict(from_attributes=True)