from src.core.database.mongodb import db
from src.core.repository import MongoDBRepository
from .schemas import Teacher


class TeacherRepository(MongoDBRepository[Teacher]):
    model = Teacher

    def __init__(self):
        collection = db["teachers"]
        super().__init__(collection)
