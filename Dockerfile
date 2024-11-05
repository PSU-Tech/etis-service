FROM python:3.12 as python-base

# Make a new directory and set it as work dir
RUN mkdir /psutech_etis_service
WORKDIR /psutech_etis_service

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install -e .

# Copy all files
COPY . .
