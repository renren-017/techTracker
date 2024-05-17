FROM python:3.12

WORKDIR /code

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /code/
RUN poetry install --no-interaction --no-ansi

COPY . /code/


