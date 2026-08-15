from app.api.transactions.repository import TransactionRepository
from app.schemas.Transaction import TransactionCreate, TransactionUpdate

class TransactionService:
    def __init__(self):
        self.transaction_repository = TransactionRepository()

    async def create_transaction(self, transaction: TransactionCreate, user_id: int):
        return await self.transaction_repository.create_transaction(transaction, user_id)

    async def get_transactions(self, user_id: int):
        return await self.transaction_repository.get_transactions(user_id)

    async def get_transaction(self, transaction_id: int, user_id: int):
        return await self.transaction_repository.get_transaction(transaction_id, user_id)

    async def update_transaction(self, transaction_id: int, transaction_update: TransactionUpdate, user_id: int):
        return await self.transaction_repository.update_transaction(transaction_id, transaction_update, user_id)

    async def delete_transaction(self, transaction_id: int, user_id: int):
        return await self.transaction_repository.delete_transaction(transaction_id, user_id)