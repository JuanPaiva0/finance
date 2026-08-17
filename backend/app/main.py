from fastapi import FastAPI

from app.api.auth.router import auth_router
from app.api.users.router import user_router
from app.api.transactions.router import transaction_router
from app.api.categories.router import category_router
from app.api.dashboard.router import dashboard_router

from app.core.handlers import register_exception_handlers

app = FastAPI(title="finance")

register_exception_handlers(app)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(category_router)
app.include_router(dashboard_router)
