from app.models.user import User
from app.schemas.User import UserCreate
from app.database.session import SessionLocal 
from sqlalchemy import select

class UserRepository:
    async def get_user_by_email(self, email: str) -> User | None:
        async with SessionLocal() as session:
            stmt = select(User).where(User.email == email)
            result = await session.execute(stmt)
            user = result.scalar_one_or_none()
        return user

    async def create_user(self, user_create: UserCreate) -> User:
        async with SessionLocal() as session:
            new_user = User(
                name=user_create.name,
                email=user_create.email,
                password_hash=user_create.hashed_password
            )

            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)

            return new_user