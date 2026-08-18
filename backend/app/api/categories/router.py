from fastapi import APIRouter, Depends, status

from app.core.security import login_required, get_current_user
from app.api.categories.service import CategoryService
from app.schemas.Category import CategoryCreate, CategoryUpdate, CategoryOut
from typing import Sequence

category_router = APIRouter(prefix="/categories", tags=["categories"], dependencies=[Depends(login_required)])
service = CategoryService()

@category_router.post("/", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def create_category(
    category: CategoryCreate,
    current_user: dict = Depends(get_current_user)
):
    return await service.create_category(category, current_user["user_id"])

@category_router.get("/", response_model=Sequence[CategoryOut])
async def get_categories(current_user: dict = Depends(get_current_user)):
    return await service.get_categories(current_user["user_id"])

@category_router.get("/{category_id}", response_model=CategoryOut)
async def get_category(
    category_id: int,
    current_user: dict = Depends(get_current_user)
):
    return await service.get_category(category_id, current_user["user_id"])

@category_router.patch("/{category_id}", response_model=CategoryOut)
async def update_category(
    category_id: int,
    category_update: CategoryUpdate,
    current_user: dict = Depends(get_current_user)
):
    return await service.update_category(category_id, category_update, current_user["user_id"])

@category_router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int,
    current_user: dict = Depends(get_current_user)
):
    await service.delete_category(category_id, current_user["user_id"])
    return None
