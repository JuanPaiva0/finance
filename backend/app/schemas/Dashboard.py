from pydantic import BaseModel
from decimal import Decimal

class MonthlySummaryOut(BaseModel):
    total_income: Decimal
    total_expense: Decimal
    balance: Decimal


class CategoryExpenseOut(BaseModel):
    category: str
    total_amount: Decimal
