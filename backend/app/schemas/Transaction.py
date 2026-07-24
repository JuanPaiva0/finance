from pydantic import BaseModel, ConfigDict
from app.enum.Transaction import TransactionType 
from decimal import Decimal

class TransactionBase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str | None = None
    amount: Decimal
    transaction_type: TransactionType
    
class TransactionCreate(TransactionBase):
    category_id: int

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