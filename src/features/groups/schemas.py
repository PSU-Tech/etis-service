from pydantic import BaseModel, Field, ConfigDict

from src.features.faculties.schemas import Faculty


class GroupName(BaseModel):
    full: str
    """Полное название группы"""
    short: str
    """Короткое название группы"""


class PartialFaculty(BaseModel):
    id: str
    short_name: str


class Group(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="_id")
    """Идентификатор группы в ЕТИС"""
    name: GroupName
    """Имя группы в ЕТИС"""
    faculty: PartialFaculty
    """Факультет группы"""
    year: int
    """Год"""
    degree: str
    """Степень образования"""
    speciality: str
    """Специальность. Включает в себя код и полное название"""
