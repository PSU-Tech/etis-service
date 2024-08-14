from src.core.repository import MongoDBRepository
from .schemas import PeriodWeek


class PeriodWeekRepository(MongoDBRepository[PeriodWeek]):
    model = PeriodWeek
