from fastapi import APIRouter

category_router = APIRouter(prefix="/categories", tags=["categories"])

@category_router.post("/categories")
async def create_category():
    pass

@category_router.get("/categories")
async def get_categories():
    pass

@category_router.get("/categories/{category_id}")
async def get_category(category_id: int):
    pass

@category_router.patch("/categories/{category_id}")
async def update_category(category_id: int):
    pass

@category_router.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    pass