from fastapi import APIRouter

from .dependencies import AudienceTimetableServiceDep

router = APIRouter(prefix="/audience", tags=["ЕТИС::Аудитории::Расписание"])


@router.get("/{audience_id}/timetable", response_model_by_alias=False, response_model_exclude_none=True)
async def get_audience_timetable(
    audience_id: int, period: int, week: int, service: AudienceTimetableServiceDep
) -> dict:
    """
    Получение расписания аудитории
    """
    return service.get_audience_timetable(audience_id, period, week)
