from src.core.repository.base_repository import BaseRepository


class FacultyService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def get_faculty_by_id(self, id: str):
        return await self.repository.get_by_id(id)

    async def get_all_faculties(self):
        return await self.repository.get_all()
