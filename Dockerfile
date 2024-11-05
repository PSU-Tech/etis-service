FROM python:3.12 as python-base

RUN pip install poetry

RUN mkdir /psutech_etis_service
WORKDIR /psutech_etis_service

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

EXPOSE 8010

CMD ["poetry", "run", "gunicorn", "src.main:app", "--workers", "3", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8010"]