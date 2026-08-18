from app.schemas.Category import CategoryCreate, CategoryUpdate
from app.api.categories.repository import CategoryRepository
from app.api.categories.exceptions import NoFieldsUpdateException, CategoryAlreadyExistsException, CategoryNotFoundException

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    async def create_category(self, category: CategoryCreate, user_id: int):
        existing_category = await self.category_repository.get_category_by_name(category.name, user_id)
        if existing_category:
            raise CategoryAlreadyExistsException()

        return await self.category_repository.create_category(category, user_id)

    async def get_categories(self, user_id: int):
        return await self.category_repository.get_categories(user_id)

    async def get_category(self, category_id: int, user_id: int):
        category = await self.category_repository.get_category(category_id, user_id)
        if not category:
            raise CategoryNotFoundException()

        return category

    async def update_category(self, category_id: int, category_update: CategoryUpdate, user_id: int):
        if category_update.name is None:
            raise NoFieldsUpdateException()

        existing_category = await self.category_repository.get_category_by_name(category_update.name, user_id)
        if existing_category and existing_category.id != category_id:
            raise CategoryAlreadyExistsException()

        updated_category = await self.category_repository.update_category(category_id, category_update, user_id)
        if not updated_category:
            raise CategoryNotFoundException()

        return updated_category

    async def delete_category(self, category_id: int, user_id: int):
        success = await self.category_repository.delete_category(category_id, user_id)
        if not success:
            raise CategoryNotFoundException()
