from typing import Any, Optional

from abc import abstractmethod


class BaseRepository:
    @abstractmethod
    async def get_by_id(self, id: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    async def get_list(self, limit: int, skip: int) -> Any:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> Any:
        raise NotImplementedError()

    @abstractmethod
    async def search_by_field(self, field_name: str, query: str, filter: Optional[dict] = None) -> Any:
        raise NotImplementedError()
