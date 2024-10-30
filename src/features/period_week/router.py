from fastapi import APIRouter

from .dependencies import PeriodWeekServiceDep
from .schemas import PeriodWeek
from ..common.enums import PeriodType

router = APIRouter(prefix="/periods", tags=["ЕТИС::Периоды обучения"])


@router.get("/")
async def get_period(
    service: PeriodWeekServiceDep,
    period_type: PeriodType,
    year: int
) -> PeriodWeek:
    return await service.get(period_type, year)
