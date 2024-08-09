from typing import Any, Optional

from motor.motor_asyncio import AsyncIOMotorCollection
import pydantic

from .base_repository import BaseRepository


class MongoDBRepository[T: pydantic.BaseModel](BaseRepository):
    model: type[T]

    def __init__(self, collection: AsyncIOMotorCollection):
        self.__collection = collection

    async def get_by_id(self, id: Any) -> Optional[T]:
        data = await self.__collection.find_one({"_id": id})
        if data is None:
            return None
        return self.model(**data)

    async def get_list(self, limit: int, skip: int) -> list[T]:
        return [
            self.model(**item) async for item in self.__collection.find(limit=limit, skip=skip)
        ]

    async def get_all(self) -> list[T]:
        return [
            self.model(**item) async for item in self.__collection.find()
        ]

    async def search_by_field(self, field_name: str, query: str, filter: Optional[dict] = None, *, limit: int = 100) -> list[T]:
        if filter is None:
            filter = {}

        return [
            self.model(**item)
            async for item in self.__collection.find(
                {field_name: {"$regex": f".*{query}.*", "$options": 'i'}, **filter},
                limit=limit,
                sort=[field_name]
            )
        ]
