from app.database.base import Base
from sqlalchemy import String, ForeignKey, func, Text, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING    

if TYPE_CHECKING:
    from app.models.User import User
    from app.models.Category import Category

class Transaction(Base):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False   
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    transaction_type: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    transaction_date: Mapped[date] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now()
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="transactions"
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="transactions"
    )
