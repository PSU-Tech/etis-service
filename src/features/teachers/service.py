from src.core.repository.mongodb_repository import MongoDBRepository
from .schemas import Teacher


class TeacherService:
    def __init__(self, repository: MongoDBRepository[Teacher]):
        self.repository = repository

    async def get_teacher_by_id(self, id: str, /):
        return await self.repository.get_by_id(id)

    async def search_teacher(self, query: str):
        return await self.repository.search_by_field("name", query)
