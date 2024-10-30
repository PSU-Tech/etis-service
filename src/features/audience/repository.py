from src.core.database.mongodb import db
from src.core.repository import MongoDBRepository
from .schemas import Audience


class AudienceRepository(MongoDBRepository[Audience]):
    model = Audience

    def __init__(self):
        collection = db["audience"]
        super().__init__(collection)
