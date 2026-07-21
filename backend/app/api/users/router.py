from fastapi import APIRouter

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.get("/users/{user_id}")
async def get_user(user_id: int):
    pass

@user_router.patch("/users/{user_id}")
async def update_user(user_id: int):
    pass

@user_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    pass