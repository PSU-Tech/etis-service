from typing import Annotated

from fastapi import Depends

from .repository import DepartmentRepository
from .service import DepartmentService


def get_department_service():
    return DepartmentService(DepartmentRepository())


DepartmentServiceDep = Annotated[DepartmentService, Depends(get_department_service)]
