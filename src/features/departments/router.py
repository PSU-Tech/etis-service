from fastapi import APIRouter

from .schemas import Department
from .dependencies import DepartmentServiceDep

router = APIRouter(prefix="/departments", tags=["ЕТИС::Учебные подразделения"])


@router.get("/", response_model_by_alias=False, response_model_exclude_none=True)
async def get_department_list(service: DepartmentServiceDep) -> list[Department]:
    """
    Получение списка всех учебных подразделений университета.
    Включает в себя кафедры всех факультетов, институты, колледж и лицей.
    """

    return await service.get_all_departments()
