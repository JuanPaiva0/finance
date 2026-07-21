from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/register")
async def register():
    pass

@auth_router.post("/login")
async def login():
    pass

@auth_router.post("/refresh")
async def refresh():
    pass

@auth_router.post("/logout")
async def logout():
    pass

@auth_router.post("/forgot-password")
async def forgot_password():
    pass

@auth_router.post("/reset-password")
async def reset_password():
    pass