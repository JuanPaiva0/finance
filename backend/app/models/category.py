from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, func
from datetime import datetime
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from backend.app.models.user import User
    from backend.app.models.transaction import Transaction

class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        init=False, 
        primary_key=True, 
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now()
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="categories"
    )

    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction",
        back_populates="category",
        cascade="all, delete-orphan"
    )
