from app.schemas.Auth import RegisterRequest, LoginRequest
from app.api.users.repository import UserRepository
from app.schemas.User import UserCreate
from app.core.security import sign_jwt, hash_password, DUMMY_HASH
from app.api.auth.exceptions import UserAlreadyExistsException, InvalidCredentialsException
import bcrypt

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def register(self, register_request: RegisterRequest):
        if (await self.user_repository.get_user_by_email(register_request.email) is not None):
            raise UserAlreadyExistsException()

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

        password_hash = user.password_hash if user else DUMMY_HASH

        is_password_valid = bcrypt.checkpw(
            login_request.password.encode('utf-8'),
            password_hash.encode('utf-8')
        )

        if user is None or not is_password_valid:
            raise InvalidCredentialsException()

        return sign_jwt(user.id)