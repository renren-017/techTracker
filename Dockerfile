FROM python:3.12

WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock /code/

RUN poetry install

COPY . /code/
