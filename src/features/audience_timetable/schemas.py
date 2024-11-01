from enum import Enum

from pydantic import BaseModel


class LessonTypes(str, Enum):
    LECTURE = 'LECTURE'
    PRACTICE = 'PRACTICE'
    LABORATORY = 'LABORATORY'


class WeekDates(BaseModel):
    start: str
    end: str


class WeekInfo(BaseModel):
    first: int
    selected: int
    last: int
    dates: WeekDates


class Teacher(BaseModel):
    name: str


class Subject(BaseModel):
    discipline: str
    type: LessonTypes


class Lesson(BaseModel):
    subject: Subject
    teacher: Teacher
    groups: list[str]


class Event(BaseModel):
    name: str
    contact_info: str
    department: str


class Pair(BaseModel):
    position: int
    time: str
    lessons: list[Lesson]
    event: Event


class Day(BaseModel):
    date: str
    pairs: list[Pair]


class Timetable(BaseModel):
    week_info: WeekInfo
    days: list[Day]
