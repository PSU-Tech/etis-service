from src.core.database.mongodb import db
from src.core.repository import MongoDBRepository
from .schemas import Faculty


class FacultyRepository(MongoDBRepository[Faculty]):
    model = Faculty

    def __init__(self):
        collection = db["faculties"]
        super().__init__(collection)
