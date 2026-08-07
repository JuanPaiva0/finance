from app.schemas.Auth import RegisterRequest, LoginRequest
from app.api.users.repository import UserRepository
from app.schemas.User import UserCreate
from app.core.security import sign_jwt

import bcrypt
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def register(self, register_request: RegisterRequest):
        if (await self.user_repository.get_user_by_email(register_request.email) is not None):
            raise ValueError("User already exists")

        hash_pass = hash_password(register_request.password)

        user_create = UserCreate(
            name=register_request.name,
            email=register_request.email,
            hashed_password=hash_pass
        )
        user = await self.user_repository.create_user(user_create)
        return sign_jwt(user.id)

    async def login(self, login_request: LoginRequest):
        user = await self.user_repository.get_user_by_email(login_request.email)

        if user is None:
            raise ValueError("Invalid email or password!")

        if not bcrypt.checkpw(login_request.password.encode('utf-8'), user.password_hash.encode('utf-8')):
            raise ValueError("Invalid email or password!")

        return sign_jwt(user.id)