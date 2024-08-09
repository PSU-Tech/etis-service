from fastapi import APIRouter

from .dependencies import TeacherServiceDep
from .schemas import Teacher

router = APIRouter(prefix="/teachers", tags=["ЕТИС::Преподаватели"])


@router.get("/search", response_model_by_alias=False, response_model_exclude_none=True)
async def search_teachers(query: str, service: TeacherServiceDep) -> list[Teacher]:
    """
    Поиск преподавателя по полному имени
    """
    return await service.search_teacher(query)


@router.get("/{teacher_id}", response_model_by_alias=False, response_model_exclude_none=True)
async def get_teacher_by_id(teacher_id: int, service: TeacherServiceDep) -> Teacher:
    """
    Получение преподавателя по идентификатору
    """
    return await service.get_teacher_by_id(str(teacher_id))
