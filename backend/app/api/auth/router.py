from fastapi import APIRouter, Depends
from app.core.security import login_required
from app.schemas.Auth import LoginRequest, RegisterRequest
from app.api.auth.service import AuthService

auth_router = APIRouter(prefix="/auth", tags=["auth"])
service = AuthService()

@auth_router.post("/register")
async def register(register_request: RegisterRequest):
    return await service.register(register_request)

@auth_router.post("/login")
async def login(login_request: LoginRequest):
    return await service.login(login_request)

@auth_router.post("/refresh", dependencies=[Depends(login_required)])
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