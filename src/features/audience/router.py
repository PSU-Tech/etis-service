from typing import Optional

from fastapi import APIRouter

from .schemas import Audience
from .dependencies import AudienceServiceDep

router = APIRouter(prefix="/audience", tags=["ЕТИС::Аудитории"])


@router.get("/", response_model_by_alias=False, response_model_exclude_none=True)
async def get_audience_by_number(audience_number: str, service: AudienceServiceDep) -> Optional[Audience]:
    """
    Получение аудитории по её номеру
    """
    return await service.get_audience_by_number(audience_number)


@router.get("/search", response_model_by_alias=False, response_model_exclude_none=True)
async def search_audience_by_number(
    query: str, service: AudienceServiceDep, building: Optional[str] = None
) -> list[Audience]:
    """
    Поиск аудитории по её номеру и указанному корпусу
    """
    return await service.search_audience(query, building)


@router.get("/{audience_id}", response_model_by_alias=False, response_model_exclude_none=True)
async def get_audience_by_id(audience_id: int, service: AudienceServiceDep) -> Optional[Audience]:
    """
    Получение аудитории по её идентификатору
    """
    return await service.get_audience_by_id(audience_id)
