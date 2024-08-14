from src.core.repository.mongodb_repository import MongoDBRepository
from .schemas import PeriodWeek
from ..common.enums import PeriodType


class PeriodWeekService:
    def __init__(self, repository: MongoDBRepository[PeriodWeek]):
        self.repository = repository

    async def get_all(self):
        return await self.repository.get_all()

    async def get(self, period_type: PeriodType, year: int):
        print({"period_type": period_type, "year": year})
        return await self.repository.get_one_by_filter({"period_type": period_type.value, "year": year})
