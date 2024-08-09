from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class Department(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="_id")
    """Идентификатор учебного подразделения в ЕТИС"""
    name: Optional[str] = Field(default=None)
    """Название учебного подразделения в ЕТИС"""
    faculty_name: Optional[str] = Field(default=None)
    """Название факультета учебного подразделения в ЕТИС. Пустое значение для институтов, колледжа и лицея."""
