from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class Audience(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="_id")
    """Идентификатор аудитории в ЕТИС"""
    number: str
    """Номер аудитории в ЕТИС"""
    building: str
    """Номер или название корпуса"""
    size: int
    """Размерность аудитории"""
    note: Optional[str] = Field(default=None)
    """Примечание к аудитории"""
