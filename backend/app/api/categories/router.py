from fastapi import APIRouter, Depends

from app.core.security import login_required, get_current_user
from app.api.categories.service import CategoryService
from app.schemas.Category import CategoryCreate, CategoryUpdate, CategoryOut
from app.api.users.repository import UserRepository
from app.models.user import User

category_router = APIRouter(prefix="/categories", tags=["categories"], dependencies=[Depends(login_required)])
service = CategoryService()
user_repository = UserRepository()

@category_router.post("/")
async def create_category(
    category: CategoryCreate,
    current_user: dict = Depends(get_current_user)
):
    return await service.create_category(category, current_user["user_id"])

@category_router.get("/")
async def get_categories(current_user: dict = Depends(get_current_user)):
    return await service.get_categories(current_user["user_id"])

@category_router.get("/{category_id}")
async def get_category(category_id: int):
    return await service.get_category(category_id)

@category_router.patch("/{category_id}")
async def update_category(category_id: int, category_update: CategoryUpdate):
    return await service.update_category(category_id, category_update)

@category_router.delete("/{category_id}")
async def delete_category(category_id: int):
    return await service.delete_category(category_id)