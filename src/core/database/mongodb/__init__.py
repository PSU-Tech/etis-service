from motor.motor_asyncio import AsyncIOMotorClient

from src.settings import settings

cluster_client = AsyncIOMotorClient(settings.MONGODB_CONNECTION_URI)
db = cluster_client["psutech"]
