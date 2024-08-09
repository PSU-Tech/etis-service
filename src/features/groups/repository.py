from src.core.database.mongodb import db
from src.core.repository import MongoDBRepository
from .schemas import Group


class GroupsRepository(MongoDBRepository[Group]):
    model = Group

    def __init__(self):
        collection = db["groups"]
        super().__init__(collection)
