from typing import Annotated

from fastapi import Depends

from .repository import TeacherRepository
from .service import TeacherService


def get_teacher_service():
    return TeacherService(TeacherRepository())


TeacherServiceDep = Annotated[TeacherService, Depends(get_teacher_service)]
