from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool

from .dependencies import AudienceTimetableServiceDep
from .schemas import Timetable
from ..audience.dependencies import AudienceServiceDep

router = APIRouter(prefix="/audience", tags=["ЕТИС::Аудитории::Расписание"])


@router.get("/{audience_id}/timetable", response_model_by_alias=False, response_model_exclude_none=True)
async def get_audience_timetable(
    audience_id: int, week: int, service: AudienceServiceDep, timetable_service: AudienceTimetableServiceDep
) -> Timetable:
    """
    Получение расписания аудитории
    """
    audience = await service.get_audience_by_id(audience_id)
    if not audience:
        raise HTTPException(status_code=404, detail="Audience not found")

    return await run_in_threadpool(timetable_service.get_audience_timetable, audience_id, week, audience)
