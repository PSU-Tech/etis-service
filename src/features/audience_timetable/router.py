from fastapi import APIRouter

from .dependencies import AudienceTimetableServiceDep
from .schemas import Timetable

router = APIRouter(prefix="/audience", tags=["ЕТИС::Аудитории::Расписание"])


@router.get("/{audience_id}/timetable", response_model_by_alias=False, response_model_exclude_none=True)
async def get_audience_timetable(audience_id: int, week: int, service: AudienceTimetableServiceDep) -> Timetable:
    """
    Получение расписания аудитории
    """
    return service.get_audience_timetable(audience_id, week)
