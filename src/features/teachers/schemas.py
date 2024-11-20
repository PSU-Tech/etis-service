from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class TeacherPSUData(BaseModel):
    page_url: str


class Teacher(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="_id")
    name: str
    psu: Optional[TeacherPSUData] = Field(default=None)
