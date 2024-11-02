from typing import Optional
from ...core.repository import MongoDBRepository


class AudienceService:
    def __init__(self, repository: MongoDBRepository):
        self.repository = repository

    async def get_audience_by_id(self, id: str):
        return await self.repository.get_by_id(id)

    async def get_audience_by_number(self, number: str):
        return await self.repository.get_one_by_filter({"number": number})

    async def search_audience(self, number: str, building: Optional[str] = None):
        return await self.repository.search_by_field("number", number, filter={"building": building} if building is not None else None)
