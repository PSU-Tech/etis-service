from typing import Annotated

from fastapi import Depends

from .repository import FacultyRepository
from .service import FacultyService


def get_faculty_service():
    return FacultyService(FacultyRepository())


FacultyServiceDep = Annotated[FacultyService, Depends(get_faculty_service)]
