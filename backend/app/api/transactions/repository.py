from app.models.transaction import Transaction
from app.schemas.Transaction import TransactionCreate, TransactionUpdate
from app.database.session import SessionLocal
from sqlalchemy import select
from typing import Sequence

class TransactionRepository:
    async def create_transaction(self, transaction: TransactionCreate, user_id: int) -> Transaction:
        async with SessionLocal() as session:
            transaction_data = transaction.model_dump()
            new_transaction = Transaction(**transaction_data, user_id=user_id)

            session.add(new_transaction)
            await session.commit()
            await session.refresh(new_transaction)
            return new_transaction
    
    async def get_transactions(self, user_id: int) -> Sequence[Transaction]:
        async with SessionLocal() as session:
            stmt = select(Transaction).where(Transaction.user_id == user_id)
            result = await session.execute(stmt)
            transactions = result.scalars().all()
            return transactions

    async def get_transaction(self, transaction_id: int, user_id: int) -> Transaction | None:
        async with SessionLocal() as session:
            stmt = select(Transaction).where(Transaction.id == transaction_id, Transaction.user_id == user_id)
            result = await session.execute(stmt)
            transaction = result.scalar_one_or_none()
            return transaction

    async def update_transaction(self, transaction_id: int, transaction_update: TransactionUpdate, user_id: int) -> Transaction | None:
        async with SessionLocal() as session:
            stmt = select(Transaction).where(Transaction.id == transaction_id, Transaction.user_id == user_id)
            result = await session.execute(stmt)
            transaction = result.scalar_one_or_none()

            if transaction is None:
                return None

            for field, value in transaction_update.model_dump(exclude_unset=True).items():
                setattr(transaction, field, value)

            await session.commit()
            await session.refresh(transaction)

            return transaction

    async def delete_transaction(self, transaction_id: int, user_id: int) -> bool:
        async with SessionLocal() as session:
            stmt = select(Transaction).where(Transaction.id == transaction_id, Transaction.user_id == user_id)
            result = await session.execute(stmt)
            transaction = result.scalar_one_or_none()

            if transaction is None:
                return False

            await session.delete(transaction)
            await session.commit()
            return True