from src.core.repository.base_repository import BaseRepository


class GroupsService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def search_group(self, query: str, faculty_id: str, limit: int):
        return await self.repository.search_by_field("name.short", query, {"faculty.id": faculty_id}, limit=limit)

    async def get_group_by_id(self, group_id: str):
        return await self.repository.get_by_id(group_id)
