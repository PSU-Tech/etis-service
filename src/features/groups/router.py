from fastapi import APIRouter

from .schemas import Group
from .dependencies import GroupsServiceDep

router = APIRouter(prefix="/groups", tags=["ЕТИС::Группы"])


@router.get("/search", response_model_by_alias=False)
async def search_groups(query: str, faculty_id: str, service: GroupsServiceDep, limit: int = 100,) -> list[Group]:
    """
    Поиск группы по её короткому имени
    """
    return await service.search_group(query, faculty_id, limit=limit)


@router.get("/{group_id}", response_model_by_alias=False, )
async def get_group_by_id(group_id: int, service: GroupsServiceDep):
    return await service.get_group_by_id(str(group_id))