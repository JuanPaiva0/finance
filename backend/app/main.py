from fastapi import FastAPI

from backend.app.api.auth.router import auth_router
from backend.app.api.users.router import user_router
from backend.app.api.transactions.router import transaction_router
from backend.app.api.categories.router import category_router
from backend.app.api.dashboard.router import dashboard_router

app = FastAPI(title="finance")

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(category_router)
app.include_router(dashboard_router)
