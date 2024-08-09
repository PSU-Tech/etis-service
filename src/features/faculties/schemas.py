from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class FacultyContacts(BaseModel):
    vk: Optional[str] = Field(default=None)
    """Ссылка на сообщество ВКонтакте"""
    telegram: Optional[str] = Field(default=None)
    """Ссылка на телеграм-канал"""
    sites: Optional[list[str]] = Field(default=None)
    """Перечень ссылок на официальные сайты факультета"""
    phones: Optional[list[str]] = Field(default=None)
    """Перечень номеров телефона"""
    emails: Optional[list[str]] = Field(default=None)
    """Перечень электронных почт"""


class Faculty(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias="_id")
    """Идентификатор факультета в ЕТИС"""
    name: str
    """Название факультета в ЕТИС"""
    logo_image_url: str
    """Ссылка на официальный логотип факультета"""
    psu_page_url: str
    """Ссылка на страницу факультета на официальном сайте ПГНИУ"""
    contacts: FacultyContacts
    """Контактная информация факультета"""
