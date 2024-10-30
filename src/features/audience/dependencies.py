from typing import Annotated

from fastapi import Depends

from .repository import AudienceRepository
from .service import AudienceService


def get_audience_service():
    return AudienceService(AudienceRepository())


AudienceServiceDep = Annotated[AudienceService, Depends(get_audience_service)]
