from app.api.transactions.repository import TransactionRepository
from app.schemas.Transaction import TransactionCreate, TransactionUpdate
from app.api.transactions.exceptions import NoFieldsUpdateException, TransactionNotFoundException
from app.api.categories.repository import CategoryRepository
from app.api.categories.exceptions import CategoryNotFoundException

class TransactionService:
    def __init__(self):
        self.transaction_repository = TransactionRepository()
        self.category_repository = CategoryRepository()

    async def create_transaction(self, transaction: TransactionCreate, user_id: int):
        category = await self.category_repository.get_category(transaction.category_id, user_id)
        if not category:
            raise CategoryNotFoundException()

        return await self.transaction_repository.create_transaction(transaction, user_id)

    async def get_transactions(self, user_id: int):
        return await self.transaction_repository.get_transactions(user_id)

    async def get_transaction(self, transaction_id: int, user_id: int):
        transaction = await self.transaction_repository.get_transaction(transaction_id, user_id)
        if not transaction:
            raise TransactionNotFoundException()

        return transaction

    async def update_transaction(self, transaction_id: int, transaction_update: TransactionUpdate, user_id: int):
        if not transaction_update.model_dump(exclude_unset=True):
            raise NoFieldsUpdateException()

        if transaction_update.category_id is not None:
            category = await self.category_repository.get_category(transaction_update.category_id, user_id)
            if not category:
                raise CategoryNotFoundException()

        updated_transaction = await self.transaction_repository.update_transaction(transaction_id, transaction_update, user_id)
        if not updated_transaction:
            raise TransactionNotFoundException()

        return updated_transaction

    async def delete_transaction(self, transaction_id: int, user_id: int):
        success = await self.transaction_repository.delete_transaction(transaction_id, user_id)
        if not success:
            raise TransactionNotFoundException()
