from .faculties import router as faculties_router
from .teachers import router as teachers_router
from .departments import router as departments_router
from .groups import router as groups_router

routers = [
    departments_router.router,
    teachers_router.router,
    faculties_router.router,
    groups_router.router
]
