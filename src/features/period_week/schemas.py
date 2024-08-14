from pydantic import BaseModel

from ..common.enums import PeriodType


class PeriodWeek(BaseModel):
    period_type: PeriodType
    """Тип периода"""
    year: int
    """Учебный год, для которого актуальны данные"""
    periods_to_weeks: list[list[int]]
    """Список периодов, который содержит список начала и окончания конкретного периода"""
