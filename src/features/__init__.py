from .faculties import router as faculties_router
from .teachers import router as teachers_router
from .departments import router as departments_router
from .groups import router as groups_router
from .period_week import router as period_week_router
from .audience import router as audience_router
from .audience_timetable import router as audience_timetable_router

routers = [
    departments_router.router,
    teachers_router.router,
    faculties_router.router,
    groups_router.router,
    period_week_router.router,
    audience_router.router,
    audience_timetable_router.router,
]
