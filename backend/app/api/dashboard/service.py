from app.api.dashboard.repository import DashboardRepository
from datetime import date 
import calendar

class DashboardService:
    def __init__(self):
        self.repository = DashboardRepository()

    async def  get_monthly_summary(self, 
        user_id: int,
        start_date: date | None = None,
        end_date: date | None = None 
    ):    
        if start_date is None or end_date is None:
            today = date.today()

            _start = today.replace(day=1)
            _, last_day_of_month = calendar.monthrange(today.year, today.month)
            _end = today.replace(day=last_day_of_month)
        else:
            _start = start_date
            _end = end_date

        return await self.repository.get_monthly_summary(user_id, _start, _end)

    async def get_expense_by_category(self, user_id: int):
        return await self.repository.get_expense_by_category(user_id)