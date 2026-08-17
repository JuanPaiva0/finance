from app.api.dashboard.repository import DashboardRepository


class DashboardService:
    def __init__(self):
        self.repository = DashboardRepository()

    async def  get_monthly_summary(self, user_id: int):
        return await self.repository.get_monthly_summary(user_id)

    async def get_expense_by_category(self, user_id: int):
        return await self.repository.get_expense_by_category(user_id)