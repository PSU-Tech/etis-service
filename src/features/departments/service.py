from ...core.repository.base_repository import BaseRepository


class DepartmentService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def get_department(self, id: str):
        return await self.repository.get_by_id(id)

    async def get_all_departments(self):
        return await self.repository.get_all()

    async def search_department(self, query: str):
        return await self.repository.search(query)
