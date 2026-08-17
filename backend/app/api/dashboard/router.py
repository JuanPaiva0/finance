from fastapi import APIRouter, Depends
from app.core.security import login_required, get_current_user
from app.schemas.Dashboard import MonthlySummaryOut, CategoryExpenseOut
from app.api.dashboard.service import DashboardService

dashboard_router = APIRouter(prefix="/dashboard", tags=["dashboard"], dependencies=[Depends(login_required)])
service = DashboardService()

@dashboard_router.get("/summary", response_model=MonthlySummaryOut)
async def get_summary(current_user: dict = Depends(get_current_user)):
    return await service.get_monthly_summary(current_user["user_id"])

@dashboard_router.get("/expenses-by-category", response_model=list[CategoryExpenseOut])
async def get_expense_by_category(current_user: dict = Depends(get_current_user)):
    return await service.get_expense_by_category(current_user["user_id"])
