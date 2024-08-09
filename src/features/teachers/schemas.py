from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from src.features.departments.schemas import Department


class TeacherETISData(BaseModel):
    image_url: str
    position: str
    departments: list[Department]


class TeacherContacts(BaseModel):
    emails: Optional[list[str]] = Field(default=None)
    phones: Optional[list[str]] = Field(default=None)


class TeacherPSUData(BaseModel):
    page_url: str
    image_url: str
    contacts: TeacherContacts


class Teacher(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="_id")
    name: str
    etis: Optional[TeacherETISData] = Field(default=None)
    psu: Optional[TeacherPSUData] = Field(default=None)
