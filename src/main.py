import os
import sys

from fastapi import FastAPI

from .features import routers

sys.path.insert(1, os.path.join(sys.path[0], ".."))

app = FastAPI(
    title="ЕТИС ПГНИУ | Неофициальное АПИ",
    description="Вся информация взята из открытых источников",
    version="1.0.0",
)
list(map(app.include_router, routers))






