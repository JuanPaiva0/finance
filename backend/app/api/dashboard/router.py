from fastapi import APIRouter

dashboard_router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@dashboard_router.get("/dashboard")
async def get_dashboard():
    pass
