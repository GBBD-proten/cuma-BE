FROM python:3.9-slim AS base
WORKDIR /python-app
COPY . .
RUN pip install poetry==1.8.5
RUN poetry install --no-root
EXPOSE 5000

# 개발환경
FROM base AS development
CMD ["poetry", "run", "python", "run.py"]

# 운영환경
FROM base AS production
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "run:app"]