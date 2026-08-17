from app.database.session import SessionLocal
from app.models.transaction import Transaction
from app.models.category import Category
from app.enum.Transaction import TransactionType
from sqlalchemy import select, func
from decimal import Decimal

class DashboardRepository:
    async def get_monthly_summary(self, user_id: int) -> dict:
        async with SessionLocal() as session:
            stmt = (
                select(
                    Transaction.transaction_type,
                    func.coalesce(func.sum(Transaction.amount), 0).label("total_amount")
                )
                .where(Transaction.user_id == user_id)
                .group_by(Transaction.transaction_type)
            )

            result = await session.execute(stmt)
            rows = result.all()

            summary = {"income": Decimal(0), "expense": Decimal(0)}
            for row in rows:
                if row.transaction_type == TransactionType.INCOME:
                    summary["income"] = row.total_amount
                elif row.transaction_type == TransactionType.EXPENSE:
                    summary["expense"] = row.total_amount

            return {
                "total_income": summary["income"],
                "total_expense": summary["expense"],
                "balance": summary["income"] - summary["expense"]
            }

    async def get_expense_by_category(self, user_id: int) -> list[dict]:
        async with SessionLocal() as session:
            stmt = (
                select(
                    Category.name,
                    func.sum(Transaction.amount).label("total_amount")       
                )
                .join(Transaction.category)
                .where(
                    Transaction.user_id == user_id,
                    Transaction.transaction_type == TransactionType.EXPENSE
                )
                .group_by(Category.name)
                .order_by(func.sum(Transaction.amount).desc())
            )

            result = await session.execute(stmt)
            return [{"category_name": row.name, "total_amount": row.total_amount} for row in result.all()]