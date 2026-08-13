from app.schemas.Category import CategoryCreate, CategoryUpdate
from app.api.categories.repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    async def create_category(self, category: CategoryCreate, user_id: int):
        return await self.category_repository.create_category(category, user_id)

    async def get_categories(self, user_id: int):
        return await self.category_repository.get_name_categories(user_id)

    async def get_category(self, category_id: int):
        return await self.category_repository.get_category(category_id)

    async def update_category(self, category_id: int, category_update: CategoryUpdate):
        if (category_update.name is None):
            raise ValueError("No fields to update")

        return await self.category_repository.update_category(category_id, category_update)

    async def delete_category(self, category_id: int):
        return await self.category_repository.delete_category(category_id)