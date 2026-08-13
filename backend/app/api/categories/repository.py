from app.models.category import Category
from app.schemas.Category import CategoryCreate, CategoryUpdate
from app.database.session import SessionLocal
from sqlalchemy import select
from typing import Sequence

class CategoryRepository:
    async def create_category(self, category: CategoryCreate, user_id: int) -> Category:
        async with SessionLocal() as session:
            new_category = Category(
                name=category.name,
                user_id=user_id
            )

            session.add(new_category)
            await session.commit()
            await session.refresh(new_category)
            return new_category
        
    async def get_categories(self, user_id: int) -> Sequence[Category]:
        async with SessionLocal() as session:
            stmt = select(Category).where(Category.user_id == user_id)
            result = await session.execute(stmt)
            categories = result.scalars().all()
            return categories

    async def get_name_categories(self, user_id: int) -> Sequence[str]:
        async with SessionLocal() as session:
            stmt = select(Category.name).where(Category.user_id == user_id)
            result = await session.execute(stmt)
            category_names = result.scalars().all()
            return category_names

    async def get_category(self, category_id: int) -> Category | None:
        async with SessionLocal() as session:
            stmt = select(Category).where(Category.id == category_id)
            result = await session.execute(stmt)
            category = result.scalar_one_or_none()
            return category

    async def update_category(self, category_id: int, category_update: CategoryUpdate) -> Category | None:
        async with SessionLocal() as session:
            stmt = select(Category).where(Category.id == category_id)
            result = await session.execute(stmt)
            category = result.scalar_one_or_none()

            if category is None:
                return None

            if category_update.name is not None:
                category.name = category_update.name

            await session.commit()
            await session.refresh(category)
            return category

    async def delete_category(self, category_id: int) -> bool:
        async with SessionLocal() as session:
            stmt = select(Category).where(Category.id == category_id)
            result = await session.execute(stmt)
            category = result.scalar_one_or_none()

            if category is None:
                return False

            await session.delete(category)
            await session.commit()
            return True