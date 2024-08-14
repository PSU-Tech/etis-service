from typing import Annotated

from fastapi import Depends

from .repository import PeriodWeekRepository
from .service import PeriodWeekService
from src.core.database.mongodb import db


def get_period_week_service():
    return PeriodWeekService(PeriodWeekRepository(db["period_week"]))


PeriodWeekServiceDep = Annotated[PeriodWeekService, Depends(get_period_week_service)]
