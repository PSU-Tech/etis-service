from src.core.database.mongodb import db
from src.core.repository import MongoDBRepository
from .schemas import Department


class DepartmentRepository(MongoDBRepository[Department]):
    model = Department

    def __init__(self):
        collection = db["teachers"]
        super().__init__(collection)
