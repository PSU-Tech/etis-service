from typing import Annotated

from fastapi import Depends

from .service import AudienceTimetableService


def get_audience_timetable_service():
    return AudienceTimetableService()


AudienceTimetableServiceDep = Annotated[AudienceTimetableService, Depends(get_audience_timetable_service)]
