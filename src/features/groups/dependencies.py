from typing import Annotated

from fastapi import Depends

from .repository import GroupsRepository
from .service import GroupsService


def get_groups_service():
    return GroupsService(GroupsRepository())


GroupsServiceDep = Annotated[GroupsService, Depends(get_groups_service)]
