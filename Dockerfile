FROM python:3.9-slim AS base
WORKDIR /python-app
COPY . .
RUN pip install poetry==1.8.5
RUN poetry install --no-root
EXPOSE 5000

CMD ["poetry", "run", "python", "run.py"]