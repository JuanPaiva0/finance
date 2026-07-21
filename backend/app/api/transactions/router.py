from fastapi import APIRouter

transaction_router = APIRouter(prefix="/transactions", tags=["transactions"])

@transaction_router.post("/transactions")
async def create_transaction():
    pass

@transaction_router.get("/transactions")
async def get_transactions():
    pass

@transaction_router.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: int):
    pass

@transaction_router.patch("/transactions/{transaction_id}")
async def update_transaction(transaction_id: int):
    pass

@transaction_router.delete("/transactions/{transaction_id}")
async def delete_transaction(transaction_id: int):
    pass