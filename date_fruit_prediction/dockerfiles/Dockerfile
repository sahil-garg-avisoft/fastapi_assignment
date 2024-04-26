# FROM python:3.11.4

# WORKDIR /Fastapi

# COPY requirement.txt /Fastapi

# RUN pip install -r requirement.txt

# COPY . .

# CMD ["uvicorn", "ml_deployment.fastapi_application:app", "--host", "0.0.0.0", "--port", "8000"]



FROM python:3.11

WORKDIR /date_fruit_prediction

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

ENV PATH="/etc/poetry/bin:$PATH"

COPY ../poetry.lock /date_fruit_prediction/
COPY ../pyproject.toml /date_fruit_prediction/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-ansi 
COPY .. .

# EXPOSE 8000

CMD ["uvicorn", "dates_fruits_class_api.fastapi_application:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["sleep", "infinity"]