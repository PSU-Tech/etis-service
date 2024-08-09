from fastapi import APIRouter

from .schemas import Faculty
from .dependencies import FacultyServiceDep

router = APIRouter(prefix="/faculties", tags=["ЕТИС::Факультеты"])


@router.get("/", response_model_by_alias=False, response_model_exclude_none=True)
async def get_faculty_list(service: FacultyServiceDep) -> list[Faculty]:
    """
    Получение списка всех факультетов университета.
    """
    return await service.get_all_faculties()


@router.get("/{faculty_id}", response_model_by_alias=False, response_model_exclude_none=True)
async def get_faculty_by_id(faculty_id: int, service: FacultyServiceDep):
    """
    Получение факультета по идентификатору
    """
    return await service.get_faculty_by_id(str(faculty_id))
