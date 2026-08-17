from fastapi import APIRouter, Depends
from app.core.security import login_required, get_current_user

from app.schemas.Transaction import TransactionCreate, TransactionUpdate, TransactionOut
from app.api.transactions.service import TransactionService
from typing import Sequence

transaction_router = APIRouter(prefix="/transactions", tags=["transactions"], dependencies=[Depends(login_required)])
service = TransactionService()

@transaction_router.post("/", response_model=TransactionOut)
async def create_transaction(
    transaction: TransactionCreate,
    current_user: dict = Depends(get_current_user)
):
    return await service.create_transaction(transaction, current_user["user_id"])

@transaction_router.get("/", response_model=Sequence[TransactionOut])
async def get_transactions(current_user: dict = Depends(get_current_user)):
    return await service.get_transactions(current_user["user_id"])

@transaction_router.get("/{transaction_id}", response_model=TransactionOut)
async def get_transaction(transaction_id: int, current_user: dict = Depends(get_current_user)):
    return await service.get_transaction(transaction_id, current_user["user_id"])

@transaction_router.patch("/{transaction_id}")
async def update_transaction(transaction_id: int, transaction_update: TransactionUpdate, current_user: dict = Depends(get_current_user)):
    return await service.update_transaction(transaction_id, transaction_update, current_user["user_id"])

@transaction_router.delete("/{transaction_id}")
async def delete_transaction(transaction_id: int, current_user: dict = Depends(get_current_user)):
    return await service.delete_transaction(transaction_id, current_user["user_id"])