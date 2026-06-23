FROM python:3.11-slim
WORKDIR /bench
COPY . .
ENTRYPOINT ["python"]

