from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
from datetime import datetime
from sqlalchemy import func, String
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.Category import Category
    from app.models.Transaction import Transaction

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        init=False, 
        primary_key=True, 
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )
    
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        init=False, 
        server_default=func.now(),
        onupdate=func.now()
    )

    categories: Mapped[List["Category"]] = relationship(
        "Category",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction",
        back_populates="user",
        cascade="all, delete-orphan"
    )
